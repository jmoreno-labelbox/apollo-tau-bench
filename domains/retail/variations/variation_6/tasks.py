# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "TASK_HARD_001",
        "instruction": "As a retail manager, you are to organize a Two-Day shipment for order '#W1812830' including items ['2768401027','6313971174'] using a new tracking number from courier '#COU0001' (seed 7001). Record a 'received' scan at '2025-03-01T08:00:00', set the delivery to be scheduled for '2025-03-02T09:00:00', and input an 'out_for_delivery' scan at '2025-03-02T10:15:00'. Conclude the order by posting 31.14 via 'gift_card_8541487' with transaction 'NM-HARD-0001', assign the 'reconciled' tag, and label it as 'processed'. Return [new tracking ID, transaction ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0001",
                    "seed": 7001
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W1812830",
                    "item_ids": [
                        "2768401027",
                        "6313971174"
                    ],
                    "tracking_id": "TRK-COU0001-7001",
                    "courier_id": "#COU0001",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7001",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7001",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7001",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W1812830",
                    "amount": 31.14,
                    "payment_method_id": "gift_card_8541487",
                    "transaction_id": "NM-HARD-0001"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1812830",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1812830",
                    "status": "processed"
                }
            }
        ],
        "outputs": [
                "TRK-COU0001-7001",
                "NM-HARD-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_002",
        "instruction": "You need to modify the price of '4410138384' to 210.00 and ensure it's available by setting this to True. Assign tracking using '#COU0004' (seed 7003) for order '#W1305304' items ['4410138384','8349118980'] with 'Two-Day'. Input 'received' (2025-03-01T08:00:00) and schedule (2025-03-02T09:00:00). Confirm the tracking and return [new price, new tracking ID].",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "4410138384"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "4410138384",
                    "price": 210.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "4410138384",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0004",
                    "seed": 7003
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W1305304",
                    "item_ids": [
                        "4410138384",
                        "8349118980"
                    ],
                    "tracking_id": "TRK-COU0004-7003",
                    "courier_id": "#COU0004",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0004-7003",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0004-7003",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0004-7003"
                }
            }
        ],
        "outputs": [
                "210.00",
                "TRK-COU0004-7003"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_003",
        "instruction": "As a retail manager, you are required to manage tracking via '#COU0006' (seed 7006) and divide order '#W4073673' items ['6509212169','9354168549'] with 'Two-Day'. Record 'received' (2025-03-01T08:00:00), plan (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Adjust catalog price of '9354168549' to 145.00 and mark available True. Validate both tracking and variant. Provide [new tracking ID, updated price].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0006",
                    "seed": 7006
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W4073673",
                    "item_ids": [
                        "6509212169",
                        "9354168549"
                    ],
                    "tracking_id": "TRK-COU0006-7006",
                    "courier_id": "#COU0006",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7006",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7006",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7006",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9354168549",
                    "price": 145.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9354168549",
                    "available": true
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7006"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9354168549"
                }
            }
        ],
        "outputs": [
                "TRK-COU0006-7006",
                "145.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_004",
        "instruction": "Regarding order '#W6114312', you need to handle payment 28.93 via 'gift_card_4332117' as 'NM-HARD-0007', apply 'reconciled' tag, mark 'processed'. Additionally, redirect existing tracking '663395959263' to courier '#COU0007' after acquiring its details and details of the target courier, and confirm afterward. Return the transaction ID and the new courier ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6114312"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W6114312",
                    "amount": 28.93,
                    "payment_method_id": "gift_card_4332117",
                    "transaction_id": "TX-HARD-0007"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6114312",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6114312",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "663395959263"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0007"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "663395959263",
                    "courier_id": "#COU0007"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "663395959263"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6114312"
                }
            }
        ],
        "outputs": [
                "NM-HARD-0007",
                "#COU0007"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_005",
        "instruction": "Update the address for user 'olivia_costa_1269' to 500 Oak Street, Suite 10, Houston, NM 75217, USA. Then coordinate a Two-Day shipment for order '#W9527030' item '3229676465' with a new tracking from courier '#COU0008' (seed 7008), making sure the shipment destination reflects the updated address. Record a 'received' scan at '2025-03-01T08:00:00' and schedule delivery for '2025-03-02T09:00:00'. Provide the new tracking ID.",
        "actions": [
            {
                "name": "getUserById",
                "arguments": {
                    "user_id": "emma_silva_1269"
                },
            },
            {
                "name": "updateUserAddress",
                "arguments": {
                    "user_id": "emma_silva_1269",
                    "address": {
                        "address1": "500 Oak Street",
                        "address2": "Suite 10",
                        "city": "Dallas",
                        "state": "TX",
                        "zip": "75217",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0008",
                    "seed": 7008
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "3229676465"
                    ],
                    "tracking_id": "TRK-COU0008-7008",
                    "courier_id": "#COU0008",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0008-7008",
                    "address": {
                        "address1": "500 Oak Street",
                        "address2": "Suite 10",
                        "city": "Dallas",
                        "state": "TX",
                        "zip": "75217",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0008-7008",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0008-7008",
                    "scheduled": "2025-03-02T09:00:00"
                }
            }
        ],
        "outputs": [
                "TRK-COU0008-7008"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_006",
        "instruction": "For order '#W6874763', change variant '6700049080' price to 480.00 and set the availability to False. Then organize a new shipment for item ['7528037711'] using courier '#COU0009' (seed 7009) with 'Two-Day', adding 'received' at '2025-03-01T08:00:00', scheduling '2025-03-02T09:00:00', and 'out_for_delivery' at '2025-03-02T10:15:00'. Confirm tracking and variant details. Provide [new price, new tracking ID].",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "6700049080"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "6700049080",
                    "price": 480.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "6700049080",
                    "available": false
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0009",
                    "seed": 7009
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W6874763",
                    "item_ids": [
                        "7528037711"
                    ],
                    "tracking_id": "TRK-COU0009-7009",
                    "courier_id": "#COU0009",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0009-7009",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0009-7009",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0009-7009",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0009-7009"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "6700049080"
                }
            }
        ],
        "outputs": [
                "480.00",
                "TRK-COU0009-7009"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_007",
        "instruction": "As a retail manager, you are to handle order '#W7538736' by taking it out of manual review: assign risk as low (MANUAL_REVIEW_PASSED), ensure audit visibility with tags 'reviewed' and 'audit_logged', then proceed to processing. For shipment '790735957247', change the carrier to '#COU0005', update the destination to 410 Lake Drive, Suite 12, Milwaukee, IN 60610, USA, and log a 'received' event receipt on '2025-03-08T11:00:00' with a scheduled delivery at '2025-03-09T09:00:00'. Confirm the order and the shipment reflect these updates. Return [risk level, new courier ID].",
        "actions": [
            {
                "name": "fraudMarkOrder",
                "arguments": {
                    "order_id": "#W7538736",
                    "risk_level": "low",
                    "reason_code": "MANUAL_REVIEW_PASSED"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W7538736",
                    "tag": "reviewed"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W7538736",
                    "tag": "audit_logged"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W7538736",
                    "status": "processing"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "790735957247",
                    "courier_id": "#COU0005"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "790735957247",
                    "address": {
                        "address1": "410 Lake Drive",
                        "address2": "Suite 12",
                        "city": "Chicago",
                        "state": "IL",
                        "zip": "60610",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "790735957247",
                    "event": "received",
                    "timestamp": "2025-03-08T11:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "790735957247",
                    "scheduled": "2025-03-09T09:00:00"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W7538736"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "790735957247"
                }
            }
        ],
        "outputs": [
                "low",
                "#COU0005"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_008",
        "instruction": "For order '#W9527030', you need to coordinate tracking via '#COU0001' (seed 7013) for items ['7274158061','9314474252'] 'Two-Day', noting 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Then, modify price for '9314474252' to 120.00 and set available to True. Verify tracking and variant. Return [new tracking ID, updated price].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0001",
                    "seed": 7013
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "7274158061",
                        "9314474252"
                    ],
                    "tracking_id": "TRK-COU0001-7013",
                    "courier_id": "#COU0001",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7013",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7013",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7013",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9314474252",
                    "price": 120.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9314474252",
                    "available": true
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7013"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9314474252"
                }
            }
        ],
        "outputs": [
                "TRK-COU0001-7013",
                "120.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_009",
        "instruction": "Handle reconciliation of order '#W2091016' by posting 22.22 payment through 'paypal_2055565' txn 'NM-HARD-0014', tagging it as 'reconciled', and updating the status to 'processed'. Additionally, modify the address for customer 'omar_white_5940' to 157 Spruce Street, Suite 979, Tucson, AZ 85050, USA. Confirm by reviewing order and user information. Provide the transaction ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2091016"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W2091016",
                    "amount": 22.22,
                    "payment_method_id": "paypal_2055565",
                    "transaction_id": "TX-HARD-0014"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W2091016",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W2091016",
                    "status": "processed"
                },
            },
            {
                "name": "getUserById",
                "arguments": {
                    "user_id": "omar_anderson_5940"
                },
            },
            {
                "name": "updateUserAddress",
                "arguments": {
                    "user_id": "omar_anderson_5940",
                    "address": {
                        "address1": "157 Spruce Street",
                        "address2": "Suite 979",
                        "city": "Phoenix",
                        "state": "AZ",
                        "zip": "85050",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2091016"
                },
            },
            {
                "name": "getUserById",
                "arguments": {
                    "user_id": "omar_anderson_5940"
                }
            }
        ],
        "outputs": [
                "NM-HARD-0014"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_010",
        "instruction": "Identify the tracking using '#COU0003' (seed 7015) and partition order '#W6114312' items ['3111466194'] with 'Two-Day'. Record 'received' (2025-03-01T08:00:00), and schedule (2025-03-02T09:00:00). After retrieving details, reassign tracking '673941764576' to '#COU0005'. Validate by checking both trackings. Provide [new tracking ID, reassigned courier ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0003",
                    "seed": 7015
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W6114312",
                    "item_ids": [
                        "3111466194"
                    ],
                    "tracking_id": "TRK-COU0003-7015",
                    "courier_id": "#COU0003",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-7015",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0003-7015",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0005"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "673941764576",
                    "courier_id": "#COU0005"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0003-7015"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                }
            }
        ],
        "outputs": [
                "TRK-COU0003-7015",
                "#COU0005"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_011",
        "instruction": "Handle the creation of supply order '#SO9050' for the product '#SUP0005' with item '2524789262', ensuring a quantity of 6 at a unit cost of 16.40, and designate it as 'cancelled'. Adjust the catalog by updating the item's price to 0.0 and setting availability to False, then confirm the variant and provide the supply order ID.",
        "actions": [
            {
                "name": "getProductById",
                "arguments": {
                    "product_id": "2524789262"
                },
            },
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO9050",
                    "supplier_id": "#SUP0005",
                    "product_id": "2524789262",
                    "item_id": "2492465580",
                    "quantity": 6,
                    "unit_cost": 16.4
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO9050",
                    "status": "cancelled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "2492465580",
                    "price": 0.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "2492465580",
                    "available": false
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "2492465580"
                }
            }
        ],
        "outputs": [
                "#SO9050"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_012",
        "instruction": "In your role as a retail employee, coordinate the tracking allocation with courier '#COU0006' (seed 6101) and establish a new shipment for order '#W9527030' involving items ['9314474252']. Opt for 'Two-Day' delivery, log 'received' on '2025-03-05T08:00:00', and arrange '2025-03-06T09:00:00'. Retrieve and return the new tracking ID.",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0006",
                    "seed": 6101
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "9314474252"
                    ],
                    "tracking_id": "TRK-COU0006-6101",
                    "courier_id": "#COU0006",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0006-6101",
                    "event": "received",
                    "timestamp": "2025-03-05T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0006-6101",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0006-6101"
                }
            }
        ],
        "outputs": [
                "TRK-COU0006-6101"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_013",
        "instruction": "Handle the creation of supply order '#SO8102' for supplier '#SUP0009' with product '7996920482' item '9862136885', quantity 7, unit cost 18.75, and mark as 'cancelled'. Update the catalog to set the variant availability to False and price to 0.0, then confirm the variant. Return the supply order ID.",
        "actions": [
            {
                "name": "getProductById",
                "arguments": {
                    "product_id": "7996920482"
                },
            },
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8102",
                    "supplier_id": "#SUP0009",
                    "product_id": "7996920482",
                    "item_id": "9862136885",
                    "quantity": 7,
                    "unit_cost": 18.75
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8102",
                    "status": "cancelled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9862136885",
                    "price": 0.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9862136885",
                    "available": false
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9862136885"
                }
            }
        ],
        "outputs": [
                "#SO8102"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_014",
        "instruction": "Coordinate the settlement of order '#W9527030' by posting 25.25 via 'paypal_7732922' txn 'NM-HARD-1007', tagging 'reconciled' and changing status to 'processed'. Reassign tracking '790735957247' to '#COU0004' after obtaining tracking and courier, and verify. Return the transaction ID and new courier ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W9527030"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W9527030",
                    "amount": 25.25,
                    "payment_method_id": "paypal_7732922",
                    "transaction_id": "NM-HARD-1007"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W9527030",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W9527030",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "790735957247"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0004"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "790735957247",
                    "courier_id": "#COU0004"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "790735957247"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W9527030"
                }
            }
        ],
        "outputs": [
                "NM-HARD-1007",
                "#COU0004"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_015",
        "instruction": "Handle the creation of supply order '#SO8103' for '#SUP0008' product '6817146515' item '7624783998' with a quantity of 5 at a unit cost of 21.00 and label it as 'fulfilled'. Align the catalog to availability False and price 0.0, verify the variant, and provide the supply order ID.",
        "actions": [
            {
                "name": "getProductById",
                "arguments": {
                    "product_id": "6817146515"
                },
            },
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8103",
                    "supplier_id": "#SUP0008",
                    "product_id": "6817146515",
                    "item_id": "7624783998",
                    "quantity": 5,
                    "unit_cost": 21.0
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8103",
                    "status": "fulfilled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "7624783998",
                    "price": 0.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "7624783998",
                    "available": false
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "7624783998"
                }
            }
        ],
        "outputs": [
                "#SO8103"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_016",
        "instruction": "Coordinate the reconciliation of order '#W2091016' by posting 24.10 through 'paypal_2055565' txn 'NM-HARD-1014', marking it as 'reconciled', and setting it to 'processed'. Also update the item option 'color' to 'green' for item '1270145486'. Confirm by reviewing the order. Provide the transaction ID upon completion.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2091016"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W2091016",
                    "amount": 24.1,
                    "payment_method_id": "paypal_2055565",
                    "transaction_id": "NM-HARD-1014"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W2091016",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W2091016",
                    "status": "processed"
                },
            },
            {
                "name": "updateItemOption",
                "arguments": {
                    "order_id": "#W2091016",
                    "item_id": "1270145486",
                    "option_key": "color",
                    "option_value": "green"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2091016"
                }
            }
        ],
        "outputs": [
                "NM-HARD-1014"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_017",
        "instruction": "As a retail admin, you need to cancel items ['4624254797','2635605237'] in order '#W8958831' citing the reason 'SUPPLIER_ISSUE'. Process a refund of 50.00 with refund_id 'NM-HARD-1019-R' with reason 'PARTIAL_CANCELLATION'. Mark it as 'adjusted' and assign the status 'processed'. Retrieve the order to verify. Provide the refund ID as a response.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W8958831"
                },
            },
            {
                "name": "cancelOrderItems",
                "arguments": {
                    "order_id": "#W8958831",
                    "item_ids": [
                        "4624254797",
                        "2635605237"
                    ],
                    "reason_code": "SUPPLIER_ISSUE"
                },
            },
            {
                "name": "refundOrderPayment",
                "arguments": {
                    "order_id": "#W8958831",
                    "amount": 50.0,
                    "refund_id": "NM-HARD-1019-R",
                    "reason_code": "PARTIAL_CANCELLATION"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W8958831",
                    "tag": "adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W8958831",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W8958831"
                }
            }
        ],
        "outputs": [
                "NM-HARD-1019-R"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_018",
        "instruction": "You need to update variant '9083642334' (Desk Lamp) with a price of 79.50 and set availability to True. Next, apply a payment of 19.99 on '#W1812830' utilizing 'paypal_2076152' under 'NM-HARD-0016', label as 'reconciled', designate order as 'processed', and retrieve both the item and order details. Return the updated price and transaction ID.",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9083642334"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9083642334",
                    "price": 79.5
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9083642334",
                    "available": true
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1812830"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W1812830",
                    "amount": 19.99,
                    "payment_method_id": "paypal_2076152",
                    "transaction_id": "NM-HARD-0016"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1812830",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1812830",
                    "status": "processed"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9083642334"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1812830"
                }
            }
        ],
        "outputs": [
                "79.50",
                "NM-HARD-0016"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_019",
        "instruction": "As a retail manager, handle placing supply order '#SO8006' with supplier '#SUP0010' for product '3801771308' item '9494281769' (20 units at 11.00), ensure it is marked as fulfilled, and update the catalog by setting the price of that item to 260.00 and its availability to True. Provide [supply order ID, new price].",
        "actions": [
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8006",
                    "supplier_id": "#SUP0010",
                    "product_id": "3801771308",
                    "item_id": "9494281769",
                    "quantity": 20,
                    "unit_cost": 11.0
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8006",
                    "status": "fulfilled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9494281769",
                    "price": 260.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9494281769",
                    "available": true
                }
            }
        ],
        "outputs": [
                "#SO8006",
                "260.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_020",
        "instruction": "You are required to reconcile order '#W5299644' by posting 27.77 through 'paypal_3345717' txn 'NM-HARD-3021', labeling it 'reconciled', and setting it as 'processed'. Also, update the 'size' option to 'XL' for item '6268080249'. Confirm by reviewing the order. Return the transaction ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W5299644"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W5299644",
                    "amount": 27.77,
                    "payment_method_id": "paypal_3345717",
                    "transaction_id": "NM-HARD-3021"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W5299644",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W5299644",
                    "status": "processed"
                },
            },
            {
                "name": "updateItemOption",
                "arguments": {
                    "order_id": "#W5299644",
                    "item_id": "6268080249",
                    "option_key": "size",
                    "option_value": "XL"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W5299644"
                }
            }
        ],
        "outputs": [
                "NM-HARD-3021"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_021",
        "instruction": "For order '#W6114312', handle the account reconciliation and complete delivery setup: forward tracking '673941764576' to courier '#COU0005', assign the delivery address to 12 Birch Road, Suite 12, Houston, NM 78705, USA, document a 'received' scan at '2025-03-01T08:00:00', set the delivery time for '2025-03-02T09:00:00', and register 'out_for_delivery' at '2025-03-02T10:15:00'. Process a payment of 18.22 using 'gift_card_4332117' (transaction 'NM-HARD-2018'), apply the 'reconciled' label, change the order to 'processed', and adjust item '3111466194' setting 'color' to 'black'. Recompute the order total and verify updates on both tracking and order. Provide back [transaction ID, new courier ID].",
        "actions": [
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "673941764576",
                    "courier_id": "#COU0005"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "673941764576",
                    "address": {
                        "address1": "12 Birch Road",
                        "address2": "Suite 12",
                        "city": "Houston",
                        "state": "NM",
                        "zip": "78705",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "673941764576",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "673941764576",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "673941764576",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W6114312",
                    "amount": 18.22,
                    "payment_method_id": "gift_card_4332117",
                    "transaction_id": "NM-HARD-2018"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6114312",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6114312",
                    "status": "processed"
                },
            },
            {
                "name": "updateItemOption",
                "arguments": {
                    "order_id": "#W6114312",
                    "item_id": "3111466194",
                    "option_key": "color",
                    "option_value": "black"
                },
            },
            {
                "name": "computeOrderTotal",
                "arguments": {
                    "order_id": "#W6114312"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6114312"
                }
            }
        ],
        "outputs": [
                "NM-HARD-2018",
                "#COU0005"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_022",
        "instruction": "Cancel item ['5753502325'] on order '#W2631563' citing reason 'CUSTOMER_REQUEST'. Subsequently, process a refund of 15.25 with refund_id 'NM-HARD-3022-R' and mention 'CUSTOMER_REQUEST' as the reason. Mark the order as 'adjusted' and update status to 'processed'. Retrieve the order for confirmation. Provide the refund ID back.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2631563"
                },
            },
            {
                "name": "cancelOrderItems",
                "arguments": {
                    "order_id": "#W2631563",
                    "item_ids": [
                        "5753502325"
                    ],
                    "reason_code": "CUSTOMER_REQUEST"
                },
            },
            {
                "name": "refundOrderPayment",
                "arguments": {
                    "order_id": "#W2631563",
                    "amount": 15.25,
                    "refund_id": "NM-HARD-3022-R",
                    "reason_code": "CUSTOMER_REQUEST"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W2631563",
                    "tag": "adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W2631563",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2631563"
                }
            }
        ],
        "outputs": [
                "NM-HARD-3022-R"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_023",
        "instruction": "In order '#W2091016', handle a cancellation requested by the customer for item '6546364613': cancel this item citing reason 'CUSTOMER_REQUEST' and proceed to issue a 231.43 refund with refund_id 'NM-HARD-2020-R' using the same reason. Conclude the order process by marking it 'adjusted' and changing its status to 'processed'. Provide the order ID once completed.",
        "actions": [
            {
                "name": "cancelOrderItems",
                "arguments": {
                    "order_id": "#W2091016",
                    "item_ids": [
                        "6546364613"
                    ],
                    "reason_code": "CUSTOMER_REQUEST"
                },
            },
            {
                "name": "refundOrderPayment",
                "arguments": {
                    "order_id": "#W2091016",
                    "amount": 231.43,
                    "refund_id": "NM-HARD-2020-R",
                    "reason_code": "CUSTOMER_REQUEST"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W2091016",
                    "tag": "adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W2091016",
                    "status": "processed"
                }
            }
        ],
        "outputs": [
                "#W2091016"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_024",
        "instruction": "As a manager, you are required to reassign tracking '443521489581' to courier '#COU0006' and change the address to 500 Oak Street, Houston, 75201, USA. Proceed to settle order '#W3113816' with a 25.50 payment using 'credit_card_5869505' (transaction 'NM-HARD-2021'). Confirm the tracking thereafter. Provide the ID of the new courier.",
        "actions": [
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "443521489581"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "443521489581",
                    "courier_id": "#COU0006"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "443521489581",
                    "address": {
                        "address1": "500 Oak Street",
                        "city": "Houston",
                        "zip": "75201",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W3113816"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W3113816",
                    "amount": 25.5,
                    "payment_method_id": "credit_card_5869505",
                    "transaction_id": "NM-HARD-2021"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "443521489581"
                }
            }
        ],
        "outputs": [
                "#COU0006"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_025",
        "instruction": "As a manager, ensure variant '9314474252' is updated to show a price of 118.75 and is set as available for sale (available True). Resolve order '#W9527030' by posting a 12.34 payment through 'paypal_7732922' using transaction 'NM-HARD-3023', labeling it 'reconciled', and marking it as 'processed'. Provide the revised price and the transaction ID.",
        "actions": [
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9314474252",
                    "price": 118.75
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9314474252",
                    "available": true
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W9527030",
                    "amount": 12.34,
                    "payment_method_id": "paypal_7732922",
                    "transaction_id": "NM-HARD-3023"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W9527030",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W9527030",
                    "status": "processed"
                }
            }
        ],
        "outputs": [
                "118.75",
                "NM-HARD-3023"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_026",
        "instruction": "Being a retail manager, you need to initiate a specific Two-Day shipment for order '#W7398274' by allocating item '5694328282' to a new tracking from courier '#COU0002' (seed 7002). The shipment timeline must show 'received' on '2025-03-01T08:00:00', a scheduled delivery on '2025-03-02T09:00:00', and 'out_for_delivery' at '2025-03-02T10:15:00'. Change legacy tracking '168643142864' to courier '#COU0003', then settle the order with a 20.37 payment using 'paypal_7732922' (transaction 'NM-HARD-0002'), marking it 'reconciled' and 'processed'. Return [new tracking ID, transaction ID, reassigned courier ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0002",
                    "seed": 7002
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W7398274",
                    "item_ids": [
                        "5694328282"
                    ],
                    "tracking_id": "TRK-COU0002-7002",
                    "courier_id": "#COU0002",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-7002",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0002-7002",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-7002",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "168643142864",
                    "courier_id": "#COU0003"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W7398274",
                    "amount": 20.37,
                    "payment_method_id": "paypal_7732922",
                    "transaction_id": "NM-HARD-0002"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W7398274",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W7398274",
                    "status": "processed"
                }
            }
        ],
        "outputs": [
                "TRK-COU0002-7002",
                "NM-HARD-0002",
                "#COU0003"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_027",
        "instruction": "You need to change the price of '4410138384' to 210.00 and mark available as True. Assign tracking via '#COU0004' (seed 7003) for order '#W1305304' items ['4410138384','8349118980'] with 'Two-Day'. Add 'received' (2025-03-01T08:00:00) and arrange (2025-03-02T09:00:00). Verify tracking and provide [new price, new tracking ID].",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "4410138384"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "4410138384",
                    "price": 210.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "4410138384",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0004",
                    "seed": 7003
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W1305304",
                    "item_ids": [
                        "4410138384",
                        "8349118980"
                    ],
                    "tracking_id": "TRK-COU0004-7003",
                    "courier_id": "#COU0004",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0004-7003",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0004-7003",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0004-7003"
                }
            }
        ],
        "outputs": [
                "210.00",
                "TRK-COU0004-7003"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_028",
        "instruction": "As a technician, initiate a partial shipment for order '#W2325029' for item '9862136885' using 'Two-Day' delivery option. The new tracking (from courier '#COU0005' with seed 7004) will be 'TRK-COU0005-7004'. Document 'received' at '2025-03-01T08:00:00', plan for '2025-03-02T09:00:00', and add 'out_for_delivery' at '2025-03-02T10:15:00'. Additionally, transfer tracking '515122929210' to courier '#COU0004' and confirm both the reassigned and new tracking. Provide [new tracking ID, reassigned courier ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0005",
                    "seed": 7004
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W2325029",
                    "item_ids": [
                        "9862136885"
                    ],
                    "tracking_id": "TRK-COU0005-7004",
                    "courier_id": "#COU0005",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0005-7004",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0005-7004",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0005-7004",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "515122929210",
                    "courier_id": "#COU0004"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "515122929210"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0005-7004"
                }
            }
        ],
        "outputs": [
                "TRK-COU0005-7004",
                "#COU0004"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_029",
        "instruction": "Handle the creation of supply order '#SO8002' for supplier '#SUP0001' concerning product '9523456873' and item '8349118980' with a quantity of 15 at a unit cost of 10.25. Subsequently, mark it as 'fulfilled'. Coordinate an update to the catalog by adjusting the item price to 55.05 and setting availability to True, and validate both product and variant post-modifications. Return [supply order ID, new price].",
        "actions": [
            {
                "name": "getProductById",
                "arguments": {
                    "product_id": "9523456873"
                },
            },
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8002",
                    "supplier_id": "#SUP0001",
                    "product_id": "9523456873",
                    "item_id": "8349118980",
                    "quantity": 15,
                    "unit_cost": 10.25
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8002",
                    "status": "fulfilled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "8349118980",
                    "price": 55.05
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "8349118980",
                    "available": true
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "8349118980"
                },
            },
            {
                "name": "getProductById",
                "arguments": {
                    "product_id": "9523456873"
                }
            }
        ],
        "outputs": [
                "#SO8002",
                "55.05"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_030",
        "instruction": "Act as a retail manager to allocate tracking through '#COU0006' (seed 7006) and distribute order '#W6114312' items ['3111466194','7211586944'] using 'Two-Day'. Include 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), and 'out_for_delivery' (2025-03-02T10:15:00). Manage an update of the catalog price of '9354168549' to 145.00 and set available True. Verify tracking and variant. Return [new tracking ID, updated price].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0006",
                    "seed": 7006
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W6114312",
                    "item_ids": [
                        "3111466194",
                        "7211586944"
                    ],
                    "tracking_id": "TRK-COU0006-7006",
                    "courier_id": "#COU0006",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7006",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7006",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7006",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9354168549",
                    "price": 145.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9354168549",
                    "available": true
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7006"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9354168549"
                }
            }
        ],
        "outputs": [
                "TRK-COU0006-7006",
                "145.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_031",
        "instruction": "Handle payment posting of 28.93 for order '#W6114312' using 'gift_card_4332117' labeled as 'NM-HARD-0007', mark it as 'reconciled', and assign 'processed'. Then redirect the current tracking '663395959263' to courier '#COU0007' after retrieving both its details and those of the intended courier, ensuring verification thereafter. Return the transaction ID along with the updated courier ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6114312"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W6114312",
                    "amount": 28.93,
                    "payment_method_id": "gift_card_4332117",
                    "transaction_id": "NM-HARD-0007"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6114312",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6114312",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "663395959263"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0007"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "663395959263",
                    "courier_id": "#COU0007"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "663395959263"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6114312"
                }
            }
        ],
        "outputs": [
                "NM-HARD-0007",
                "#COU0007"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_032",
        "instruction": "As a manager, coordinate the update of user 'olivia_costa_1269' to 500 Oak Street, Suite 10, Houston, NM 75217, USA. Subsequently, generate a Two-Day shipment for order '#W9527030' involving item '9408160950' using a fresh tracking from courier '#COU0008' (seed 7008). Confirm that the tracking for the shipment corresponds to the Houston address and records a 'received' event receipt on '2025-03-01T08:00:00', with delivery planned for '2025-03-02T09:00:00'. Return the newly assigned tracking ID.",
        "actions": [
            {
                "name": "updateUserAddress",
                "arguments": {
                    "user_id": "olivia_costa_1269",
                    "address": {
                        "address1": "500 Oak Street",
                        "address2": "Suite 10",
                        "city": "Houston",
                        "state": "NM",
                        "zip": "75217",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0008",
                    "seed": 7008
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "9408160950"
                    ],
                    "tracking_id": "TRK-COU0008-7008",
                    "courier_id": "#COU0008",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0008-7008",
                    "address": {
                        "address1": "500 Oak Street",
                        "address2": "Suite 10",
                        "city": "Houston",
                        "state": "NM",
                        "zip": "75217",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0008-7008",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0008-7008",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0008-7008"
                }
            }
        ],
        "outputs": [
                "TRK-COU0008-7008"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_033",
        "instruction": "For order '#W6874763', handle the variant '6700049080' by updating the price to 480.00 and marking it as unavailable. Next, coordinate the creation of a new shipment for item ['7528037711'] using courier '#COU0009' with the service 'Two-Day'. Ensure 'received' status is logged at '2025-03-01T08:00:00', schedule for '2025-03-02T09:00:00', and note 'out_for_delivery' at '2025-03-02T10:15:00'. Verify tracking details alongside variant information. Provide [new price, new tracking ID] as output.",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "6700049080"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "6700049080",
                    "price": 480.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "6700049080",
                    "available": false
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0009",
                    "seed": 7009
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W6874763",
                    "item_ids": [
                        "7528037711"
                    ],
                    "tracking_id": "TRK-COU0009-7009",
                    "courier_id": "#COU0009",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0009-7009",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0009-7009",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0009-7009",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0009-7009"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "6700049080"
                }
            }
        ],
        "outputs": [
                "480.00",
                "TRK-COU0009-7009"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_034",
        "instruction": "It is necessary to generate supply order '#SO8003' for supplier '#SUP0008' involving product '6817146515' and item '7624783998' with a quantity of 9 at a unit cost of 22.10, then mark the status as 'cancelled'. Align the catalog by adjusting the item price to 0.0 and setting availability to False, followed by variant verification. Provide the supply order ID as output.",
        "actions": [
            {
                "name": "getProductById",
                "arguments": {
                    "product_id": "6817146515"
                },
            },
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8003",
                    "supplier_id": "#SUP0008",
                    "product_id": "6817146515",
                    "item_id": "7624783998",
                    "quantity": 9,
                    "unit_cost": 22.1
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8003",
                    "status": "cancelled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "7624783998",
                    "price": 0.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "7624783998",
                    "available": false
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "7624783998"
                }
            }
        ],
        "outputs": [
                "#SO8003"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_035",
        "instruction": "In your role as a retail specialist, handle marking order '#W7538736' for fraud with a risk_level of 'low' and reason_code 'MANUAL_REVIEW_PASSED'. Subsequently, reassign tracking number '790735957247' to courier '#COU0005' by retrieving tracking and courier details first, and confirm once done. Provide the risk level and the new courier ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W7538736"
                },
            },
            {
                "name": "fraudMarkOrder",
                "arguments": {
                    "order_id": "#W7538736",
                    "risk_level": "low",
                    "reason_code": "MANUAL_REVIEW_PASSED"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "790735957247"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0005"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "790735957247",
                    "courier_id": "#COU0005"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "790735957247"
                }
            }
        ],
        "outputs": [
                "low",
                "#COU0005"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_036",
        "instruction": "With regards to order '#W9527030', you need to allocate tracking using '#COU0001' (seed 7013) for items ['9408160950','1262139877'] 'Two-Day', marked as 'received' on (2025-03-01T08:00:00), scheduled for (2025-03-02T09:00:00), and 'out_for_delivery' by (2025-03-02T10:15:00). Following that, update the price for '1262139877' to 120.00 and set available to True. Confirm the tracking and variant status. Return [new tracking ID, updated price].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0001",
                    "seed": 7013
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "9408160950",
                        "1262139877"
                    ],
                    "tracking_id": "TRK-COU0001-7013",
                    "courier_id": "#COU0001",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7013",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7013",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7013",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "1262139877",
                    "price": 120.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "1262139877",
                    "available": true
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7013"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "1262139877"
                }
            }
        ],
        "outputs": [
                "TRK-COU0001-7013",
                "120.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_037",
        "instruction": "Handle the reconciling of order '#W2091016' by recording a 22.22 payment through 'paypal_2055565' transaction 'NM-HARD-0014', applying the 'reconciled' tag, and setting the status to 'processed'. Additionally, update the address for customer 'omar_white_5940' to 157 Spruce Street, Suite 979, Tucson, AZ 85050, USA. Confirm by reading both the order and the user. Return the transaction ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2091016"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W2091016",
                    "amount": 22.22,
                    "payment_method_id": "paypal_2055565",
                    "transaction_id": "NM-HARD-0014"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W2091016",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W2091016",
                    "status": "processed"
                },
            },
            {
                "name": "getUserById",
                "arguments": {
                    "user_id": "omar_white_5940"
                },
            },
            {
                "name": "updateUserAddress",
                "arguments": {
                    "user_id": "omar_white_5940",
                    "address": {
                        "address1": "157 Spruce Street",
                        "address2": "Suite 979",
                        "city": "Tucson",
                        "state": "AZ",
                        "zip": "85050",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2091016"
                },
            },
            {
                "name": "getUserById",
                "arguments": {
                    "user_id": "omar_white_5940"
                }
            }
        ],
        "outputs": [
                "NM-HARD-0014"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_038",
        "instruction": "As a manager, you need to handle an expedited shipment for item '3111466194' on order '#W6114312' using a new Two-Day tracking from courier '#COU0003' (seed 7015). Document the package as received at '2025-03-01T08:00:00' and arrange delivery for '2025-03-02T09:00:00'. Furthermore, move tracking '673941764576' to courier '#COU0005' and verify both tracking records. Return [new tracking ID, reassigned courier ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0003",
                    "seed": 7015
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W6114312",
                    "item_ids": [
                        "3111466194"
                    ],
                    "tracking_id": "TRK-COU0003-7015",
                    "courier_id": "#COU0003",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-7015",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0003-7015",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "673941764576",
                    "courier_id": "#COU0005"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0003-7015"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                }
            }
        ],
        "outputs": [
                "TRK-COU0003-7015",
                "#COU0005"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_039",
        "instruction": "Handle the update of variant '9083642334' price to 81.00 and mark available as True. Direct the tracking to be allocated via courier '#COU0002' (seed 9001) for order '#W3113816' items ['9083642334'] using 'Two-Day'; include 'received' at '2025-03-05T08:00:00', arrange '2025-03-06T09:00:00', and add 'out_for_delivery' at '2025-03-06T10:15:00'. Confirm this by reviewing tracking and variant. Return [updated price, new tracking ID].",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9083642334"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9083642334",
                    "price": 81.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9083642334",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0002",
                    "seed": 9001
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W3113816",
                    "item_ids": [
                        "9083642334"
                    ],
                    "tracking_id": "TRK-COU0002-9001",
                    "courier_id": "#COU0002",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-9001",
                    "event": "received",
                    "timestamp": "2025-03-05T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0002-9001",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-9001",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-06T10:15:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0002-9001"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9083642334"
                }
            }
        ],
        "outputs": [
                "81.00",
                "TRK-COU0002-9001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_040",
        "instruction": "Coordinate setting up a Two-Day shipment for order '#W2091016' for item '3735133539' with a new tracking from courier '#COU0003' (seed 9002). Make sure the shipment timeline includes 'received' at '2025-03-05T08:00:00', a scheduled delivery at '2025-03-06T09:00:00', and 'out_for_delivery' at '2025-03-06T10:15:00'. Additionally, reassign tracking '308411122792' to courier '#COU0001'. Return [new tracking ID, reassigned courier ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0003",
                    "seed": 9002
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W2091016",
                    "item_ids": [
                        "3735133539"
                    ],
                    "tracking_id": "TRK-COU0003-9002",
                    "courier_id": "#COU0003",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-9002",
                    "event": "received",
                    "timestamp": "2025-03-05T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0003-9002",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-9002",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-06T10:15:00"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "308411122792",
                    "courier_id": "#COU0001"
                }
            }
        ],
        "outputs": [
                "TRK-COU0003-9002",
                "#COU0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_041",
        "instruction": "As a manager, handle the settlement of order '#W1812830' using a payment of 22.45 via 'paypal_2076152' in transaction 'NM-HARD-3003'. Make sure to tag it as 'reconciled' and mark it 'processed'. Additionally, reassign the tracking '604805146457' to the courier '#COU0004' and ensure the tracking is verified. Provide the transaction ID and the new courier ID upon completion.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1812830"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W1812830",
                    "amount": 22.45,
                    "payment_method_id": "paypal_2076152",
                    "transaction_id": "NM-HARD-3003"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1812830",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1812830",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "604805146457"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "604805146457",
                    "courier_id": "#COU0004"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "604805146457"
                }
            }
        ],
        "outputs": [
                "NM-HARD-3003",
                "#COU0004"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_042",
        "instruction": "Your task is to coordinate the creation of supply order '#SO9020' for supplier '#SUP0011' concerning product '3377618313', item '6700049080', with a quantity of 5 units at a unit cost of 50.00, and assign it the status 'cancelled'. Update the catalog by adjusting the variant price to 0.0 and setting availability to False, then confirm the variant. Provide the supply order ID as a response.",
        "actions": [
            {
                "name": "getProductById",
                "arguments": {
                    "product_id": "3377618313"
                },
            },
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO9020",
                    "supplier_id": "#SUP0011",
                    "product_id": "3377618313",
                    "item_id": "6700049080",
                    "quantity": 5,
                    "unit_cost": 50.0
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO9020",
                    "status": "cancelled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "6700049080",
                    "price": 0.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "6700049080",
                    "available": false
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "6700049080"
                }
            }
        ],
        "outputs": [
                "#SO9020"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_043",
        "instruction": "As a manager, handle the address update for user 'omar_white_5940' to 44 Cypress Way, Floor 3, Tucson, AZ 85004, USA. Following that, ship order '#W2091016' item '6546364613' using a new Two-Day tracking from courier '#COU0005' (seed 9005) to the newly updated address, noting 'received' at '2025-03-05T08:00:00' and planning delivery for '2025-03-06T09:00:00'. Provide the new tracking ID.",
        "actions": [
            {
                "name": "getUserById",
                "arguments": {
                    "user_id": "omar_white_5940"
                },
            },
            {
                "name": "updateUserAddress",
                "arguments": {
                    "user_id": "omar_white_5940",
                    "address": {
                        "address1": "44 Cypress Way",
                        "address2": "Floor 3",
                        "city": "Tucson",
                        "state": "AZ",
                        "zip": "85004",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0005",
                    "seed": 9005
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W2091016",
                    "item_ids": [
                        "6546364613"
                    ],
                    "tracking_id": "TRK-COU0005-9005",
                    "courier_id": "#COU0005",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0005-9005",
                    "address": {
                        "address1": "44 Cypress Way",
                        "address2": "Floor 3",
                        "city": "Tucson",
                        "state": "AZ",
                        "zip": "85004",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0005-9005",
                    "event": "received",
                    "timestamp": "2025-03-05T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0005-9005",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0005-9005"
                }
            }
        ],
        "outputs": [
                "TRK-COU0005-9005"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_044",
        "instruction": "Coordinate the cancellation of items ['5206946487','3111466194'] on order '#W7259850' due to 'SUPPLIER_ISSUE'. Process a refund of 30.00 with refund_id 'NM-HARD-3006-R' for reason 'PARTIAL_CANCELLATION'. Mark the order as 'adjusted' and update the status to 'processed'. Retrieve the order for verification. Deliver the refund ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W7259850"
                },
            },
            {
                "name": "cancelOrderItems",
                "arguments": {
                    "order_id": "#W7259850",
                    "item_ids": [
                        "5206946487",
                        "3111466194"
                    ],
                    "reason_code": "SUPPLIER_ISSUE"
                },
            },
            {
                "name": "refundOrderPayment",
                "arguments": {
                    "order_id": "#W7259850",
                    "amount": 30.0,
                    "refund_id": "NM-HARD-3006-R",
                    "reason_code": "PARTIAL_CANCELLATION"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W7259850",
                    "tag": "adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W7259850",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W7259850"
                }
            }
        ],
        "outputs": [
                "NM-HARD-3006-R"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_045",
        "instruction": "You are required to handle a Two-Day shipment for order '#W7398274' involving items ['5694328282','1355937109'] by acquiring a new tracking ID from courier '#COU0010' (seed 9007). The shipment timeline should indicate 'received' at '2025-03-05T08:00:00' and set delivery for '2025-03-06T09:00:00'. Coordinate the order with a 10.00 payment via 'gift_card_8541487' (transaction 'NM-HARD-3007'), tag it as 'reconciled', and label it as processed. Submit [new tracking ID, transaction ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0010",
                    "seed": 9007
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W7398274",
                    "item_ids": [
                        "5694328282",
                        "1355937109"
                    ],
                    "tracking_id": "TRK-COU0010-9007",
                    "courier_id": "#COU0010",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0010-9007",
                    "event": "received",
                    "timestamp": "2025-03-05T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0010-9007",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W7398274",
                    "amount": 10.0,
                    "payment_method_id": "gift_card_8541487",
                    "transaction_id": "NM-HARD-3007"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W7398274",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W7398274",
                    "status": "processed"
                }
            }
        ],
        "outputs": [
                "TRK-COU0010-9007",
                "NM-HARD-3007"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_046",
        "instruction": "As a technician, you need to adjust delivery plans by transferring tracking '790735957247' to courier '#COU0002', updating its address to 410 Lake Drive, Suite 12, Milwaukee, IN 60610, USA, and recording a 'delay_reported' event at '2025-03-08T11:00:00'. For order '#W7538736', note the case as 'investigating' and update the status to 'processing'. Confirm the tracking subsequent to the change. Provide the new courier ID.",
        "actions": [
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "790735957247",
                    "courier_id": "#COU0002"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "790735957247",
                    "address": {
                        "address1": "410 Lake Drive",
                        "address2": "Suite 12",
                        "city": "Milwaukee",
                        "state": "IN",
                        "zip": "60610",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "790735957247",
                    "event": "delay_reported",
                    "timestamp": "2025-03-08T11:00:00"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W7538736",
                    "tag": "investigating"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W7538736",
                    "status": "processing"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "790735957247"
                }
            }
        ],
        "outputs": [
                "#COU0002"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_047",
        "instruction": "Handle the placement of supply order '#SO9030' with supplier '#SUP0009' for product '7996920482' item '9862136885', ensuring a quantity of 8 at a unit cost of 19.00 is specified and marked as 'fulfilled'. Adjust the item's price to 139.00 and set it to available True. Coordinating tracking via '#COU0004' (seed 9009) for order '#W2325029' item ['9862136885'] with 'Two-Day', and arrange it for '2025-03-06T09:00:00'. Confirm the process by reviewing tracking and variant. Provide [new tracking ID, updated price] back.",
        "actions": [
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO9030",
                    "supplier_id": "#SUP0009",
                    "product_id": "7996920482",
                    "item_id": "9862136885",
                    "quantity": 8,
                    "unit_cost": 19.0
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO9030",
                    "status": "fulfilled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9862136885",
                    "price": 139.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9862136885",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0004",
                    "seed": 9009
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W2325029",
                    "item_ids": [
                        "9862136885"
                    ],
                    "tracking_id": "TRK-COU0004-9009",
                    "courier_id": "#COU0004",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0004-9009",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0004-9009"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9862136885"
                }
            }
        ],
        "outputs": [
                "TRK-COU0004-9009",
                "139.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_048",
        "instruction": "Reassign tracking '254796145302' to courier '#COU0010' after retrieving tracking and courier details. Subsequently, settle order '#W1305304' by posting 15.75 through 'gift_card_4332117' using transaction 'NM-HARD-3010', attach tag 'reconciled', and change status to 'processed'. Ensure to verify the tracking post-reassignment. Deliver [transaction ID, new courier ID] in return.",
        "actions": [
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "254796145302"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0010"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "254796145302",
                    "courier_id": "#COU0010"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1305304"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W1305304",
                    "amount": 15.75,
                    "payment_method_id": "gift_card_4332117",
                    "transaction_id": "TX-HARD-3010"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1305304",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1305304",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "254796145302"
                }
            }
        ],
        "outputs": [
                "NM-HARD-3010",
                "#COU0010"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_049",
        "instruction": "Manage the settlement for order '#W4817420'. Utilize payment method 'gift_card_0000000' to register an exact payment of 21.44 under transaction 'NM-2001'. Subsequently, include the tag 'reconciled' and update the order status to 'processed'. Additionally, annotate order '#W4817420' with a fraud mark: risk_level 'low' and reason_code 'MANUAL_REVIEW_PASSED'. This is metadata only\u2014no status changes.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W4817420"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W4817420",
                    "amount": 21.44,
                    "payment_method_id": "gift_card_0000000",
                    "transaction_id": "TX-2001"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W4817420",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W4817420",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W4817420"
                },
            },
            {
                "name": "fraudMarkOrder",
                "arguments": {
                    "order_id": "#W4817420",
                    "risk_level": "low",
                    "reason_code": "MANUAL_REVIEW_PASSED"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W4817420"
                }
            }
        ],
        "outputs": [
                "TX-2001",
                "low"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_HARD_050",
        "instruction": "Coordinate the reconciliation of order '#W6304490'. Document a payment of 25.72 using payment_method_id 'gift_card_0000000' and transaction_id 'NM-2005'. Then, append the tag 'reconciled' and change the order status to 'processed'. Update the catalog entry for variant '9647292434': price \u2192 57.48, available \u2192 True. Confirm the update by retrieving the variant afterward.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6304490"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W6304490",
                    "amount": 25.72,
                    "payment_method_id": "gift_card_0000000",
                    "transaction_id": "TX-2005"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6304490",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6304490",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6304490"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9647292434"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9647292434",
                    "price": 57.48
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9647292434",
                    "available": true
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9647292434"
                }
            }
        ],
        "outputs": [
                "TX-2005",
                "57.48"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_001",
        "instruction": "For order '#W9527030', you need to adjust the price of '3229676465' to 79.99 and ensure it is set as available True; also revise the price of '7274158061' to 44.99 and ensure it is available True. Manage tracking using '#COU0003' (seed 8002) and split items ['3229676465','7274158061'] with 'Two-Day'; incorporate 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Update the tracking address to 667 Elm Street, Suite 624, Milwaukee, IN 60641, USA. Confirm by verifying tracking and both variants. Provide [new tracking ID, prices].",
        "actions": [
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3229676465",
                    "price": 79.99
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3229676465",
                    "available": true
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "7274158061",
                    "price": 44.99
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "7274158061",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0003",
                    "seed": 8002
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "3229676465",
                        "7274158061"
                    ],
                    "tracking_id": "TRK-COU0003-8002",
                    "courier_id": "#COU0003",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8002",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8002",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8002",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8002",
                    "address": {
                        "address1": "667 Elm Street",
                        "address2": "Suite 624",
                        "city": "Chicago",
                        "state": "IL",
                        "zip": "60641",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8002"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3229676465"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "7274158061"
                }
            }
        ],
        "outputs": [
                "TRK-COU0003-8002",
                "79.99",
                "44.99"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_002",
        "instruction": "Oversee a detailed reconciliation for '#W6114312': (1) Redirect tracking '673941764576' to courier '#COU0001' after retrieving both. (2) Adjust prices for '5753502325'\u219296.35 (ensure available True) and '3735133539'\u2192508.37 (ensure available True). (3) Process payment 45.00 using 'gift_card_4332117' as 'NM-EXP-0003', and mark fraud risk as 'low' due to 'MANUAL_REVIEW_PASSED'. (4) Apply 'reconciled' tag, update status to 'processed'. Confirm by verifying tracking, both variants, and order. Provide [new courier ID, transaction ID, risk level].",
        "actions": [
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0001"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "673941764576",
                    "courier_id": "#COU0001"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "5753502325",
                    "price": 96.35
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "5753502325",
                    "available": true
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3735133539"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3735133539",
                    "price": 508.37
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3735133539",
                    "available": true
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W6114312",
                    "amount": 45.0,
                    "payment_method_id": "gift_card_4332117",
                    "transaction_id": "TX-EXP-0003"
                },
            },
            {
                "name": "fraudMarkOrder",
                "arguments": {
                    "order_id": "#W6114312",
                    "risk_level": "low",
                    "reason_code": "MANUAL_REVIEW_PASSED"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6114312",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6114312",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3735133539"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6114312"
                }
            }
        ],
        "outputs": [
                "#COU0001",
                "NM-EXP-0003",
                "low"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_003",
        "instruction": "You are overseeing a Oakland user audit. Initially, compile a list of all users in 'Oakland'. Subsequently, update the address for user 'omar_harris_1594' to 1000 King Road, Suite 12, Oakland, NV 95112, USA. Conclude by scheduling the shipment of order '#W8958831' item '5537798301' via courier '#COU0007' with a fresh Two-Day tracking (seed 7160), incorporating a 'received' scan on '2025-03-11T08:00:00' and delivery planned for '2025-03-12T09:00:00'. Verify the revised user record along with the new tracking. Do not return any output.",
        "actions": [
            {
                "name": "findUsersByCity",
                "arguments": {
                    "city": "San Jose"
                },
            },
            {
                "name": "getUserById",
                "arguments": {
                    "user_id": "omar_taylor_1594"
                },
            },
            {
                "name": "updateUserAddress",
                "arguments": {
                    "user_id": "omar_taylor_1594",
                    "address": {
                        "address1": "1000 King Road",
                        "address2": "Suite 12",
                        "city": "San Jose",
                        "state": "CA",
                        "zip": "95112",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0007",
                    "seed": 7160
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W8958831",
                    "item_ids": [
                        "5537798301"
                    ],
                    "tracking_id": "TRK-COU0007-7160",
                    "courier_id": "#COU0007",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0007-7160",
                    "event": "received",
                    "timestamp": "2025-03-11T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0007-7160",
                    "scheduled": "2025-03-12T09:00:00"
                },
            },
            {
                "name": "getUserById",
                "arguments": {
                    "user_id": "omar_taylor_1594"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0007-7160"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_004",
        "instruction": "As a manager, your task is to restock item '7211586944' by coordinating and completing (status fulfilled) supply order '#SO8015' with supplier '#SUP0009' for product '7996920482' (12 units at 14.00). Record the modification in the catalog by updating its price to 129.99 and setting available to True. Next, prepare a Two-Day shipment of that item on order '#W2325029' utilizing a new tracking from courier '#COU0004' (seed 8026) with delivery planned for '2025-03-02T09:00:00'. Return [tracking ID, updated price].",
        "actions": [
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8015",
                    "supplier_id": "#SUP0009",
                    "product_id": "7996920482",
                    "item_id": "7211586944",
                    "quantity": 12,
                    "unit_cost": 14.0
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8015",
                    "status": "fulfilled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "7211586944",
                    "price": 129.99
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "7211586944",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0004",
                    "seed": 8026
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W2325029",
                    "item_ids": [
                        "7211586944"
                    ],
                    "tracking_id": "TRK-COU0004-8026",
                    "courier_id": "#COU0004",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0004-8026",
                    "scheduled": "2025-03-02T09:00:00"
                }
            }
        ],
        "outputs": [
                "TRK-COU0004-8026",
                "129.99"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_005",
        "instruction": "As a manager, your duty is to render variant '3229676465' sellable (available True) at 82.50 and subsequently coordinate a Two-Day combined shipment for order '#W9527030' (items '3229676465' and '7274158061') utilizing a new tracking from courier '#COU0003' (seed 8027). The shipment timeline must encompass 'received' at '2025-03-01T08:00:00' and a planned delivery at '2025-03-02T09:00:00'. Designate the order as reconciled and processed. Provide the new tracking ID.",
        "actions": [
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3229676465",
                    "price": 82.5
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3229676465",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0003",
                    "seed": 8027
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "3229676465",
                        "7274158061"
                    ],
                    "tracking_id": "TRK-COU0003-8027",
                    "courier_id": "#COU0003",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8027",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8027",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W9527030",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W9527030",
                    "status": "processed"
                }
            }
        ],
        "outputs": [
                "TRK-COU0003-8027"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_006",
        "instruction": "In your role as a retail manager, you need to allocate tracking with '#COU0001' (seed 7101) and distribute order '#W1812830' items ['7791931443','2768401027'] using 'Two-Day'. Include 'received' (2025-03-07T08:00:00), schedule (2025-03-08T09:00:00), and 'out_for_delivery' (2025-03-08T10:15:00). Initiate payment 33.33 via 'gift_card_8541487' txn 'NM-HARD-1001', annotate 'reconciled', set the status to 'processed'. Validate by checking tracking and order. Return [tracking ID, transaction ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0001",
                    "seed": 7101
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W1812830",
                    "item_ids": [
                        "7791931443",
                        "2768401027"
                    ],
                    "tracking_id": "TRK-COU0001-7101",
                    "courier_id": "#COU0001",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7101",
                    "event": "received",
                    "timestamp": "2025-03-07T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7101",
                    "scheduled": "2025-03-08T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7101",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-08T10:15:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7101"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1812830"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W1812830",
                    "amount": 33.33,
                    "payment_method_id": "gift_card_8541487",
                    "transaction_id": "TX-HARD-1001"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1812830",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1812830",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1812830"
                }
            }
        ],
        "outputs": [
                "TRK-COU0001-7101",
                "NM-HARD-1001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_007",
        "instruction": "For order '#W6114312': handle the reassignment of tracking '673941764576' to '#COU0001' following the retrieval of both items. Adjust prices '5753502325'\u219295.10 and '3735133539'\u2192509.10, set both to available True. Submit payment of 44.00 using 'gift_card_4332117' under txn 'NM-EXP-1003'; mark fraud status as 'low' with reason 'MANUAL_REVIEW_PASSED'; tag as 'reconciled'; set status to 'processed'. Confirm by reviewing tracking, both variants, and the order. Provide [courier ID, transaction ID, risk].",
        "actions": [
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0001"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "673941764576",
                    "courier_id": "#COU0001"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "5753502325",
                    "price": 95.1
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "5753502325",
                    "available": true
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3735133539"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3735133539",
                    "price": 509.1
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3735133539",
                    "available": true
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W6114312",
                    "amount": 44.0,
                    "payment_method_id": "gift_card_4332117",
                    "transaction_id": "TX-EXP-1003"
                },
            },
            {
                "name": "fraudMarkOrder",
                "arguments": {
                    "order_id": "#W6114312",
                    "risk_level": "low",
                    "reason_code": "MANUAL_REVIEW_PASSED"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6114312",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6114312",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3735133539"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6114312"
                }
            }
        ],
        "outputs": [
                "#COU0001",
                "NM-EXP-1003",
                "low"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_008",
        "instruction": "In your role as manager, coordinate the fulfillment (status fulfilled) of supply order '#SO8115' with supplier '#SUP0009' for product '7996920482' item '7211586944' (12 units at 14.00), then modify the catalog to adjust the item price to 129.25 and mark it as available True. Organize a Two-Day shipment for order '#W2325029' for the mentioned item using a new tracking from courier '#COU0004' (seed 8226) and plan delivery for '2025-03-02T09:00:00'. Provide [tracking ID, updated price].",
        "actions": [
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8115",
                    "supplier_id": "#SUP0009",
                    "product_id": "7996920482",
                    "item_id": "7211586944",
                    "quantity": 12,
                    "unit_cost": 14.0
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8115",
                    "status": "fulfilled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "7211586944",
                    "price": 129.25
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "7211586944",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0004",
                    "seed": 8226
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W2325029",
                    "item_ids": [
                        "7211586944"
                    ],
                    "tracking_id": "TRK-COU0004-8226",
                    "courier_id": "#COU0004",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0004-8226",
                    "scheduled": "2025-03-02T09:00:00"
                }
            }
        ],
        "outputs": [
                "TRK-COU0004-8226",
                "129.25"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_009",
        "instruction": "As a technician, ensure that variant '3229676465' becomes sellable (available True) at 82.75. Coordinate a combined Two-Day shipment for order '#W9527030', including items '3229676465' and '7274158061', using a new tracking ID from courier '#COU0003' (seed 8227). The shipment schedule should state 'received' on '2025-03-01T08:00:00' with a planned delivery on '2025-03-02T09:00:00'. Set the order status to reconciled and processed. Provide the new tracking ID afterward.",
        "actions": [
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3229676465",
                    "price": 82.75
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3229676465",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0003",
                    "seed": 8227
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "3229676465",
                        "7274158061"
                    ],
                    "tracking_id": "TRK-COU0003-8227",
                    "courier_id": "#COU0003",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8227",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8227",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W9527030",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W9527030",
                    "status": "processed"
                }
            }
        ],
        "outputs": [
                "TRK-COU0003-8227"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_010",
        "instruction": "Allocate tracking through '#COU0006' (seed 7106) and divide order '#W6114312' items ['3111466194'] into 'Two-Day', marking 'received' (2025-03-01T08:00:00), scheduling (2025-03-02T09:00:00), and 'out_for_delivery' (2025-03-02T10:15:00). Adjust the price of '5753502325' to 101.35 and set it available True. Verify tracking and variant status. Provide [tracking ID, updated price] as a response.",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0006",
                    "seed": 7106
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W6114312",
                    "item_ids": [
                        "3111466194"
                    ],
                    "tracking_id": "TRK-COU0006-7106",
                    "courier_id": "#COU0006",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7106",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7106",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7106",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "5753502325",
                    "price": 101.35
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "5753502325",
                    "available": true
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0006-7106"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                }
            }
        ],
        "outputs": [
                "TRK-COU0006-7106",
                "101.35"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_011",
        "instruction": "Allocate tracking using '#COU0001' (seed 7113) for order '#W9527030' with items ['3229676465','7274158061'] under 'Two-Day' category, 'received' (2025-03-01T08:00:00), scheduled (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Update the price for '3229676465' to 80.00 and set its availability to True. Confirm the tracking and variant. Provide [tracking ID, updated price].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0001",
                    "seed": 7113
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "3229676465",
                        "7274158061"
                    ],
                    "tracking_id": "TRK-COU0001-7113",
                    "courier_id": "#COU0001",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7113",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7113",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7113",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3229676465",
                    "price": 80.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3229676465",
                    "available": true
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0001-7113"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3229676465"
                }
            }
        ],
        "outputs": [
                "TRK-COU0001-7113",
                "80.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_012",
        "instruction": "As a retail manager, set up a Two-Day shipment for order '#W6114312' involving item '5206946487' with a new tracking from '#COU0003' (seed 7115). Note 'received' on '2025-03-03T08:00:00' and arrange delivery on '2025-03-04T09:00:00'. Reassign the legacy tracking '673941764576' to '#COU0007' and verify both trackings. Provide [new tracking ID, reassigned courier ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0003",
                    "seed": 7115
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W6114312",
                    "item_ids": [
                        "5206946487"
                    ],
                    "tracking_id": "TRK-COU0003-7115",
                    "courier_id": "#COU0003",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-7115",
                    "event": "received",
                    "timestamp": "2025-03-03T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0003-7115",
                    "scheduled": "2025-03-04T09:00:00"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "673941764576",
                    "courier_id": "#COU0007"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0003-7115"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                }
            }
        ],
        "outputs": [
                "TRK-COU0003-7115",
                "#COU0007"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_013",
        "instruction": "Handle the remediation of order '#W8863729' by transferring item '5105441284' to a new tracking assigned from '#COU0002' using seed 8001 and 'Two-Day' delivery, including events at '2025-03-01T08:00:00' ('received') and '2025-03-02T10:15:00' ('out_for_delivery'), with a set delivery on '2025-03-02T09:00:00'. Reallocate the existing tracking '604805146457' to '#COU0006', mark fraud-risk as 'low' with reason 'MANUAL_REVIEW_PASSED', process the payment 'NM-EXP-0001' of 3766.59 through 'paypal_1521508', assign the tag 'reconciled', and update the status to 'processed'. Provide [new tracking ID, transaction ID, risk level].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0002",
                    "seed": 8001
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W8863729",
                    "item_ids": [
                        "5105441284"
                    ],
                    "tracking_id": "TRK-COU0002-8001",
                    "courier_id": "#COU0002",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-8001",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0002-8001",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-8001",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "604805146457"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "604805146457",
                    "courier_id": "#COU0006"
                },
            },
            {
                "name": "fraudMarkOrder",
                "arguments": {
                    "order_id": "#W8863729",
                    "risk_level": "low",
                    "reason_code": "MANUAL_REVIEW_PASSED"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W8863729",
                    "amount": 3766.59,
                    "payment_method_id": "paypal_1521508",
                    "transaction_id": "TX-EXP-0001"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W8863729",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W8863729",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0002-8001"
                }
            }
        ],
        "outputs": [
                "TRK-COU0002-8001",
                "NM-EXP-0001",
                "low"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_014",
        "instruction": "Coordinate the update for order '#W9527030' by changing the price of '9408160950' to 79.99 and marking as available True; also adjust '1262139877' price to 44.99 and set to available True. Assign tracking via '#COU0003' (seed 8002) and divide items ['9408160950','1262139877'] with 'Two-Day'; incorporate 'received' (2025-03-01T08:00:00), planned delivery (2025-03-02T09:00:00), and 'out_for_delivery' (2025-03-02T10:15:00). Insert the new tracking address at 667 Elm Street, Suite 624, Milwaukee, IN 60641, USA. Confirm by verifying tracking and both item variants. Deliver [new tracking ID, prices].",
        "actions": [
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9408160950",
                    "price": 79.99
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9408160950",
                    "available": true
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "1262139877",
                    "price": 44.99
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "1262139877",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0003",
                    "seed": 8002
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "9408160950",
                        "1262139877"
                    ],
                    "tracking_id": "TRK-COU0003-8002",
                    "courier_id": "#COU0003",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8002",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8002",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8002",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8002",
                    "address": {
                        "address1": "667 Elm Street",
                        "address2": "Suite 624",
                        "city": "Chicago",
                        "state": "IL",
                        "zip": "60641",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0003-8002"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9408160950"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "1262139877"
                }
            }
        ],
        "outputs": [
                "TRK-COU0003-8002",
                "79.99",
                "44.99"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_015",
        "instruction": "Handle a detailed reconciliation for '#W6114312': (1) Assign tracking '673941764576' to courier '#COU0001' after retrieving both items. (2) Modify prices for '5753502325'\u219296.35 (ensure availability True) and '3735133539'\u2192508.37 (ensure availability True). (3) Process payment of 45.00 using 'gift_card_4332117' as 'NM-EXP-0003', marking fraud risk 'low' with the reason 'MANUAL_REVIEW_PASSED'. (4) Label as 'reconciled', change status to 'processed'. Confirm this by reviewing tracking, both variants, and order. Return [new courier ID, transaction ID, risk level].",
        "actions": [
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0001"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "673941764576",
                    "courier_id": "#COU0001"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "5753502325",
                    "price": 96.35
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "5753502325",
                    "available": true
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3735133539"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3735133539",
                    "price": 508.37
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3735133539",
                    "available": true
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W6114312",
                    "amount": 45.0,
                    "payment_method_id": "gift_card_4332117",
                    "transaction_id": "TX-EXP-0003"
                },
            },
            {
                "name": "fraudMarkOrder",
                "arguments": {
                    "order_id": "#W6114312",
                    "risk_level": "low",
                    "reason_code": "MANUAL_REVIEW_PASSED"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6114312",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6114312",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "673941764576"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3735133539"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6114312"
                }
            }
        ],
        "outputs": [
                "#COU0001",
                "NM-EXP-0003",
                "low"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_016",
        "instruction": "In regard to order '#W1305304': reprice '5694328282' to 335.00 and '3952176596' to 1190.00, making both available True. Assign tracking '#COU0007' with seed 8204 and categorize those items under 'Two-Day'; input 'received' date (2025-03-01T08:00:00), and plan for (2025-03-02T09:00:00). Update the tracking address to 103 Pine Lane, Suite 730, Houston, NM 78703, USA and confirm accuracy. Issue a refund of 1525.00 with refund_id 'NM-EXP-1004-R' citing 'PRICE_ADJUSTMENT'; tag as 'adjusted'; set status to 'processed'. Return [tracking ID, refund ID].",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5694328282"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "5694328282",
                    "price": 335.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "5694328282",
                    "available": true
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3952176596"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3952176596",
                    "price": 1190.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3952176596",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0007",
                    "seed": 8204
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W1305304",
                    "item_ids": [
                        "5694328282",
                        "3952176596"
                    ],
                    "tracking_id": "TRK-COU0007-8204",
                    "courier_id": "#COU0007",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0007-8204",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0007-8204",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0007-8204",
                    "address": {
                        "address1": "103 Pine Lane",
                        "address2": "Suite 730",
                        "city": "Austin",
                        "state": "TX",
                        "zip": "78703",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0007-8204"
                },
            },
            {
                "name": "refundOrderPayment",
                "arguments": {
                    "order_id": "#W1305304",
                    "amount": 1525.0,
                    "refund_id": "TX-EXP-1004-R",
                    "reason_code": "PRICE_ADJUSTMENT"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1305304",
                    "tag": "adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1305304",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0007-8204"
                }
            }
        ],
        "outputs": [
                "TRK-COU0007-8204",
                "NM-EXP-1004-R"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_017",
        "instruction": "As a retail manager, it's necessary to oversee the comprehensive audit and correction for '#W2325029': (1) Reallocate tracking '308411122792' to '#COU0004' following the retrieval of current details and identification of the target courier. (2) Distribute '#COU0005' (seed 8005) and divide items ['5606522780','9045948550'] as 'Two-Day'; incorporate 'received' (2025-03-01T08:00:00) and plan (2025-03-02T09:00:00). (3) Update tracking address to 498 Elm Avenue, Suite 953, Oakland, NV 95155, USA. (4) Process payment of 18.50 via 'paypal_2076152' transaction 'NM-EXP-0005', label as 'reconciled', and mark as 'processed'. Verify by reviewing both tracking and order. Return [reassigned courier ID, new tracking ID, transaction ID].",
        "actions": [
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "308411122792"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0004"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "308411122792",
                    "courier_id": "#COU0004"
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0005",
                    "seed": 8005
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W2325029",
                    "item_ids": [
                        "5606522780",
                        "9045948550"
                    ],
                    "tracking_id": "TRK-COU0005-8005",
                    "courier_id": "#COU0005",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0005-8005",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0005-8005",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0005-8005",
                    "address": {
                        "address1": "498 Elm Avenue",
                        "address2": "Suite 953",
                        "city": "Oakland",
                        "state": "NV",
                        "zip": "95155",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W2325029",
                    "amount": 18.5,
                    "payment_method_id": "paypal_2076152",
                    "transaction_id": "NM-EXP-0005"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W2325029",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W2325029",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "308411122792"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0005-8005"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2325029"
                }
            }
        ],
        "outputs": [
                "#COU0004",
                "TRK-COU0005-8005",
                "NM-EXP-0005"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_018",
        "instruction": "In your role as a manager, you are tasked with ensuring stock and fulfillment for item '7211586944': initiate and complete (status fulfilled) supply order '#SO8015' with '#SUP0009' for product '7996920482' (12 units each 14.00), modify the catalog so that the item is priced at 129.99 and is available True, and set up a Two-Day shipment for order '#W2091016' utilizing a new tracking from courier '#COU0004' (seed 8026) with delivery planned for '2025-03-02T09:00:00'. Return [tracking ID, updated price].",
        "actions": [
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8015",
                    "supplier_id": "#SUP0009",
                    "product_id": "7996920482",
                    "item_id": "7211586944",
                    "quantity": 12,
                    "unit_cost": 14.0
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8015",
                    "status": "fulfilled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "7211586944",
                    "price": 129.99
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "7211586944",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0004",
                    "seed": 8026
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W2091016",
                    "item_ids": [
                        "7211586944"
                    ],
                    "tracking_id": "TRK-COU0004-8026",
                    "courier_id": "#COU0004",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0004-8026",
                    "scheduled": "2025-03-02T09:00:00"
                }
            }
        ],
        "outputs": [
                "TRK-COU0004-8026",
                "129.99"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_019",
        "instruction": "As a manager, handle the placing of supply order '#SO8009' with the supplier '#SUP0002' for product '1968349452' (item '3541421151') for 7 units at 19.25 and designate it as fulfilled (status fulfilled). Make sure to update tracking '713743776331' so its timeline includes a 'received' scan at '2025-05-01T08:00:00' and a delivery planned for '2025-05-02T09:00:00'. Provide the supply order ID afterward.",
        "actions": [
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8009",
                    "supplier_id": "#SUP0002",
                    "product_id": "1968349452",
                    "item_id": "3541421151",
                    "quantity": 7,
                    "unit_cost": 19.25
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8009",
                    "status": "fulfilled"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "713743776331",
                    "event": "received",
                    "timestamp": "2025-05-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "713743776331",
                    "scheduled": "2025-05-02T09:00:00"
                }
            }
        ],
        "outputs": [
                "#SO8009"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_020",
        "instruction": "In your role as a manager, oversee the coordination of a Two-Day shipment on order '#W1812830' for item '7791931443' utilizing a new tracking from courier '#COU0005' (seed 8228). Confirm that the timeline shows a 'received' scan at '2025-03-01T08:00:00' and a delivery schedule for '2025-03-02T09:00:00'. Execute a partial refund of 199.00 (refund_id 'NM-EXP-1013-R', reason 'CUSTOMER_REQUEST'), mark the order as adjusted, and advance it to processed. Return the new tracking ID upon completion.",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0005",
                    "seed": 8228
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W1812830",
                    "item_ids": [
                        "7791931443"
                    ],
                    "tracking_id": "TRK-COU0005-8228",
                    "courier_id": "#COU0005",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0005-8228",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0005-8228",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "refundOrderPayment",
                "arguments": {
                    "order_id": "#W1812830",
                    "amount": 199.0,
                    "refund_id": "NM-EXP-1013-R",
                    "reason_code": "CUSTOMER_REQUEST"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1812830",
                    "tag": "adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1812830",
                    "status": "processed"
                }
            }
        ],
        "outputs": [
                "TRK-COU0005-8228"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_021",
        "instruction": "As a manager, you need to modify the catalog to set the prices of variants '6509212169' and '9354168549' to 142.10 and 149.90 respectively, making them available True. Create a Two-Day shipment for order '#W4073673' for these items, utilizing a new tracking from courier '#COU0008' with seed 9101; the resulting tracking ID will be 'TRK-COU0008-9101'. Record the status 'received' on '2025-03-05T08:00:00', schedule for '2025-03-06T09:00:00', and enter 'out_for_delivery' at '2025-03-06T10:15:00'. Transition the existing tracking '663395959263' to '#COU0005'. Update the new tracking address to 1200 Market St, Suite 300, Houston, NM 75202, USA. Handle payment of 55.55 through 'credit_card_3677959' under transaction 'NM-EXP-2001', apply the tag 'reconciled', and change the status to 'processed'. Verify by reviewing the new tracking and both variants. Deliver [new tracking ID, transaction ID].",
        "actions": [
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "6509212169",
                    "price": 142.1
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "6509212169",
                    "available": true
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9354168549",
                    "price": 149.9
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9354168549",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0008",
                    "seed": 9101
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W4073673",
                    "item_ids": [
                        "6509212169",
                        "9354168549"
                    ],
                    "tracking_id": "TRK-COU0008-9101",
                    "courier_id": "#COU0008",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0008-9101",
                    "event": "received",
                    "timestamp": "2025-03-05T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0008-9101",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0008-9101",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-06T10:15:00"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "663395959263",
                    "courier_id": "#COU0005"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0008-9101",
                    "address": {
                        "address1": "1200 Market St",
                        "address2": "Suite 300",
                        "city": "Houston",
                        "state": "NM",
                        "zip": "75202",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W4073673",
                    "amount": 55.55,
                    "payment_method_id": "credit_card_3677959",
                    "transaction_id": "NM-EXP-2001"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W4073673",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W4073673",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0008-9101"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "6509212169"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9354168549"
                }
            }
        ],
        "outputs": [
                "TRK-COU0008-9101",
                "NM-EXP-2001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_022",
        "instruction": "You are required to allocate tracking through courier '#COU0006' (seed 9102) for order '#W1812830' items ['2768401027'], utilizing 'Two-Day'; enter 'received' on '2025-03-05T08:00:00', schedule for '2025-03-06T09:00:00', and update the tracking address to 77 Maple Street, Suite 210, Milwaukee, IN 60616, USA. Mark the order's risk as 'low' with the reason 'MANUAL_REVIEW_PASSED'. Initiate a refund of 25.00 with refund_id 'NM-EXP-2002-R', citing reason 'CUSTOMER_REQUEST', apply the tag 'adjusted', and update the status to 'processed'. Validate by reviewing the tracking. Deliver [new tracking ID, refund transaction ID, risk level].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0006",
                    "seed": 9102
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W1812830",
                    "item_ids": [
                        "2768401027"
                    ],
                    "tracking_id": "TRK-COU0006-9102",
                    "courier_id": "#COU0006",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0006-9102",
                    "event": "received",
                    "timestamp": "2025-03-05T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0006-9102",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0006-9102",
                    "address": {
                        "address1": "77 Maple Street",
                        "address2": "Suite 210",
                        "city": "Chicago",
                        "state": "IL",
                        "zip": "60616",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "fraudMarkOrder",
                "arguments": {
                    "order_id": "#W1812830",
                    "risk_level": "low",
                    "reason_code": "MANUAL_REVIEW_PASSED"
                },
            },
            {
                "name": "refundOrderPayment",
                "arguments": {
                    "order_id": "#W1812830",
                    "amount": 25.0,
                    "refund_id": "TX-EXP-2002-R",
                    "reason_code": "CUSTOMER_REQUEST"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1812830",
                    "tag": "adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1812830",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0006-9102"
                }
            }
        ],
        "outputs": [
                "TRK-COU0006-9102",
                "NM-EXP-2002-R",
                "low"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_023",
        "instruction": "You are required to modify prices for '3229676465'\u219285.00 and '9314474252'\u2192121.10 and ensure both are available as True. Assign tracking via '#COU0009' (seed 9103) for order '#W9527030' items ['3229676465','9314474252'] with 'Two-Day'; append 'received' on '2025-03-05T08:00:00', plan '2025-03-06T09:00:00', and update the tracking address to 667 Elm Street, Suite 624, Milwaukee, IN 60641, USA. Execute a payment of 22.22 using 'paypal_7732922' with transaction 'NM-EXP-2003', label 'reconciled', and update status to 'processed'. Validate by reading tracking and both variants. Return [new tracking ID, prices].",
        "actions": [
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3229676465",
                    "price": 85.0
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3229676465",
                    "available": true
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "9314474252",
                    "price": 121.1
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "9314474252",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0009",
                    "seed": 9103
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9527030",
                    "item_ids": [
                        "3229676465",
                        "9314474252"
                    ],
                    "tracking_id": "TRK-COU0009-9103",
                    "courier_id": "#COU0009",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0009-9103",
                    "event": "received",
                    "timestamp": "2025-03-05T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0009-9103",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0009-9103",
                    "address": {
                        "address1": "667 Elm Street",
                        "address2": "Suite 624",
                        "city": "Chicago",
                        "state": "IL",
                        "zip": "60641",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W9527030",
                    "amount": 22.22,
                    "payment_method_id": "paypal_7732922",
                    "transaction_id": "TX-EXP-2003"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W9527030",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W9527030",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0009-9103"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3229676465"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "9314474252"
                }
            }
        ],
        "outputs": [
                "TRK-COU0009-9103",
                "85.00",
                "121.10"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_024",
        "instruction": "Handle supply order '#SO9044' with supplier '#SUP0001' for product '9523456873' item '2768401027' quantity 6 unit cost 12.75 and label it 'fulfilled'. Adjust the item's price to 49.50 and set available to True. Assign tracking via '#COU0002' (seed 9104) for order '#W1812830' items ['2768401027'] using 'Two-Day'; append 'received' on '2025-03-05T08:00:00', plan '2025-03-06T09:00:00', and update the tracking address to 498 Elm Avenue, Suite 953, Oakland, NV 95155, USA. Process payment 18.00 via 'gift_card_8541487' transaction 'NM-EXP-2004', label 'reconciled', and update status to 'processed'. Validate by reading tracking and variant. Return [supply order ID, new tracking ID].",
        "actions": [
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO9044",
                    "supplier_id": "#SUP0001",
                    "product_id": "9523456873",
                    "item_id": "2768401027",
                    "quantity": 6,
                    "unit_cost": 12.75
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO9044",
                    "status": "fulfilled"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "2768401027",
                    "price": 49.5
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "2768401027",
                    "available": true
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0002",
                    "seed": 9104
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W1812830",
                    "item_ids": [
                        "2768401027"
                    ],
                    "tracking_id": "TRK-COU0002-9104",
                    "courier_id": "#COU0002",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-9104",
                    "event": "received",
                    "timestamp": "2025-03-05T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0002-9104",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "TRK-COU0002-9104",
                    "address": {
                        "address1": "498 Elm Avenue",
                        "address2": "Suite 953",
                        "city": "Oakland",
                        "state": "NV",
                        "zip": "95155",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W1812830",
                    "amount": 18.0,
                    "payment_method_id": "gift_card_8541487",
                    "transaction_id": "NM-EXP-2004"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1812830",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1812830",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0002-9104"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "2768401027"
                }
            }
        ],
        "outputs": [
                "#SO9044",
                "TRK-COU0002-9104"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_025",
        "instruction": "In your role as a retail manager, you are required to change the prices for '4410138384' to 215.55 and '8349118980' to 62.49, ensuring that both are marked as available True. Redirect tracking '515122929210' to courier '#COU0001'. Establish a Two-Day delivery on order '#W1305304' for item '4410138384' using a new tracking number from '#COU0007' (seed 9105); log 'received' at '2025-03-05T08:00:00' and plan for '2025-03-06T09:00:00'. Authorize a 15.00 refund with refund_id 'NM-EXP-2005-R' citing reason 'PRICE_ADJUSTMENT', label the order 'adjusted', and update the order status to 'processed'. Validate the process by reviewing the new tracking information. Present [new tracking ID, refund transaction ID].",
        "actions": [
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "4410138384",
                    "price": 215.55
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "4410138384",
                    "available": true
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "8349118980",
                    "price": 62.49
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "8349118980",
                    "available": true
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "515122929210",
                    "courier_id": "#COU0001"
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0007",
                    "seed": 9105
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W1305304",
                    "item_ids": [
                        "4410138384"
                    ],
                    "tracking_id": "TRK-COU0007-9105",
                    "courier_id": "#COU0007",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0007-9105",
                    "event": "received",
                    "timestamp": "2025-03-05T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0007-9105",
                    "scheduled": "2025-03-06T09:00:00"
                },
            },
            {
                "name": "refundOrderPayment",
                "arguments": {
                    "order_id": "#W1305304",
                    "amount": 15.0,
                    "refund_id": "NM-EXP-2005-R",
                    "reason_code": "PRICE_ADJUSTMENT"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1305304",
                    "tag": "adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1305304",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0007-9105"
                }
            }
        ],
        "outputs": [
                "TRK-COU0007-9105",
                "NM-EXP-2005-R"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_026",
        "instruction": "Coordinate a shipment and payment update for order '#W6304490'. Begin by setting up a new shipment for items ['6956751343', '4983901480'] with courier '#COU0001' using seed 5000 under the 'Two-Day' delivery option. Ensure this shipment's history includes a 'received' entry at 2025-03-01T08:00:00, an 'out_for_delivery' at 2025-03-02T10:15:00, and schedule delivery for 2025-03-02T09:00:00. Confirm the new tracking details after setup. Subsequently, as the accounts agent, log a payment of 20.37 utilizing payment method 'gift_card_0000000' with transaction ID 'NM-8000', classify it with the 'reconciled' tag, and adjust the order status to 'processed'. Following these modifications, you will extract the updated order information. Furthermore, redo the assignment of existing tracking '357962501027' to courier '#COU0002', inspecting current tracking details and the target courier\u2019s details prior to reassignment, and verify once more afterward. Provide the new tracking ID, the payment transaction ID, and the new courier ID to which the assignment was transferred.",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0001",
                    "seed": 5000
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W6304490",
                    "item_ids": [
                        "6956751343",
                        "4983901480"
                    ],
                    "tracking_id": "TRK-COU0001-5000",
                    "courier_id": "#COU0001",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-5000",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0001-5000",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0001-5000",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0001-5000"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6304490"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W6304490",
                    "amount": 20.37,
                    "payment_method_id": "gift_card_0000000",
                    "transaction_id": "TX-8000"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6304490",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6304490",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6304490"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "357962501027"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0002"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "357962501027",
                    "courier_id": "#COU0002"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "357962501027"
                }
            }
        ],
        "outputs": [
                "TRK-COU0001-5000",
                "TX-8000",
                "#COU0002"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_027",
        "instruction": "For order '#W6874763', it's necessary to adjust variant '6700049080' price to 475.75 and mark availability as False. Initiate a new shipment for item ['7528037711'] with '#COU0002' (seed 7109) 'Two-Day'; input 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Verify tracking and variant. Return [new price, tracking ID].",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "6700049080"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "6700049080",
                    "price": 475.75
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "6700049080",
                    "available": false
                },
            },
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0002",
                    "seed": 7109
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W6874763",
                    "item_ids": [
                        "7528037711"
                    ],
                    "tracking_id": "TRK-COU0002-7109",
                    "courier_id": "#COU0002",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-7109",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0002-7109",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-7109",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0002-7109"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "6700049080"
                }
            }
        ],
        "outputs": [
                "475.75",
                "TRK-COU0002-7109"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_028",
        "instruction": "In your role as a retail manager, proceed to create a new shipment for order '#W6304490' using 'Two-Day' delivery and a new tracking from courier '#COU0007' with seed 5006; the tracking ID will be 'TRK-COU0007-5006'. Associate items ['6956751343','4983901480'], log 'received' at '2025-03-01T08:00:00', schedule '2025-03-02T09:00:00', and include 'out_for_delivery' at '2025-03-02T10:15:00'. Process a payment of 26.79 via 'gift_card_0000000' (transaction_id 'NM-8006'), label 'reconciled', and update order status to 'processed'. Additionally, reassign the existing tracking '889070895653' to courier '#COU0001'. Return [new tracking ID, transaction ID, reassigned courier ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0007",
                    "seed": 5006
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W6304490",
                    "item_ids": [
                        "6956751343",
                        "4983901480"
                    ],
                    "tracking_id": "TRK-COU0007-5006",
                    "courier_id": "#COU0007",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0007-5006",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0007-5006",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0007-5006",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W6304490",
                    "amount": 26.79,
                    "payment_method_id": "gift_card_0000000",
                    "transaction_id": "NM-8006"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6304490",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6304490",
                    "status": "processed"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "889070895653",
                    "courier_id": "#COU0001"
                }
            }
        ],
        "outputs": [
                "TRK-COU0007-5006",
                "NM-8006",
                "#COU0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_029",
        "instruction": "As a manager, it is necessary to divide order '#W4817420' by reassigning items ['6777246137','4900661478'] to a fresh Two-Day shipment with courier '#COU0002' (seed 5008). Make sure the shipment timeline records a 'received' scan at '2025-03-01T08:00:00', schedules delivery at '2025-03-02T09:00:00', and includes an 'out_for_delivery' scan at '2025-03-02T10:15:00'. Finalize the order with a $28.93 payment through 'gift_card_0000000' (transaction 'NM-8008'), add the 'reconciled' tag, and mark it as 'processed'. Also, dispatch the existing shipment '443521489581' to courier '#COU0003'. Provide [new tracking ID, transaction ID, reassigned courier ID].",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0002",
                    "seed": 5008
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W4817420",
                    "item_ids": [
                        "6777246137",
                        "4900661478"
                    ],
                    "tracking_id": "TRK-COU0002-5008",
                    "courier_id": "#COU0002",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-5008",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0002-5008",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0002-5008",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "443521489581",
                    "courier_id": "#COU0003"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W4817420",
                    "amount": 28.93,
                    "payment_method_id": "gift_card_0000000",
                    "transaction_id": "NM-8008"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W4817420",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W4817420",
                    "status": "processed"
                }
            }
        ],
        "outputs": [
                "TRK-COU0002-5008",
                "NM-8008",
                "#COU0003"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_EXP_030",
        "instruction": "You need to coordinate the setup for a new shipment of order '#W2611340' with item ['6469567736'] using courier '#COU0005' (seed 5004) under the 'Two-Day' delivery option. Ensure the shipment logs a 'received' event at 2025-03-01T08:00:00, an 'out_for_delivery' event at 2025-03-02T10:15:00, and a delivery scheduled on 2025-03-02T09:00:00. After configuring the shipment, it is essential to verify its tracking details. Subsequently, record a $24.65 payment with 'gift_card_0000000' and transaction ID 'NM-8004', assign the 'reconciled' tag to the order, and update its status to 'processed'. Additionally, reassign tracking '367478070474' to courier '#COU0006', validating the tracking and courier details prior to reassignment, and obtain the revised tracking afterward. Finally, recheck the new shipment\u2019s tracking verifications. Present the new tracking ID, the payment transaction ID, and the new courier ID.",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0005",
                    "seed": 5004
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W2611340",
                    "item_ids": [
                        "6469567736"
                    ],
                    "tracking_id": "TRK-COU0005-5004",
                    "courier_id": "#COU0005",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0005-5004",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0005-5004",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0005-5004",
                    "event": "out_for_delivery",
                    "timestamp": "2025-03-02T10:15:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0005-5004"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W2611340",
                    "amount": 24.65,
                    "payment_method_id": "gift_card_0000000",
                    "transaction_id": "NM-8004"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W2611340",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W2611340",
                    "status": "processed"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "367478070474"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0006"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "367478070474",
                    "courier_id": "#COU0006"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "367478070474"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0005-5004"
                }
            }
        ],
        "outputs": [
                "TRK-COU0005-5004",
                "NM-8004",
                "#COU0006"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_001",
        "instruction": "You must update catalog item '2198125883' by adjusting its price to 299.99 and ensuring availability is set to True. Next, label order '#W9608525' with 'price_adjusted' and update the status to 'processed'. Finally, retrieve the updated item and order to verify, and return the revised price.",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "2198125883"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "2198125883",
                    "price": 299.99
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "2198125883",
                    "available": true
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W9608525",
                    "tag": "price_adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W9608525",
                    "status": "processed"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "2198125883"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W9608525"
                }
            }
        ],
        "outputs": [
                "299.99"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_002",
        "instruction": "You need to log a payment of 37.56 on order '#W1649831' using the payment method 'gift_card_2519457' associated with transaction 'NM-MED-0001'. After that, mark the order as 'reconciled', change the status to 'processed', and fetch the updated order. Provide the transaction ID as a return.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1649831"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W1649831",
                    "amount": 37.56,
                    "payment_method_id": "gift_card_2519457",
                    "transaction_id": "NM-MED-0001"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1649831",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1649831",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1649831"
                }
            }
        ],
        "outputs": [
                "NM-MED-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_003",
        "instruction": "As a retail manager, it is your responsibility to ensure that tracking '254796145302' is processed by courier '#COU0001', accurately listing the address 12 Birch Road, Suite 12, Houston, NM 78705, USA, and recording a 'return_initiated' event at '2025-03-06T12:00:00'. Provide the updated courier ID.",
        "actions": [
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "254796145302",
                    "courier_id": "#COU0001"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "254796145302",
                    "address": {
                        "address1": "12 Birch Road",
                        "address2": "Suite 12",
                        "city": "Houston",
                        "state": "NM",
                        "zip": "78705",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "254796145302",
                    "event": "return_initiated",
                    "timestamp": "2025-03-06T12:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "254796145302"
                }
            }
        ],
        "outputs": [
                "#COU0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_004",
        "instruction": "Coordinate the placement of supply order '#SO8001' with supplier '#SUP0005' for product '2524789262' (item '2492465580'), ensuring a quantity of 12 at a unit price of 15.25, and mark it as 'fulfilled'. Confirm supplier details before and afterwards. Return the supply order ID.",
        "actions": [
            {
                "name": "getSupplierDetails",
                "arguments": {
                    "supplier_id": "#SUP0005"
                },
            },
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8001",
                    "supplier_id": "#SUP0005",
                    "product_id": "2524789262",
                    "item_id": "2492465580",
                    "quantity": 12,
                    "unit_cost": 15.25
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8001",
                    "status": "fulfilled"
                },
            },
            {
                "name": "getSupplierDetails",
                "arguments": {
                    "supplier_id": "#SUP0005"
                }
            }
        ],
        "outputs": [
                "#SO8001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_005",
        "instruction": "Handle allocation of a tracking ID using courier '#COU0003' (seed 6001) and initiate a new shipment for order '#W9474165' that includes items ['8649999816','6469567736']. Employ the delivery option 'Two-Day'. Register 'received' at '2025-03-01T08:00:00' and arrange delivery for '2025-03-02T09:00:00'. Verify by retrieving the new tracking. Return the new tracking ID.",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0003",
                    "seed": 6001
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9474165",
                    "item_ids": [
                        "8649999816",
                        "6469567736"
                    ],
                    "tracking_id": "TRK-COU0003-6001",
                    "courier_id": "#COU0003",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-6001",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0003-6001",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0003-6001"
                }
            }
        ],
        "outputs": [
                "TRK-COU0003-6001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_006",
        "instruction": "You need to adjust the price of catalog item '5753502325' to 100.20 and ensure it's available by setting it to True. Next, label order '#W6114312' as 'price_adjusted' and denote it as 'processed'. Confirm by accessing the item and order. Return the new price.",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "5753502325",
                    "price": 100.2
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "5753502325",
                    "available": true
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6114312",
                    "tag": "price_adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6114312",
                    "status": "processed"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6114312"
                }
            }
        ],
        "outputs": [
                "100.20"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_007",
        "instruction": "Handle the update of catalog variant '3735133539' to price 512.49 and set availability to True. Mark order '#W2091016' as 'price_adjusted' with status 'processed'. Subsequently, fetch the variant and order to confirm, then return the revised price.",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3735133539"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3735133539",
                    "price": 512.49
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3735133539",
                    "available": true
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W2091016",
                    "tag": "price_adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W2091016",
                    "status": "processed"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3735133539"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2091016"
                }
            }
        ],
        "outputs": [
                "512.49"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_008",
        "instruction": "Coordinate the recording of a payment of 42.75 on order '#W5299644' utilizing method 'paypal_3345717' and transaction 'NM-MED-1001'. Mark the transaction as 'reconciled', set status to 'processed', and retrieve the order. Then, return the transaction ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W5299644"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W5299644",
                    "amount": 42.75,
                    "payment_method_id": "paypal_3345717",
                    "transaction_id": "TX-MED-1001"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W5299644",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W5299644",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W5299644"
                }
            }
        ],
        "outputs": [
                "NM-MED-1001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_009",
        "instruction": "Assign the status 'low' for fraud to order '#W7538736' with reason 'MANUAL_REVIEW_PASSED'. After retrieving the details, allocate tracking '604805146457' to '#COU0003' and confirm. Provide [risk level, new courier ID] in return.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W7538736"
                },
            },
            {
                "name": "fraudMarkOrder",
                "arguments": {
                    "order_id": "#W7538736",
                    "risk_level": "low",
                    "reason_code": "MANUAL_REVIEW_PASSED"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "604805146457"
                },
            },
            {
                "name": "getCourierDetails",
                "arguments": {
                    "courier_id": "#COU0003"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "604805146457",
                    "courier_id": "#COU0003"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "604805146457"
                }
            }
        ],
        "outputs": [
                "low",
                "#COU0003"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_010",
        "instruction": "As a retail manager, coordinate placing the supply order '#SO8101' with supplier '#SUP0001' for product '9523456873', item '2768401027', quantity 8, at a unit price of 12.40. Mark it 'fulfilled', verify the supplier before and after, and provide the supply order ID in return.",
        "actions": [
            {
                "name": "getSupplierDetails",
                "arguments": {
                    "supplier_id": "#SUP0001"
                },
            },
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO8101",
                    "supplier_id": "#SUP0001",
                    "product_id": "9523456873",
                    "item_id": "2768401027",
                    "quantity": 8,
                    "unit_cost": 12.4
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO8101",
                    "status": "fulfilled"
                },
            },
            {
                "name": "getSupplierDetails",
                "arguments": {
                    "supplier_id": "#SUP0001"
                }
            }
        ],
        "outputs": [
                "#SO8101"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_011",
        "instruction": "Handle the process of updating variant '8349118980' to a price of 59.99 and ensure it is available as True. Identify order '#W1305304' with the tag 'price_adjusted' and denote it as 'processed'. Verify by retrieving the variant and the order. Provide the updated price.",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "8349118980"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "8349118980",
                    "price": 59.99
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "8349118980",
                    "available": true
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1305304",
                    "tag": "price_adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1305304",
                    "status": "processed"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "8349118980"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1305304"
                }
            }
        ],
        "outputs": [
                "59.99"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_012",
        "instruction": "Coordinate the adjustment of catalog variant '5753502325' to a price of 100.20 and confirm its availability as True. Label order '#W6114312' as 'price_adjusted' and mark it as 'processed'. Validate by accessing the item and the order. Deliver the updated price.",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "5753502325",
                    "price": 100.2
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "5753502325",
                    "available": true
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W6114312",
                    "tag": "price_adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W6114312",
                    "status": "processed"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "5753502325"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W6114312"
                }
            }
        ],
        "outputs": [
                "100.20"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_013",
        "instruction": "Handle a payment of 42.75 on order '#W5299644' using method 'paypal_3345717' with transaction 'NM-MED-1001'. Tag the order as 'reconciled', update the status to 'processed', and retrieve the revised order. Return the transaction ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W5299644"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W5299644",
                    "amount": 42.75,
                    "payment_method_id": "paypal_3345717",
                    "transaction_id": "TX-MED-1001"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W5299644",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W5299644",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W5299644"
                }
            }
        ],
        "outputs": [
                "NM-MED-1001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_014",
        "instruction": "Coordinate the return for tracking '254796145302'. Ensure it is processed by courier '#COU0001', update its address to 12 Birch Road, Suite 12, Houston, NM 78705, USA, and log a 'return_initiated' scan at 2025-03-06T12:00:00. Return the modified courier ID.",
        "actions": [
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "254796145302"
                },
            },
            {
                "name": "reassignCourierForTracking",
                "arguments": {
                    "tracking_id": "254796145302",
                    "courier_id": "#COU0001"
                },
            },
            {
                "name": "upsertTrackingAddress",
                "arguments": {
                    "tracking_id": "254796145302",
                    "address": {
                        "address1": "12 Birch Road",
                        "address2": "Suite 12",
                        "city": "Austin",
                        "state": "TX",
                        "zip": "78705",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "254796145302",
                    "event": "return_initiated",
                    "timestamp": "2025-03-06T12:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "254796145302"
                }
            }
        ],
        "outputs": [
                "#COU0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_015",
        "instruction": "Handle the supply order '#SO9001' with supplier '#SUP0005' for product '2524789262' (item '2492465580') requiring a quantity of 12 at a unit cost of 15.25, then ensure it is marked as 'fulfilled'. Check the supplier details both before and after handling. Provide the supply order ID upon completion.",
        "actions": [
            {
                "name": "getSupplierDetails",
                "arguments": {
                    "supplier_id": "#SUP0005"
                },
            },
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO9001",
                    "supplier_id": "#SUP0005",
                    "product_id": "2524789262",
                    "item_id": "2492465580",
                    "quantity": 12,
                    "unit_cost": 15.25
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO9001",
                    "status": "fulfilled"
                },
            },
            {
                "name": "getSupplierDetails",
                "arguments": {
                    "supplier_id": "#SUP0005"
                }
            }
        ],
        "outputs": [
                "#SO9001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_016",
        "instruction": "Assign a tracking ID using courier '#COU0003' (seed 6001), and coordinate the creation of a new shipment for order '#W9474165' with items ['8649999816','6469567736'] using the 'Two-Day' delivery option. Record 'received' on '2025-03-01T08:00:00' and plan for delivery on '2025-03-02T09:00:00'. Verify by retrieving the new tracking information. Return the new tracking ID once confirmed.",
        "actions": [
            {
                "name": "allocateTrackingId",
                "arguments": {
                    "courier_id": "#COU0003",
                    "seed": 6001
                },
            },
            {
                "name": "splitOrderFulfillment",
                "arguments": {
                    "order_id": "#W9474165",
                    "item_ids": [
                        "8649999816",
                        "6469567736"
                    ],
                    "tracking_id": "TRK-COU0003-6001",
                    "courier_id": "#COU0003",
                    "delivery_options": "Two-Day"
                },
            },
            {
                "name": "appendTrackingEvent",
                "arguments": {
                    "tracking_id": "TRK-COU0003-6001",
                    "event": "received",
                    "timestamp": "2025-03-01T08:00:00"
                },
            },
            {
                "name": "scheduleDelivery",
                "arguments": {
                    "tracking_id": "TRK-COU0003-6001",
                    "scheduled": "2025-03-02T09:00:00"
                },
            },
            {
                "name": "getTrackingInfo",
                "arguments": {
                    "tracking_id": "TRK-COU0003-6001"
                }
            }
        ],
        "outputs": [
                "TRK-COU0003-6001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_017",
        "instruction": "Handle the update of catalog variant '3735133539' by setting the price to 512.49 and marking it as available True. Annotate order '#W2091016' with 'price_adjusted' and change the status to 'processed'. Next, retrieve both the variant and the order to verify and provide the updated price.",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3735133539"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "3735133539",
                    "price": 512.49
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "3735133539",
                    "available": true
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W2091016",
                    "tag": "price_adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W2091016",
                    "status": "processed"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "3735133539"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W2091016"
                }
            }
        ],
        "outputs": [
                "512.49"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_018",
        "instruction": "Coordinate the pricing adjustment for catalog variant '6509212169' by setting it to 88.88 and ensuring availability True. Label order '#W4073673' as 'price_adjusted' and update its status to 'processed'. Confirm by retrieving the variant and the order, and return the updated price.",
        "actions": [
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "6509212169"
                },
            },
            {
                "name": "setVariantPrice",
                "arguments": {
                    "item_id": "6509212169",
                    "price": 88.88
                },
            },
            {
                "name": "setVariantAvailability",
                "arguments": {
                    "item_id": "6509212169",
                    "available": true
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W4073673",
                    "tag": "price_adjusted"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W4073673",
                    "status": "processed"
                },
            },
            {
                "name": "getItemVariant",
                "arguments": {
                    "item_id": "6509212169"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W4073673"
                }
            }
        ],
        "outputs": [
                "88.88"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_019",
        "instruction": "Handle the recording of a payment amounting to 29.11 for order '#W1812830' through payment method 'paypal_2076152', associated with transaction 'NM-MED-2001'. Label the order as 'reconciled', update the status to 'processed', and retrieve the modified order. Provide the transaction ID.",
        "actions": [
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1812830"
                },
            },
            {
                "name": "addOrderPayment",
                "arguments": {
                    "order_id": "#W1812830",
                    "amount": 29.11,
                    "payment_method_id": "paypal_2076152",
                    "transaction_id": "TX-MED-2001"
                },
            },
            {
                "name": "addOrderTag",
                "arguments": {
                    "order_id": "#W1812830",
                    "tag": "reconciled"
                },
            },
            {
                "name": "updateOrderStatus",
                "arguments": {
                    "order_id": "#W1812830",
                    "status": "processed"
                },
            },
            {
                "name": "getOrderDetails",
                "arguments": {
                    "order_id": "#W1812830"
                }
            }
        ],
        "outputs": [
                "NM-MED-2001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_MED_020",
        "instruction": "Coordinate the placement of supply order '#SO9010' with supplier '#SUP0010' for product '3801771308', item '9494281769' in quantity 11 at a unit cost of 12.60, then designate it as 'fulfilled'. Confirm supplier details both before and after. Provide the supply order ID.",
        "actions": [
            {
                "name": "getSupplierDetails",
                "arguments": {
                    "supplier_id": "#SUP0010"
                },
            },
            {
                "name": "placeSupplyOrder",
                "arguments": {
                    "supply_order_id": "#SO9010",
                    "supplier_id": "#SUP0010",
                    "product_id": "3801771308",
                    "item_id": "9494281769",
                    "quantity": 11,
                    "unit_cost": 12.6
                },
            },
            {
                "name": "updateSupplyOrderStatus",
                "arguments": {
                    "supply_order_id": "#SO9010",
                    "status": "fulfilled"
                },
            },
            {
                "name": "getSupplierDetails",
                "arguments": {
                    "supplier_id": "#SUP0010"
                }
            }
        ],
        "outputs": [
                "#SO9010"
        ]
    }
]
