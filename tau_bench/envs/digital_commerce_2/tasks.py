
tasks = [
    {
        "annotator": v1,
        "user_id": "task_001",
        "instruction": "Handle a B2B quote for Maria Garcia for one QuantumBook Pro and two USB-C Hubs, apply B2BVOLUME15, check stock, and initiate a low-priority case titled 'B2B Quote Prepared'. Return the subtotal, discount, and total after discount.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "QuantumBook Pro",
                        "USB-C Hub"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1005",
                            "required_quantity": 1
                        },
                        {
                            "product_id": "1002",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1005",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1005",
                            "quantity": 1,
                            "price": 1900.0
                        },
                        {
                            "product_id": "1002",
                            "quantity": 2,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 2020.0,
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "B2B Quote Prepared",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"201\",\"account_id\":\"101\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1005\",\"quantity\":1,\"unit_price\":1900.0,\"line_total\":1900.0},{\"product_id\":\"1002\",\"quantity\":2,\"unit_price\":60.0,\"line_total\":120.0}],\"subtotal\":2020.0,\"applied_offer_code\":\"B2BVOLUME15\",\"discount_amount\":303.0,\"total_after_discount\":1717.0},\"case\":{\"subject\":\"B2B Quote Prepared\",\"priority\":\"Low\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_002",
        "instruction": "Coordinate the creation of a 25% promo code 'FALL25' and quote Nora Patel for four 1TB NVMe SSDs at B2B rates, use FALL25, and provide the subtotal, discount, and total after discount.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "109"
                },
            },
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "FALL25",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 25
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "1TB NVMe SSD"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "quantity": 4,
                            "price": 95.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 380.0,
                    "offer_code": "FALL25"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"210\",\"account_id\":\"109\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1016\",\"quantity\":4,\"unit_price\":95.0,\"line_total\":380.0}],\"subtotal\":380.0,\"applied_offer_code\":\"FALL25\",\"discount_amount\":95.0,\"total_after_discount\":285.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_003",
        "instruction": "Arrange a retail quote for Leo Martinez for one 4K Webcam and two Wireless Mice, confirm stock availability, and open a low-priority case titled 'Retail Quote Prepared'. Return the subtotal.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "113"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "4K Webcam",
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "required_quantity": 1
                        },
                        {
                            "product_id": "1003",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "pricebook_id": "1"
                        },
                        {
                            "product_id": "1003",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 1,
                            "price": 199.0
                        },
                        {
                            "product_id": "1003",
                            "quantity": 2,
                            "price": 40.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Retail Quote Prepared",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"215\",\"account_id\":\"113\",\"used_pricebook_id\":\"1\",\"items\":[{\"product_id\":\"1018\",\"quantity\":1,\"unit_price\":199.0,\"line_total\":199.0},{\"product_id\":\"1003\",\"quantity\":2,\"unit_price\":40.0,\"line_total\":80.0}],\"subtotal\":279.0},\"case\":{\"subject\":\"Retail Quote Prepared\",\"priority\":\"Low\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_004",
        "instruction": "Draft a B2B reorder quote for Maria Garcia based on his shipped order #9002 and open a case 'Reorder Quote Prepared' (Low).",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9002"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9002"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 1,
                            "price": 1250.0
                        },
                        {
                            "product_id": "1002",
                            "quantity": 1,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "required_quantity": 1
                        },
                        {
                            "product_id": "1002",
                            "required_quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Reorder Quote Prepared",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"reorder_quote\":{\"contact_id\":\"201\",\"account_id\":\"101\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1001\",\"quantity\":1,\"unit_price\":1250.0,\"line_total\":1250.0},{\"product_id\":\"1002\",\"quantity\":1,\"unit_price\":60.0,\"line_total\":60.0}],\"subtotal\":1310.0},\"case\":{\"subject\":\"Reorder Quote Prepared\",\"priority\":\"Low\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_005",
        "instruction": "Add four 'USB-C Hub' and two 'Wireless Mouse' to Maria Garcia\u2019s cart and calculate a B2B subtotal.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Emily",
                    "last_name": "White"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "102"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "203"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "USB-C Hub",
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "required_quantity": 4
                        },
                        {
                            "product_id": "1003",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "AddItemsToCartBatch",
                "arguments": {
                    "cart_id": "701",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 4
                        },
                        {
                            "product_id": "1003",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1003",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 4,
                            "price": 60.0
                        },
                        {
                            "product_id": "1003",
                            "quantity": 2,
                            "price": 32.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\"cart_quote\":{\"contact_id\":\"203\",\"account_id\":\"102\",\"cart_id\":\"701\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1002\",\"quantity\":4,\"unit_price\":60.0,\"line_total\":240.0},{\"product_id\":\"1003\",\"quantity\":2,\"unit_price\":32.0,\"line_total\":64.0}],\"subtotal\":304.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_006",
        "instruction": "Handle pricing for Maria Garcia at WorldWide Systems by offering two ProBook X15 at B2B rates, applying a flat $500 discount, and logging a low-priority case 'Math Check Logged'. Provide the subtotal and the total after the discount.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAccountByName",
                "arguments": {
                    "name": "WorldWide Systems"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "ProBook X15"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 2,
                            "price": 1250.0
                        }
                    ]
                },
            },
            {
                "name": "CalculateDiscountFlat",
                "arguments": {
                    "subtotal": 2500.0,
                    "discount_amount": 500
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Math Check Logged",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"math_check\":{\"product_id\":\"1001\",\"quantity\":2,\"unit_price\":1250.0,\"subtotal\":2500.0,\"flat_discount\":500,\"total_after_discount\":2000.0},\"case\":{\"subject\":\"Math Check Logged\",\"priority\":\"Low\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_007",
        "instruction": "Coordinate a B2B quote for Nora Patel involving six 1TB NVMe SSDs, apply the WINTER20 promotion, provide the subtotal and the discounted total, and open a low-priority case with the title 'B2B Quote Prepared'.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "1TB NVMe SSD"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "required_quantity": 6
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "quantity": 6,
                            "price": 95.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 570.0,
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "B2B Quote Prepared",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"210\",\"account_id\":\"109\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1016\",\"quantity\":6,\"unit_price\":95.0,\"line_total\":570.0}],\"subtotal\":570.0,\"applied_offer_code\":\"WINTER20\",\"discount_amount\":114.0,\"total_after_discount\":456.0},\"case\":{\"subject\":\"B2B Quote Prepared\",\"priority\":\"Low\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_008",
        "instruction": "Make adjustments in David Chen\u2019s cart by increasing the 'Ergo Laptop Stand' to quantity 2, removing the 'Branded Water Bottle', and displaying the final cart items.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Sandra",
                    "last_name": "Dee"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "208"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Ergo Laptop Stand",
                        "Branded Water Bottle"
                    ]
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "703"
                },
            },
            {
                "name": "UpdateItemsInCartBatch",
                "arguments": {
                    "cart_id": "703",
                    "items": [
                        {
                            "product_id": "1010",
                            "new_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "703",
                    "product_ids": [
                        "1012"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1010",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "703"
                }
            }
        ],
        "outputs": [
                "{\"final_cart\":[{\"cart_id\":\"703\",\"product_id\":\"1010\",\"quantity\":2}],\"removed_products\":[\"1012\"]}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_009",
        "instruction": "You create a new 10% promo code 'MIDMONTH10', confirm it by ID, apply it to a $75 subtotal to demonstrate the discount, then deactivate it and confirm by ID, and open and resolve a case 'Promo Lifecycle Logged' (Low) for Maria Garcia at Global Tech Inc.",
        "actions": [
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "MIDMONTH10",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 10
                },
            },
            {
                "name": "GetOfferDetails",
                "arguments": {
                    "offer_id": "offer_5"
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 75.0,
                    "offer_code": "MIDMONTH10"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "MIDMONTH10"
                },
            },
            {
                "name": "GetOfferDetails",
                "arguments": {
                    "offer_id": "offer_5"
                },
            },
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Promo Lifecycle Logged",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"offer_status\":{\"offer_code\":\"MIDMONTH10\",\"checked_offer_id\":\"offer_5\",\"applied_demo\":{\"subtotal\":75.0,\"discount_percent\":10,\"discount_amount\":7.5,\"total_after_discount\":67.5},\"final_is_active\":false},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Promo Lifecycle Logged\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_010",
        "instruction": "Cancel David Chen\u2019s order #9010, record a high-priority case with the title 'Ordered By Mistake', and return both the order status and updated stock counts after restocking the items.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Mike",
                    "last_name": "Rivera"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9010"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9010"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "209",
                    "account_id": "108",
                    "order_id": "9010",
                    "subject": "Ordered By Mistake",
                    "priority": "High"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "9010",
                    "new_status": "Cancelled"
                },
            },
            {
                "name": "AddStockQuantities",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1005",
                            "quantity_to_add": 1
                        },
                        {
                            "product_id": "1011",
                            "quantity_to_add": 5
                        }
                    ]
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"order_update\":{\"order_id\":\"9010\",\"final_status\":\"Cancelled\"},\"restocked\":[{\"product_id\":\"1005\",\"stock_quantity\":26},{\"product_id\":\"1011\",\"stock_quantity\":80}],\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_011",
        "instruction": "Handle the listing of Maria Garcia's orders, recalculate their subtotal, and document the audit by opening a support case with the subject 'Order audit recorded' and setting the priority to 'Medium' for this customer.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetOrdersByContactId",
                "arguments": {
                    "contact_id": "201"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9002"
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 1,
                            "price": 1250.0
                        },
                        {
                            "product_id": "1002",
                            "quantity": 1,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Order audit recorded",
                    "priority": "Medium"
                }
            }
        ],
        "outputs": [
                "{\"audit\":{\"contact_id\":\"201\",\"orders_found\":[\"9002\",\"9012\"],\"order_9002_items\":[{\"product_id\":\"1001\",\"quantity\":1,\"price\":1250.0},{\"product_id\":\"1002\",\"quantity\":1,\"price\":60.0}],\"recomputed_subtotal\":1310.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_012",
        "instruction": "You want a B2B quote for Mike Rivera for one USB-C Hub and open a low-priority case titled 'Pricing Clarification'. You want to update the case status as resolved.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "202",
                    "account_id": "101",
                    "subject": "Pricing Clarification",
                    "priority": "Low"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "USB-C Hub"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"quote_check\":{\"contact_id\":\"202\",\"account_id\":\"101\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1002\",\"quantity\":1,\"unit_price\":60.0,\"line_total\":60.0}],\"subtotal\":60.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Pricing Clarification\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_013",
        "instruction": "Coordinate the computation of a retail quote for Nora Patel for two 4K Webcams, apply WELCOME5, provide the subtotal and the total post-discount, and open a low-priority case named 'Retail Quote Prepared'.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Davis"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "110"
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 2,
                            "price": 199.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 398.0,
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "211",
                    "account_id": "110",
                    "subject": "Retail Quote Prepared",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"211\",\"account_id\":\"110\",\"used_pricebook_id\":\"1\",\"items\":[{\"product_id\":\"1018\",\"quantity\":2,\"unit_price\":199.0,\"line_total\":398.0}],\"subtotal\":398.0,\"applied_offer_code\":\"WELCOME5\",\"discount_amount\":5.0,\"total_after_discount\":393.0},\"case\":{\"subject\":\"Retail Quote Prepared\",\"priority\":\"Low\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_014",
        "instruction": "Perform a comparison of ProBook X15 pricing for quantity one at retail versus B2B for Maria Garcia at Global Tech Inc, and log the findings in a medium-priority case titled 'ProBook X15 pricing comparison'. Provide both totals and the price difference.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 1,
                            "price": 1500.0
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 1,
                            "price": 1250.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "ProBook X15 pricing comparison",
                    "priority": "Medium"
                },
            },
            {
                "name": "CalculateDiscountFlat",
                "arguments": {
                    "subtotal": 1500.0,
                    "discount_amount": 1250.0
                }
            }
        ],
        "outputs": [
                "{\"comparison\":{\"contact_id\":\"201\",\"account_id\":\"101\",\"product_id\":\"1001\",\"retail_used_pricebook_id\":\"1\",\"retail_total_qty1\":1500.0,\"b2b_used_pricebook_id\":\"2\",\"b2b_total_qty1\":1250.0,\"difference\":250.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_015",
        "instruction": "Initiate the process of opening a case titled 'Address Update' for Maria Garcia at Pioneer Technologies, standardize the address to '456 Innovation Ave, Suite 900', and incorporate a quick B2B price snapshot for one USB-C Hub. Return both the snapshot and the updated address.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Emily",
                    "last_name": "White"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "102"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "203",
                    "account_id": "102",
                    "subject": "Address Update",
                    "priority": "Medium"
                },
            },
            {
                "name": "UpdateStreetAddress",
                "arguments": {
                    "account_id": "102",
                    "new_shipping_street": "456 Innovation Ave, Suite 900",
                    "new_billing_street": "456 Innovation Ave, Suite 900"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "USB-C Hub"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1,
                            "price": 60.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\"address_update\":{\"account_id\":\"102\",\"shipping_street\":\"456 Innovation Ave, Suite 900\",\"billing_street\":\"456 Innovation Ave, Suite 900\"},\"price_snapshot\":{\"product_id\":\"1002\",\"used_pricebook_id\":\"2\",\"subtotal_qty1\":60.0},\"case\":{\"subject\":\"Address Update\",\"priority\":\"Medium\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_016",
        "instruction": "Focus on replacing the unrestricted Redis access on rule 'sgr-badbadbadbadbadbad' by confining TCP 6379 to '10.0.5.0/24' while assigning the description 'Redis \u2013 restricted [CLOSED] tightened 6379'. Ensure Redis descriptions are uniform on that group. Provide a before/after.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [CLOSED] tightened 6379",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [CLOSED] tightened 6379",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 2
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                }
            }
        ],
        "outputs": [
                "{\"after_rule\":{\"rule_id\":\"sgr-badbadbadbadbadbad\",\"source_ip\":\"10.0.5.0/24\",\"description_contains\":[\"Redis – restricted\",\"[CLOSED]\",\"[DEV]\"]}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_017",
        "instruction": "Coordinate a retail reorder quote for Maria Garcia derived from order history and initiate a low-priority case named 'Reorder Quote Prepared'. Deliver the subtotal.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Alice",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "103"
                },
            },
            {
                "name": "GetOrdersByContactId",
                "arguments": {
                    "contact_id": "204"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9016"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9016"
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 1,
                            "price": 199.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "204",
                    "account_id": "103",
                    "subject": "Reorder Quote Prepared",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"reorder_quote\":{\"contact_id\":\"204\",\"account_id\":\"103\",\"used_pricebook_id\":\"1\",\"items\":[{\"product_id\":\"1018\",\"quantity\":1,\"unit_price\":199.0,\"line_total\":199.0}],\"subtotal\":199.0},\"case\":{\"subject\":\"Reorder Quote Prepared\",\"priority\":\"Low\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_018",
        "instruction": "Organize an exchange estimate for Maria Garcia: reprice a Branded T-Shirt (L) and a Wireless Mouse at retail, and document it in a medium-priority case titled 'Exchange Estimate Logged'. Provide the subtotal.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Alice",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "103"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Branded T-Shirt (L)",
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1004",
                            "pricebook_id": "1"
                        },
                        {
                            "product_id": "1003",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1004",
                            "quantity": 1,
                            "price": 25.0
                        },
                        {
                            "product_id": "1003",
                            "quantity": 1,
                            "price": 40.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "204",
                    "account_id": "103",
                    "subject": "Exchange Estimate Logged",
                    "priority": "Medium"
                }
            }
        ],
        "outputs": [
                "{\"exchange_estimate\":{\"contact_id\":\"204\",\"account_id\":\"103\",\"used_pricebook_id\":\"1\",\"items\":[{\"product_id\":\"1004\",\"quantity\":1,\"unit_price\":25.0},{\"product_id\":\"1003\",\"quantity\":1,\"unit_price\":40.0}],\"subtotal\":65.0}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_019",
        "instruction": "Handle the cleaning of Leo Martinez\u2019s cart by taking out the Branded Water Bottle, display the final cart, and register a low-priority case titled 'Cart cleanup completed'. Supply the final cart contents.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Branded Water Bottle"
                    ]
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "215"
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "705"
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "705",
                    "product_ids": [
                        "1012"
                    ]
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "705"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Cart cleanup completed",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"cart_cleanup\":{\"contact_id\":\"215\",\"cart_id\":\"705\",\"removed_product_ids\":[\"1019\"]}}"
        ]
    }
    ,
    {
        "annotator": v7,
        "user_id": "task_020",
        "instruction": "Reset Maria Garcia\u2019s cart and assemble a B2B quote for four USB-C Hubs and two Wireless Mice. Furnish the itemized subtotal.",
        "actions": [
            {
                "name": "ClearCart",
                "arguments": {
                    "cart_id": "701"
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "required_quantity": 4
                        },
                        {
                            "product_id": "1003",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "AddItemsToCartBatch",
                "arguments": {
                    "cart_id": "701",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 4
                        },
                        {
                            "product_id": "1003",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1003",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 4,
                            "price": 60.0
                        },
                        {
                            "product_id": "1003",
                            "quantity": 2,
                            "price": 32.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"cart_id\":\"701\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1002\",\"quantity\":4,\"unit_price\":60.0,\"line_total\":240.0},{\"product_id\":\"1003\",\"quantity\":2,\"unit_price\":32.0,\"line_total\":64.0}],\"subtotal\":304.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_021",
        "instruction": "Handle the creation of a B2B quote intended for Maria Garcia at WorldWide Systems, involving ten USB-C Hubs, apply WINTER20, and compute both the subtotal and the total after discount. Initiate a low-priority case named 'Bulk Quote Prepared'.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "USB-C Hub"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "required_quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 10,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 600.0,
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Bulk Quote Prepared",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"201\",\"account_id\":\"101\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1002\",\"quantity\":10,\"unit_price\":60.0,\"line_total\":600.0}],\"subtotal\":600.0,\"applied_offer_code\":\"WINTER20\",\"discount_amount\":120.0,\"total_after_discount\":480.0},\"case\":{\"subject\":\"Bulk Quote Prepared\",\"priority\":\"Low\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_022",
        "instruction": "Organize for 'dcomm-uat-redis' to utilize the UAT group referenced by rule 'sgr-fedcba9876543210f': ensure status is 'available', the name is 'UAT Redis Cache (Hardened)', and note 'audit: uat-redis-hardening'. Use '[UAT]' for standardization and consolidate to '10.0.5.0/24' in 'Redis \u2013 UAT app tier'. Provide the updated cluster.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "reference_rule_id": "sgr-fedcba9876543210f",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "available",
                    "new_name": "UAT Redis Cache (Hardened)",
                    "note": "audit: uat-redis-hardening",
                    "env_tag": "UAT",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – UAT app tier",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 3
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 4
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 5
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 6
                }
            }
        ],
        "outputs": [
                "{\"cluster\":{\"cluster_id\":\"dcomm-uat-redis\",\"cluster_name\":\"UAT Redis Cache (Hardened)\",\"status\":\"available\",\"instance_type_note\":\"audit: uat-redis-hardening\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_023",
        "instruction": "Ensure the $50 promo code 'FLASH50' is available, correctly applies to discount a $75 subtotal, and subsequently disable it so it ceases to apply.",
        "actions": [
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "FLASH50",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 50
                },
            },
            {
                "name": "GetOfferDetails",
                "arguments": {
                    "offer_id": "offer_5"
                },
            },
            {
                "name": "CalculateDiscountFlat",
                "arguments": {
                    "subtotal": 75.0,
                    "discount_amount": 50
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 75.0,
                    "offer_code": "FLASH50"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "FLASH50"
                },
            },
            {
                "name": "GetOfferDetails",
                "arguments": {
                    "offer_id": "offer_5"
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 75.0,
                    "offer_code": "FLASH50"
                }
            }
        ],
        "outputs": [
                "{\"offer_status\":{\"offer_code\":\"FLASH50\",\"checked_offer_id\":\"offer_5\",\"math_check\":{\"subtotal\":75.0,\"discount_amount\":50,\"total_after_discount\":25.0},\"applied_before_deactivate\":{\"subtotal\":75.0,\"discount_amount\":50,\"total_after_discount\":25.0},\"final_is_active\":false,\"reapply_valid_after_deactivate\":false}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_024",
        "instruction": "Evaluate David Chen\u2019s cart and increase the quantity of 'Ergo Laptop Stand' to 2, remove the 'Branded Water Bottle', and display the final list of cart items.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Sandra",
                    "last_name": "Dee"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Ergo Laptop Stand",
                        "Branded Water Bottle"
                    ]
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "208"
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "703"
                },
            },
            {
                "name": "UpdateItemsInCartBatch",
                "arguments": {
                    "cart_id": "703",
                    "items": [
                        {
                            "product_id": "1010",
                            "new_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "703",
                    "product_ids": [
                        "1012"
                    ]
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "703"
                }
            }
        ],
        "outputs": [
                "{\"final_cart\":[{\"cart_id\":\"703\",\"product_id\":\"1010\",\"quantity\":2}],\"removed_products\":[\"1012\"]}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_025",
        "instruction": "Coordinate the hardening of 'dcomm-uat-redis' with a UAT rule 'sgr-fedcba9876543210f': attach SG and subnet 'esg-uat-1', configure status/name/note, and consolidate Redis 6379 to '10.0.5.0/24' with 'Redis \u2013 UAT app tier' without changing the endpoint (NOCHANGE). Standardize using '[UAT]' in a separate step. Return the updated cluster.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "reference_rule_id": "sgr-fedcba9876543210f",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "available",
                    "new_name": "UAT Redis Cache [Reviewed]",
                    "note": "subnet group reviewed",
                    "env_tag": "UAT",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – UAT app tier",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 3
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 4
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 6
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "reference_rule_id": "sgr-fedcba9876543210f",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "available",
                    "new_name": "UAT Redis Cache [Reviewed]",
                    "note": "subnet group reviewed",
                    "env_tag": "UAT",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – UAT app tier",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 5
                }
            }
        ],
        "outputs": [
                "{\"cluster\":{\"cluster_id\":\"dcomm-uat-redis\",\"cluster_name\":\"UAT Redis Cache [Reviewed]\",\"status\":\"available\",\"instance_type_note\":\"subnet group reviewed\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_026",
        "instruction": "Handle a return for Maria Garcia\u2019s delivered order #9001: return the 'Branded T-Shirt (L)' item, initiate a case titled 'Return Requested' (Low), update the order status to Returned, and close the case.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Alice",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9001"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9001"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "204",
                    "account_id": "103",
                    "order_id": "9001",
                    "subject": "Return Requested",
                    "priority": "Low"
                },
            },
            {
                "name": "AddStockQuantities",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1004",
                            "quantity_to_add": 1
                        }
                    ]
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "9001",
                    "new_status": "Returned"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"return_processed\":{\"order_id\":\"9001\",\"restocked\":[{\"product_id\":\"1004\",\"stock_quantity\":151}],\"final_order_status\":\"Returned\",\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_027",
        "instruction": "Coordinate a retail reorder quote for Maria Garcia based on her latest delivered order and initiate a low-priority case to track the quote. Keep the case active. Provide the computed subtotal along with the case ID.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Alice",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "103"
                },
            },
            {
                "name": "GetOrdersByContactId",
                "arguments": {
                    "contact_id": "204"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9016"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9016"
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 1,
                            "price": 199.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "204",
                    "account_id": "103",
                    "subject": "Reorder Quote Prepared",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"reorder_quote\":{\"contact_id\":\"204\",\"account_id\":\"103\",\"used_pricebook_id\":\"1\",\"items\":[{\"product_id\":\"1018\",\"quantity\":1,\"unit_price\":199.0,\"line_total\":199.0}],\"subtotal\":199.0},\"case_open\":{\"case_id\":\"case_9\",\"status\":\"New\",\"subject\":\"Reorder Quote Prepared\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_028",
        "instruction": "Request a B2B quick quote for Maria Garcia for one 'Wireless Mouse', and then initiate and conclude a low-priority case titled exactly 'Quick Quote Prepared'. Present the subtotal and the final status of the case.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Emily",
                    "last_name": "White"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "102"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1,
                            "price": 32.0
                        }
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "required_quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "203",
                    "account_id": "102",
                    "subject": "Quick Quote Prepared",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"203\",\"account_id\":\"102\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1003\",\"quantity\":1,\"unit_price\":32.0,\"line_total\":32.0}],\"subtotal\":32.0},\"case\":{\"case_id\":\"case_9\",\"subject\":\"B2B Quick Quote Prepared\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_029",
        "instruction": "Request a pricing comparison for ProBook X15 for a quantity of one at retail versus B2B for Maria Garcia, and document the outcome in a medium-priority case titled 'ProBook X15 price comparison'. Provide both totals as well as the difference.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "ProBook X15"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 1,
                            "price": 1500.0
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 1,
                            "price": 1250.0
                        }
                    ]
                },
            },
            {
                "name": "CalculateDiscountFlat",
                "arguments": {
                    "subtotal": 1500.0,
                    "discount_amount": 1250.0
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "ProBook X15 price comparison",
                    "priority": "Medium"
                }
            }
        ],
        "outputs": [
                "{\"comparison\":{\"product_id\":\"1001\",\"retail_used_pricebook_id\":\"1\",\"retail_total_qty1\":1500.0,\"b2b_used_pricebook_id\":\"2\",\"b2b_total_qty1\":1250.0,\"difference\":250.0}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_030",
        "instruction": "Implement least-privilege Redis on the UAT group denoted by 'sgr-fedcba9876543210f': unify to a single 6379/TCP rule '10.0.5.0/24' with the description 'Redis \u2013 UAT app tier', and standardize descriptions with '[UAT]' in a separate phase. Provide the final UAT Redis rule.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier",
                    "env_tag": "UAT"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier",
                    "env_tag": "UAT"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 2
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                }
            }
        ],
        "outputs": [
                "{\"final_rule\":{\"rule_id\":\"sgr-fedcba9876543210f\",\"source_ip\":\"10.0.5.0/24\",\"description_contains\":[\"Redis – UAT app tier\",\"[UAT]\"]}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_031",
        "instruction": "You want to tidy Nora Patel\u2019s cart by removing the Server Rack Mount Kit, 1008, briefly add an AC-USBC-HUB to verify the cart works, then clear the cart and log a low-priority case titled 'Cart Cleaned'. Return a confirmation of the cleared cart.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "210"
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "704",
                    "product_ids": [
                        "1008"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "required_quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "AddItemsToCartBatch",
                "arguments": {
                    "cart_id": "704",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ClearCart",
                "arguments": {
                    "cart_id": "704"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Cart Cleaned",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"cart_cleared\":{\"cart_id\":\"704\",\"removed_products\":[\"1008\"],\"cleared\":true},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Cart Cleaned\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_032",
        "instruction": "Check the stock availability for Nora Patel for ten 'Flash Sale Power Bank' and two 'Mechanical Keyboard', then initiate a case 'Stock Verified' (Low) detailing the inquiry and resolve it.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Flash Sale Power Bank",
                        "Mechanical Keyboard"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1015",
                            "required_quantity": 10
                        },
                        {
                            "product_id": "1017",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Stock Verified",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"stock_check\":{\"is_valid\":true,\"requested\":[{\"product_id\":\"1015\",\"qty\":10},{\"product_id\":\"1017\",\"qty\":2}]},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Stock Verified\"}}"
        ]
    }
    ,
    {
        "annotator": v7,
        "user_id": "task_033",
        "instruction": "Reset Nora Patel\u2019s cart, insert one USB-C Hub and one Wireless Mouse at B2B pricing, apply the WINTER20 promo, and deliver a concise receipt listing the items, subtotal, discount, and total.",
        "actions": [
            {
                "name": "ClearCart",
                "arguments": {
                    "cart_id": "704"
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "required_quantity": 1
                        },
                        {
                            "product_id": "1003",
                            "required_quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "AddItemsToCartBatch",
                "arguments": {
                    "cart_id": "704",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        },
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1003",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1,
                            "price": 60.0
                        },
                        {
                            "product_id": "1003",
                            "quantity": 1,
                            "price": 32.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 92.0,
                    "offer_code": "WINTER20"
                }
            }
        ],
        "outputs": [
                "{\"order_like_receipt\":{\"cart_id\":\"704\",\"used_pricebook_id\":\"2\",\"applied_offer_code\":\"WINTER20\",\"items\":[{\"product_id\":\"1002\",\"quantity\":1,\"unit_price\":60.0,\"line_total\":60.0},{\"product_id\":\"1003\",\"quantity\":1,\"unit_price\":32.0,\"line_total\":32.0}],\"subtotal\":92.0,\"discount_amount\":18.4,\"total_after_discount\":73.6}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_034",
        "instruction": "Calculate a retail estimate for Nora Patel for two 4K Webcams, incorporate the WELCOME5 discount, provide the subtotal and discounted total, and initiate a low-priority case called 'Retail Quote Prepared'.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Davis"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "110"
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 2,
                            "price": 199.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 398.0,
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "211",
                    "account_id": "110",
                    "subject": "Retail Quote Prepared",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"211\",\"account_id\":\"110\",\"used_pricebook_id\":\"1\",\"items\":[{\"product_id\":\"1018\",\"quantity\":2,\"unit_price\":199.0,\"line_total\":398.0}],\"subtotal\":398.0,\"applied_offer_code\":\"WELCOME5\",\"discount_amount\":5.0,\"total_after_discount\":393.0},\"case\":{\"subject\":\"Retail Quote Prepared\",\"priority\":\"Low\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_035",
        "instruction": "Contrast the retail and B2B totals for one 'USB-C Hub' utilizing Leo Martinez\u2019s retail account and Maria Garcia\u2019s B2B account, then commence and settle a case 'Price Comparison Logged' (Low) that outlines both totals.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "113"
                },
            },
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "USB-C Hub"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1,
                            "price": 75.0
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Price Comparison Logged",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"comparison\":{\"product_id\":\"1002\",\"retail_used_pricebook_id\":\"1\",\"retail_total_qty1\":75.0,\"b2b_used_pricebook_id\":\"2\",\"b2b_total_qty1\":60.0,\"difference\":15.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Price Comparison Logged\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_036",
        "instruction": "Handle the listing of all orders for Alice Johnson and proceed to open and resolve a case 'Order Audit Logged' (Low).",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "GetOrdersByContactId",
                "arguments": {
                    "contact_id": "207"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9005"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "207",
                    "account_id": "106",
                    "order_id": "9005",
                    "subject": "Order Audit Logged",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"audit\":{\"contact_id\":\"207\",\"orders_found\":[\"9005\"],\"order_9005_items\":[{\"product_id\":\"1006\",\"quantity\":2,\"price\":60.0},{\"product_id\":\"1003\",\"quantity\":1,\"price\":40.0}]},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Order Audit Logged\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_037",
        "instruction": "Coordinate the tagging of approval on UAT Redis using rule 'sgr-fedcba9876543210f' by setting source '10.0.5.0/24' and description 'Redis \u2013 UAT app tier [APPROVED] peer-reviewed 2025-08-10', and ensure standardization with '[UAT]'.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [APPROVED] peer-reviewed 2025-08-10",
                    "env_tag": "UAT"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [APPROVED] peer-reviewed 2025-08-10",
                    "env_tag": "UAT"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 2
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                }
            }
        ],
        "outputs": [
                "{\"updated_rule\":{\"rule_id\":\"sgr-fedcba9876543210f\",\"source_ip\":\"10.0.5.0/24\",\"description_contains\":[\"[APPROVED]\",\"peer-reviewed 2025-08-10\",\"[UAT]\"]}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_038",
        "instruction": "For Leo Martinez, determine a retail subtotal for eight Flash Sale Power Banks, subtract $5, and document the result in a low-priority case 'Discount Math Checked'. Provide both the subtotal and the after-discount total.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "113"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Flash Sale Power Bank"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1015",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1015",
                            "quantity": 8,
                            "price": 19.99
                        }
                    ]
                },
            },
            {
                "name": "CalculateDiscountFlat",
                "arguments": {
                    "subtotal": 159.92,
                    "discount_amount": 5
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Discount Math Checked",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"math_check\":{\"product_id\":\"1015\",\"quantity\":8,\"unit_price\":19.99,\"subtotal\":159.92,\"flat_discount\":5,\"total_after_discount\":154.92},\"case_created\":{\"case_id\":\"case_9\",\"status\":\"New\",\"subject\":\"Discount Math Checked\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_039",
        "instruction": "Remove the Mechanical Keyboard from Leo Martinez\u2019s cart and display the final cart, then record a low-priority case titled 'Cart Cleanup Complete'. Provide the final cart contents.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "215"
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "705"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Branded Water Bottle"
                    ]
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "705",
                    "product_ids": [
                        "1017"
                    ]
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "705"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Cart Cleanup Complete",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"final_cart\":[{\"cart_id\":\"705\",\"product_id\":\"1017\",\"quantity\":1}],\"removed_products\":[\"1017\"],\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Cart Cleanup Complete\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_040",
        "instruction": "Facilitate the decommissioning of the dev cache 'dcomm-dev-redis' using the dev rule 'sgr-badbadbadbadbadbad': status 'deleted', name 'Dev Redis (Decommissioned)', note 'failed-provisioning-cleanup', endpoint 'NULL', standardize with '[DEV]' and consolidate to '10.0.5.0/24' 'Redis \u2013 restricted'. Return the final cluster.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "reference_rule_id": "sgr-badbadbadbadbadbad",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "deleted",
                    "new_name": "Dev Redis (Decommissioned)",
                    "note": "failed-provisioning-cleanup",
                    "env_tag": "DEV",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – restricted",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 3
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 4
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 6
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "reference_rule_id": "sgr-badbadbadbadbadbad",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "deleted",
                    "new_name": "Dev Redis (Decommissioned)",
                    "note": "failed-provisioning-cleanup",
                    "env_tag": "DEV",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – restricted",
                    "endpoint_url": "NULL"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 5
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 7
                }
            }
        ],
        "outputs": [
                "{\"cluster\":{\"cluster_id\":\"dcomm-dev-redis\",\"cluster_name\":\"Dev Redis (Decommissioned)\",\"status\":\"deleted\",\"endpoint_url\":\"NULL\",\"instance_type_note\":\"failed-provisioning-cleanup\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_041",
        "instruction": "Handle the review of the UAT Redis ingress identified by 'sgr-fedcba9876543210f'. The intended configuration is source '10.0.5.0/24' with the description 'Redis \u2013 UAT app tier [REVIEWED] rationale: uat-redis-only', ensuring Redis descriptions in that group have '[UAT]'. Provide the revised rule.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [REVIEWED] rationale: uat-redis-only",
                    "env_tag": "UAT"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [REVIEWED] rationale: uat-redis-only",
                    "env_tag": "UAT"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 2
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                }
            }
        ],
        "outputs": [
                "{\"updated_rule\":{\"rule_id\":\"sgr-fedcba9876543210f\",\"source_ip\":\"10.0.5.0/24\",\"description_contains\":[\"Redis – UAT app tier\",\"[REVIEWED]\",\"rationale: uat-redis-only\",\"[UAT]\"]}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_042",
        "instruction": "Coordinate a B2B quote for Mike Rivera for four Server Rack Mount Kit (10-Pack) and five USB-C Hubs, apply B2BVOLUME15, and initiate a medium-priority case titled 'B2BVOLUME15 Evaluation Logged'. Deliver the subtotal, discount, and total after applying the discount.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Susan",
                    "last_name": "Adams"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "112"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Server Rack Mount Kit (10-Pack)",
                        "USB-C Hub"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1008",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1008",
                            "quantity": 4,
                            "price": 450.0
                        },
                        {
                            "product_id": "1002",
                            "quantity": 5,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 2100.0,
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "213",
                    "account_id": "112",
                    "subject": "B2BVOLUME15 Evaluation Logged",
                    "priority": "Medium"
                }
            }
        ],
        "outputs": [
                "{\"offer_evaluation\":{\"contact_id\":\"213\",\"account_id\":\"112\",\"used_pricebook_id\":\"2\",\"subtotal\":2100.0,\"applied_offer_code\":\"B2BVOLUME15\",\"eligible\":true,\"discount_amount\":315.0,\"total_after_discount\":1785.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_043",
        "instruction": "Manage a partial return for Maria Garcia\u2019s order shipped under #9002: restock one 'USB-C Hub', initiate a case 'Return Requested' (Medium), recalculate the returned subtotal, and resolve the case.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9002"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9002"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "order_id": "9002",
                    "subject": "Return Requested",
                    "priority": "Medium"
                },
            },
            {
                "name": "AddStockQuantities",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity_to_add": 1
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"return_processed\":{\"order_id\":\"9002\",\"returned_items_subtotal\":60.0,\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_044",
        "instruction": "Aim to quarantine dev Redis by limiting the rule 'sgr-badbadbadbadbadbad' to '10.0.5.0/24' with the description 'Redis \u2013 restricted [QUARANTINED]' and ensuring descriptions have '[DEV]'. Provide a before/after comparison.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [QUARANTINED]",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [QUARANTINED]",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 2
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                }
            }
        ],
        "outputs": [
                "{\"after_rule\":{\"rule_id\":\"sgr-badbadbadbadbadbad\",\"source_ip\":\"10.0.5.0/24\",\"description_contains\":[\"[QUARANTINED]\",\"[DEV]\"]}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_045",
        "instruction": "Organize Leo Martinez\u2019s cart by setting the Mechanical Keyboard to a quantity of two and removing the Branded Water Bottle, then display the final cart. Provide the final cart contents.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Mechanical Keyboard",
                        "Branded Water Bottle"
                    ]
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "215"
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "705"
                },
            },
            {
                "name": "UpdateItemsInCartBatch",
                "arguments": {
                    "cart_id": "705",
                    "items": [
                        {
                            "product_id": "1017",
                            "new_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "705",
                    "product_ids": [
                        "1012"
                    ]
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "705"
                }
            }
        ],
        "outputs": [
                "{\"final_cart\":[{\"cart_id\":\"705\",\"product_id\":\"1017\",\"quantity\":2}],\"removed_products\":[\"1012\"]}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_046",
        "instruction": "Handle the creation of the 'SPRING12' 12% promo for two 'ProBook X15' at WorldWide Systems B2B pricing. Confirm the stock availability for the two units, display the discounted total, and retire the code.",
        "actions": [
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "SPRING12",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 12
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "ProBook X15"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 2,
                            "price": 1250.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 2500.0,
                    "offer_code": "SPRING12"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "SPRING12"
                }
            }
        ],
        "outputs": [
                "{\"offer_demo\":{\"offer_code\":\"SPRING12\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1001\",\"quantity\":2,\"unit_price\":1250.0,\"line_total\":2500.0}],\"subtotal\":2500.0,\"discount_amount\":300.0,\"total_after_discount\":2200.0,\"final_is_active\":false,\"stock_checked_qty\":2}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_047",
        "instruction": "Coordinate the validation of a retail promotion. Ensure that a 15% code 'SPRING15' is available and confirmed by ID. Demonstrate its effect on two 'ProBook X15' at retail pricing for Leo Martinez, and then retire the code. Provide the subtotal, discount, total, and the final active flag in return.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "113"
                },
            },
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "SPRING15",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 15
                },
            },
            {
                "name": "GetOfferDetails",
                "arguments": {
                    "offer_id": "offer_5"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "ProBook X15"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 2,
                            "price": 1500.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 3000.0,
                    "offer_code": "SPRING15"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "SPRING15"
                },
            },
            {
                "name": "GetOfferDetails",
                "arguments": {
                    "offer_id": "offer_5"
                }
            }
        ],
        "outputs": [
                "{\"offer_demo\":{\"offer_code\":\"SPRING15\",\"used_pricebook_id\":\"1\",\"subtotal\":3000.0,\"discount_amount\":450.0,\"total_after_discount\":2550.0,\"final_is_active\":false}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_048",
        "instruction": "Confirm B2B stock and calculate a B2B subtotal for Nora Patel for thirty '1TB NVMe SSD'. Then, open and resolve a case 'Bulk Stock & Estimate Prepared' (Low) by summarizing the result.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "109"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "1TB NVMe SSD"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "required_quantity": 30
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "quantity": 30,
                            "price": 95.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Bulk Stock & Estimate Prepared",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"stock_and_estimate\":{\"contact_id\":\"210\",\"account_id\":\"109\",\"used_pricebook_id\":\"2\",\"product_id\":\"1016\",\"requested_qty\":30,\"unit_price\":95.0,\"subtotal\":2850.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Bulk Stock & Estimate Prepared\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_049",
        "instruction": "You need to quarantine the dev cache 'dcomm-dev-redis' using the dev rule 'sgr-badbadbadbadbadbad'. Set subnet group to 'esg-uat-1', status 'failed', name 'Dev Redis (Quarantined)', note 'quarantined for review', standardize Redis with '[DEV]', and consolidate to '10.0.5.0/24' with description 'Redis \u2013 restricted'. Keep the endpoint unchanged. Return the final cluster.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "reference_rule_id": "sgr-badbadbadbadbadbad",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "failed",
                    "new_name": "Dev Redis (Quarantined)",
                    "note": "quarantined for review",
                    "env_tag": "DEV",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – restricted",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 3
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 4
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 5
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 6
                }
            }
        ],
        "outputs": [
                "{\"cluster\":{\"cluster_id\":\"dcomm-dev-redis\",\"cluster_name\":\"Dev Redis (Quarantined)\",\"status\":\"failed\",\"subnet_group_id\":\"esg-uat-1\",\"instance_type_note\":\"quarantined for review\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_050",
        "instruction": "Quarantine dev Redis access without removing rules by limiting the group for 'sgr-badbadbadbadbadbad' to '10.0.5.0/24' with description 'Redis \u2013 restricted [QUARANTINED]' and standardizing with '[DEV]'. Provide a summary of what was removed or changed.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [QUARANTINED]",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [QUARANTINED]",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 2
                },
            },
            {
                "name": "InventorySecurityGroupRules",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                "{\"changed_rule\":{\"rule_id\":\"sgr-badbadbadbadbadbad\",\"source_ip\":\"10.0.5.0/24\",\"description_contains\":[\"[QUARANTINED]\",\"[DEV]\"]}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_051",
        "instruction": "Initiate a case titled 'Address Update' for Moonbeam Corp, modify the address to '555 Galaxy Blvd, Suite 20', conduct a spot-check on B2B pricing and stock for one 1TB NVMe SSD, and then close the case.",
        "actions": [
            {
                "name": "GetAccountByName",
                "arguments": {
                    "name": "Moonbeam Corp"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Address Update",
                    "priority": "Medium"
                },
            },
            {
                "name": "UpdateStreetAddress",
                "arguments": {
                    "account_id": "109",
                    "new_shipping_street": "555 Galaxy Blvd, Suite 20",
                    "new_billing_street": "555 Galaxy Blvd, Suite 20"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "1TB NVMe SSD"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "quantity": 1,
                            "price": 95.0
                        }
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "required_quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"address_update\":{\"account_id\":\"109\",\"shipping_street\":\"555 Galaxy Blvd, Suite 20\",\"billing_street\":\"555 Galaxy Blvd, Suite 20\"},\"spot_check\":{\"product_id\":\"1016\",\"used_pricebook_id\":\"2\",\"unit_price\":95.0,\"subtotal_qty1\":95.0,\"stock_checked_qty\":1},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_052",
        "instruction": "Erase the items in Nora Patel\u2019s cart, then include one 'USB-C Hub' and one 'Wireless Mouse', validate stock availability, check the price at B2B (id '2'), and present the subtotal.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "210"
                },
            },
            {
                "name": "ClearCart",
                "arguments": {
                    "cart_id": "704"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "USB-C Hub",
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "required_quantity": 1
                        },
                        {
                            "product_id": "1003",
                            "required_quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "AddItemsToCartBatch",
                "arguments": {
                    "cart_id": "704",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        },
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1003",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1,
                            "price": 60.0
                        },
                        {
                            "product_id": "1003",
                            "quantity": 1,
                            "price": 32.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\"cart_quote\":{\"cart_id\":\"704\",\"contact_id\":\"210\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1002\",\"quantity\":1,\"unit_price\":60.0,\"line_total\":60.0},{\"product_id\":\"1003\",\"quantity\":1,\"unit_price\":32.0,\"line_total\":32.0}],\"subtotal\":92.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_053",
        "instruction": "Cancel David Chen\u2019s order #9010 due to 'Ordered By Mistake' (High). Create a case and proceed with restocking the items.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Mike",
                    "last_name": "Rivera"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9010"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9010"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "209",
                    "account_id": "108",
                    "order_id": "9010",
                    "subject": "Ordered By Mistake",
                    "priority": "High"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "9010",
                    "new_status": "Cancelled"
                },
            },
            {
                "name": "AddStockQuantities",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1005",
                            "quantity_to_add": 1
                        },
                        {
                            "product_id": "1011",
                            "quantity_to_add": 5
                        }
                    ]
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"order_update\":{\"order_id\":\"9010\",\"final_status\":\"Cancelled\"},\"restocked\":[{\"product_id\":\"1005\",\"stock_quantity\":26},{\"product_id\":\"1011\",\"stock_quantity\":80}],\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_054",
        "instruction": "Generate a new fixed $5 promo code 'CLEARANCE5', verify it by ID, implement it on ten 'Flash Sale Power Bank', then deactivate it and confirm by ID.",
        "actions": [
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "CLEARANCE5",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 5
                },
            },
            {
                "name": "GetOfferDetails",
                "arguments": {
                    "offer_id": "offer_5"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Flash Sale Power Bank"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1015",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1015",
                            "quantity": 10,
                            "price": 19.99
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 199.9,
                    "offer_code": "CLEARANCE5"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "CLEARANCE5"
                },
            },
            {
                "name": "GetOfferDetails",
                "arguments": {
                    "offer_id": "offer_5"
                }
            }
        ],
        "outputs": [
                "{\"offer_status\":{\"offer_code\":\"CLEARANCE5\",\"checked_offer_id\":\"offer_5\",\"created\":true,\"applied_demo\":{\"product_id\":\"1015\",\"subtotal\":199.9,\"discount_amount\":5,\"total_after_discount\":194.9},\"final_is_active\":false}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_055",
        "instruction": "Replenish one 'USB-C Hub (Deluxe)' from Alice Johnson\u2019s delivered order #9005; if the precise variant is not present in the catalog, utilize the standard 'USB-C Hub'. Update the order status to Returned and document a low-priority case named 'Partial Return \u2212 1 item'.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9005"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9005"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "USB-C Hub (Deluxe)",
                        "USB-C Hub"
                    ]
                },
            },
            {
                "name": "AddStockQuantities",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1006",
                            "quantity_to_add": 1
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "207",
                    "account_id": "106",
                    "order_id": "9005",
                    "subject": "Partial Return − 1 item",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "9005",
                    "new_status": "Returned"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9005"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"return_processed\":{\"order_id\":\"9005\",\"order_status\":\"Returned\",\"restock_input\":[{\"product_id\":\"1006\",\"quantity_added\":1}],\"case_update\":{\"case_id\":\"case_9\",\"subject\":\"Partial Return − 1 item\",\"final_status\":\"Resolved\"}}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_056",
        "instruction": "Handle the reorganization of David Chen\u2019s cart: adjust 'Ergo Laptop Stand' to a quantity of 3, exclude 'Branded Water Bottle', confirm the stand's stock, and provide the final list of items.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Sandra",
                    "last_name": "Dee"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "208"
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "703"
                },
            },
            {
                "name": "UpdateItemsInCartBatch",
                "arguments": {
                    "cart_id": "703",
                    "items": [
                        {
                            "product_id": "1010",
                            "new_quantity": 3
                        }
                    ]
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "703",
                    "product_ids": [
                        "1012"
                    ]
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Ergo Laptop Stand",
                        "Branded Water Bottle"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1010",
                            "required_quantity": 3
                        }
                    ]
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "703"
                }
            }
        ],
        "outputs": [
                "{\"final_cart\":[{\"cart_id\":\"703\",\"product_id\":\"1010\",\"quantity\":3}],\"removed_products\":[\"1012\"],\"stock_check\":{\"product_id\":\"1010\",\"qty\":3}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_057",
        "instruction": "Coordinate a B2B quotation for Nora Patel for two 1TB NVMe SSDs, apply WINTER20, check stock levels, and initiate a low-priority case titled 'B2B Quote Prepared'. Provide the subtotal, discount, and the total after discount.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "109"
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "quantity": 2,
                            "price": 95.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 190.0,
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "B2B Quote Prepared",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"210\",\"account_id\":\"109\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1016\",\"quantity\":2,\"unit_price\":95.0,\"line_total\":190.0}],\"subtotal\":190.0,\"applied_offer_code\":\"WINTER20\",\"discount_amount\":38.0,\"total_after_discount\":152.0},\"case\":{\"subject\":\"B2B Quote Prepared\",\"priority\":\"Low\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_058",
        "instruction": "Organize a complete return for delivered order #9005 by replenishing the items and updating the order status to Returned. Supply a concise receipt with the final status and revised stock counts.",
        "actions": [
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9005"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9005"
                },
            },
            {
                "name": "AddStockQuantities",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1006",
                            "quantity_to_add": 2
                        },
                        {
                            "product_id": "1003",
                            "quantity_to_add": 1
                        }
                    ]
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "9005",
                    "new_status": "Returned"
                }
            }
        ],
        "outputs": [
                "{\"return_receipt\":{\"order_id\":\"9005\",\"restocked\":[{\"product_id\":\"1006\",\"quantity_added\":2},{\"product_id\":\"1003\",\"quantity_added\":1}],\"final_status\":\"Returned\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_059",
        "instruction": "Coordinate a B2B quote for Maria Garcia for six ProBook X15, verify the 10% discount calculation, and document the result in a low-priority case titled 'B2B Math Check'. Provide the subtotal and the discounted total.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "ProBook X15"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 6,
                            "price": 1250.0
                        }
                    ]
                },
            },
            {
                "name": "CalculateDiscountPercent",
                "arguments": {
                    "subtotal": 7500.0,
                    "discount_percent": 10
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "B2B Math Check",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"math_check\":{\"product_id\":\"1001\",\"quantity\":6,\"unit_price\":1250.0,\"subtotal\":7500.0,\"percent_discount\":10,\"total_after_discount\":6750.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"B2B Math Check\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_060",
        "instruction": "Execute a swift retail pricing review for Alice Johnson on one 'Wireless Mouse' and record the outcome by opening and closing a case.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "106"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1,
                            "price": 40.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "207",
                    "account_id": "106",
                    "subject": "Retail Price Check",
                    "priority": "Medium"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"price_check\":{\"contact_id\":\"207\",\"account_id\":\"106\",\"used_pricebook_id\":\"1\",\"items\":[{\"product_id\":\"1003\",\"quantity\":1,\"unit_price\":40.0,\"line_total\":40.0}],\"subtotal\":40.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Retail Price Check\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_061",
        "instruction": "Set the description for subnet group 'esg-uat-1' to 'Subnets for UAT caches [REVIEWED 2025-08-10]'. Strengthen 'dcomm-uat-redis' using UAT rule 'sgr-fedcba9876543210f': attach to 'esg-uat-1', ensure the status is 'available', give it the name 'UAT Redis Cache [Reviewed]', annotate with 'subnet group reviewed 2025-08-10', align with '[UAT]' and integrate into '10.0.5.0/24' 'Redis \u2013 UAT app tier'. Return both subnet group and cluster.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "UpdateSubnetGroupDescription",
                "arguments": {
                    "subnet_group_id": "esg-uat-1",
                    "new_description": "Subnets for UAT caches [REVIEWED 2025-08-10]"
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "reference_rule_id": "sgr-fedcba9876543210f",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "available",
                    "new_name": "UAT Redis Cache [Reviewed]",
                    "note": "subnet group reviewed 2025-08-10",
                    "env_tag": "UAT",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – UAT app tier",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 3
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 4
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 6
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "reference_rule_id": "sgr-fedcba9876543210f",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "available",
                    "new_name": "UAT Redis Cache [Reviewed]",
                    "note": "subnet group reviewed 2025-08-10",
                    "env_tag": "UAT",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – UAT app tier",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 5
                }
            }
        ],
        "outputs": [
                "{\"subnet_group\":{\"subnet_group_id\":\"esg-uat-1\",\"description\":\"Subnets for UAT caches [REVIEWED 2025-08-10]\"},\"cluster\":{\"cluster_id\":\"dcomm-uat-redis\",\"cluster_name\":\"UAT Redis Cache [Reviewed]\",\"status\":\"available\",\"instance_type_note\":\"subnet group reviewed 2025-08-10\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_062",
        "instruction": "Assess the 'Q4SAVE10' 10% promotion on a single 'ProBook X15' at B2B pricing, confirm one unit's availability, and subsequently deactivate the promo code.",
        "actions": [
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "Q4SAVE10",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 10
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "ProBook X15"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "required_quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 1,
                            "price": 1250.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 1250.0,
                    "offer_code": "Q4SAVE10"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "Q4SAVE10"
                }
            }
        ],
        "outputs": [
                "{\"offer_demo\":{\"offer_code\":\"Q4SAVE10\",\"used_pricebook_id\":\"2\",\"subtotal\":1250.0,\"discount_amount\":125.0,\"total_after_discount\":1125.0,\"final_is_active\":false,\"stock_checked_qty\":1}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_063",
        "instruction": "Transfer the dev group's Redis access according to rule 'sgr-badbadbadbadbadbad' to CIDR '10.0.5.0/24', described as 'Redis \u2013 restricted [LOCKED] remediation:redis-open', and align with '[DEV]'. Provide a before and after comparison.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [LOCKED] remediation:redis-open",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [LOCKED] remediation:redis-open",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 2
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                }
            }
        ],
        "outputs": [
                "{\"after_rule\":{\"rule_id\":\"sgr-badbadbadbadbadbad\",\"source_ip\":\"10.0.5.0/24\",\"description_contains\":[\"[LOCKED]\",\"remediation:redis-open\",\"[DEV]\"]}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_064",
        "instruction": "Audit 'dcomm-dev-redis' on subnet group 'esg-uat-1' and maintain its health. Ensure it associates with the security group 'sgr-badbadbadbadbadbad', concludes with status 'available', and incorporates the note 'subnet-audit-complete' under the name 'Dev Redis (Audit)'. Return the final state of the cluster.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "reference_rule_id": "sgr-badbadbadbadbadbad",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "available",
                    "new_name": "Dev Redis (Audit)",
                    "note": "subnet-audit-complete",
                    "env_tag": "DEV",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – restricted",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 3
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 4
                }
            }
        ],
        "outputs": [
                "{\"cluster\":{\"cluster_id\":\"dcomm-dev-redis\",\"cluster_name\":\"Dev Redis (Audit)\",\"status\":\"available\",\"subnet_group_id\":\"esg-uat-1\",\"instance_type_note\":\"subnet-audit-complete\"}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_065",
        "instruction": "Change Starlight Enterprises\u2019 address to '555 Galaxy Blvd, Suite 100', take a B2B price snapshot for a 1TB NVMe SSD, and resolve the associated case. Provide the updated addresses, the final status of the case, and the snapshot subtotal.",
        "actions": [
            {
                "name": "GetAccountByName",
                "arguments": {
                    "name": "Moonbeam Corp"
                },
            },
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "1TB NVMe SSD"
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Address Update",
                    "priority": "Medium"
                },
            },
            {
                "name": "UpdateStreetAddress",
                "arguments": {
                    "account_id": "109",
                    "new_shipping_street": "555 Galaxy Blvd, Suite 100",
                    "new_billing_street": "555 Galaxy Blvd, Suite 100"
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "quantity": 1,
                            "price": 95.0
                        }
                    ]
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"address_update\":{\"account_id\":\"109\",\"shipping_street\":\"555 Galaxy Blvd, Suite 100\",\"billing_street\":\"555 Galaxy Blvd, Suite 100\"},\"case_receipt\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"},\"price_snapshot\":{\"product_id\":\"1016\",\"used_pricebook_id\":\"2\",\"subtotal_qty1\":95.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_066",
        "instruction": "Handle the creation of a case and reorganize David Chen\u2019s cart: adjust 'Ergo Laptop Stand' to a quantity of 2, eliminate 'Branded Water Bottle', and close a case 'Cart Ready' (Low).",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Sandra",
                    "last_name": "Dee"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "208"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "208",
                    "account_id": "107",
                    "subject": "Cart Ready",
                    "priority": "Low"
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "703"
                },
            },
            {
                "name": "UpdateItemsInCartBatch",
                "arguments": {
                    "cart_id": "703",
                    "items": [
                        {
                            "product_id": "1010",
                            "new_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "703",
                    "product_ids": [
                        "1012"
                    ]
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"final_cart\":[{\"cart_id\":\"703\",\"product_id\":\"1010\",\"quantity\":2}],\"removed_products\":[\"1012\"],\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_067",
        "instruction": "Coordinate the restocking of one 'USB-C Hub (Deluxe)' from Alice Johnson\u2019s completed order #9005; if the specific variant isn't listed, opt for the standard 'USB-C Hub'. Change the order status to Returned and log a low-priority case named 'Partial Return \u2212 1 item'.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9005"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9005"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "USB-C Hub"
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "207",
                    "account_id": "106",
                    "order_id": "9005",
                    "subject": "Partial Return − 1 item",
                    "priority": "Low"
                },
            },
            {
                "name": "AddStockQuantities",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1006",
                            "quantity_to_add": 1
                        }
                    ]
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "9005",
                    "new_status": "Returned"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"return_processed\":{\"order_id\":\"9005\",\"restocked\":[{\"product_id\":\"1006\",\"quantity_added\":1}],\"final_order_status\":\"Returned\",\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_068",
        "instruction": "Ensure the HTTPS ingress rule 'sgr-1122334455667788a' retains source '0.0.0.0/0' and includes the description 'Allow inbound HTTPS [APPROVED] baseline:2025-08-10 owner:cloud-netops'. Additionally, align Redis 6379 descriptions on the UAT group identified by 'sgr-fedcba9876543210f' with '[UAT]'. Submit the revised HTTPS rule along with the UAT standardization tally.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-1122334455667788a"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-1122334455667788a",
                    "target_cidr": "0.0.0.0/0",
                    "final_description": "Allow inbound HTTPS [APPROVED] baseline:2025-08-10 owner:cloud-netops",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-1122334455667788a"
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier",
                    "env_tag": "UAT"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 2
                },
            },
            {
                "name": "InventorySecurityGroupRules",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                "{\"https_rule\":{\"rule_id\":\"sgr-1122334455667788a\",\"source_ip\":\"0.0.0.0/0\",\"description\":\"Allow inbound HTTPS [APPROVED] baseline:2025-08-10 owner:cloud-netops\"},\"uat_standardized_added\":\">=0\"}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_069",
        "instruction": "Reinforce dev Redis access within the security group identified by 'sgr-badbadbadbadbadbad'. The intended final state is a solitary 6379/TCP ingress confined to '10.0.5.0/24' with a description containing 'Redis \u2013 restricted', '[LOCKED]' and '[risk:open-redis]'; and every Redis rule description in that group must feature the '[DEV]' tag. Offer a brief before-and-after comparison.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [LOCKED] [risk:open-redis]",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "InventorySecurityGroupRules",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                }
            }
        ],
        "outputs": [
                "{\"final_rule_contains\":{\"rule_id\":\"sgr-badbadbadbadbadbad\",\"source_ip\":\"10.0.5.0/24\",\"description_contains\":[\"[LOCKED]\",\"[risk:open-redis]\",\"[DEV]\"]}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_070",
        "instruction": "Administer the purchase of two 'Mechanical Keyboard' for Nora Patel at retail. Start with an empty cart (clear Nora Patel\u2019s cart), establish promo 'GEAR25' ($25 off, fixed amount), confirm inventory for two units of product_id '1017', add two to Kevin\u2019s cart, compute the retail subtotal via pricebook '1', apply 'GEAR25', then deactivate the promotion. Report cart id, subtotal, discount and total.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "210"
                },
            },
            {
                "name": "ClearCart",
                "arguments": {
                    "cart_id": "704"
                },
            },
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "GEAR25",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 25
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Mechanical Keyboard"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1017",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1017",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "AddItemsToCartBatch",
                "arguments": {
                    "cart_id": "704",
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 2,
                            "price": 150.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 300.0,
                    "offer_code": "GEAR25"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "GEAR25"
                }
            }
        ],
        "outputs": [
                "{\"purchase\":{\"cart_id\":\"704\",\"product_id\":\"1017\",\"used_pricebook_id\":\"1\",\"subtotal\":300.0,\"discount_amount\":25.0,\"total_after_discount\":275.0,\"final_is_active\":false,\"stock_checked_qty\":2}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_071",
        "instruction": "You organize a B2B bulk quote for Maria Garcia for three 'Server Rack Mount Kit (10-Pack)' and one 'ProBook X15'. Assess 'B2BVOLUME15', and initiate and finalize a case 'Bulk Quote Evaluated' (Low).",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Server Rack Mount Kit (10-Pack)",
                        "ProBook X15"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1008",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1008",
                            "quantity": 3,
                            "price": 450.0
                        },
                        {
                            "product_id": "1001",
                            "quantity": 1,
                            "price": 1250.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 2600.0,
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Bulk Quote Evaluated",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"evaluation\":{\"subtotal\":2600.0,\"applied_offer_code\":\"B2BVOLUME15\",\"discount_amount\":390.0,\"total_after_discount\":2210.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_072",
        "instruction": "Coordinate a deterministic B2B price check for Nora Patel at Starlight: start from an empty cart, incorporate two 'ProBook X15', apply WINTER20, verify availability, and deliver subtotal, discount, and total.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "109"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "210"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "ProBook X15"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ClearCart",
                "arguments": {
                    "cart_id": "704"
                },
            },
            {
                "name": "AddItemsToCartBatch",
                "arguments": {
                    "cart_id": "704",
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 2,
                            "price": 1250.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 2500.0,
                    "offer_code": "WINTER20"
                }
            }
        ],
        "outputs": [
                "{\"receipt\":{\"cart_id\":\"704\",\"used_pricebook_id\":\"2\",\"applied_offer_code\":\"WINTER20\",\"items\":[{\"product_id\":\"1001\",\"quantity\":2,\"unit_price\":1250.0,\"line_total\":2500.0}],\"subtotal\":2500.0,\"discount_amount\":500.0,\"total_after_discount\":2000.0}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_073",
        "instruction": "You should adjust the Mechanical Keyboard to quantity two and eliminate the Branded Water Bottle in Leo Martinez\u2019s cart, then determine the retail subtotal for the keyboards. Provide the subtotal.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "113"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Mechanical Keyboard",
                        "Branded Water Bottle"
                    ]
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "215"
                },
            },
            {
                "name": "UpdateItemsInCartBatch",
                "arguments": {
                    "cart_id": "705",
                    "items": [
                        {
                            "product_id": "1017",
                            "new_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "705",
                    "product_ids": [
                        "1012"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1017",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 2,
                            "price": 150.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\"final_cart\":[{\"cart_id\":\"705\",\"product_id\":\"1017\",\"quantity\":2}],\"removed_products\":[\"1012\"],\"pricing\":{\"product_id\":\"1017\",\"used_pricebook_id\":\"1\",\"unit_price\":150.0,\"subtotal\":300.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_074",
        "instruction": "Set up the '$10' promo 'WELCOME10' and apply it on two 'Wireless Mouse' at retail for Leo Martinez, providing subtotal, code, discount, and total.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "113"
                },
            },
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "WELCOME10",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 10
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 2,
                            "price": 40.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 80.0,
                    "offer_code": "WELCOME10"
                }
            }
        ],
        "outputs": [
                "{\"offer_demo\":{\"contact_id\":\"215\",\"account_id\":\"113\",\"product_id\":\"1003\",\"used_pricebook_id\":\"1\",\"subtotal\":80.0,\"applied_offer_code\":\"WELCOME10\",\"discount_amount\":10.0,\"total_after_discount\":70.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_075",
        "instruction": "You annul David Chen\u2019s order #9010, replenish its items from the order lines, and conclude a case 'Ordered By Mistake' (High).",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Mike",
                    "last_name": "Rivera"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9010"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9010"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "209",
                    "account_id": "108",
                    "order_id": "9010",
                    "subject": "Ordered By Mistake",
                    "priority": "High"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "9010",
                    "new_status": "Cancelled"
                },
            },
            {
                "name": "AddStockQuantities",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1005",
                            "quantity_to_add": 1
                        },
                        {
                            "product_id": "1011",
                            "quantity_to_add": 5
                        }
                    ]
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"order_update\":{\"order_id\":\"9010\",\"final_status\":\"Cancelled\"},\"restocked\":[{\"product_id\":\"1005\",\"stock_quantity\":26},{\"product_id\":\"1011\",\"stock_quantity\":80}],\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_076",
        "instruction": "Ensure the HTTPS ingress rule 'sgr-1122334455667788a' retains source '0.0.0.0/0' and applies the description 'Allow inbound HTTPS [APPROVED] owner:cloud-netops baseline:2025-08-10'. Provide the updated rule and inventory.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-1122334455667788a"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-1122334455667788a",
                    "target_cidr": "0.0.0.0/0",
                    "final_description": "Allow inbound HTTPS [APPROVED] owner:cloud-netops baseline:2025-08-10",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "InventorySecurityGroupRules",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-1122334455667788a"
                }
            }
        ],
        "outputs": [
                "{\"updated_rule\":{\"rule_id\":\"sgr-1122334455667788a\",\"source_ip\":\"0.0.0.0/0\",\"description\":\"Allow inbound HTTPS [APPROVED] owner:cloud-netops baseline:2025-08-10\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_077",
        "instruction": "Confirm 'dcomm-uat-redis' with the UAT rule 'sgr-fedcba9876543210f': keep using subnet group 'esg-uat-1', maintain the endpoint as (NOCHANGE), assign status 'available', set name 'UAT Redis Cache', and note 'cache.t3.medium [confirmed]'. Organize Redis 6379 to '10.0.5.0/24' using the description 'Redis \u2013 UAT app tier', ensuring standardization with '[UAT]' as a separate step. Provide the final cluster.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "reference_rule_id": "sgr-fedcba9876543210f",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "available",
                    "new_name": "UAT Redis Cache",
                    "note": "cache.t3.medium [confirmed]",
                    "env_tag": "UAT",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – UAT app tier",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 3
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 4
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 5
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 6
                }
            }
        ],
        "outputs": [
                "{\"cluster\":{\"cluster_id\":\"dcomm-uat-redis\",\"cluster_name\":\"UAT Redis Cache\",\"status\":\"available\",\"instance_type_note\":\"cache.t3.medium [confirmed]\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_078",
        "instruction": "Implement the 'SMALL5' 5% promo for Global Tech Inc, confirm it on five 'USB-C Hub' at B2B pricing, and subsequently disable the code.",
        "actions": [
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "SMALL5",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 5
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "USB-C Hub"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 5,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 300.0,
                    "offer_code": "SMALL5"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "SMALL5"
                }
            }
        ],
        "outputs": [
                "{\"offer_demo\":{\"account_id\":\"101\",\"offer_code\":\"SMALL5\",\"used_pricebook_id\":\"2\",\"product_id\":\"1002\",\"subtotal\":300.0,\"discount_amount\":15.0,\"total\":285.0,\"final_is_active\":false}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_079",
        "instruction": "Reinforce 'dcomm-uat-redis' by using the UAT rule 'sgr-fedcba9876543210f'. Ensure the endpoint remains the same (NOCHANGE). Apply env_tag 'UAT' (unbracketed) for standardization. Provide the final cluster.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "reference_rule_id": "sgr-fedcba9876543210f",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "available",
                    "new_name": "UAT Redis Cache",
                    "note": "change_reason: subnet-hygiene",
                    "env_tag": "UAT",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – UAT app tier",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 3
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 4
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 5
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 6
                }
            }
        ],
        "outputs": [
                "{\"cluster\":{\"cluster_id\":\"dcomm-uat-redis\",\"cluster_name\":\"UAT Redis Cache\",\"status\":\"available\",\"subnet_group_id\":\"esg-uat-1\",\"instance_type_note\":\"change_reason: subnet-hygiene\"}}"
        ]
    }
    ,
    {
        "annotator": dc,
        "user_id": "task_080",
        "instruction": "Apply B2B pricing for two ProBook X15 for Maria Garcia at Pioneer Technologies, use WINTER20, check stock, and provide the subtotal, discount, and total after discount.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Emily",
                    "last_name": "White"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "102"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "203"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "ProBook X15"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ClearCart",
                "arguments": {
                    "cart_id": "701"
                },
            },
            {
                "name": "AddItemsToCartBatch",
                "arguments": {
                    "cart_id": "701",
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 2,
                            "price": 1250.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 2500.0,
                    "offer_code": "WINTER20"
                }
            }
        ],
        "outputs": [
                "{\"receipt\":{\"cart_id\":\"701\",\"used_pricebook_id\":\"2\",\"applied_offer_code\":\"WINTER20\",\"items\":[{\"product_id\":\"1001\",\"quantity\":2,\"unit_price\":1250.0,\"line_total\":2500.0}],\"subtotal\":2500.0,\"discount_amount\":500.0,\"total_after_discount\":2000.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_081",
        "instruction": "Handle a B2B quote for Maria Garcia at WorldWide Systems for three 'USB-C Hub' and two 'Wireless Mouse'. Apply 'WINTER20', then initiate and resolve a case 'B2B Quote Prepared' (Low) with the totals.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "USB-C Hub",
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1003",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 3,
                            "price": 60.0
                        },
                        {
                            "product_id": "1003",
                            "quantity": 2,
                            "price": 32.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 244.0,
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "B2B Quote Prepared",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"201\",\"account_id\":\"101\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1002\",\"quantity\":3,\"unit_price\":60.0,\"line_total\":180.0},{\"product_id\":\"1003\",\"quantity\":2,\"unit_price\":32.0,\"line_total\":64.0}],\"subtotal\":244.0,\"applied_offer_code\":\"WINTER20\",\"discount_amount\":48.8,\"total_after_discount\":195.2},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_082",
        "instruction": "Coordinate the creation of the 'Q4SAVE10' 10% promo, assess it on one 'ProBook X15' at B2B pricing, and subsequently retire the code.",
        "actions": [
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "Q4SAVE10",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 10
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "ProBook X15"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 1,
                            "price": 1250.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 1250.0,
                    "offer_code": "Q4SAVE10"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "Q4SAVE10"
                }
            }
        ],
        "outputs": [
                "{\"offer_demo\":{\"offer_code\":\"Q4SAVE10\",\"used_pricebook_id\":\"2\",\"subtotal\":1250.0,\"discount_amount\":125.0,\"total_after_discount\":1125.0,\"final_is_active\":false}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_083",
        "instruction": "You should standardize and consolidate the UAT group's Redis using UAT rule 'sgr-fedcba9876543210f': establish a single '10.0.5.0/24' rule with the description 'Redis \u2013 UAT app tier change-mgr:CR-2219' and tag '[UAT]'. Provide a summary.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier change-mgr:CR-2219",
                    "env_tag": "UAT"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                }
            }
        ],
        "outputs": [
                "{\"summary\":{\"rule_id\":\"sgr-fedcba9876543210f\",\"source_ip\":\"10.0.5.0/24\",\"description_contains\":[\"change-mgr:CR-2219\",\"[UAT]\"]}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_084",
        "instruction": "For David Chen, adjust the Ergo Laptop Stand to two units and eliminate the Branded Water Bottle. Display the final cart and verify stock for the stand. Initiate a low-priority case 'Cart Ready'.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Sandra",
                    "last_name": "Dee"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "208"
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "703"
                },
            },
            {
                "name": "UpdateItemsInCartBatch",
                "arguments": {
                    "cart_id": "703",
                    "items": [
                        {
                            "product_id": "1010",
                            "new_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "703",
                    "product_ids": [
                        "1012"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1010",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "208",
                    "account_id": "107",
                    "subject": "Cart Ready",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "{\"final_cart\":[{\"cart_id\":\"703\",\"product_id\":\"1010\",\"quantity\":2}],\"removed_products\":[\"1012\"],\"stock_check\":{\"product_id\":\"1010\",\"qty\":2},\"case_created\":{\"case_id\":\"case_9\",\"status\":\"New\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_085",
        "instruction": "Arrange a B2B bulk quote for Nora Patel for twenty 1TB NVMe SSDs, confirm stock, and commence a low-priority case titled 'Bulk Stock Verified'. Return the subtotal.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Kevin",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "109"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "1TB NVMe SSD"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "required_quantity": 20
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1016",
                            "quantity": 20,
                            "price": 95.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Bulk Stock Verified",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"stock_and_estimate\":{\"product_id\":\"1016\",\"requested_qty\":20,\"used_pricebook_id\":\"2\",\"subtotal\":1900.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_086",
        "instruction": "You need to clear Maria Garcia\u2019s cart, insert two USB-C Hubs and one Wireless Mouse at B2B rates, display the cart, then increase the hubs to three and provide the updated items and subtotal.",
        "actions": [
            {
                "name": "ClearCart",
                "arguments": {
                    "cart_id": "701"
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "required_quantity": 3
                        },
                        {
                            "product_id": "1003",
                            "required_quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "AddItemsToCartBatch",
                "arguments": {
                    "cart_id": "701",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 2
                        },
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "701"
                },
            },
            {
                "name": "UpdateItemsInCartBatch",
                "arguments": {
                    "cart_id": "701",
                    "items": [
                        {
                            "product_id": "1002",
                            "new_quantity": 3
                        }
                    ]
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "701"
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1003",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 3,
                            "price": 60.0
                        },
                        {
                            "product_id": "1003",
                            "quantity": 1,
                            "price": 32.0
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\"updated_quote\":{\"cart_id\":\"701\",\"used_pricebook_id\":\"2\",\"items_after_update\":[{\"product_id\":\"1002\",\"quantity\":3},{\"product_id\":\"1003\",\"quantity\":1}],\"subtotal\":212.0}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_087",
        "instruction": "Your task is to replace permissive UAT Redis entries by integrating via rule 'sgr-fedcba9876543210f' into a single '10.0.5.0/24' rule, described as 'Redis \u2013 UAT app tier [CONSOLIDATED]' and ensure standardization with '[UAT]'.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [CONSOLIDATED]",
                    "env_tag": "UAT"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                }
            }
        ],
        "outputs": [
                "{\"final_rule\":{\"rule_id\":\"sgr-fedcba9876543210f\",\"source_ip\":\"10.0.5.0/24\",\"description_contains\":[\"[CONSOLIDATED]\",\"[UAT]\"]}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_088",
        "instruction": "You initiate and terminate the 'TEAM15' fixed $15 promo on two 'Wireless Mouse' at the retail rate.",
        "actions": [
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "TEAM15",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 15
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 2,
                            "price": 40.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 80.0,
                    "offer_code": "TEAM15"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "TEAM15"
                }
            }
        ],
        "outputs": [
                "{\"offer_demo\":{\"offer_code\":\"TEAM15\",\"used_pricebook_id\":\"1\",\"product_id\":\"1003\",\"subtotal\":80.0,\"discount_amount\":15.0,\"total_after_discount\":65.0,\"final_is_active\":false}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_089",
        "instruction": "You generate a retail quote for Nora Patel for a webcam and two wireless mice, apply WELCOME5, and address a case.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Davis"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "110"
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "pricebook_id": "1"
                        },
                        {
                            "product_id": "1003",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 1,
                            "price": 199.0
                        },
                        {
                            "product_id": "1003",
                            "quantity": 2,
                            "price": 40.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 279.0,
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "211",
                    "account_id": "110",
                    "subject": "Retail Quote Prepared",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"211\",\"account_id\":\"110\",\"used_pricebook_id\":\"1\",\"items\":[{\"product_id\":\"1018\",\"quantity\":1,\"unit_price\":199.0},{\"product_id\":\"1003\",\"quantity\":2,\"unit_price\":40.0}],\"subtotal\":279.0,\"applied_offer_code\":\"WELCOME5\",\"discount_amount\":5.0,\"total_after_discount\":274.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_090",
        "instruction": "The objective is to fortify 'dcomm-uat-redis' using the UAT rule 'sgr-fedcba9876543210f': subnet 'esg-uat-1', status 'available', title 'UAT Redis Cache (Hardened)', note 'hardened 2025-08-10', standardize with '[UAT]' and consolidate to '10.0.5.0/24' 'Redis \u2013 UAT app tier', endpoint 'NULL'.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "reference_rule_id": "sgr-fedcba9876543210f",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "available",
                    "new_name": "UAT Redis Cache (Hardened)",
                    "note": "hardened 2025-08-10",
                    "env_tag": "UAT",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – UAT app tier",
                    "endpoint_url": "NULL"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 3
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 4
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 5
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 6
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 7
                }
            }
        ],
        "outputs": [
                "{\"cluster\":{\"cluster_id\":\"dcomm-uat-redis\",\"cluster_name\":\"UAT Redis Cache (Hardened)\",\"status\":\"available\",\"subnet_group_id\":\"esg-uat-1\",\"instance_type_note\":\"hardened 2025-08-10\",\"endpoint_url\":\"NULL\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_091",
        "instruction": "Initiate an update to the subnet group 'esg-prod-1' by modifying the description to 'Subnets for production Redis and Memcached [REVIEWED]'. Align the environments by configuring 'dcomm-uat-redis' using UAT rule 'sgr-fedcba9876543210f' to connect to subnet 'esg-uat-1', ensuring the status is 'available', with the name 'UAT Redis Cache [Reviewed]', note 'prod/uat subnet policies aligned', and consolidate to '10.0.5.0/24' incorporating 'Redis \u2013 UAT app tier'. Provide the updated subnet group and cluster.",
        "actions": [
            {
                "name": "UpdateSubnetGroupDescription",
                "arguments": {
                    "subnet_group_id": "esg-prod-1",
                    "new_description": "Subnets for production Redis and Memcached [REVIEWED]"
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateClusterChangePlan",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "reference_rule_id": "sgr-fedcba9876543210f",
                    "subnet_group_id": "esg-uat-1",
                    "new_status": "available",
                    "new_name": "UAT Redis Cache [Reviewed]",
                    "note": "prod/uat subnet policies aligned",
                    "env_tag": "UAT",
                    "consolidate_cidr": "10.0.5.0/24",
                    "consolidate_desc": "Redis – UAT app tier",
                    "endpoint_url": "NOCHANGE"
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 0
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 1
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 3
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 4
                },
            },
            {
                "name": "ApplyClusterPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 6
                }
            }
        ],
        "outputs": [
                "{\"subnet_group\":{\"subnet_group_id\":\"esg-prod-1\",\"description\":\"Subnets for production Redis and Memcached [REVIEWED]\"},\"cluster\":{\"cluster_id\":\"dcomm-uat-redis\",\"cluster_name\":\"UAT Redis Cache [Reviewed]\",\"status\":\"available\",\"subnet_group_id\":\"esg-uat-1\",\"instance_type_note\":\"prod/uat subnet policies aligned\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_092",
        "instruction": "Generate a fixed $20 promotion 'MOUSE20' and present it to Maria Garcia for one Wireless Mouse at B2B pricing. Proceed to log a medium-priority case named 'MOUSE20 Applied'. Return the subtotal, discount amount, and overall total after applying the discount.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "MOUSE20",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 20
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1,
                            "price": 32.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 32.0,
                    "offer_code": "MOUSE20"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "MOUSE20 Applied",
                    "priority": "Medium"
                }
            }
        ],
        "outputs": [
                "{\"offer_demo\":{\"contact_id\":\"201\",\"account_id\":\"101\",\"used_pricebook_id\":\"2\",\"product_id\":\"1003\",\"subtotal\":32.0,\"discount_amount\":20.0,\"total_after_discount\":12.0}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_093",
        "instruction": "Confirm retail stock availability for Leo Martinez for two 'Mechanical Keyboard', calculate the retail subtotal, and record the outcome.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Mechanical Keyboard"
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1017",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1017",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 2,
                            "price": 150.0
                        }
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Mechanical Keyboard",
                    "priority": "Medium"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"stock_and_price\":{\"product_id\":\"1017\",\"requested_qty\":2,\"used_pricebook_id\":\"1\",\"unit_price\":150.0,\"subtotal\":300.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Mechanical Keyboard\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_094",
        "instruction": "Calculate a B2B quote for Maria Garcia for one 'ProBook X15' and five 'USB-C Hub', apply the 'WINTER20' promotion, then initiate and finalize a case 'Bundle Quote Prepared' (Low).",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "ProBook X15",
                        "USB-C Hub"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "pricebook_id": "2"
                        },
                        {
                            "product_id": "1002",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1001",
                            "quantity": 1,
                            "price": 1250.0
                        },
                        {
                            "product_id": "1002",
                            "quantity": 5,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 1550.0,
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Bundle Quote Prepared",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"201\",\"account_id\":\"101\",\"used_pricebook_id\":\"2\",\"subtotal\":1550.0,\"applied_offer_code\":\"WINTER20\",\"discount_amount\":310.0,\"total_after_discount\":1240.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_095",
        "instruction": "Demonstrate and conclude the 'RACK30' fixed $30 promotion on one 'Server Rack Mount Kit (10-Pack)' with B2B pricing.",
        "actions": [
            {
                "name": "CreateNewOffer",
                "arguments": {
                    "offer_code": "RACK30",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 30
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Server Rack Mount Kit (10-Pack)"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1008",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1008",
                            "quantity": 1,
                            "price": 450.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 450.0,
                    "offer_code": "RACK30"
                },
            },
            {
                "name": "DeactivateOffer",
                "arguments": {
                    "offer_code": "RACK30"
                }
            }
        ],
        "outputs": [
                "{\"offer_demo\":{\"offer_code\":\"RACK30\",\"used_pricebook_id\":\"2\",\"product_id\":\"1008\",\"subtotal\":450.0,\"discount_amount\":30.0,\"total_after_discount\":420.0,\"final_is_active\":false}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_096",
        "instruction": "Organize Leo Martinez\u2019s cart by adjusting the 'Mechanical Keyboard' quantity to two and eliminating the 'Branded Water Bottle'; when eliminating, ensure to use the product_id from the cart line items if it does not match the catalog id. Record a low-priority case titled 'Cart Tidy Completed' and provide the finalized cart.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetCartByContactId",
                "arguments": {
                    "contact_id": "215"
                },
            },
            {
                "name": "GetAllItemsInCart",
                "arguments": {
                    "cart_id": "705"
                },
            },
            {
                "name": "UpdateItemsInCartBatch",
                "arguments": {
                    "cart_id": "705",
                    "items": [
                        {
                            "product_id": "1017",
                            "new_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "RemoveItemsFromCartBatch",
                "arguments": {
                    "cart_id": "705",
                    "product_ids": [
                        "1019"
                    ]
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Cart Tidy Completed",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"final_cart\":[{\"cart_id\":\"705\",\"product_id\":\"1017\",\"quantity\":2}],\"removed_products\":[\"1019\"],\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_097",
        "instruction": "Finalize a return for Maria Garcia\u2019s delivered order #9002 by restocking exactly the returned item ('USB-C Hub' only) and marking the order as Returned, then initiate a high-priority case 'Return Completed'. Provide the final order status and updated stock levels.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetOrderDetailsById",
                "arguments": {
                    "order_id": "9002"
                },
            },
            {
                "name": "GetAllOrderItemsByOrderId",
                "arguments": {
                    "order_id": "9002"
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1,
                            "price": 60.0
                        }
                    ]
                },
            },
            {
                "name": "AddStockQuantities",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity_to_add": 1
                        }
                    ]
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "9002",
                    "new_status": "Returned"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Return Completed",
                    "priority": "High"
                }
            }
        ],
        "outputs": [
                "{\"return_receipt\":{\"contact_id\":\"201\",\"account_id\":\"101\",\"order_id\":\"9002\",\"product_id\":\"1002\",\"quantity\":1,\"refund_amount\":60.0,\"final_status\":\"Returned\"}}"
        ]
    }
    ,
    {
        "annotator": aws,
        "user_id": "task_098",
        "instruction": "Harmonize Redis 6379 descriptions by adding environment tags without altering meanings. In the UAT group identified by 'sgr-fedcba9876543210f', maintain base 'Redis \u2013 UAT app tier' and append '[UAT]'; within the DEV group identified by 'sgr-badbadbadbadbadbad', maintain base 'Redis \u2013 restricted' and append '[DEV]'. Return counts of rules updated per group.",
        "actions": [
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier",
                    "env_tag": "UAT"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0001",
                    "step_index": 2
                },
            },
            {
                "name": "GetSecurityGroupRuleById",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad"
                },
            },
            {
                "name": "CreateIngressChangePlan",
                "arguments": {
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted",
                    "env_tag": "DEV"
                },
            },
            {
                "name": "ApplyIngressPlanStep",
                "arguments": {
                    "plan_id": "ap-0002",
                    "step_index": 2
                }
            }
        ],
        "outputs": [
                "{\"standardized\":{\"uat_added\":\">=0\",\"dev_added\":\">=0\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_099",
        "instruction": "Initiate a case 'Retail Mouse Bundle' for Leo Martinez, list four 'Wireless Mouse' at retail price, apply 'WELCOME5', and resolve the case (status 'Resolved'). Provide totals and the case id.",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "Nora",
                    "last_name": "Patel"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "113"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Retail Mouse Bundle",
                    "priority": "Medium"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Wireless Mouse"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "pricebook_id": "1"
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 4,
                            "price": 40.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 160.0,
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"215\",\"account_id\":\"113\",\"used_pricebook_id\":\"1\",\"subtotal\":160.0,\"applied_offer_code\":\"WELCOME5\",\"discount_amount\":5.0,\"total_after_discount\":155.0},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\"}}"
        ]
    }
    ,
    {
        "annotator": v1,
        "user_id": "task_100",
        "instruction": "Calculate a B2B subtotal for two 'Server Rack Mount Kit (10-Pack)' and apply 'WINTER20' for Maria Garcia, then establish and finalize a case 'Rack Kits Discounted' (Low).",
        "actions": [
            {
                "name": "GetContactByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAccountById",
                "arguments": {
                    "account_id": "101"
                },
            },
            {
                "name": "GetProductsByNames",
                "arguments": {
                    "names": [
                        "Server Rack Mount Kit (10-Pack)"
                    ]
                },
            },
            {
                "name": "GetPriceOfProduct",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1008",
                            "pricebook_id": "2"
                        }
                    ]
                },
            },
            {
                "name": "VerifyOrderFromStock",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1008",
                            "required_quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "CalculateSubTotalPrice",
                "arguments": {
                    "items": [
                        {
                            "product_id": "1008",
                            "quantity": 2,
                            "price": 450.0
                        }
                    ]
                },
            },
            {
                "name": "ApplyOfferToSubtotal",
                "arguments": {
                    "subtotal": 900.0,
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "CreateNewCase",
                "arguments": {
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Rack Kits Discounted",
                    "priority": "Low"
                },
            },
            {
                "name": "UpdateCaseStatus",
                "arguments": {
                    "case_id": "case_9",
                    "status": "Resolved"
                }
            }
        ],
        "outputs": [
                "{\"quote\":{\"contact_id\":\"201\",\"account_id\":\"101\",\"used_pricebook_id\":\"2\",\"items\":[{\"product_id\":\"1008\",\"quantity\":2,\"unit_price\":450.0,\"line_total\":900.0}],\"subtotal\":900.0,\"applied_offer_code\":\"WINTER20\",\"discount_amount\":180.0,\"total_after_discount\":720.0,\"stock_checked_qty\":2},\"case_update\":{\"case_id\":\"case_9\",\"final_status\":\"Resolved\",\"subject\":\"Rack Kits Discounted\"}}"
        ]
    }
]
