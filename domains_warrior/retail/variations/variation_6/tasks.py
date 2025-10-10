from domains.dto import Task, Action

TASKS = [
    # HARD
    # GOLD 1
    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_001",
        instruction="You are a retail manager and must arrange a Two-Day shipment for order '#W1812830' covering items ['2768401027','6313971174'] using a new tracking from courier '#COU0001' (seed 7001). Record a 'received' scan at '2025-03-01T08:00:00', schedule delivery for '2025-03-02T09:00:00', and add an 'out_for_delivery' scan at '2025-03-02T10:15:00'. Reconcile the order by posting 31.14 via 'gift_card_8541487' with transaction 'TX-HARD-0001', tagging 'reconciled', and marking it 'processed'. Return [new tracking ID, transaction ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0001', 'seed': 7001}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W1812830', 'item_ids': ['2768401027','6313971174'], 'tracking_id': 'TRK-COU0001-7001', 'courier_id': '#COU0001', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-7001', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0001-7001', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-7001', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W1812830', 'amount': 31.14, 'payment_method_id': 'gift_card_8541487', 'transaction_id': 'TX-HARD-0001'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1812830', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1812830', 'status': 'processed'})
        ],
        outputs=["TRK-COU0001-7001","TX-HARD-0001"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_002",
        instruction="You have to adjust price of '4410138384' to 210.00 and set available True. Allocate tracking via '#COU0004' (seed 7003) for order '#W1305304' items ['4410138384','8349118980'] with 'Two-Day'. Add 'received' (2025-03-01T08:00:00) and schedule (2025-03-02T09:00:00). Confirm tracking and return [new price, new tracking ID].",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '4410138384'}),
            Action(name='set_variant_price', kwargs={'item_id': '4410138384', 'price': 210.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '4410138384', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0004', 'seed': 7003}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W1305304', 'item_ids': ['4410138384','8349118980'], 'tracking_id': 'TRK-COU0004-7003', 'courier_id': '#COU0004', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0004-7003', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0004-7003', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0004-7003'})
        ],
        outputs=["210.00","TRK-COU0004-7003"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_003",
        instruction="As a retail manager, you must allocate tracking via '#COU0006' (seed 7006) and split order '#W4073673' items ['6509212169','9354168549'] with 'Two-Day'. Add 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Update catalog price of '9354168549' to 145.00 and set available True. Confirm tracking and variant. Return [new tracking ID, updated price].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0006', 'seed': 7006}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W4073673', 'item_ids': ['6509212169','9354168549'], 'tracking_id': 'TRK-COU0006-7006', 'courier_id': '#COU0006', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0006-7006', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0006-7006', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0006-7006', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='set_variant_price', kwargs={'item_id': '9354168549', 'price': 145.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '9354168549', 'available': True}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0006-7006'}),
            Action(name='get_item_variant', kwargs={'item_id': '9354168549'})
        ],
        outputs=["TRK-COU0006-7006","145.00"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_004",
        instruction="For order '#W6114312', you must post payment 28.93 via 'gift_card_4332117' as 'TX-HARD-0007', tag 'reconciled', set 'processed'. Also reassign existing tracking '663395959263' to courier '#COU0007' after fetching its details and the target courier, and verify after. Return the transaction ID and the new courier ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6114312'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W6114312', 'amount': 28.93, 'payment_method_id': 'gift_card_4332117', 'transaction_id': 'TX-HARD-0007'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6114312', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6114312', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '663395959263'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0007'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '663395959263', 'courier_id': '#COU0007'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '663395959263'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6114312'})
        ],
        outputs=["TX-HARD-0007","#COU0007"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_005",
        instruction="You must update the address for user 'emma_silva_1269' to 500 Oak Street, Suite 10, Dallas, TX 75217, USA. Then arrange a Two-Day shipment for order '#W9527030' item '3229676465' with a new tracking from courier '#COU0008' (seed 7008), ensuring the shipment destination reflects the updated address. Record a 'received' scan at '2025-03-01T08:00:00' and schedule delivery for '2025-03-02T09:00:00'. Return the new tracking ID.",
        actions=[
            Action(name='get_user_by_id', kwargs={'user_id': 'emma_silva_1269'}),
            Action(name='update_user_address', kwargs={'user_id': 'emma_silva_1269', 'address': {'address1':'500 Oak Street','address2':'Suite 10','city':'Dallas','state':'TX','zip':'75217','country':'USA'}}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0008', 'seed': 7008}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['3229676465'], 'tracking_id': 'TRK-COU0008-7008', 'courier_id': '#COU0008', 'delivery_options': 'Two-Day'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0008-7008', 'address': {'address1':'500 Oak Street','address2':'Suite 10','city':'Dallas','state':'TX','zip':'75217','country':'USA'}}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0008-7008', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0008-7008', 'scheduled': '2025-03-02T09:00:00'})
        ],
        outputs=["TRK-COU0008-7008"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_006",
        instruction="For order '#W6874763', you must set variant '6700049080' price to 480.00 and set available False. Then create a new shipment for item ['7528037711'] using courier '#COU0009' (seed 7009) with 'Two-Day', adding 'received' at '2025-03-01T08:00:00', scheduling '2025-03-02T09:00:00', and 'out_for_delivery' at '2025-03-02T10:15:00'. Confirm tracking and variant details. Return [new price, new tracking ID].",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '6700049080'}),
            Action(name='set_variant_price', kwargs={'item_id': '6700049080', 'price': 480.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '6700049080', 'available': False}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0009', 'seed': 7009}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W6874763', 'item_ids': ['7528037711'], 'tracking_id': 'TRK-COU0009-7009', 'courier_id': '#COU0009', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0009-7009', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0009-7009', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0009-7009', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0009-7009'}),
            Action(name='get_item_variant', kwargs={'item_id': '6700049080'})
        ],
        outputs=["480.00","TRK-COU0009-7009"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_007",
        instruction="As a retail manager, you must bring order '#W7538736' out of manual review: classify risk as low (MANUAL_REVIEW_PASSED), add audit visibility with tags 'reviewed' and 'audit_logged', and move it to processing. For shipment '790735957247', switch the carrier to '#COU0005', correct the destination to 410 Lake Drive, Suite 12, Chicago, IL 60610, USA, and reflect a 'received' event receipt on '2025-03-08T11:00:00' with a scheduled delivery at '2025-03-09T09:00:00'. Verify the order and the shipment reflect these changes. Return [risk level, new courier ID].",
        actions=[
            Action(name='fraud_mark_order', kwargs={'order_id': '#W7538736', 'risk_level': 'low', 'reason_code': 'MANUAL_REVIEW_PASSED'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W7538736', 'tag': 'reviewed'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W7538736', 'tag': 'audit_logged'}),
            Action(name='update_order_status', kwargs={'order_id': '#W7538736', 'status': 'processing'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '790735957247', 'courier_id': '#COU0005'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': '790735957247', 'address': {'address1': '410 Lake Drive', 'address2': 'Suite 12', 'city': 'Chicago', 'state': 'IL', 'zip': '60610', 'country': 'USA'}}),
            Action(name='append_tracking_event', kwargs={'tracking_id': '790735957247', 'event': 'received', 'timestamp': '2025-03-08T11:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': '790735957247', 'scheduled': '2025-03-09T09:00:00'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7538736'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '790735957247'})
        ],
        outputs=["low","#COU0005"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_008",
        instruction="For order '#W9527030', you must allocate tracking via '#COU0001' (seed 7013) for items ['7274158061','9314474252'] 'Two-Day', with 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Then update price for '9314474252' to 120.00 and set available True. Confirm tracking and variant. Return [new tracking ID, updated price].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0001', 'seed': 7013}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['7274158061','9314474252'], 'tracking_id': 'TRK-COU0001-7013', 'courier_id': '#COU0001', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-7013', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0001-7013', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-7013', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='set_variant_price', kwargs={'item_id': '9314474252', 'price': 120.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '9314474252', 'available': True}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0001-7013'}),
            Action(name='get_item_variant', kwargs={'item_id': '9314474252'})
        ],
        outputs=["TRK-COU0001-7013","120.00"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_009",
        instruction="You have to reconcile order '#W2091016' by posting 22.22 payment via 'paypal_2055565' txn 'TX-HARD-0014', tagging 'reconciled', and setting status 'processed'. Also update customer 'omar_anderson_5940' address to 157 Spruce Street, Suite 979, Phoenix, AZ 85050, USA. Confirm by reading order and user. Return the transaction ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2091016'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W2091016', 'amount': 22.22, 'payment_method_id': 'paypal_2055565', 'transaction_id': 'TX-HARD-0014'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W2091016', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W2091016', 'status': 'processed'}),
            Action(name='get_user_by_id', kwargs={'user_id': 'omar_anderson_5940'}),
            Action(name='update_user_address', kwargs={'user_id': 'omar_anderson_5940', 'address': {'address1':'157 Spruce Street','address2':'Suite 979','city':'Phoenix','state':'AZ','zip':'85050','country':'USA'}}),
            Action(name='get_order_details', kwargs={'order_id': '#W2091016'}),
            Action(name='get_user_by_id', kwargs={'user_id': 'omar_anderson_5940'})
        ],
        outputs=["TX-HARD-0014"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_010",
        instruction="You have to locate tracking via '#COU0003' (seed 7015) and split order '#W6114312' items ['3111466194'] with 'Two-Day'. Add 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00). Reassign tracking '673941764576' to '#COU0005' after fetching details. Confirm by reading both trackings. Return [new tracking ID, reassigned courier ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0003', 'seed': 7015}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W6114312', 'item_ids': ['3111466194'], 'tracking_id': 'TRK-COU0003-7015', 'courier_id': '#COU0003', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-7015', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0003-7015', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0005'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '673941764576', 'courier_id': '#COU0005'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0003-7015'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'})
        ],
        outputs=["TRK-COU0003-7015","#COU0005"]
    ),

    # GOLD 2
    # complexity_edges: 15 HARD
    Task(
        annotator="0",
        user_id="TASK_HARD_011",
        instruction="You must create supply order '#SO9050' for '#SUP0005' product '2524789262' item '2492465580' qty 6 at unit cost 16.40 and mark it 'cancelled'. Align the catalog by setting the item's price to 0.0 and availability to False, then verify the variant and return the supply order ID.",
        actions=[
            Action(name='get_product_by_id', kwargs={'product_id': '2524789262'}),
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO9050', 'supplier_id': '#SUP0005', 'product_id': '2524789262', 'item_id': '2492465580', 'quantity': 6, 'unit_cost': 16.40}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO9050', 'status': 'cancelled'}),
            Action(name='set_variant_price', kwargs={'item_id': '2492465580', 'price': 0.0}),
            Action(name='set_variant_availability', kwargs={'item_id': '2492465580', 'available': False}),
            Action(name='get_item_variant', kwargs={'item_id': '2492465580'})
        ],
        outputs=["#SO9050"]
    ),

    # complexity_edges: 13 HARD
    Task(
        annotator="0",
        user_id="TASK_HARD_012",
        instruction="As a retail employee, you must allocate tracking with courier '#COU0006' (seed 6101) and create a new shipment for order '#W9527030' for items ['9314474252']. Use delivery 'Two-Day', add 'received' at '2025-03-05T08:00:00' and schedule '2025-03-06T09:00:00'. Fetch the new tracking and return the tracking ID.",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0006', 'seed': 6101}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['9314474252'], 'tracking_id': 'TRK-COU0006-6101', 'courier_id': '#COU0006', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0006-6101', 'event': 'received', 'timestamp': '2025-03-05T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0006-6101', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0006-6101'})
        ],
        outputs=["TRK-COU0006-6101"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_013",
        instruction="You must create supply order '#SO8102' for supplier '#SUP0009' on product '7996920482' item '9862136885' quantity 7 unit cost 18.75 and mark 'cancelled'. Update catalog by setting the variant availability False and price 0.0, then verify the variant. Return the supply order ID.",
        actions=[
            Action(name='get_product_by_id', kwargs={'product_id': '7996920482'}),
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8102', 'supplier_id': '#SUP0009', 'product_id': '7996920482', 'item_id': '9862136885', 'quantity': 7, 'unit_cost': 18.75}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8102', 'status': 'cancelled'}),
            Action(name='set_variant_price', kwargs={'item_id': '9862136885', 'price': 0.0}),
            Action(name='set_variant_availability', kwargs={'item_id': '9862136885', 'available': False}),
            Action(name='get_item_variant', kwargs={'item_id': '9862136885'})
        ],
        outputs=["#SO8102"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_014",
        instruction="You have to settle order '#W9527030' by posting 25.25 via 'paypal_7732922' txn 'TX-HARD-1007', tagging 'reconciled' and marking 'processed'. Reassign tracking '790735957247' to '#COU0004' after fetching tracking and courier, and verify. Return the transaction ID and new courier ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W9527030'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W9527030', 'amount': 25.25, 'payment_method_id': 'paypal_7732922', 'transaction_id': 'TX-HARD-1007'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W9527030', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W9527030', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '790735957247'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0004'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '790735957247', 'courier_id': '#COU0004'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '790735957247'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9527030'})
        ],
        outputs=["TX-HARD-1007", "#COU0004"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_015",
        instruction="You must create supply order '#SO8103' for '#SUP0008' product '6817146515' item '7624783998' qty 5 at unit cost 21.00 and mark 'fulfilled'. Align catalog to availability False and price 0.0, verify variant, and return the supply order ID.",
        actions=[
            Action(name='get_product_by_id', kwargs={'product_id': '6817146515'}),
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8103', 'supplier_id': '#SUP0008', 'product_id': '6817146515', 'item_id': '7624783998', 'quantity': 5, 'unit_cost': 21.00}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8103', 'status': 'fulfilled'}),
            Action(name='set_variant_price', kwargs={'item_id': '7624783998', 'price': 0.0}),
            Action(name='set_variant_availability', kwargs={'item_id': '7624783998', 'available': False}),
            Action(name='get_item_variant', kwargs={'item_id': '7624783998'})
        ],
        outputs=["#SO8103"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_016",
        instruction="You must reconcile order '#W2091016' by posting 24.10 via 'paypal_2055565' txn 'TX-HARD-1014', tagging 'reconciled', and setting 'processed'. Also update item option 'color' to 'green' for item '1270145486'. Confirm by reading order. Return the transaction ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2091016'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W2091016', 'amount': 24.10, 'payment_method_id': 'paypal_2055565', 'transaction_id': 'TX-HARD-1014'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W2091016', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W2091016', 'status': 'processed'}),
            Action(name='update_item_option', kwargs={'order_id': '#W2091016', 'item_id': '1270145486', 'option_key': 'color', 'option_value': 'green'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2091016'})
        ],
        outputs=["TX-HARD-1014"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_017",
        instruction="As a retail admin, you have to cancel items ['4624254797','2635605237'] on order '#W8958831' with reason 'SUPPLIER_ISSUE'. Refund 50.00 with refund_id 'TX-HARD-1019-R' reason 'PARTIAL_CANCELLATION'. Tag 'adjusted' and set status 'processed'. Fetch the order to confirm. Return the refund ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W8958831'}),
            Action(name='cancel_order_items', kwargs={'order_id': '#W8958831', 'item_ids': ['4624254797', '2635605237'], 'reason_code': 'SUPPLIER_ISSUE'}),
            Action(name='refund_order_payment', kwargs={'order_id': '#W8958831', 'amount': 50.00, 'refund_id': 'TX-HARD-1019-R', 'reason_code': 'PARTIAL_CANCELLATION'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W8958831', 'tag': 'adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W8958831', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W8958831'})
        ],
        outputs=["TX-HARD-1019-R"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_018",
        instruction="You have to set variant '9083642334' (Desk Lamp) price to 79.50 and make available True. Then post a payment of 19.99 on '#W1812830' using 'paypal_2076152' as 'TX-HARD-0016', tag 'reconciled', mark order 'processed', and fetch both item and order. Return the new price and transaction ID.",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '9083642334'}),
            Action(name='set_variant_price', kwargs={'item_id': '9083642334', 'price': 79.50}),
            Action(name='set_variant_availability', kwargs={'item_id': '9083642334', 'available': True}),
            Action(name='get_order_details', kwargs={'order_id': '#W1812830'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W1812830', 'amount': 19.99, 'payment_method_id': 'paypal_2076152', 'transaction_id': 'TX-HARD-0016'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1812830', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1812830', 'status': 'processed'}),
            Action(name='get_item_variant', kwargs={'item_id': '9083642334'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1812830'})
        ],
        outputs=["79.50","TX-HARD-0016"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_019",
        instruction="As a retail manager, you must place supply order '#SO8006' with supplier '#SUP0010' for product '3801771308' item '9494281769' (20 units at 11.00), mark it fulfilled, and align the catalog by setting that item's price to 260.00 and availability to True. Return [supply order ID, new price].",
        actions=[
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8006', 'supplier_id': '#SUP0010', 'product_id': '3801771308', 'item_id': '9494281769', 'quantity': 20, 'unit_cost': 11.00}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8006', 'status': 'fulfilled'}),
            Action(name='set_variant_price', kwargs={'item_id': '9494281769', 'price': 260.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '9494281769', 'available': True})
        ],
        outputs=["#SO8006","260.00"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_020",
        instruction="You must reconcile order '#W5299644' by posting 27.77 via 'paypal_3345717' txn 'TX-HARD-3021', tagging 'reconciled', and setting 'processed'. Also update item option 'size' to 'XL' for item '6268080249'. Confirm by reading the order. Return the transaction ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5299644'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W5299644', 'amount': 27.77, 'payment_method_id': 'paypal_3345717', 'transaction_id': 'TX-HARD-3021'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W5299644', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W5299644', 'status': 'processed'}),
            Action(name='update_item_option', kwargs={'order_id': '#W5299644', 'item_id': '6268080249', 'option_key': 'size', 'option_value': 'XL'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5299644'})
        ],
        outputs=["TX-HARD-3021"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_021",
        instruction="For order '#W6114312', you must reconcile the account and finalize delivery arrangements: transfer tracking '673941764576' to courier '#COU0005', set the delivery address to 12 Birch Road, Suite 12, Austin, TX 78705, USA, capture a 'received' scan at '2025-03-01T08:00:00', schedule the delivery for '2025-03-02T09:00:00', and log 'out_for_delivery' at '2025-03-02T10:15:00'. Record a payment of 18.22 via 'gift_card_4332117' (transaction 'TX-HARD-2018'), apply the 'reconciled' tag, move the order to 'processed', and update item '3111466194' option 'color' to 'black'. Recalculate the order total and confirm the updates on tracking and order. Return [transaction ID, new courier ID].",
        actions=[
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '673941764576', 'courier_id': '#COU0005'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': '673941764576', 'address': {'address1': '12 Birch Road', 'address2': 'Suite 12', 'city': 'Austin', 'state': 'TX', 'zip': '78705', 'country': 'USA'}}),
            Action(name='append_tracking_event', kwargs={'tracking_id': '673941764576', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': '673941764576', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': '673941764576', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W6114312', 'amount': 18.22, 'payment_method_id': 'gift_card_4332117', 'transaction_id': 'TX-HARD-2018'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6114312', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6114312', 'status': 'processed'}),
            Action(name='update_item_option', kwargs={'order_id': '#W6114312', 'item_id': '3111466194', 'option_key': 'color', 'option_value': 'black'}),
            Action(name='compute_order_total', kwargs={'order_id': '#W6114312'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6114312'})
        ],
        outputs=["TX-HARD-2018", "#COU0005"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_022",
        instruction="You must cancel item ['5753502325'] on order '#W2631563' with reason 'CUSTOMER_REQUEST'. Then refund 15.25 with refund_id 'TX-HARD-3022-R' and reason 'CUSTOMER_REQUEST'. Tag the order 'adjusted' and set status 'processed'. Fetch the order to confirm. Return the refund ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2631563'}),
            Action(name='cancel_order_items', kwargs={'order_id': '#W2631563', 'item_ids': ['5753502325'], 'reason_code': 'CUSTOMER_REQUEST'}),
            Action(name='refund_order_payment', kwargs={'order_id': '#W2631563', 'amount': 15.25, 'refund_id': 'TX-HARD-3022-R', 'reason_code': 'CUSTOMER_REQUEST'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W2631563', 'tag': 'adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W2631563', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2631563'})
        ],
        outputs=["TX-HARD-3022-R"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_023",
        instruction="On order '#W2091016', you must resolve a customer-request cancellation for item '6546364613': cancel the item with reason 'CUSTOMER_REQUEST' and issue a 231.43 refund with refund_id 'TX-HARD-2020-R' using the same reason. Finalize the order appropriately by tagging it 'adjusted' and setting status to 'processed'. Return the order ID.",
        actions=[
            Action(name='cancel_order_items', kwargs={'order_id': '#W2091016', 'item_ids': ['6546364613'], 'reason_code': 'CUSTOMER_REQUEST'}),
            Action(name='refund_order_payment', kwargs={'order_id': '#W2091016', 'amount': 231.43, 'refund_id': 'TX-HARD-2020-R', 'reason_code': 'CUSTOMER_REQUEST'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W2091016', 'tag': 'adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W2091016', 'status': 'processed'})
        ],
        outputs=["#W2091016"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_024",
        instruction="As a manager, you must reassign tracking '443521489581' to courier '#COU0006' and set its address to 500 Oak Street, Dallas, 75201, USA. Then settle order '#W3113816' with a 25.50 payment via 'credit_card_5869505' (transaction 'TX-HARD-2021'). Verify the tracking afterward. Return the new courier ID.",
        actions=[
            Action(name='get_tracking_info', kwargs={'tracking_id': '443521489581'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '443521489581', 'courier_id': '#COU0006'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': '443521489581', 'address': {'address1': '500 Oak Street', 'city': 'Dallas', 'zip': '75201', 'country': 'USA'}}),
            Action(name='get_order_details', kwargs={'order_id': '#W3113816'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W3113816', 'amount': 25.50, 'payment_method_id': 'credit_card_5869505', 'transaction_id': 'TX-HARD-2021'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '443521489581'})
        ],
        outputs=["#COU0006"]
    ),

    # GOLD 3
    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_025",
        instruction="You are a manager and must have variant '9314474252' reflect a price of 118.75 and be available for sale (available True). Reconcile order '#W9527030' by recording a 12.34 payment via 'paypal_7732922' with transaction 'TX-HARD-3023', tagging it 'reconciled', and marking it 'processed'. Return the new price and the transaction ID.",
        actions=[
            Action(name='set_variant_price', kwargs={'item_id': '9314474252', 'price': 118.75}),
            Action(name='set_variant_availability', kwargs={'item_id': '9314474252', 'available': True}),
            Action(name='add_order_payment', kwargs={'order_id': '#W9527030', 'amount': 12.34, 'payment_method_id': 'paypal_7732922', 'transaction_id': 'TX-HARD-3023'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W9527030', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W9527030', 'status': 'processed'})
        ],
        outputs=["118.75", "TX-HARD-3023"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_026",
        instruction="You are a retail manager and myst create a dedicated Two-Day shipment for order '#W7398274' by moving item '5694328282' onto a new tracking from courier '#COU0002' (seed 7002). The shipment timeline should include 'received' at '2025-03-01T08:00:00', a scheduled delivery at '2025-03-02T09:00:00', and 'out_for_delivery' at '2025-03-02T10:15:00'. Reassign legacy tracking '168643142864' to courier '#COU0003', then reconcile the order with a 20.37 payment via 'paypal_7732922' (transaction 'TX-HARD-0002'), tagging 'reconciled' and marking it 'processed'. Return [new tracking ID, transaction ID, reassigned courier ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0002', 'seed': 7002}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W7398274', 'item_ids': ['5694328282'], 'tracking_id': 'TRK-COU0002-7002', 'courier_id': '#COU0002', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-7002', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0002-7002', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-7002', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '168643142864', 'courier_id': '#COU0003'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W7398274', 'amount': 20.37, 'payment_method_id': 'paypal_7732922', 'transaction_id': 'TX-HARD-0002'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W7398274', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W7398274', 'status': 'processed'}),
        ],
        outputs=["TRK-COU0002-7002", "TX-HARD-0002", "#COU0003"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_027",
        instruction="You have to adjust price of '4410138384' to 210.00 and set available True. Allocate tracking via '#COU0004' (seed 7003) for order '#W1305304' items ['4410138384','8349118980'] with 'Two-Day'. Add 'received' (2025-03-01T08:00:00) and schedule (2025-03-02T09:00:00). Confirm tracking and return [new price, new tracking ID].",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '4410138384'}),
            Action(name='set_variant_price', kwargs={'item_id': '4410138384', 'price': 210.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '4410138384', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0004', 'seed': 7003}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W1305304', 'item_ids': ['4410138384','8349118980'], 'tracking_id': 'TRK-COU0004-7003', 'courier_id': '#COU0004', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0004-7003', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0004-7003', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0004-7003'})
        ],
        outputs=["210.00","TRK-COU0004-7003"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_028",
        instruction="You are a technician and must create a partial shipment on order '#W2325029' for item '9862136885' using delivery option 'Two-Day'. The new tracking (from courier '#COU0005' with seed 7004) will be 'TRK-COU0005-7004'. Record 'received' at '2025-03-01T08:00:00', schedule '2025-03-02T09:00:00', and add 'out_for_delivery' at '2025-03-02T10:15:00'. Also reassign tracking '515122929210' to courier '#COU0004' and verify both the reassigned tracking and the new tracking. Return [new tracking ID, reassigned courier ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0005', 'seed': 7004}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W2325029', 'item_ids': ['9862136885'], 'tracking_id': 'TRK-COU0005-7004', 'courier_id': '#COU0005', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0005-7004', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0005-7004', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0005-7004', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '515122929210', 'courier_id': '#COU0004'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '515122929210'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0005-7004'}),
        ],
        outputs=["TRK-COU0005-7004", "#COU0004"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_029",
        instruction="You create supply order '#SO8002' for supplier '#SUP0001' on product '9523456873' and item '8349118980' in quantity 15 at unit cost 10.25, then mark it 'fulfilled'. You update the catalog by setting the item price to 55.05 and availability to True, and you confirm both product and variant after changes. Return [supply order ID, new price].",
        actions=[
            Action(name='get_product_by_id', kwargs={'product_id': '9523456873'}),
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8002', 'supplier_id': '#SUP0001', 'product_id': '9523456873', 'item_id': '8349118980', 'quantity': 15, 'unit_cost': 10.25}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8002', 'status': 'fulfilled'}),
            Action(name='set_variant_price', kwargs={'item_id': '8349118980', 'price': 55.05}),
            Action(name='set_variant_availability', kwargs={'item_id': '8349118980', 'available': True}),
            Action(name='get_item_variant', kwargs={'item_id': '8349118980'}),
            Action(name='get_product_by_id', kwargs={'product_id': '9523456873'}),
        ],
        outputs=["#SO8002", "55.05"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_030",
        instruction="As a retail manager, you must allocate tracking via '#COU0006' (seed 7006) and split order '#W6114312' items ['3111466194','7211586944'] with 'Two-Day'. Add 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), and 'out_for_delivery' (2025-03-02T10:15:00). Update catalog price of '9354168549' to 145.00 and set available True. Confirm tracking and variant. Return [new tracking ID, updated price].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0006', 'seed': 7006}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W6114312', 'item_ids': ['3111466194','7211586944'], 'tracking_id': 'TRK-COU0006-7006', 'courier_id': '#COU0006', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0006-7006', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0006-7006', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0006-7006', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='set_variant_price', kwargs={'item_id': '9354168549', 'price': 145.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '9354168549', 'available': True}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0006-7006'}),
            Action(name='get_item_variant', kwargs={'item_id': '9354168549'})
        ],
        outputs=["TRK-COU0006-7006","145.00"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_031",
        instruction="For order '#W6114312', you must post payment 28.93 via 'gift_card_4332117' as 'TX-HARD-0007', tag 'reconciled', set 'processed'. Also reassign existing tracking '663395959263' to courier '#COU0007' after fetching its details and the target courier, and verify after. Return the transaction ID and the new courier ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6114312'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W6114312', 'amount': 28.93, 'payment_method_id': 'gift_card_4332117', 'transaction_id': 'TX-HARD-0007'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6114312', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6114312', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '663395959263'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0007'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '663395959263', 'courier_id': '#COU0007'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '663395959263'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6114312'})
        ],
        outputs=["TX-HARD-0007","#COU0007"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_032",
        instruction="You are a manager and must update user 'emma_silva_1269' to 500 Oak Street, Suite 10, Dallas, TX 75217, USA, then create a Two-Day shipment for order '#W9527030' for item '9408160950' using a new tracking from courier '#COU0008' (seed 7008). Ensure the shipment's tracking reflects the Dallas address and shows a 'received' event receipt at '2025-03-01T08:00:00' with delivery scheduled for '2025-03-02T09:00:00'. Return the new tracking ID.",
        actions=[
            Action(name='update_user_address', kwargs={'user_id': 'emma_silva_1269', 'address': {'address1':'500 Oak Street','address2':'Suite 10','city':'Dallas','state':'TX','zip':'75217','country':'USA'}}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0008', 'seed': 7008}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['9408160950'], 'tracking_id': 'TRK-COU0008-7008', 'courier_id': '#COU0008', 'delivery_options': 'Two-Day'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0008-7008', 'address': {'address1':'500 Oak Street','address2':'Suite 10','city':'Dallas','state':'TX','zip':'75217','country':'USA'}}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0008-7008', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0008-7008', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0008-7008'})
        ],
        outputs=["TRK-COU0008-7008"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_033",
        instruction="For order '#W6874763', you must set variant '6700049080' price to 480.00 and set available False. Then create a new shipment for item ['7528037711'] using courier '#COU0009' (seed 7009) with 'Two-Day', adding 'received' at '2025-03-01T08:00:00', scheduling '2025-03-02T09:00:00', and 'out_for_delivery' at '2025-03-02T10:15:00'. Confirm tracking and variant details. Return [new price, new tracking ID].",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '6700049080'}),
            Action(name='set_variant_price', kwargs={'item_id': '6700049080', 'price': 480.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '6700049080', 'available': False}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0009', 'seed': 7009}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W6874763', 'item_ids': ['7528037711'], 'tracking_id': 'TRK-COU0009-7009', 'courier_id': '#COU0009', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0009-7009', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0009-7009', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0009-7009', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0009-7009'}),
            Action(name='get_item_variant', kwargs={'item_id': '6700049080'})
        ],
        outputs=["480.00","TRK-COU0009-7009"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_034",
        instruction="You must create supply order '#SO8003' for supplier '#SUP0008' on product '6817146515' and item '7624783998' in quantity 9 at unit cost 22.10, then mark it 'cancelled'. You align the catalog by setting the item price to 0.0 and availability to False, and you verify the variant afterward. Return the supply order ID.",
        actions=[
            Action(name='get_product_by_id', kwargs={'product_id': '6817146515'}),
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8003', 'supplier_id': '#SUP0008', 'product_id': '6817146515', 'item_id': '7624783998', 'quantity': 9, 'unit_cost': 22.10}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8003', 'status': 'cancelled'}),
            Action(name='set_variant_price', kwargs={'item_id': '7624783998', 'price': 0.0}),
            Action(name='set_variant_availability', kwargs={'item_id': '7624783998', 'available': False}),
            Action(name='get_item_variant', kwargs={'item_id': '7624783998'}),
        ],
        outputs=["#SO8003"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_035",
        instruction="As a retail specialist, you must fraud-mark order '#W7538736' with risk_level 'low' and reason_code 'MANUAL_REVIEW_PASSED'. Then reassign tracking '790735957247' to courier '#COU0005' after fetching tracking and courier details, and confirm after. Return the risk level and the new courier ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7538736'}),
            Action(name='fraud_mark_order', kwargs={'order_id': '#W7538736', 'risk_level': 'low', 'reason_code': 'MANUAL_REVIEW_PASSED'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '790735957247'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0005'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '790735957247', 'courier_id': '#COU0005'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '790735957247'})
        ],
        outputs=["low","#COU0005"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_036",
        instruction="For order '#W9527030', you must allocate tracking via '#COU0001' (seed 7013) for items ['9408160950','1262139877'] 'Two-Day', with 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Then update price for '1262139877' to 120.00 and set available True. Confirm tracking and variant. Return [new tracking ID, updated price].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0001', 'seed': 7013}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['9408160950','1262139877'], 'tracking_id': 'TRK-COU0001-7013', 'courier_id': '#COU0001', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-7013', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0001-7013', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-7013', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='set_variant_price', kwargs={'item_id': '1262139877', 'price': 120.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '1262139877', 'available': True}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0001-7013'}),
            Action(name='get_item_variant', kwargs={'item_id': '1262139877'})
        ],
        outputs=["TRK-COU0001-7013","120.00"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_037",
        instruction="You have to reconcile order '#W2091016' by posting 22.22 payment via 'paypal_2055565' txn 'TX-HARD-0014', tagging 'reconciled', and setting status 'processed'. Also update customer 'omar_anderson_5940' address to 157 Spruce Street, Suite 979, Phoenix, AZ 85050, USA. Confirm by reading the order and the user. Return the transaction ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W2091016'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W2091016', 'amount': 22.22, 'payment_method_id': 'paypal_2055565', 'transaction_id': 'TX-HARD-0014'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W2091016', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W2091016', 'status': 'processed'}),
            Action(name='get_user_by_id', kwargs={'user_id': 'omar_anderson_5940'}),
            Action(name='update_user_address', kwargs={'user_id': 'omar_anderson_5940', 'address': {'address1':'157 Spruce Street','address2':'Suite 979','city':'Phoenix','state':'AZ','zip':'85050','country':'USA'}}),
            Action(name='get_order_details', kwargs={'order_id': '#W2091016'}),
            Action(name='get_user_by_id', kwargs={'user_id': 'omar_anderson_5940'})
        ],
        outputs=["TX-HARD-0014"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_038",
        instruction="You are a manager and must arrange an expedited shipment for item '3111466194' on order '#W6114312' using a new Two-Day tracking from courier '#COU0003' (seed 7015). Record the package as received at '2025-03-01T08:00:00' and schedule delivery for '2025-03-02T09:00:00'. Also move tracking '673941764576' under courier '#COU0005' and confirm both tracking records. Return [new tracking ID, reassigned courier ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0003', 'seed': 7015}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W6114312', 'item_ids': ['3111466194'], 'tracking_id': 'TRK-COU0003-7015', 'courier_id': '#COU0003', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-7015', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0003-7015', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '673941764576', 'courier_id': '#COU0005'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0003-7015'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'})
        ],
        outputs=["TRK-COU0003-7015", "#COU0005"]
    ),

    # GOLD 4
    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_039",
        instruction="You must update variant '9083642334' price to 81.00 and set available True. Allocate tracking via courier '#COU0002' (seed 9001) for order '#W3113816' items ['9083642334'] using 'Two-Day'; add 'received' at '2025-03-05T08:00:00', schedule '2025-03-06T09:00:00', and add 'out_for_delivery' at '2025-03-06T10:15:00'. Confirm by reading tracking and variant. Return [updated price, new tracking ID].",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '9083642334'}),
            Action(name='set_variant_price', kwargs={'item_id': '9083642334', 'price': 81.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '9083642334', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0002', 'seed': 9001}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W3113816', 'item_ids': ['9083642334'], 'tracking_id': 'TRK-COU0002-9001', 'courier_id': '#COU0002', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-9001', 'event': 'received', 'timestamp': '2025-03-05T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0002-9001', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-9001', 'event': 'out_for_delivery', 'timestamp': '2025-03-06T10:15:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0002-9001'}),
            Action(name='get_item_variant', kwargs={'item_id': '9083642334'}),
        ],
        outputs=["81.00", "TRK-COU0002-9001"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_040",
        instruction="You are a manager and must set up a Two-Day shipment for order '#W2091016' for item '3735133539' using a new tracking from courier '#COU0003' (seed 9002). Ensure the shipment timeline records 'received' at '2025-03-05T08:00:00', a scheduled delivery at '2025-03-06T09:00:00', and 'out_for_delivery' at '2025-03-06T10:15:00'. Also reassign tracking '308411122792' to courier '#COU0001'. Return [new tracking ID, reassigned courier ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0003', 'seed': 9002}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W2091016', 'item_ids': ['3735133539'], 'tracking_id': 'TRK-COU0003-9002', 'courier_id': '#COU0003', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-9002', 'event': 'received', 'timestamp': '2025-03-05T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0003-9002', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-9002', 'event': 'out_for_delivery', 'timestamp': '2025-03-06T10:15:00'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '308411122792', 'courier_id': '#COU0001'}),
        ],
        outputs=["TRK-COU0003-9002", "#COU0001"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_041",
        instruction="As a manager, you must settle order '#W1812830' with a 22.45 payment using 'paypal_2076152' (transaction 'TX-HARD-3003'), tag 'reconciled', and mark it 'processed'. Also reassign tracking '604805146457' to courier '#COU0004' and verify the tracking. Return the transaction ID and the new courier ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1812830'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W1812830', 'amount': 22.45, 'payment_method_id': 'paypal_2076152', 'transaction_id': 'TX-HARD-3003'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1812830', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1812830', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '604805146457'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '604805146457', 'courier_id': '#COU0004'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '604805146457'})
        ],
        outputs=["TX-HARD-3003", "#COU0004"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_042",
        instruction="You must create supply order '#SO9020' for supplier '#SUP0011' on product '3377618313' item '6700049080' quantity 5 unit cost 50.00 and mark it 'cancelled'. Update the catalog by setting the variant price to 0.0 and availability to False, then verify the variant. Return the supply order ID.",
        actions=[
            Action(name='get_product_by_id', kwargs={'product_id': '3377618313'}),
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO9020', 'supplier_id': '#SUP0011', 'product_id': '3377618313', 'item_id': '6700049080', 'quantity': 5, 'unit_cost': 50.00}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO9020', 'status': 'cancelled'}),
            Action(name='set_variant_price', kwargs={'item_id': '6700049080', 'price': 0.0}),
            Action(name='set_variant_availability', kwargs={'item_id': '6700049080', 'available': False}),
            Action(name='get_item_variant', kwargs={'item_id': '6700049080'}),
        ],
        outputs=["#SO9020"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_043",
        instruction="As a manager, you must update the address for user 'omar_anderson_5940' to 44 Cypress Way, Floor 3, Phoenix, AZ 85004, USA. Then ship order '#W2091016' item '6546364613' with a new Two-Day tracking from courier '#COU0005' (seed 9005) to that updated address, recording 'received' at '2025-03-05T08:00:00' and scheduling delivery for '2025-03-06T09:00:00'. Return the new tracking ID.",
        actions=[
            Action(name='get_user_by_id', kwargs={'user_id': 'omar_anderson_5940'}),
            Action(name='update_user_address', kwargs={'user_id': 'omar_anderson_5940', 'address': {'address1': '44 Cypress Way', 'address2': 'Floor 3', 'city': 'Phoenix', 'state': 'AZ', 'zip': '85004', 'country': 'USA'}}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0005', 'seed': 9005}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W2091016', 'item_ids': ['6546364613'], 'tracking_id': 'TRK-COU0005-9005', 'courier_id': '#COU0005', 'delivery_options': 'Two-Day'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0005-9005', 'address': {'address1': '44 Cypress Way', 'address2': 'Floor 3', 'city': 'Phoenix', 'state': 'AZ', 'zip': '85004', 'country': 'USA'}}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0005-9005', 'event': 'received', 'timestamp': '2025-03-05T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0005-9005', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0005-9005'})
        ],
        outputs=["TRK-COU0005-9005"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_044",
        instruction="You must cancel items ['5206946487','3111466194'] on order '#W7259850' with reason 'SUPPLIER_ISSUE'. Refund 30.00 with refund_id 'TX-HARD-3006-R' reason 'PARTIAL_CANCELLATION'. Tag the order 'adjusted' and set status 'processed'. Fetch the order to confirm. Return the refund ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7259850'}),
            Action(name='cancel_order_items', kwargs={'order_id': '#W7259850', 'item_ids': ['5206946487', '3111466194'], 'reason_code': 'SUPPLIER_ISSUE'}),
            Action(name='refund_order_payment', kwargs={'order_id': '#W7259850', 'amount': 30.00, 'refund_id': 'TX-HARD-3006-R', 'reason_code': 'PARTIAL_CANCELLATION'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W7259850', 'tag': 'adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W7259850', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W7259850'}),
        ],
        outputs=["TX-HARD-3006-R"]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="TASK_HARD_045",
        instruction="You must prepare a Two-Day shipment for order '#W7398274' covering items ['5694328282','1355937109'] using a new tracking from courier '#COU0010' (seed 9007). The shipment timeline should reflect 'received' at '2025-03-05T08:00:00' and a scheduled delivery at '2025-03-06T09:00:00'. Reconcile the order with a 10.00 payment via 'gift_card_8541487' (transaction 'TX-HARD-3007'), apply the 'reconciled' tag, and mark it processed. Return [new tracking ID, transaction ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0010', 'seed': 9007}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W7398274', 'item_ids': ['5694328282','1355937109'], 'tracking_id': 'TRK-COU0010-9007', 'courier_id': '#COU0010', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0010-9007', 'event': 'received', 'timestamp': '2025-03-05T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0010-9007', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W7398274', 'amount': 10.00, 'payment_method_id': 'gift_card_8541487', 'transaction_id': 'TX-HARD-3007'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W7398274', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W7398274', 'status': 'processed'}),
        ],
        outputs=["TRK-COU0010-9007", "TX-HARD-3007"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_046",
        instruction="You are a technician and must update delivery arrangements by moving tracking '790735957247' to courier '#COU0002', setting its address to 410 Lake Drive, Suite 12, Chicago, IL 60610, USA, and logging a 'delay_reported' event at '2025-03-08T11:00:00'. On order '#W7538736', mark the case as 'investigating' and change status to 'processing'. Verify the tracking after the change. Return the new courier ID.",
        actions=[
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '790735957247', 'courier_id': '#COU0002'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': '790735957247', 'address': {'address1': '410 Lake Drive', 'address2': 'Suite 12', 'city': 'Chicago', 'state': 'IL', 'zip': '60610', 'country': 'USA'}}),
            Action(name='append_tracking_event', kwargs={'tracking_id': '790735957247', 'event': 'delay_reported', 'timestamp': '2025-03-08T11:00:00'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W7538736', 'tag': 'investigating'}),
            Action(name='update_order_status', kwargs={'order_id': '#W7538736', 'status': 'processing'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '790735957247'})
        ],
        outputs=["#COU0002"]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="TASK_HARD_047",
        instruction="You must place supply order '#SO9030' with supplier '#SUP0009' for product '7996920482' item '9862136885' quantity 8 at unit cost 19.00 and mark it 'fulfilled'. Set the item's price to 139.00 and available True. Allocate tracking via '#COU0004' (seed 9009) for order '#W2325029' item ['9862136885'] with 'Two-Day' and schedule '2025-03-06T09:00:00'. Confirm by reading tracking and variant. Return [new tracking ID, updated price].",
        actions=[
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO9030', 'supplier_id': '#SUP0009', 'product_id': '7996920482', 'item_id': '9862136885', 'quantity': 8, 'unit_cost': 19.00}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO9030', 'status': 'fulfilled'}),
            Action(name='set_variant_price', kwargs={'item_id': '9862136885', 'price': 139.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '9862136885', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0004', 'seed': 9009}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W2325029', 'item_ids': ['9862136885'], 'tracking_id': 'TRK-COU0004-9009', 'courier_id': '#COU0004', 'delivery_options': 'Two-Day'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0004-9009', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0004-9009'}),
            Action(name='get_item_variant', kwargs={'item_id': '9862136885'}),
        ],
        outputs=["TRK-COU0004-9009", "139.00"]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="TASK_HARD_048",
        instruction="You must reassign tracking '254796145302' to courier '#COU0010' after fetching tracking and courier details. Then settle order '#W1305304' by posting 15.75 via 'gift_card_4332117' with transaction 'TX-HARD-3010', tag 'reconciled', and set status 'processed'. Verify the tracking after reassignment. Return [transaction ID, new courier ID].",
        actions=[
                Action(name='get_tracking_info', kwargs={'tracking_id': '254796145302'}),
                Action(name='get_courier_details', kwargs={'courier_id': '#COU0010'}),
                Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '254796145302', 'courier_id': '#COU0010'}),
                Action(name='get_order_details', kwargs={'order_id': '#W1305304'}),
                Action(name='add_order_payment', kwargs={'order_id': '#W1305304', 'amount': 15.75, 'payment_method_id': 'gift_card_4332117', 'transaction_id': 'TX-HARD-3010'}),
                Action(name='add_order_tag', kwargs={'order_id': '#W1305304', 'tag': 'reconciled'}),
                Action(name='update_order_status', kwargs={'order_id': '#W1305304', 'status': 'processed'}),
                Action(name='get_tracking_info', kwargs={'tracking_id': '254796145302'}),
        ],
        outputs=["TX-HARD-3010", "#COU0010"]
    ),

    # ADDITIONAL
    Task(
        annotator="0",
        user_id="TASK_HARD_049",
        instruction="You are handling settlement for order '#W4817420'. Use payment method 'gift_card_0000000' to record an exact payment of 21.44 under transaction 'TX-2001'. Then you must add the tag 'reconciled' and switch the order status to 'processed'. You also need to annotate the order '#W4817420' with a fraud mark: risk_level 'low' and reason_code 'MANUAL_REVIEW_PASSED'. This is metadata only—no status changes.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W4817420'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W4817420', 'amount': 21.44, 'payment_method_id': 'gift_card_0000000', 'transaction_id': 'TX-2001'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W4817420', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W4817420', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4817420'}),
            Action(name='fraud_mark_order', kwargs={'order_id': '#W4817420', 'risk_level': 'low', 'reason_code': 'MANUAL_REVIEW_PASSED'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4817420'})
        ],
        outputs=['TX-2001', 'low']
    ),

    Task(
        annotator="0",
        user_id="TASK_HARD_050",
        instruction="You are reconciling order '#W6304490'. Record a payment of 25.72 with payment_method_id 'gift_card_0000000' and transaction_id 'TX-2005'. Next, you should add the tag 'reconciled' and mark the order 'processed'. You should update the catalog entry for variant '9647292434': price → 57.48, available → True. Verify the change by fetching the variant afterwards.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W6304490'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W6304490', 'amount': 25.72, 'payment_method_id': 'gift_card_0000000', 'transaction_id': 'TX-2005'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6304490', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6304490', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6304490'}),
            Action(name='get_item_variant', kwargs={'item_id': '9647292434'}),
            Action(name='set_variant_price', kwargs={'item_id': '9647292434', 'price': 57.48}),
            Action(name='set_variant_availability', kwargs={'item_id': '9647292434', 'available': True}),
            Action(name='get_item_variant', kwargs={'item_id': '9647292434'})
        ],
        outputs=['TX-2005', '57.48']
    ),

    # EXPERT
    # GOLD 1
    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="TASK_EXP_001",
        instruction="For order '#W9527030', you have to update the price of '3229676465' to 79.99 and set available True; also update '7274158061' price to 44.99 and set available True. Allocate tracking via '#COU0003' (seed 8002) and split items ['3229676465','7274158061'] with 'Two-Day'; add 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Upsert tracking address to 667 Elm Street, Suite 624, Chicago, IL 60641, USA. Confirm by reading tracking and both variants. Return [new tracking ID, prices].",
        actions=[
            Action(name='set_variant_price', kwargs={'item_id': '3229676465', 'price': 79.99}),
            Action(name='set_variant_availability', kwargs={'item_id': '3229676465', 'available': True}),
            Action(name='set_variant_price', kwargs={'item_id': '7274158061', 'price': 44.99}),
            Action(name='set_variant_availability', kwargs={'item_id': '7274158061', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0003', 'seed': 8002}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['3229676465','7274158061'], 'tracking_id': 'TRK-COU0003-8002', 'courier_id': '#COU0003', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-8002', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0003-8002', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-8002', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0003-8002', 'address': {'address1':'667 Elm Street','address2':'Suite 624','city':'Chicago','state':'IL','zip':'60641','country':'USA'}}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0003-8002'}),
            Action(name='get_item_variant', kwargs={'item_id': '3229676465'}),
            Action(name='get_item_variant', kwargs={'item_id': '7274158061'})
        ],
        outputs=["TRK-COU0003-8002","79.99","44.99"]
    ),

    # complexity_edges: 16
    Task(
        annotator="0",
        user_id="TASK_EXP_002",
        instruction="You must handle a complex reconciliation for '#W6114312': (1) Reassign tracking '673941764576' to courier '#COU0001' after fetching both. (2) Update prices for '5753502325'→96.35 (set available True) and '3735133539'→508.37 (set available True). (3) Post payment 45.00 via 'gift_card_4332117' as 'TX-EXP-0003', fraud-mark risk 'low' with reason 'MANUAL_REVIEW_PASSED'. (4) Tag 'reconciled', set status 'processed'. Confirm by reading tracking, both variants, and order. Return [new courier ID, transaction ID, risk level].",
        actions=[
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0001'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '673941764576', 'courier_id': '#COU0001'}),
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'}),
            Action(name='set_variant_price', kwargs={'item_id': '5753502325', 'price': 96.35}),
            Action(name='set_variant_availability', kwargs={'item_id': '5753502325', 'available': True}),
            Action(name='get_item_variant', kwargs={'item_id': '3735133539'}),
            Action(name='set_variant_price', kwargs={'item_id': '3735133539', 'price': 508.37}),
            Action(name='set_variant_availability', kwargs={'item_id': '3735133539', 'available': True}),
            Action(name='add_order_payment', kwargs={'order_id': '#W6114312', 'amount': 45.00, 'payment_method_id': 'gift_card_4332117', 'transaction_id': 'TX-EXP-0003'}),
            Action(name='fraud_mark_order', kwargs={'order_id': '#W6114312', 'risk_level': 'low', 'reason_code': 'MANUAL_REVIEW_PASSED'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6114312', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6114312', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'}),
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'}),
            Action(name='get_item_variant', kwargs={'item_id': '3735133539'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6114312'})
        ],
        outputs=["#COU0001","TX-EXP-0003","low"]
    ),

    # complexity_edges: 23
    Task(
        annotator="0",
        user_id="TASK_EXP_003",
        instruction="You are conducting a San Jose user audit. First, list all users in 'San Jose'. Then correct the address for user 'omar_taylor_1594' to 1000 King Road, Suite 12, San Jose, CA 95112, USA. Finally, arrange shipment of order '#W8958831' item '5537798301' via courier '#COU0007' using a new Two-Day tracking (seed 7160) with a 'received' scan on '2025-03-11T08:00:00' and delivery scheduled for '2025-03-12T09:00:00'. Confirm the updated user record and the new tracking. Return nothing.",
        actions=[
            Action(name='find_users_by_city', kwargs={'city': 'San Jose'}),
            Action(name='get_user_by_id', kwargs={'user_id': 'omar_taylor_1594'}),
            Action(name='update_user_address', kwargs={'user_id': 'omar_taylor_1594', 'address': {'address1': '1000 King Road', 'address2': 'Suite 12', 'city': 'San Jose', 'state': 'CA', 'zip': '95112', 'country': 'USA'}}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0007', 'seed': 7160}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W8958831', 'item_ids': ['5537798301'], 'tracking_id': 'TRK-COU0007-7160', 'courier_id': '#COU0007', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0007-7160', 'event': 'received', 'timestamp': '2025-03-11T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0007-7160', 'scheduled': '2025-03-12T09:00:00'}),
            Action(name='get_user_by_id', kwargs={'user_id': 'omar_taylor_1594'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0007-7160'})
        ],
        outputs=[]
    ),

    # complexity_edges: 20
    Task(
        annotator="0",
        user_id="TASK_EXP_004",
        instruction="As a manager, you must replenish item '7211586944' by placing and fulfilling (status fulfilled) supply order '#SO8015' with supplier '#SUP0009' for product '7996920482' (12 units at 14.00). Reflect the change in the catalog by setting its price to 129.99 and making available True. Then arrange a Two-Day shipment of that item on order '#W2325029' using a new tracking from courier '#COU0004' (seed 8026) with delivery scheduled for '2025-03-02T09:00:00'. Return [tracking ID, updated price].",
        actions=[
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8015', 'supplier_id': '#SUP0009', 'product_id': '7996920482', 'item_id': '7211586944', 'quantity': 12, 'unit_cost': 14.00}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8015', 'status': 'fulfilled'}),
            Action(name='set_variant_price', kwargs={'item_id': '7211586944', 'price': 129.99}),
            Action(name='set_variant_availability', kwargs={'item_id': '7211586944', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0004', 'seed': 8026}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W2325029', 'item_ids': ['7211586944'], 'tracking_id': 'TRK-COU0004-8026', 'courier_id': '#COU0004', 'delivery_options': 'Two-Day'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0004-8026', 'scheduled': '2025-03-02T09:00:00'}),
        ],
        outputs=["TRK-COU0004-8026", "129.99"]
    ),

    # complexity_edges: 20
    Task(
        annotator="0",
        user_id="TASK_EXP_005",
        instruction="You are a manager and must make variant '3229676465' sellable (available True) at 82.50 and then arrange a Two-Day combined shipment for order '#W9527030' (items '3229676465' and '7274158061') using a new tracking from courier '#COU0003' (seed 8027). The shipment timeline should include 'received' at '2025-03-01T08:00:00' and a scheduled delivery at '2025-03-02T09:00:00'. Mark the order reconciled and processed. Return the new tracking ID.",
        actions=[
            Action(name='set_variant_price', kwargs={'item_id': '3229676465', 'price': 82.50}),
            Action(name='set_variant_availability', kwargs={'item_id': '3229676465', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0003', 'seed': 8027}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['3229676465','7274158061'], 'tracking_id': 'TRK-COU0003-8027', 'courier_id': '#COU0003', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-8027', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0003-8027', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W9527030', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W9527030', 'status': 'processed'}),
        ],
        outputs=["TRK-COU0003-8027"]
    ),

    # GOLD 2
    # complexity_edges: 27 #EXP
    Task(
        annotator="0",
        user_id="TASK_EXP_006",
        instruction="As a retail manager, you must allocate tracking with '#COU0001' (seed 7101) and split order '#W1812830' items ['7791931443','2768401027'] with 'Two-Day'. Add 'received' (2025-03-07T08:00:00), schedule (2025-03-08T09:00:00), and 'out_for_delivery' (2025-03-08T10:15:00). Post payment 33.33 via 'gift_card_8541487' txn 'TX-HARD-1001', tag 'reconciled', set status 'processed'. Confirm by reading tracking and order. Return [tracking ID, transaction ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0001', 'seed': 7101}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W1812830', 'item_ids': ['7791931443', '2768401027'], 'tracking_id': 'TRK-COU0001-7101', 'courier_id': '#COU0001', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-7101', 'event': 'received', 'timestamp': '2025-03-07T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0001-7101', 'scheduled': '2025-03-08T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-7101', 'event': 'out_for_delivery', 'timestamp': '2025-03-08T10:15:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0001-7101'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1812830'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W1812830', 'amount': 33.33, 'payment_method_id': 'gift_card_8541487', 'transaction_id': 'TX-HARD-1001'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1812830', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1812830', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1812830'})
        ],
        outputs=["TRK-COU0001-7101", "TX-HARD-1001"]
    ),


    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="TASK_EXP_007",
        instruction="For order '#W6114312': you must reassign tracking '673941764576' to '#COU0001' after fetching both. Update prices '5753502325'→95.10 and '3735133539'→509.10, set both available True. Post payment 44.00 via 'gift_card_4332117' txn 'TX-EXP-1003'; fraud-mark 'low' reason 'MANUAL_REVIEW_PASSED'; tag 'reconciled'; set 'processed'. Confirm by reading tracking, both variants, and order. Return [courier ID, transaction ID, risk].",
        actions=[
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0001'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '673941764576', 'courier_id': '#COU0001'}),
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'}),
            Action(name='set_variant_price', kwargs={'item_id': '5753502325', 'price': 95.10}),
            Action(name='set_variant_availability', kwargs={'item_id': '5753502325', 'available': True}),
            Action(name='get_item_variant', kwargs={'item_id': '3735133539'}),
            Action(name='set_variant_price', kwargs={'item_id': '3735133539', 'price': 509.10}),
            Action(name='set_variant_availability', kwargs={'item_id': '3735133539', 'available': True}),
            Action(name='add_order_payment', kwargs={'order_id': '#W6114312', 'amount': 44.00, 'payment_method_id': 'gift_card_4332117', 'transaction_id': 'TX-EXP-1003'}),
            Action(name='fraud_mark_order', kwargs={'order_id': '#W6114312', 'risk_level': 'low', 'reason_code': 'MANUAL_REVIEW_PASSED'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6114312', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6114312', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'}),
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'}),
            Action(name='get_item_variant', kwargs={'item_id': '3735133539'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6114312'})
        ],
        outputs=["#COU0001", "TX-EXP-1003", "low"]
    ),

    # complexity_edges: 21
    Task(
        annotator="0",
        user_id="TASK_EXP_008",
        instruction="As a manager, you must fulfill (status fulfilled) supply order '#SO8115' with supplier '#SUP0009' for product '7996920482' item '7211586944' (12 units at 14.00), then update the catalog to price the item at 129.25 and mark available True. Arrange a Two-Day shipment on order '#W2325029' for that item using a new tracking from courier '#COU0004' (seed 8226) and schedule delivery for '2025-03-02T09:00:00'. Return [tracking ID, updated price].",
        actions=[
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8115', 'supplier_id': '#SUP0009', 'product_id': '7996920482', 'item_id': '7211586944', 'quantity': 12, 'unit_cost': 14.00}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8115', 'status': 'fulfilled'}),
            Action(name='set_variant_price', kwargs={'item_id': '7211586944', 'price': 129.25}),
            Action(name='set_variant_availability', kwargs={'item_id': '7211586944', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0004', 'seed': 8226}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W2325029', 'item_ids': ['7211586944'], 'tracking_id': 'TRK-COU0004-8226', 'courier_id': '#COU0004', 'delivery_options': 'Two-Day'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0004-8226', 'scheduled': '2025-03-02T09:00:00'})
        ],
        outputs=["TRK-COU0004-8226", "129.25"]
    ),

    # complexity_edges: 20
    Task(
        annotator="0",
        user_id="TASK_EXP_009",
        instruction="You are a technician and have to make variant '3229676465' sellable (available True) at 82.75. Arrange a combined Two-Day shipment on order '#W9527030' for items '3229676465' and '7274158061' using a new tracking from courier '#COU0003' (seed 8227). The shipment timeline should include 'received' at '2025-03-01T08:00:00' and a scheduled delivery at '2025-03-02T09:00:00'. Mark the order reconciled and processed. Return the new tracking ID.",
        actions=[
            Action(name='set_variant_price', kwargs={'item_id': '3229676465', 'price': 82.75}),
            Action(name='set_variant_availability', kwargs={'item_id': '3229676465', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0003', 'seed': 8227}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['3229676465','7274158061'], 'tracking_id': 'TRK-COU0003-8227', 'courier_id': '#COU0003', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-8227', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0003-8227', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W9527030', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W9527030', 'status': 'processed'}),
        ],
        outputs=["TRK-COU0003-8227"]
    ),

    # complexity_edges: 21 EXP
    Task(
        annotator="0",
        user_id="TASK_EXP_010",
        instruction="You must allocate tracking via '#COU0006' (seed 7106) and split order '#W6114312' items ['3111466194'] 'Two-Day', add 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), and 'out_for_delivery' (2025-03-02T10:15:00). Update price of '5753502325' to 101.35 and set available True. Confirm tracking and variant. Return [tracking ID, updated price].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0006', 'seed': 7106}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W6114312', 'item_ids': ['3111466194'], 'tracking_id': 'TRK-COU0006-7106', 'courier_id': '#COU0006', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0006-7106', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0006-7106', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0006-7106', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='set_variant_price', kwargs={'item_id': '5753502325', 'price': 101.35}),
            Action(name='set_variant_availability', kwargs={'item_id': '5753502325', 'available': True}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0006-7106'}),
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'})
        ],
        outputs=["TRK-COU0006-7106", "101.35"]
    ),

    # complexity_edges: 22 EXP
    Task(
        annotator="0",
        user_id="TASK_EXP_011",
        instruction="You must allocate tracking via '#COU0001' (seed 7113) for order '#W9527030' items ['3229676465','7274158061'] 'Two-Day' with 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Update price for '3229676465' to 80.00 and set available True. Confirm tracking and variant. Return [tracking ID, updated price].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0001', 'seed': 7113}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['3229676465', '7274158061'], 'tracking_id': 'TRK-COU0001-7113', 'courier_id': '#COU0001', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-7113', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0001-7113', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-7113', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='set_variant_price', kwargs={'item_id': '3229676465', 'price': 80.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '3229676465', 'available': True}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0001-7113'}),
            Action(name='get_item_variant', kwargs={'item_id': '3229676465'})
        ],
        outputs=["TRK-COU0001-7113", "80.00"]
    ),

    # complexity_edges: 18 EXP
    Task(
        annotator="0",
        user_id="TASK_EXP_012",
        instruction="As a retail manager, you must create a Two-Day shipment on order '#W6114312' for item '5206946487' using a new tracking from '#COU0003' (seed 7115). Record 'received' on '2025-03-03T08:00:00' and schedule delivery '2025-03-04T09:00:00'. Reassign legacy tracking '673941764576' to '#COU0007' and verify both trackings. Return [new tracking ID, reassigned courier ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0003', 'seed': 7115}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W6114312', 'item_ids': ['5206946487'], 'tracking_id': 'TRK-COU0003-7115', 'courier_id': '#COU0003', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-7115', 'event': 'received', 'timestamp': '2025-03-03T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0003-7115', 'scheduled': '2025-03-04T09:00:00'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '673941764576', 'courier_id': '#COU0007'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0003-7115'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'})
        ],
        outputs=["TRK-COU0003-7115", "#COU0007"]
    ),

    # GOLD 3
    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="TASK_EXP_013",
        instruction="You remediate order '#W8863729' by moving item '5105441284' to a new tracking allocated from '#COU0002' with seed 8001 and delivery 'Two-Day' with events at '2025-03-01T08:00:00' ('received') and '2025-03-02T10:15:00' ('out_for_delivery') and a scheduled delivery at '2025-03-02T09:00:00'. You reassign existing tracking '604805146457' to '#COU0006', fraud-mark risk 'low' with reason 'MANUAL_REVIEW_PASSED', post the payment 'TX-EXP-0001' of 3766.59 using 'paypal_1521508', tag 'reconciled', and set status 'processed'. Return [new tracking ID, transaction ID, risk level].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0002', 'seed': 8001}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W8863729', 'item_ids': ['5105441284'], 'tracking_id': 'TRK-COU0002-8001', 'courier_id': '#COU0002', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-8001', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0002-8001', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-8001', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '604805146457'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '604805146457', 'courier_id': '#COU0006'}),
            Action(name='fraud_mark_order', kwargs={'order_id': '#W8863729', 'risk_level': 'low', 'reason_code': 'MANUAL_REVIEW_PASSED'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W8863729', 'amount': 3766.59, 'payment_method_id': 'paypal_1521508', 'transaction_id': 'TX-EXP-0001'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W8863729', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W8863729', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0002-8001'}),
        ],
        outputs=["TRK-COU0002-8001", "TX-EXP-0001", "low"]
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="TASK_EXP_014",
        instruction="For order '#W9527030', you have to update the price of '9408160950' to 79.99 and set available True; also update '1262139877' price to 44.99 and set available True. Allocate tracking via '#COU0003' (seed 8002) and split items ['9408160950','1262139877'] with 'Two-Day'; add 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), and 'out_for_delivery' (2025-03-02T10:15:00). Upsert the new tracking address to 667 Elm Street, Suite 624, Chicago, IL 60641, USA. Confirm by reading tracking and both variants. Return [new tracking ID, prices].",
        actions=[
            Action(name='set_variant_price', kwargs={'item_id': '9408160950', 'price': 79.99}),
            Action(name='set_variant_availability', kwargs={'item_id': '9408160950', 'available': True}),
            Action(name='set_variant_price', kwargs={'item_id': '1262139877', 'price': 44.99}),
            Action(name='set_variant_availability', kwargs={'item_id': '1262139877', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0003', 'seed': 8002}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['9408160950','1262139877'], 'tracking_id': 'TRK-COU0003-8002', 'courier_id': '#COU0003', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-8002', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0003-8002', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-8002', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0003-8002', 'address': {'address1':'667 Elm Street','address2':'Suite 624','city':'Chicago','state':'IL','zip':'60641','country':'USA'}}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0003-8002'}),
            Action(name='get_item_variant', kwargs={'item_id': '9408160950'}),
            Action(name='get_item_variant', kwargs={'item_id': '1262139877'})
        ],
        outputs=["TRK-COU0003-8002","79.99","44.99"]
    ),

    # complexity_edges: 16
    Task(
        annotator="0",
        user_id="TASK_EXP_015",
        instruction="You must handle a complex reconciliation for '#W6114312': (1) Reassign tracking '673941764576' to courier '#COU0001' after fetching both. (2) Update prices for '5753502325'→96.35 (set available True) and '3735133539'→508.37 (set available True). (3) Post payment 45.00 via 'gift_card_4332117' as 'TX-EXP-0003', fraud-mark risk 'low' with reason 'MANUAL_REVIEW_PASSED'. (4) Tag 'reconciled', set status 'processed'. Confirm by reading tracking, both variants, and order. Return [new courier ID, transaction ID, risk level].",
        actions=[
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0001'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '673941764576', 'courier_id': '#COU0001'}),
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'}),
            Action(name='set_variant_price', kwargs={'item_id': '5753502325', 'price': 96.35}),
            Action(name='set_variant_availability', kwargs={'item_id': '5753502325', 'available': True}),
            Action(name='get_item_variant', kwargs={'item_id': '3735133539'}),
            Action(name='set_variant_price', kwargs={'item_id': '3735133539', 'price': 508.37}),
            Action(name='set_variant_availability', kwargs={'item_id': '3735133539', 'available': True}),
            Action(name='add_order_payment', kwargs={'order_id': '#W6114312', 'amount': 45.00, 'payment_method_id': 'gift_card_4332117', 'transaction_id': 'TX-EXP-0003'}),
            Action(name='fraud_mark_order', kwargs={'order_id': '#W6114312', 'risk_level': 'low', 'reason_code': 'MANUAL_REVIEW_PASSED'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6114312', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6114312', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '673941764576'}),
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'}),
            Action(name='get_item_variant', kwargs={'item_id': '3735133539'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6114312'})
        ],
        outputs=["#COU0001","TX-EXP-0003","low"]
    ),

    # complexity_edges: 30
    Task(
        annotator="0",
        user_id="TASK_EXP_016",
        instruction="For order '#W1305304': you must reprice '5694328282' to 335.00 and '3952176596' to 1190.00, set both available True. Allocate tracking '#COU0007' seed 8204 and split those items 'Two-Day'; add 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00). Upsert tracking address to 103 Pine Lane, Suite 730, Austin, TX 78703, USA and verify. Refund amount 1525.00 with refund_id 'TX-EXP-1004-R' reason 'PRICE_ADJUSTMENT'; tag 'adjusted'; set 'processed'. Return [tracking ID, refund ID].",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '5694328282'}),
            Action(name='set_variant_price', kwargs={'item_id': '5694328282', 'price': 335.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '5694328282', 'available': True}),
            Action(name='get_item_variant', kwargs={'item_id': '3952176596'}),
            Action(name='set_variant_price', kwargs={'item_id': '3952176596', 'price': 1190.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '3952176596', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0007', 'seed': 8204}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W1305304', 'item_ids': ['5694328282', '3952176596'], 'tracking_id': 'TRK-COU0007-8204', 'courier_id': '#COU0007', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0007-8204', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0007-8204', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0007-8204', 'address': {'address1': '103 Pine Lane', 'address2': 'Suite 730', 'city': 'Austin', 'state': 'TX', 'zip': '78703', 'country': 'USA'}}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0007-8204'}),
            Action(name='refund_order_payment', kwargs={'order_id': '#W1305304', 'amount': 1525.00, 'refund_id': 'TX-EXP-1004-R', 'reason_code': 'PRICE_ADJUSTMENT'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1305304', 'tag': 'adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1305304', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0007-8204'})
        ],
        outputs=["TRK-COU0007-8204", "TX-EXP-1004-R"]
    ),

    # complexity_edges: 16
    Task(
        annotator="0",
        user_id="TASK_EXP_017",
        instruction="As a retail manager, you should handle the full audit and correction on '#W2325029': (1) Reassign tracking '308411122792' to '#COU0004' after fetching current details and target courier. (2) Allocate '#COU0005' (seed 8005) and split items ['5606522780','9045948550'] 'Two-Day'; add 'received' (2025-03-01T08:00:00) and schedule (2025-03-02T09:00:00). (3) Upsert tracking address to 498 Elm Avenue, Suite 953, San Jose, CA 95155, USA. (4) Post payment 18.50 via 'paypal_2076152' txn 'TX-EXP-0005', tag 'reconciled', set 'processed'. Confirm by reading both trackings and order. Return [reassigned courier ID, new tracking ID, transaction ID].",
        actions=[
            Action(name='get_tracking_info', kwargs={'tracking_id': '308411122792'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0004'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '308411122792', 'courier_id': '#COU0004'}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0005', 'seed': 8005}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W2325029', 'item_ids': ['5606522780','9045948550'], 'tracking_id': 'TRK-COU0005-8005', 'courier_id': '#COU0005', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0005-8005', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0005-8005', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0005-8005', 'address': {'address1':'498 Elm Avenue','address2':'Suite 953','city':'San Jose','state':'CA','zip':'95155','country':'USA'}}),
            Action(name='add_order_payment', kwargs={'order_id': '#W2325029', 'amount': 18.50, 'payment_method_id': 'paypal_2076152', 'transaction_id': 'TX-EXP-0005'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W2325029', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W2325029', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '308411122792'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0005-8005'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2325029'})
        ],
        outputs=["#COU0004","TRK-COU0005-8005","TX-EXP-0005"]
    ),

    # complexity_edges: 22
    Task(
        annotator="0",
        user_id="TASK_EXP_018",
        instruction="You are a manager and must ensure stock and fulfillment for item '7211586944': place and fulfill (status fulfilled) supply order '#SO8015' with '#SUP0009' for product '7996920482' (12 units each 14.00), update the catalog so that item is priced 129.99 and available True, and arrange a Two-Day shipment on order '#W2091016' using a fresh tracking from courier '#COU0004' (seed 8026) with delivery scheduled for '2025-03-02T09:00:00'. Return [tracking ID, updated price].",
        actions=[
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8015', 'supplier_id': '#SUP0009', 'product_id': '7996920482', 'item_id': '7211586944', 'quantity': 12, 'unit_cost': 14.00}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8015', 'status': 'fulfilled'}),
            Action(name='set_variant_price', kwargs={'item_id': '7211586944', 'price': 129.99}),
            Action(name='set_variant_availability', kwargs={'item_id': '7211586944', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0004', 'seed': 8026}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W2091016', 'item_ids': ['7211586944'], 'tracking_id': 'TRK-COU0004-8026', 'courier_id': '#COU0004', 'delivery_options': 'Two-Day'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0004-8026', 'scheduled': '2025-03-02T09:00:00'}),
        ],
        outputs=["TRK-COU0004-8026", "129.99"]
    ),

    # complexity_edges: 16
    Task(
        annotator="0",
        user_id="TASK_EXP_019",
        instruction="You are a manager and must place supply order '#SO8009' with supplier '#SUP0002' for product '1968349452' (item '3541421151') for 7 units at 19.25 and mark it fulfilled (status fulfilled). Update tracking '713743776331' so its timeline reflects a 'received' scan at '2025-05-01T08:00:00' and a scheduled delivery at '2025-05-02T09:00:00'. Return the supply order ID.",
        actions=[
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8009', 'supplier_id': '#SUP0002', 'product_id': '1968349452', 'item_id': '3541421151', 'quantity': 7, 'unit_cost': 19.25}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8009', 'status': 'fulfilled'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': '713743776331', 'event': 'received', 'timestamp': '2025-05-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': '713743776331', 'scheduled': '2025-05-02T09:00:00'}),
        ],
        outputs=["#SO8009"]
    ),

    # complexity_edges: 21
    Task(
        annotator="0",
        user_id="TASK_EXP_020",
        instruction="You are a manager and must arrange a Two-Day shipment on order '#W1812830' for item '7791931443' using a new tracking from courier '#COU0005' (seed 8228). Ensure the timeline reflects a 'received' scan at '2025-03-01T08:00:00' and a scheduled delivery at '2025-03-02T09:00:00'. Process a partial refund of 199.00 (refund_id 'TX-EXP-1013-R', reason 'CUSTOMER_REQUEST'), label the order as adjusted, and move it to processed. Return the new tracking ID.",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0005', 'seed': 8228}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W1812830', 'item_ids': ['7791931443'], 'tracking_id': 'TRK-COU0005-8228', 'courier_id': '#COU0005', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0005-8228', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0005-8228', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='refund_order_payment', kwargs={'order_id': '#W1812830', 'amount': 199.00, 'refund_id': 'TX-EXP-1013-R', 'reason_code': 'CUSTOMER_REQUEST'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1812830', 'tag': 'adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1812830', 'status': 'processed'}),
        ],
        outputs=["TRK-COU0005-8228"]
    ),

    # GOLD 4
    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="TASK_EXP_021",
        instruction="You are a manager and must update the catalog so variants '6509212169' and '9354168549' are priced at 142.10 and 149.90 and available True. Create a Two-Day shipment on order '#W4073673' for those items using a new tracking from courier '#COU0008' with seed 9101; the tracking ID will be 'TRK-COU0008-9101'. Record 'received' at '2025-03-05T08:00:00', schedule '2025-03-06T09:00:00', and add 'out_for_delivery' at '2025-03-06T10:15:00'. Reassign existing tracking '663395959263' to '#COU0005'. Upsert the new tracking's address to 1200 Market St, Suite 300, Dallas, TX 75202, USA. Post payment 55.55 via 'credit_card_3677959' (transaction 'TX-EXP-2001'), tag 'reconciled', and set status 'processed'. Confirm by reading the new tracking and both variants. Return [new tracking ID, transaction ID].",
        actions=[
            Action(name='set_variant_price', kwargs={'item_id': '6509212169', 'price': 142.10}),
            Action(name='set_variant_availability', kwargs={'item_id': '6509212169', 'available': True}),
            Action(name='set_variant_price', kwargs={'item_id': '9354168549', 'price': 149.90}),
            Action(name='set_variant_availability', kwargs={'item_id': '9354168549', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0008', 'seed': 9101}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W4073673', 'item_ids': ['6509212169','9354168549'], 'tracking_id': 'TRK-COU0008-9101', 'courier_id': '#COU0008', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0008-9101', 'event': 'received', 'timestamp': '2025-03-05T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0008-9101', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0008-9101', 'event': 'out_for_delivery', 'timestamp': '2025-03-06T10:15:00'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '663395959263', 'courier_id': '#COU0005'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0008-9101', 'address': {'address1': '1200 Market St', 'address2': 'Suite 300', 'city': 'Dallas', 'state': 'TX', 'zip': '75202', 'country': 'USA'}}),
            Action(name='add_order_payment', kwargs={'order_id': '#W4073673', 'amount': 55.55, 'payment_method_id': 'credit_card_3677959', 'transaction_id': 'TX-EXP-2001'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W4073673', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W4073673', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0008-9101'}),
            Action(name='get_item_variant', kwargs={'item_id': '6509212169'}),
            Action(name='get_item_variant', kwargs={'item_id': '9354168549'}),
        ],
        outputs=["TRK-COU0008-9101", "TX-EXP-2001"]
    ),

    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="TASK_EXP_022",
        instruction="You must allocate tracking via courier '#COU0006' (seed 9102) for order '#W1812830' items ['2768401027'] using 'Two-Day'; add 'received' at '2025-03-05T08:00:00', schedule '2025-03-06T09:00:00', and upsert the tracking address to 77 Maple Street, Suite 210, Chicago, IL 60616, USA. Fraud-mark the order risk 'low' with reason 'MANUAL_REVIEW_PASSED'. Issue a refund of 25.00 with refund_id 'TX-EXP-2002-R' reason 'CUSTOMER_REQUEST', tag 'adjusted', and set status 'processed'. Confirm by reading the tracking. Return [new tracking ID, refund transaction ID, risk level].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0006', 'seed': 9102}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W1812830', 'item_ids': ['2768401027'], 'tracking_id': 'TRK-COU0006-9102', 'courier_id': '#COU0006', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0006-9102', 'event': 'received', 'timestamp': '2025-03-05T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0006-9102', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0006-9102', 'address': {'address1': '77 Maple Street', 'address2': 'Suite 210', 'city': 'Chicago', 'state': 'IL', 'zip': '60616', 'country': 'USA'}}),
            Action(name='fraud_mark_order', kwargs={'order_id': '#W1812830', 'risk_level': 'low', 'reason_code': 'MANUAL_REVIEW_PASSED'}),
            Action(name='refund_order_payment', kwargs={'order_id': '#W1812830', 'amount': 25.00, 'refund_id': 'TX-EXP-2002-R', 'reason_code': 'CUSTOMER_REQUEST'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1812830', 'tag': 'adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1812830', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0006-9102'}),
        ],
        outputs=["TRK-COU0006-9102", "TX-EXP-2002-R", "low"]
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="TASK_EXP_023",
        instruction="You must update prices for '3229676465'→85.00 and '9314474252'→121.10 and set both available True. Allocate tracking via '#COU0009' (seed 9103) for order '#W9527030' items ['3229676465','9314474252'] with 'Two-Day'; add 'received' at '2025-03-05T08:00:00', schedule '2025-03-06T09:00:00', and upsert the tracking address to 667 Elm Street, Suite 624, Chicago, IL 60641, USA. Post a payment of 22.22 using 'paypal_7732922' with transaction 'TX-EXP-2003', tag 'reconciled', and set status 'processed'. Confirm by reading tracking and both variants. Return [new tracking ID, prices].",
        actions=[
            Action(name='set_variant_price', kwargs={'item_id': '3229676465', 'price': 85.00}),
            Action(name='set_variant_availability', kwargs={'item_id': '3229676465', 'available': True}),
            Action(name='set_variant_price', kwargs={'item_id': '9314474252', 'price': 121.10}),
            Action(name='set_variant_availability', kwargs={'item_id': '9314474252', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0009', 'seed': 9103}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9527030', 'item_ids': ['3229676465','9314474252'], 'tracking_id': 'TRK-COU0009-9103', 'courier_id': '#COU0009', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0009-9103', 'event': 'received', 'timestamp': '2025-03-05T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0009-9103', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0009-9103', 'address': {'address1': '667 Elm Street', 'address2': 'Suite 624', 'city': 'Chicago', 'state': 'IL', 'zip': '60641', 'country': 'USA'}}),
            Action(name='add_order_payment', kwargs={'order_id': '#W9527030', 'amount': 22.22, 'payment_method_id': 'paypal_7732922', 'transaction_id': 'TX-EXP-2003'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W9527030', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W9527030', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0009-9103'}),
            Action(name='get_item_variant', kwargs={'item_id': '3229676465'}),
            Action(name='get_item_variant', kwargs={'item_id': '9314474252'}),
        ],
        outputs=["TRK-COU0009-9103", "85.00", "121.10"]
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="TASK_EXP_024",
        instruction="You must place supply order '#SO9044' with supplier '#SUP0001' for product '9523456873' item '2768401027' quantity 6 unit cost 12.75 and mark it 'fulfilled'. Set the item's price to 49.50 and available True. Allocate tracking via '#COU0002' (seed 9104) for order '#W1812830' items ['2768401027'] using 'Two-Day'; add 'received' at '2025-03-05T08:00:00', schedule '2025-03-06T09:00:00', and upsert the tracking address to 498 Elm Avenue, Suite 953, San Jose, CA 95155, USA. Post payment 18.00 via 'gift_card_8541487' transaction 'TX-EXP-2004', tag 'reconciled', and set status 'processed'. Confirm by reading tracking and variant. Return [supply order ID, new tracking ID].",
        actions=[
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO9044', 'supplier_id': '#SUP0001', 'product_id': '9523456873', 'item_id': '2768401027', 'quantity': 6, 'unit_cost': 12.75}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO9044', 'status': 'fulfilled'}),
            Action(name='set_variant_price', kwargs={'item_id': '2768401027', 'price': 49.50}),
            Action(name='set_variant_availability', kwargs={'item_id': '2768401027', 'available': True}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0002', 'seed': 9104}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W1812830', 'item_ids': ['2768401027'], 'tracking_id': 'TRK-COU0002-9104', 'courier_id': '#COU0002', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-9104', 'event': 'received', 'timestamp': '2025-03-05T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0002-9104', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': 'TRK-COU0002-9104', 'address': {'address1': '498 Elm Avenue', 'address2': 'Suite 953', 'city': 'San Jose', 'state': 'CA', 'zip': '95155', 'country': 'USA'}}),
            Action(name='add_order_payment', kwargs={'order_id': '#W1812830', 'amount': 18.00, 'payment_method_id': 'gift_card_8541487', 'transaction_id': 'TX-EXP-2004'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1812830', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1812830', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0002-9104'}),
            Action(name='get_item_variant', kwargs={'item_id': '2768401027'}),
        ],
        outputs=["#SO9044", "TRK-COU0002-9104"]
    ),

    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="TASK_EXP_025",
        instruction="As a retail manager, you must update prices for '4410138384' to 215.55 and '8349118980' to 62.49 and set both available True. Reassign tracking '515122929210' to courier '#COU0001'. Create a Two-Day shipment on order '#W1305304' for item '4410138384' using a new tracking from '#COU0007' (seed 9105); record 'received' at '2025-03-05T08:00:00' and schedule at '2025-03-06T09:00:00'. Issue a 15.00 refund with refund_id 'TX-EXP-2005-R' for reason 'PRICE_ADJUSTMENT', tag the order 'adjusted', and set the order status to 'processed'. Confirm by reading the new tracking. Return [new tracking ID, refund transaction ID].",
        actions=[
            Action(name='set_variant_price', kwargs={'item_id': '4410138384', 'price': 215.55}),
            Action(name='set_variant_availability', kwargs={'item_id': '4410138384', 'available': True}),
            Action(name='set_variant_price', kwargs={'item_id': '8349118980', 'price': 62.49}),
            Action(name='set_variant_availability', kwargs={'item_id': '8349118980', 'available': True}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '515122929210', 'courier_id': '#COU0001'}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0007', 'seed': 9105}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W1305304', 'item_ids': ['4410138384'], 'tracking_id': 'TRK-COU0007-9105', 'courier_id': '#COU0007', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0007-9105', 'event': 'received', 'timestamp': '2025-03-05T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0007-9105', 'scheduled': '2025-03-06T09:00:00'}),
            Action(name='refund_order_payment', kwargs={'order_id': '#W1305304', 'amount': 15.00, 'refund_id': 'TX-EXP-2005-R', 'reason_code': 'PRICE_ADJUSTMENT'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1305304', 'tag': 'adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1305304', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0007-9105'}),
        ],
        outputs=["TRK-COU0007-9105", "TX-EXP-2005-R"]
    ),

    # ADDITIONAl
    Task(
        annotator="0",
        user_id="TASK_EXP_026",
        instruction="You need to handle a shipment and payment update for order '#W6304490'. First, create a new shipment for items ['6956751343', '4983901480'] using courier '#COU0001' with seed 5000 and delivery option 'Two-Day'. For this shipment, make sure its tracking history includes a 'received' event at 2025-03-01T08:00:00, an 'out_for_delivery' event at 2025-03-02T10:15:00, and that its delivery is scheduled for 2025-03-02T09:00:00. As part of your work, confirm the new tracking details after creation. Then, as the accounts agent, record a payment of 20.37 using payment method 'gift_card_0000000' with transaction ID 'TX-8000', add the tag 'reconciled', and mark the order as 'processed'. You will also retrieve the updated order details after these changes. Additionally, you need to reassign the existing tracking '357962501027' to courier '#COU0002', checking its current details and the target courier’s details before reassignment, and verifying the tracking details again afterward. Return the new tracking ID, the payment transaction ID, and the new courier ID you reassigned to.",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0001', 'seed': 5000}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W6304490', 'item_ids': ['6956751343', '4983901480'], 'tracking_id': 'TRK-COU0001-5000', 'courier_id': '#COU0001', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-5000', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0001-5000', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0001-5000', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0001-5000'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6304490'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W6304490', 'amount': 20.37, 'payment_method_id': 'gift_card_0000000', 'transaction_id': 'TX-8000'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6304490', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6304490', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6304490'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '357962501027'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0002'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '357962501027', 'courier_id': '#COU0002'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '357962501027'})
        ],
        outputs=['TRK-COU0001-5000', 'TX-8000', '#COU0002']
    ),
    Task(
        annotator="0",
        user_id="TASK_EXP_027",
        instruction="For order '#W6874763', you must set variant '6700049080' price to 475.75 and available False. Create a new shipment for item ['7528037711'] via '#COU0002' (seed 7109) 'Two-Day'; add 'received' (2025-03-01T08:00:00), schedule (2025-03-02T09:00:00), 'out_for_delivery' (2025-03-02T10:15:00). Confirm tracking and variant. Return [new price, tracking ID].",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '6700049080'}),
            Action(name='set_variant_price', kwargs={'item_id': '6700049080', 'price': 475.75}),
            Action(name='set_variant_availability', kwargs={'item_id': '6700049080', 'available': False}),
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0002', 'seed': 7109}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W6874763', 'item_ids': ['7528037711'], 'tracking_id': 'TRK-COU0002-7109', 'courier_id': '#COU0002', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-7109', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0002-7109', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-7109', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0002-7109'}),
            Action(name='get_item_variant', kwargs={'item_id': '6700049080'})
        ],
        outputs=["475.75", "TRK-COU0002-7109"]
    ),
    Task(
        annotator="0",
        user_id="TASK_EXP_028",
        instruction="As a retail manager, you must create a new shipment for order '#W6304490' using delivery option 'Two-Day' and a new tracking from courier '#COU0007' with seed 5006; the tracking ID will be 'TRK-COU0007-5006'. Link items ['6956751343','4983901480'], record 'received' at '2025-03-01T08:00:00', schedule '2025-03-02T09:00:00', and add 'out_for_delivery' at '2025-03-02T10:15:00'. Register a payment of 26.79 via 'gift_card_0000000' (transaction_id 'TX-8006'), tag 'reconciled', and set order status to 'processed'. Also reassign existing tracking '889070895653' to courier '#COU0001'. Return [new tracking ID, transaction ID, reassigned courier ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0007', 'seed': 5006}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W6304490', 'item_ids': ['6956751343', '4983901480'], 'tracking_id': 'TRK-COU0007-5006', 'courier_id': '#COU0007', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0007-5006', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0007-5006', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0007-5006', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W6304490', 'amount': 26.79, 'payment_method_id': 'gift_card_0000000', 'transaction_id': 'TX-8006'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6304490', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6304490', 'status': 'processed'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '889070895653', 'courier_id': '#COU0001'}),
        ],
        outputs=['TRK-COU0007-5006', 'TX-8006', '#COU0001']
    ),
    Task(
        annotator="0",
        user_id="TASK_EXP_029",
        instruction="You are a manager and must split order '#W4817420' by moving items ['6777246137','4900661478'] to a new Two-Day shipment under courier '#COU0002' (seed 5008). Ensure the shipment timeline shows a 'received' scan at '2025-03-01T08:00:00', a scheduled delivery at '2025-03-02T09:00:00', and an 'out_for_delivery' scan at '2025-03-02T10:15:00'. Settle the order with a 28.93 payment via 'gift_card_0000000' (transaction 'TX-8008'), apply the 'reconciled' tag, and mark it 'processed'. Also transfer the existing shipment '443521489581' to courier '#COU0003'. Return [new tracking ID, transaction ID, reassigned courier ID].",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0002', 'seed': 5008}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W4817420', 'item_ids': ['6777246137', '4900661478'], 'tracking_id': 'TRK-COU0002-5008', 'courier_id': '#COU0002', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-5008', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0002-5008', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0002-5008', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '443521489581', 'courier_id': '#COU0003'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W4817420', 'amount': 28.93, 'payment_method_id': 'gift_card_0000000', 'transaction_id': 'TX-8008'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W4817420', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W4817420', 'status': 'processed'}),
        ],
        outputs=['TRK-COU0002-5008', 'TX-8008', '#COU0003']
    ),

    Task(
        annotator="0",
        user_id="TASK_EXP_030",
        instruction="You must arrange a new shipment for order '#W2611340' containing item ['6469567736'] with courier '#COU0005' (seed 5004) using delivery option 'Two-Day'. The shipment should have a 'received' event at 2025-03-01T08:00:00, an 'out_for_delivery' event at 2025-03-02T10:15:00, and be scheduled for delivery on 2025-03-02T09:00:00. After setting up the shipment, you must confirm its tracking details. Then, as part of settlement, record a payment of 24.65 with payment method 'gift_card_0000000' and transaction ID 'TX-8004', tag the order as 'reconciled', and update its status to 'processed'. You must also reassign tracking '367478070474' to courier '#COU0006', confirming the tracking and courier details before the change, and retrieving the updated tracking afterward. Finally, verify the new shipment’s tracking again. Return the new tracking ID, the payment transaction ID, and the new courier ID.",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0005', 'seed': 5004}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W2611340', 'item_ids': ['6469567736'], 'tracking_id': 'TRK-COU0005-5004', 'courier_id': '#COU0005', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0005-5004', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0005-5004', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0005-5004', 'event': 'out_for_delivery', 'timestamp': '2025-03-02T10:15:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0005-5004'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W2611340', 'amount': 24.65, 'payment_method_id': 'gift_card_0000000', 'transaction_id': 'TX-8004'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W2611340', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W2611340', 'status': 'processed'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '367478070474'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0006'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '367478070474', 'courier_id': '#COU0006'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '367478070474'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0005-5004'})
        ],
        outputs=['TRK-COU0005-5004', 'TX-8004', '#COU0006']
    ),

    # MEDIUM
    # GOLD 1
    # complexity_edges: 11
    Task(
        annotator="0",
        user_id="TASK_MED_001",
        instruction="You have to update catalog item '2198125883' to set its price to 299.99 and set available True. Then tag order '#W9608525' as 'price_adjusted' and set status to 'processed'. Finally, fetch the updated item and order to confirm and return the new price.",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '2198125883'}),
            Action(name='set_variant_price', kwargs={'item_id': '2198125883', 'price': 299.99}),
            Action(name='set_variant_availability', kwargs={'item_id': '2198125883', 'available': True}),
            Action(name='add_order_tag', kwargs={'order_id': '#W9608525', 'tag': 'price_adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W9608525', 'status': 'processed'}),
            Action(name='get_item_variant', kwargs={'item_id': '2198125883'}),
            Action(name='get_order_details', kwargs={'order_id': '#W9608525'})
        ],
        outputs=["299.99"]
    ),

    # complexity_edges: 10
    Task(
        annotator="0",
        user_id="TASK_MED_002",
        instruction="You have to record a payment of 37.56 on order '#W1649831' using payment method 'gift_card_2519457' with transaction 'TX-MED-0001'. Then tag the order 'reconciled', set status 'processed', and retrieve the updated order. Return the transaction ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1649831'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W1649831', 'amount': 37.56, 'payment_method_id': 'gift_card_2519457', 'transaction_id': 'TX-MED-0001'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1649831', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1649831', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1649831'})
        ],
        outputs=["TX-MED-0001"]
    ),

    # complexity_edges: 9
    Task(
        annotator="0",
        user_id="TASK_MED_003",
        instruction="As a retail manager, you must ensure tracking '254796145302' is handled by courier '#COU0001', reflects the address 12 Birch Road, Suite 12, Austin, TX 78705, USA, and shows a 'return_initiated' event at '2025-03-06T12:00:00'. Provide the new courier ID.",
        actions=[
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '254796145302', 'courier_id': '#COU0001'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': '254796145302', 'address': {'address1': '12 Birch Road', 'address2': 'Suite 12', 'city': 'Austin', 'state': 'TX', 'zip': '78705', 'country': 'USA'}}),
            Action(name='append_tracking_event', kwargs={'tracking_id': '254796145302', 'event': 'return_initiated', 'timestamp': '2025-03-06T12:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '254796145302'})
        ],
        outputs=["#COU0001"]
    ),

    # complexity_edges: 12
    Task(
        annotator="0",
        user_id="TASK_MED_004",
        instruction="You have to place supply order '#SO8001' with supplier '#SUP0005' for product '2524789262' (item '2492465580'), quantity 12 at unit cost 15.25, then mark it 'fulfilled'. Verify supplier details before and after. Return the supply order ID.",
        actions=[
            Action(name='get_supplier_details', kwargs={'supplier_id': '#SUP0005'}),
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8001', 'supplier_id': '#SUP0005', 'product_id': '2524789262', 'item_id': '2492465580', 'quantity': 12, 'unit_cost': 15.25}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8001', 'status': 'fulfilled'}),
            Action(name='get_supplier_details', kwargs={'supplier_id': '#SUP0005'})
        ],
        outputs=["#SO8001"]
    ),

    # complexity_edges: 11
    Task(
        annotator="0",
        user_id="TASK_MED_005",
        instruction="You must allocate a tracking ID with courier '#COU0003' (seed 6001) and create a new shipment for order '#W9474165' containing items ['8649999816','6469567736']. Use delivery option 'Two-Day'. Add 'received' at '2025-03-01T08:00:00' and schedule delivery '2025-03-02T09:00:00'. Confirm by fetching the new tracking. Return the new tracking ID.",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0003', 'seed': 6001}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9474165', 'item_ids': ['8649999816', '6469567736'], 'tracking_id': 'TRK-COU0003-6001', 'courier_id': '#COU0003', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-6001', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0003-6001', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0003-6001'})
        ],
        outputs=["TRK-COU0003-6001"]
    ),

    # complexity_edges: 10
    Task(
        annotator="0",
        user_id="TASK_MED_006",
        instruction="You have to set the price of catalog item '5753502325' to 100.20 and set available True. Then tag order '#W6114312' as 'price_adjusted' and mark it 'processed'. Confirm by reading the item and order. Return the new price.",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'}),
            Action(name='set_variant_price', kwargs={'item_id': '5753502325', 'price': 100.20}),
            Action(name='set_variant_availability', kwargs={'item_id': '5753502325', 'available': True}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6114312', 'tag': 'price_adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6114312', 'status': 'processed'}),
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6114312'})
        ],
        outputs=["100.20"]
    ),

    # GOLD 2

    # complexity_edges: 11
    Task(
        annotator="0",
        user_id="TASK_MED_007",
        instruction="You have to update catalog variant '3735133539' to price 512.49 and set available True. Tag order '#W2091016' as 'price_adjusted' and set status 'processed'. Then fetch the variant and order to confirm and return the updated price.",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '3735133539'}),
            Action(name='set_variant_price', kwargs={'item_id': '3735133539', 'price': 512.49}),
            Action(name='set_variant_availability', kwargs={'item_id': '3735133539', 'available': True}),
            Action(name='add_order_tag', kwargs={'order_id': '#W2091016', 'tag': 'price_adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W2091016', 'status': 'processed'}),
            Action(name='get_item_variant', kwargs={'item_id': '3735133539'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2091016'})
        ],
        outputs=["512.49"]
    ),

    # complexity_edges: 10
    Task(
        annotator="0",
        user_id="TASK_MED_008",
        instruction="You must record a payment of 42.75 on order '#W5299644' using method 'paypal_3345717' with transaction 'TX-MED-1001'. Tag 'reconciled', set status 'processed', and retrieve the order. Return the transaction ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5299644'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W5299644', 'amount': 42.75, 'payment_method_id': 'paypal_3345717', 'transaction_id': 'TX-MED-1001'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W5299644', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W5299644', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5299644'})
        ],
        outputs=["TX-MED-1001"]
    ),

    # complexity_edges: 9
    Task(
        annotator="0",
        user_id="TASK_MED_009",
        instruction="You have to fraud-mark order '#W7538736' risk 'low' reason 'MANUAL_REVIEW_PASSED'. Reassign tracking '604805146457' to '#COU0003' after fetching details and confirm. Return [risk level, new courier ID].",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W7538736'}),
            Action(name='fraud_mark_order', kwargs={'order_id': '#W7538736', 'risk_level': 'low', 'reason_code': 'MANUAL_REVIEW_PASSED'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '604805146457'}),
            Action(name='get_courier_details', kwargs={'courier_id': '#COU0003'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '604805146457', 'courier_id': '#COU0003'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '604805146457'})
        ],
        outputs=["low", "#COU0003"]
    ),

    # complexity_edges: 10
    Task(
        annotator="0",
        user_id="TASK_MED_010",
        instruction="As a retail manager, you have to place supply order '#SO8101' with supplier '#SUP0001' for product '9523456873' item '2768401027' quantity 8 at unit cost 12.40, mark it 'fulfilled', verify supplier before and after, and return the supply order ID.",
        actions=[
            Action(name='get_supplier_details', kwargs={'supplier_id': '#SUP0001'}),
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO8101', 'supplier_id': '#SUP0001', 'product_id': '9523456873', 'item_id': '2768401027', 'quantity': 8, 'unit_cost': 12.40}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO8101', 'status': 'fulfilled'}),
            Action(name='get_supplier_details', kwargs={'supplier_id': '#SUP0001'})
        ],
        outputs=["#SO8101"]
    ),

    # complexity_edges: 11
    Task(
        annotator="0",
        user_id="TASK_MED_011",
        instruction="You must set variant '8349118980' price to 59.99 and available True. Tag order '#W1305304' 'price_adjusted' and mark 'processed'. Confirm by fetching variant and order. Return the new price.",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '8349118980'}),
            Action(name='set_variant_price', kwargs={'item_id': '8349118980', 'price': 59.99}),
            Action(name='set_variant_availability', kwargs={'item_id': '8349118980', 'available': True}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1305304', 'tag': 'price_adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1305304', 'status': 'processed'}),
            Action(name='get_item_variant', kwargs={'item_id': '8349118980'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1305304'})
        ],
        outputs=["59.99"]
    ),

    # GOLD 3
    # complexity_edges: 10
    Task(
        annotator="0",
        user_id="TASK_MED_012",
        instruction="You have to set the price of catalog variant '5753502325' to 100.20 and set available True. Then tag order '#W6114312' as 'price_adjusted' and mark it 'processed'. Confirm by reading the item and the order. Return the new price.",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'}),
            Action(name='set_variant_price', kwargs={'item_id': '5753502325', 'price': 100.20}),
            Action(name='set_variant_availability', kwargs={'item_id': '5753502325', 'available': True}),
            Action(name='add_order_tag', kwargs={'order_id': '#W6114312', 'tag': 'price_adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W6114312', 'status': 'processed'}),
            Action(name='get_item_variant', kwargs={'item_id': '5753502325'}),
            Action(name='get_order_details', kwargs={'order_id': '#W6114312'})
        ],
        outputs=["100.20"]
    ),

    # complexity_edges: 10
    Task(
        annotator="0",
        user_id="TASK_MED_013",
        instruction="You must record a payment of 42.75 on order '#W5299644' using method 'paypal_3345717' with transaction 'TX-MED-1001'. Tag the order 'reconciled', set status 'processed', and retrieve the updated order. Return the transaction ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W5299644'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W5299644', 'amount': 42.75, 'payment_method_id': 'paypal_3345717', 'transaction_id': 'TX-MED-1001'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W5299644', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W5299644', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W5299644'})
        ],
        outputs=["TX-MED-1001"]
    ),

    # complexity_edges: 10
    Task(
        annotator="0",
        user_id="TASK_MED_014",
        instruction="You are managing a return for tracking '254796145302'. Ensure it is handled by courier '#COU0001', update its address to 12 Birch Road, Suite 12, Austin, TX 78705, USA, and record a 'return_initiated' scan at 2025-03-06T12:00:00. Return the updated courier ID.",
        actions=[
            Action(name='get_tracking_info', kwargs={'tracking_id': '254796145302'}),
            Action(name='reassign_courier_for_tracking', kwargs={'tracking_id': '254796145302', 'courier_id': '#COU0001'}),
            Action(name='upsert_tracking_address', kwargs={'tracking_id': '254796145302', 'address': {'address1': '12 Birch Road', 'address2': 'Suite 12', 'city': 'Austin', 'state': 'TX', 'zip': '78705', 'country': 'USA'}}),
            Action(name='append_tracking_event', kwargs={'tracking_id': '254796145302', 'event': 'return_initiated', 'timestamp': '2025-03-06T12:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': '254796145302'})
        ],
        outputs=["#COU0001"]
    ),

    # complexity_edges: 10
    Task(
        annotator="0",
        user_id="TASK_MED_015",
        instruction="You have to place supply order '#SO9001' with supplier '#SUP0005' for product '2524789262' (item '2492465580') quantity 12 at unit cost 15.25, then mark it 'fulfilled'. Verify supplier details before and after. Return the supply order ID.",
        actions=[
            Action(name='get_supplier_details', kwargs={'supplier_id': '#SUP0005'}),
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO9001', 'supplier_id': '#SUP0005', 'product_id': '2524789262', 'item_id': '2492465580', 'quantity': 12, 'unit_cost': 15.25}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO9001', 'status': 'fulfilled'}),
            Action(name='get_supplier_details', kwargs={'supplier_id': '#SUP0005'})
        ],
        outputs=["#SO9001"]
    ),

    # complexity_edges: 11
    Task(
        annotator="0",
        user_id="TASK_MED_016",
        instruction="You must allocate a tracking ID with courier '#COU0003' (seed 6001) and create a new shipment for order '#W9474165' containing items ['8649999816','6469567736'] using delivery option 'Two-Day'. Add 'received' at '2025-03-01T08:00:00' and schedule delivery '2025-03-02T09:00:00'. Confirm by fetching the new tracking. Return the new tracking ID.",
        actions=[
            Action(name='allocate_tracking_id', kwargs={'courier_id': '#COU0003', 'seed': 6001}),
            Action(name='split_order_fulfillment', kwargs={'order_id': '#W9474165', 'item_ids': ['8649999816','6469567736'], 'tracking_id': 'TRK-COU0003-6001', 'courier_id': '#COU0003', 'delivery_options': 'Two-Day'}),
            Action(name='append_tracking_event', kwargs={'tracking_id': 'TRK-COU0003-6001', 'event': 'received', 'timestamp': '2025-03-01T08:00:00'}),
            Action(name='schedule_delivery', kwargs={'tracking_id': 'TRK-COU0003-6001', 'scheduled': '2025-03-02T09:00:00'}),
            Action(name='get_tracking_info', kwargs={'tracking_id': 'TRK-COU0003-6001'})
        ],
        outputs=["TRK-COU0003-6001"]
    ),

    # complexity_edges: 11
    Task(
        annotator="0",
        user_id="TASK_MED_017",
        instruction="You must update catalog variant '3735133539' to price 512.49 and set available True. Tag order '#W2091016' as 'price_adjusted' and set status 'processed'. Then fetch the variant and the order to confirm and return the updated price.",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '3735133539'}),
            Action(name='set_variant_price', kwargs={'item_id': '3735133539', 'price': 512.49}),
            Action(name='set_variant_availability', kwargs={'item_id': '3735133539', 'available': True}),
            Action(name='add_order_tag', kwargs={'order_id': '#W2091016', 'tag': 'price_adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W2091016', 'status': 'processed'}),
            Action(name='get_item_variant', kwargs={'item_id': '3735133539'}),
            Action(name='get_order_details', kwargs={'order_id': '#W2091016'})
        ],
        outputs=["512.49"]
    ),

    # GOLD 4
    # complexity_edges: 11
    Task(
        annotator="0",
        user_id="TASK_MED_018",
        instruction="You must set the price of catalog variant '6509212169' to 88.88 and set available True. Then tag order '#W4073673' as 'price_adjusted' and set status 'processed'. Confirm by reading the variant and the order, and return the updated price.",
        actions=[
            Action(name='get_item_variant', kwargs={'item_id': '6509212169'}),
            Action(name='set_variant_price', kwargs={'item_id': '6509212169', 'price': 88.88}),
            Action(name='set_variant_availability', kwargs={'item_id': '6509212169', 'available': True}),
            Action(name='add_order_tag', kwargs={'order_id': '#W4073673', 'tag': 'price_adjusted'}),
            Action(name='update_order_status', kwargs={'order_id': '#W4073673', 'status': 'processed'}),
            Action(name='get_item_variant', kwargs={'item_id': '6509212169'}),
            Action(name='get_order_details', kwargs={'order_id': '#W4073673'}),
        ],
        outputs=["88.88"]
    ),

    # complexity_edges: 10
    Task(
        annotator="0",
        user_id="TASK_MED_019",
        instruction="You must record a payment of 29.11 on order '#W1812830' using method 'paypal_2076152' with transaction 'TX-MED-2001'. Tag the order 'reconciled', set status 'processed', and fetch the updated order. Return the transaction ID.",
        actions=[
            Action(name='get_order_details', kwargs={'order_id': '#W1812830'}),
            Action(name='add_order_payment', kwargs={'order_id': '#W1812830', 'amount': 29.11, 'payment_method_id': 'paypal_2076152', 'transaction_id': 'TX-MED-2001'}),
            Action(name='add_order_tag', kwargs={'order_id': '#W1812830', 'tag': 'reconciled'}),
            Action(name='update_order_status', kwargs={'order_id': '#W1812830', 'status': 'processed'}),
            Action(name='get_order_details', kwargs={'order_id': '#W1812830'}),
        ],
        outputs=["TX-MED-2001"]
    ),

    # complexity_edges: 10
    Task(
        annotator="0",
        user_id="TASK_MED_020",
        instruction="You must place supply order '#SO9010' with supplier '#SUP0010' for product '3801771308' item '9494281769' quantity 11 at unit cost 12.60, then mark it 'fulfilled'. Verify the supplier details before and after. Return the supply order ID.",
        actions=[
            Action(name='get_supplier_details', kwargs={'supplier_id': '#SUP0010'}),
            Action(name='place_supply_order', kwargs={'supply_order_id': '#SO9010', 'supplier_id': '#SUP0010', 'product_id': '3801771308', 'item_id': '9494281769', 'quantity': 11, 'unit_cost': 12.60}),
            Action(name='update_supply_order_status', kwargs={'supply_order_id': '#SO9010', 'status': 'fulfilled'}),
            Action(name='get_supplier_details', kwargs={'supplier_id': '#SUP0010'}),
        ],
        outputs=["#SO9010"]
    ),
]
