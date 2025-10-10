from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="task_01",
        instruction="You are a pharmaceutical logistics specialist. Your client, 'Delta Pharma Inc.', located in Boston, has placed a 'Critical' priority order for 20 boxes of the 'Oncology Drug A' medication. Your objective is to ensure this order is fully fulfilled and dispatched. The source warehouse must have an 'FDA Registered' certification to handle this product, and the shipment must be sent via Air transport. After shipping, you must report the final tracking number generated for the order.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Oncology Drug A"}),
            Action(name="list_warehouses_by_capability", kwargs={"certification": "FDA Registered"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "PHRM-DRUG-S19"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Delta Pharma Inc.", "destination_city": "Boston", "priority_level": "Critical", "line_items": [{"sku": "PHRM-DRUG-S19", "quantity": 20}]}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-06", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_02",
        instruction="You are an inbound logistics coordinator. The sea shipment from 'Helsinki Chemicals Oy' originating in Helsinki is critically delayed. Your objective is to manage this incident comprehensively. First, update the shipment's status to 'Delayed' and add a note with the exact text 'HAZMAT_DELAY_IMMEDIATE_REVIEW'. Then, log a performance issue against the supplier using the issue code 'LATE_DELIVERY_CRITICAL'. Afterwards, assess the operational impact by checking the current inventory level of 'Industrial Solvent' at the 'Cleveland Chemical Storage' warehouse. Finally, you must report the phone number of the Cleveland warehouse manager so a call can be placed immediately.",
        actions=[
        Action(
            name="find_inbound_shipment",
            kwargs={
                "supplier_name": "Helsinki Chemicals Oy",
                "origin_city": "Helsinki"
            }
        ),
        Action(
            name="get_product_details",
            kwargs={
                "product_name": "Industrial Solvent"
            }
        ),
        Action(
            name="update_shipment_status",
            kwargs={
                "shipment_id": "SHIP-0013",
                "new_status": "Delayed",
                "notes": "HAZMAT_DELAY_IMMEDIATE_REVIEW"
            }
        ),
        Action(
            name="log_supplier_performance_issue",
            kwargs={
                "supplier_id": "SUP-1013",
                "issue_code": "LATE_DELIVERY_CRITICAL",
                "shipment_id": "SHIP-0013"
            }
        ),
        Action(
            name="get_inventory_by_sku",
            kwargs={
                "sku": "CHEM-SOLV-K11"
            }
        ),
        Action(
            name="get_warehouse_details",
            kwargs={
                "warehouse_name": "Cleveland Chemical Storage"
            }
        )
    ],
        outputs=["1-216-555-0113"]
    ),
    Task(
        annotator="0",
        user_id="task_03",
        instruction="You are an inventory planner preparing for a major sales promotion. Your primary goal is to increase the stock of the '8-bit Microcontroller' at the 'Chicago Parts Depot' to a target of 10,000 units. Before acting, you must first assess the total system-wide inventory for this product. Then, initiate the required transfer. The success of your task will be measured by the `quantity_inbound` at the destination warehouse being correctly updated with the transferred amount. Finally, report the new 'quantity_allocated' at the source warehouse as confirmation of the transfer.",
        actions=[
            Action(
                name="get_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1"
                }
            ),
            Action(
                name="initiate_warehouse_transfer",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "quantity": 2000,
                    "from_warehouse_id": "WH-01",
                    "to_warehouse_id": "WH-03"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                }
            )
        ],
        outputs=["4500"]
    ),
    Task(
        annotator="0",
        user_id="task_04",
        instruction="You are a network performance manager. Your task is to audit and act on underperforming partners. Identify and reassign all 'Shipped' orders from any ocean carrier that is underperforming according to company policy to the best-performing alternative. After reassigning all orders for a given carrier, update its status to 'Under Review'. Finally, confirm the new operational status of the carrier 'Maersk'.",
        actions=[
            Action(name="find_orders_by_carrier", kwargs={"carrier_name": "Maersk", "status": "Shipped"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Sea"}),
            Action(name="reassign_order_carrier", kwargs={"order_id": "ORD-0006", "new_carrier_scac": "KNLU"}),
            Action(name="update_carrier_status", kwargs={"carrier_name": "Maersk", "status": "Under Review"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "Maersk"})
        ],
        outputs=["Under Review"]
    ),
    Task(
        annotator="0",
        user_id="task_05",
        instruction="You are a quality control manager at the 'NYC Luxury Vault'. You have just inspected the recently received shipment from 'Paris Luxury Goods' that originated in Paris. You discovered that 5 'Leather Handbag' units are damaged and cannot be sold. Your objective is to fully process this incident. You must update the inventory to correctly reflect the damaged quantity, log a formal complaint against the supplier using the code 'DAMAGED_GOODS_RECEIVED', and immediately create a new, high-priority purchase order for the replacement of the 5 damaged units. Finally, you must report the purchase order number for this new replacement order.",
        actions=[
            Action(
                name="find_inbound_shipment",
                kwargs={
                    "supplier_name": "Paris Luxury Goods",
                    "origin_city": "Paris",
                    "status": "Received"
                }
            ),
            Action(
                name="get_product_details",
                kwargs={
                    "product_name": "Leather Handbag"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07"
                }
            ),
            Action(
                name="update_inventory_damage_status",
                kwargs={
                    "inventory_id": "INV-0005",
                    "damaged_quantity": 5
                }
            ),
            Action(
                name="log_supplier_performance_issue",
                kwargs={
                    "supplier_id": "SUP-1007",
                    "issue_code": "DAMAGED_GOODS_RECEIVED",
                    "shipment_id": "SHIP-0007"
                }
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1007",
                    "line_items": [
                        {
                            "sku": "APRL-BAG-E5",
                            "quantity": 5
                        }
                    ],
                    "priority": "High"
                }
            ),
            Action(
                name="get_purchase_order_details",
                kwargs={
                    "po_number": "PO-2025-0001"
                }
            )
        ],
        outputs=["PO-2025-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_06",
        instruction="You are a customer service lead. Your client, 'Alpha Electronics LLC', has requested to return 50 units of the '8-bit Microcontroller' from their original sales order 'SO-2024-0001' because they were incompatible with their new designs. Your objective is to process a full return and credit for these items. You must create a return authorization, arrange for the return shipment back to the original warehouse, update the original sales order to reflect the return, and issue a credit memo to the customer's account. Finally, you must report both the Return Authorization number and the Credit Memo ID.",
        actions=[
            Action(
                name="get_outbound_order_details_by_so",
                kwargs={"sales_order_number": "SO-2024-0001"}
            ),
            Action(
                name="get_product_details",
                kwargs={"product_name": "8-bit Microcontroller"}
            ),
            Action(
                name="create_return_authorization",
                kwargs={
                    "order_id": "ORD-0001",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}],
                    "reason": "Incompatible with new designs."
                }
            ),
            Action(
                name="create_inbound_return_shipment",
                kwargs={
                    "rma_id": "RMA-1001",
                    "from_customer_id": "CUST-2001",
                    "to_warehouse_id": "WH-01",
                    "carrier_scac": "UPSN"
                }
            ),
            Action(
                name="update_outbound_order_status",
                kwargs={
                    "order_id": "ORD-0001",
                    "new_status": "Partially Returned"
                }
            ),
            Action(
                name="issue_customer_credit_memo",
                kwargs={
                    "order_id": "ORD-0001",
                    "customer_id": "CUST-2001",
                    "returned_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}]
                }
            ),
            Action(
                name="get_return_authorization_details",
                kwargs={"rma_id": "RMA-1001"}
            ),
            Action(
                name="get_credit_memo_details",
                kwargs={"credit_memo_id": "CM-0001"}
            )
        ],
        outputs=["RMA-1001", "CM-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_07",
        instruction="You are a fulfillment specialist. 'Gamma Construction Ltd.' has placed a 'High' priority order for one 'Basic Robotic Starter Kit' to be sent to their site in Denver via 'Truck' transport. This is a virtual kit. Your objective is to fulfill this order by gathering the components. You must identify the components, verify each is available in the 'Chicago Parts Depot', and then create and ship a single outbound order containing all required components. Finally, you must calculate and report the total weight of the shipment.",
        actions=[
            Action(
                name="get_kit_components",
                kwargs={"kit_name": "Basic Robotic Starter Kit"}
            ),
            Action(
                name="get_product_details",
                kwargs={"product_name": "Articulated Robotic Arm"}
            ),
            Action(
                name="get_product_details",
                kwargs={"product_name": "Lithium-Ion Battery Pack"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "TECH-ROBO-N14", "warehouse_id": "WH-03"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "TECH-BATT-Q17", "warehouse_id": "WH-03"}
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "High",
                    "line_items": [
                        {"sku": "TECH-ROBO-N14", "quantity": 1},
                        {"sku": "TECH-BATT-Q17", "quantity": 2}
                    ]
                }
            ),
            Action(
                name="list_carriers_by_mode",
                kwargs={"mode": "Truck"}
            ),
            Action(
                name="ship_outbound_order",
                kwargs={
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "UPSN"
                }
            ),
            Action(
                name="get_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0017"
                }
            )
        ],
        outputs=["251.4"]
    ),
    Task(
        annotator="0",
        user_id="task_08",
        instruction="You are an order manager handling a very large order. Your top client, 'Alpha Electronics LLC', has placed a 'High' priority order for a total of 15,000 units of the '8-bit Microcontroller' for their main office in San Jose. All shipments for this order must be dispatched via 'Truck' transport. Your objective is to ensure this entire order is fulfilled, even if it requires shipping from multiple warehouses. You must create all necessary outbound orders based on stock availability and dispatch all shipments. Finally, report the tracking numbers for all the shipments created to fulfill this single request.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "ELEC-CHIP-A1"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC", "destination_city": "San Jose", "priority_level": "High",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 12500}]
                }
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC", "destination_city": "San Jose", "priority_level": "High",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 2500}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Truck"}),
            Action(
                name="ship_outbound_order",
                kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}
            ),
            Action(
                name="ship_outbound_order",
                kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}
            ),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0018"})
        ],
        outputs=["UPSN-0017", "UPSN-0018"]
    ),
    Task(
        annotator="0",
        user_id="task_09",
        instruction="You are a risk auditor. Your task is to conduct a risk assessment on our two main luxury product lines: the 'Leather Handbag', supplied by 'Paris Luxury Goods', and the 'Automatic Watch Movement', supplied by 'Zurich Watch Parts AG'. For each product, you must find its total inventory value, the insurance coverage limit of the carrier used for its last inbound shipment (from Paris for the Handbag, and from Zurich for the Watch Movement), and then calculate a risk exposure score (Total Value / Insurance Limit). Your final objective is to log an audit event that identifies the product with the HIGHER risk exposure score using the outcome code 'HIGHEST_RISK_IDENTIFIED'. Finally, you must report only the calculated risk score for the higher-risk product, formatted to five decimal places.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Leather Handbag"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "APRL-BAG-E5"}),
            Action(name="find_inbound_shipment", kwargs={"supplier_name": "Paris Luxury Goods", "origin_city": "Paris"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "FedEx"}),
            Action(name="get_product_details", kwargs={"product_name": "Automatic Watch Movement"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "LUX-WATCH-L12"}),
            Action(name="find_inbound_shipment", kwargs={"supplier_name": "Zurich Watch Parts AG", "origin_city": "Zurich"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "UPS"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "PRODUCT_RISK_AUDIT",
                    "subject_id": "APRL-BAG-E5",
                    "outcome_code": "HIGHEST_RISK_IDENTIFIED",
                    "outcome_details": {
                        "product_name": "Leather Handbag",
                        "risk_score": 0.00128
                    }
                }
            )
        ],
        outputs=["0.00128"]
    ),
    Task(
        annotator="0",
        user_id="task_10",
        instruction="You are a logistics auditor. Conduct a comprehensive post-delivery audit for sales order 'SO-2024-0001' shipped to 'Alpha Electronics LLC'. Ensure complete delivery compliance including inventory accuracy for the '8-bit Microcontroller' at 'Los Angeles Distribution Center', carrier performance validation for 'UPS', and proper audit documentation with code 'POST_DELIVERY_AUDIT_OK'. Report the carrier's on-time delivery percentage.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0001"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "UPS"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "POST_DELIVERY_AUDIT",
                    "subject_id": "ORD-0001",
                    "outcome_code": "POST_DELIVERY_AUDIT_OK",
                }
            )
        ],
        outputs=["98.2"]
    ),
    Task(
        annotator="0",
        user_id="task_11",
        instruction="You are a risk analyst. Assess insurance coverage adequacy for high-value international shipments on Purchase Order 'PO-2024-0011' and outbound order 'ORD-0007'. Determine coverage sufficiency by comparing shipment values against carrier insurance limits, document findings through audit event 'INSURANCE_AUDIT' with outcome 'AUDIT_COMPLETE', and provide coverage status for each shipment. Report the insurance coverage limit for carrier 'COSCO'.",
        actions=[
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2024-0011"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "MSC Mediterranean Shipping Company"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0007"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "COSCO"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "INSURANCE_AUDIT",
                    "subject_id": "SHIP-0011;ORD-0007",
                    "outcome_code": "AUDIT_COMPLETE",
                    "outcome_details": {
                        "SHIP-0011": {"value": 1200000, "insurance_limit": 65000000, "status": "COVERED"},
                        "ORD-0007": {"value": 300000, "insurance_limit": 55000000, "status": "COVERED"}
                    },
                }
            )
        ],
        outputs=["55000000"]
    ),
    Task(
        annotator="0",
        user_id="task_12",
        instruction="You are a returns manager. The client 'Alpha Electronics LLC' needs to return 50 units of the '8-bit Microcontroller' from their sales order 'SO-2024-0001' due to a defect. Use the reason code 'DEFECT_REPORTED_BY_CUSTOMER' for the return authorization. Your objective is to process the full return for these items and immediately create and dispatch an identical, 'High' priority replacement order for them. The order's status must be updated to 'RETURN_PROCESSING'. Finally, report the tracking number for the NEW replacement shipment.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0001"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(
                name="create_return_authorization",
                kwargs={
                    "order_id": "ORD-0001",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}],
                    "reason": "DEFECT_REPORTED_BY_CUSTOMER"
                }
            ),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0001", "new_status": "RETURN_PROCESSING"}),
            Action(
                name="issue_customer_credit_memo",
                kwargs={
                    "order_id": "ORD-0001", "customer_id": "CUST-2001",
                    "returned_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}]
                }
            ),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0001", "damaged_quantity": 50}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC", "destination_city": "San Jose", "priority_level": "High",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}]
                }
            ),
            Action(
                name="list_carriers_by_mode",
                kwargs={"mode": "Parcel"}
            ),
            Action(
                name="ship_outbound_order",
                kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}
            ),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_13",
        instruction="You are a fulfillment planner for a major retailer. Your client, 'Beta Retail GmbH' in Hamburg, has placed a 'High' priority order for 700 'Ceramic Brake Pad Sets' and 20 'Teak Wood Dining Chairs'. All shipments must use 'Air' transport. Your objective is to fulfill this entire order, creating separate shipments for items sourced from different warehouses. You must create all necessary outbound orders and dispatch all shipments according to policy. Finally, you must report the tracking numbers for both new shipments, joined by a semicolon.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Brake Pad Set"}),
            Action(name="get_product_details", kwargs={"product_name": "Teak Wood Dining Chair"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "AUTO-PAD-B2"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "FURN-CHAIR-M13"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Beta Retail GmbH", "destination_city": "Hamburg", "priority_level": "High",
                    "line_items": [{"sku": "AUTO-PAD-B2", "quantity": 700}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Beta Retail GmbH", "destination_city": "Hamburg", "priority_level": "High",
                    "line_items": [{"sku": "FURN-CHAIR-M13", "quantity": 20}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-14", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0018"})
        ],
        outputs=["UPSN-0017;UPSN-0018"]
    ),
    Task(
        annotator="0",
        user_id="task_14",
        instruction="You are a reverse logistics specialist. You are handling the return of 15 'Smartphone Model X' units from 'Beta Retail GmbH' on their order 'SO-2024-0002'. First, create the Return Authorization using the reason code 'CUSTOMER_RETURN'. After creating the return shipment, you are notified that it is being held by customs for inspection. Your objective is to update the shipment's status to reflect this hold, using the exact status 'CUSTOMS_HOLD' and the exact note code 'RETURN_CUSTOMS_HOLD'. You must then log the event in the audit trail with the audit event 'RETURN_SHIPMENT_EXCEPTION' and outcome code 'STATUS_CUSTOMS_HOLD'. Finally, retrieve the primary contact email for the carrier ('DHL Express') and report it.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0002"}),
            Action(name="get_product_details", kwargs={"product_name": "Smartphone Model X"}),
            Action(
                name="create_return_authorization",
                kwargs={
                    "order_id": "ORD-0002",
                    "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 15}],
                    "reason": "CUSTOMER_RETURN"
                }
            ),
            Action(
                name="create_inbound_return_shipment",
                kwargs={"rma_id": "RMA-1001", "from_customer_id": "CUST-2002", "to_warehouse_id": "WH-02", "carrier_scac": "DHLG"}
            ),
            Action(
                name="update_shipment_status",
                kwargs={"shipment_id": "SHIP-0031", "new_status": "CUSTOMS_HOLD", "notes": "RETURN_CUSTOMS_HOLD"}
            ),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "RETURN_SHIPMENT_EXCEPTION", "subject_id": "RMA-1001", "outcome_code": "STATUS_CUSTOMS_HOLD"}
            ),
            Action(name="get_carrier_details", kwargs={"carrier_name": "DHL Express"})
        ],
        outputs=["info-us@dhl.com"]
    ),
    Task(
        annotator="0",
        user_id="task_15",
        instruction="You are a proactive risk manager. The outbound order 'ORD-0006' for 'Zeta Tech Solutions' is currently marked as 'Shipped' and assigned to the ocean carrier 'Maersk'. Your objective is to check if 'Maersk' meets performance standards. If they do not, reassign the shipment to the best-performing alternative ocean carrier. After ensuring the order is assigned to a compliant carrier, log an audit event using the event code 'PROACTIVE_RISK_MANAGEMENT' and the outcome code 'PROACTIVE_CARRIER_CHANGE'. Finally, report the SCAC of the carrier now assigned to this order.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0006"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "Maersk"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Sea"}),
            Action(
                name="reassign_order_carrier",
                kwargs={"order_id": "ORD-0006", "new_carrier_scac": "KNLU"}
            ),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "PROACTIVE_RISK_MANAGEMENT",
                    "subject_id": "ORD-0006",
                    "outcome_code": "PROACTIVE_CARRIER_CHANGE",
                    "outcome_details": {"old_carrier": "MAEU", "new_carrier": "KNLU"}
                }
            ),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0006"})
        ],
        outputs=["KNLU"]
    ),
    Task(
        annotator="0",
        user_id="task_16",
        instruction="You are a risk manager conducting comprehensive compliance and risk assessment for the high-value international shipment on Purchase Order 'PO-2024-0011' from South Africa. Ensure full regulatory compliance for the 'Diamond Core Drill Bit' shipment, validate warehouse capability alignment at 'Denver Heavy Equipment Yard' for heavy equipment handling, confirm adequate insurance coverage by 'MSC Mediterranean Shipping Company', and establish audit trail with 'INTERNATIONAL_SHIPMENT_AUDIT' event and 'AUDIT_PASS' outcome. Report the carrier's insurance policy number.",
        actions=[
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2024-0011"}),
            Action(name="get_product_details", kwargs={"product_name": "Diamond Core Drill Bit"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Denver Heavy Equipment Yard"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "MSC Mediterranean Shipping Company"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "INTERNATIONAL_SHIPMENT_AUDIT",
                    "subject_id": "SHIP-0011",
                    "outcome_code": "AUDIT_PASS",
                }
            )
        ],
        outputs=["POL-MSCU-2024"]
    ),
    Task(
        annotator="0",
        user_id="task_17",
        instruction="You are an inventory specialist. A 'High' priority order from 'Alpha Electronics LLC' for 15,000 '8-bit Microcontrollers' has been received for shipment to San Jose. Your objective is to fulfill this order completely by shipping from multiple warehouses according to policy. The final state must show: 1. An outbound order for the available stock at the primary warehouse (WH-01) is created and shipped. 2. A separate order for the remaining quantity is created and shipped from the warehouse with the next-highest stock (WH-03). 3. Both shipments must use the best 'Parcel' carrier. Finally, report both tracking numbers.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "ELEC-CHIP-A1"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "High",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 12500}]
                }
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "High",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 2500}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Parcel"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0018"})
        ],
        outputs=["UPSN-0017", "UPSN-0018"]
    ),
    Task(
        annotator="0",
        user_id="task_18",
        instruction="You are a senior customer service agent. Resolve the critical fulfillment error for 'Alpha Electronics LLC' order 'SO-2024-0001' where 300 'Automotive Windshields' were incorrectly shipped instead of 300 '8-bit Microcontrollers'. Achieve complete error resolution through proper return processing with reason code 'INCORRECT_ITEM_SHIPPED' and immediate critical priority replacement fulfillment. The order's status must be updated to 'ITEM_RETURNED_INCORRECTLY'. Report the tracking number for the replacement shipment.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0001"}),
            Action(name="get_product_details", kwargs={"product_name": "Automotive Windshield"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(
                name="create_return_authorization",
                kwargs={
                    "order_id": "ORD-0001",
                    "line_items": [{"sku": "AUTO-GLAS-U21", "quantity": 300}],
                    "reason": "INCORRECT_ITEM_SHIPPED"
                }
            ),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0001", "new_status": "ITEM_RETURNED_INCORRECTLY"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0001", "customer_id": "CUST-2001", "returned_items": [{"sku": "AUTO-GLAS-U21", "quantity": 300}]}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC", "destination_city": "San Jose", "priority_level": "Critical",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 300}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_19",
        instruction="You are an international customer service lead. Your client, 'Beta Retail GmbH' in Hamburg, Germany, is returning 20 units of 'Smartphone Model X' from their order 'SO-2024-0002' due to a minor cosmetic defect. Your objective is to process this international return and immediately dispatch an identical replacement order with 'High' priority via Air transport. You must create the return authorization, arrange the return shipment via the designated international returns carrier, issue the customer a credit memo, and then create and ship the new replacement order. Finally, report the tracking number for the NEW replacement shipment.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0002"}),
            Action(name="get_product_details", kwargs={"product_name": "Smartphone Model X"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0002", "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 20}], "reason": "COSMETIC_DEFECT"}),
            Action(name="create_inbound_return_shipment", kwargs={"rma_id": "RMA-1001", "from_customer_id": "CUST-2002", "to_warehouse_id": "WH-02", "carrier_scac": "DHLG"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0002", "new_status": "Processing Return"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0002", "customer_id": "CUST-2002", "returned_items": [{"sku": "ELEC-SMART-W23", "quantity": 20}]}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Beta Retail GmbH", "destination_city": "Hamburg", "priority_level": "High", "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 20}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-02", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_20",
        instruction="You are a compliance auditor. Your objective is to conduct a full HAZMAT compliance audit for the inbound shipment under Purchase Order 'PO-2024-0013' from Helsinki, which contains 'Industrial Solvent'. You must perform and verify the following three checks: 1) The product's HAZMAT class is '3'. 2) The destination warehouse, 'Cleveland Chemical Storage', is certified for Class 3 materials. 3) The carrier's ('Hapag-Lloyd') insurance limit is greater than the shipment's total value. After verification, log an audit event with event type 'HAZMAT_COMPLIANCE_AUDIT' and outcome code 'AUDIT_PASS'. Finally, report the HAZMAT UN Number for the product.",
        actions=[
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2024-0013"}),
            Action(name="get_product_details", kwargs={"product_name": "Industrial Solvent"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Cleveland Chemical Storage"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "Hapag-Lloyd"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "HAZMAT_COMPLIANCE_AUDIT",
                    "subject_id": "SHIP-0013",
                    "outcome_code": "AUDIT_PASS",
                    "outcome_details": {"product_check": "PASS", "warehouse_check": "PASS", "insurance_check": "PASS"}
                }
            )
        ],
        outputs=["UN1993"]
    ),
    Task(
        annotator="0",
        user_id="task_21",
        instruction="You are a finance controller closing the books on sales order 'SO-2024-0003'. You have confirmed this order for 'Gamma Construction Ltd.' contained two line items: 100 'Ceramic Floor Tile' and 200 'Industrial Paper Roll'. Your objective is to perform a full financial reconciliation of this order. You must calculate the Total Revenue (based on product unit prices), the Total Cost (based on inventory unit costs), and the final Gross Profit Margin percentage for the entire order. After calculating, log a 'FINANCIAL_RECONCILIATION' audit event with the detailed results. Finally, report the calculated Gross Profit Margin as a percentage, rounded to two decimal places.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(name="get_product_details", kwargs={"product_name": "Industrial Paper Roll"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "BLDG-TILE-J10"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "MANU-PAPR-F6"}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="get_inventory_details", kwargs={"sku": "MANU-PAPR-F6", "warehouse_id": "WH-08"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "FINANCIAL_RECONCILIATION", "subject_id": "ORD-0003", "outcome_code": "RECONCILED_OK",
                    "outcome_details": {"total_revenue": 80600, "total_cost": 50350, "gross_profit_margin_pct": 37.53}
                }
            )
        ],
        outputs=["37.53"]
    ),
    Task(
        annotator="0",
        user_id="task_22",
        instruction="You are a decommissioning manager. The 'NYC Luxury Vault' is scheduled to be shut down. Your objective is to evacuate all available inventory from this location to our primary 'Los Angeles Distribution Center'. Specifically, you must create and initiate warehouse transfers for the entire available stock of 'Leather Handbag' and 'Automatic Watch Movement'. After initiating all transfers, log a single audit event with the event type 'WAREHOUSE_EVACUATION' and outcome code 'EVACUATION_COMPLETE', detailing the SKUs and quantities transferred. Finally, report the total number of individual units transferred.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Leather Handbag"}),
            Action(name="get_product_details", kwargs={"product_name": "Automatic Watch Movement"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "NYC Luxury Vault"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Los Angeles Distribution Center"}),
            Action(name="get_inventory_details", kwargs={"sku": "APRL-BAG-E5", "warehouse_id": "WH-07"}),
            Action(name="get_inventory_details", kwargs={"sku": "LUX-WATCH-L12", "warehouse_id": "WH-07"}),
            Action(name="initiate_warehouse_transfer", kwargs={"sku": "APRL-BAG-E5", "quantity": 120, "from_warehouse_id": "WH-07", "to_warehouse_id": "WH-01"}),
            Action(name="initiate_warehouse_transfer", kwargs={"sku": "LUX-WATCH-L12", "quantity": 450, "from_warehouse_id": "WH-07", "to_warehouse_id": "WH-01"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "WAREHOUSE_EVACUATION",
                    "subject_id": "WH-07",
                    "outcome_code": "EVACUATION_COMPLETE",
                    "outcome_details": { "transferred_items": [{"sku": "APRL-BAG-E5", "quantity": 120}, {"sku": "LUX-WATCH-L12", "quantity": 450}]}
                }
            )
        ],
        outputs=["570"]
    ),
    Task(
        annotator="0",
        user_id="task_23",
        instruction="You are an exceptions handler. The 'High' priority order 'ORD-0002' for 'Beta Retail GmbH' has missed its promised ship date. To fix this, your objective is to cancel the original shipment using the status 'Cancelled - Missed Deadline', log a performance issue against the carrier using the event code 'CARRIER_PERFORMANCE_ISSUE' and outcome code 'MISSED_PROMISED_DATE', and immediately create and dispatch a new replacement order for the same items ('Smartphone Model X', quantity 20). The replacement must be sent as 'Critical' priority. Finally, report the tracking number for the new, expedited shipment.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0002"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0002", "new_status": "Cancelled - Missed Deadline"}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "CARRIER_PERFORMANCE_ISSUE", "subject_id": "DHLG", "outcome_code": "MISSED_PROMISED_DATE", "outcome_details": {"order_id": "ORD-0002"}}
            ),
            Action(name="get_product_details", kwargs={"product_name": "Smartphone Model X"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Beta Retail GmbH", "destination_city": "Hamburg", "priority_level": "Critical",
                    "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 20}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-02", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_24",
        instruction="You are a senior auditor conducting a compliance check on the 'Atlanta Cold Chain Center'. Your objective is to perform a full audit on all pharmaceutical products stored there: the 'Influenza Vaccine' and the 'Oncology Drug A'. For each product, you must verify three points: 1) Its stock status is 'In Stock'. 2) Its expiration date has not passed the current date. 3) Its temperature and general handling storage requirements are met by the warehouse's special capabilities. After auditing both products, log a single, consolidated audit event with the event type 'PHARMA_AUDIT' and outcome code 'AUDIT_COMPLETE', detailing the pass/fail status of each check for both SKUs. Finally, report the total number of SKUs that passed all three checks.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Influenza Vaccine"}),
            Action(name="get_product_details", kwargs={"product_name": "Oncology Drug A"}),
            Action(name="get_inventory_details", kwargs={"sku": "PHRM-VACC-D4", "warehouse_id": "WH-06"}),
            Action(name="get_inventory_details", kwargs={"sku": "PHRM-DRUG-S19", "warehouse_id": "WH-06"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Atlanta Cold Chain Center"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "PHARMA_AUDIT",
                    "subject_id": "WH-06",
                    "outcome_code": "AUDIT_COMPLETE",
                    "outcome_details": {
                        "PHRM-VACC-D4": {"stock_status_check": "PASS", "expiration_check": "PASS", "storage_check": "PASS"},
                        "PHRM-DRUG-S19": {"stock_status_check": "PASS", "expiration_check": "PASS", "storage_check": "PASS"}
                    }
                }
            )
        ],
        outputs=["2"]
    ),
    Task(
        annotator="0",
        user_id="task_25",
        instruction="You are a HAZMAT logistics specialist. 'Iota Automotive SAS' in Lyon is returning 10 'Lithium-Ion Battery Packs' from their order 'SO-2024-0009' due to damage in transit. Your objective is to process this return and immediately dispatch a 'Critical' priority replacement. You must verify that the designated international return carrier ('DHL Express') is certified for this product's HAZMAT class. After processing the full return (including credit memo), create and ship the replacement order, ensuring the new carrier also supports the HAZMAT class. Log the full transaction. Finally, report the tracking number for the NEW replacement shipment.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0009"}),
            Action(name="get_product_details", kwargs={"product_name": "Lithium-Ion Battery Pack"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "DHL Express"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0009", "line_items": [{"sku": "TECH-BATT-Q17", "quantity": 10}], "reason": "DAMAGED_IN_TRANSIT"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0009", "customer_id": "CUST-2009", "returned_items": [{"sku": "TECH-BATT-Q17", "quantity": 10}]}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-BATT-Q17", "warehouse_id": "WH-03"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0017", "damaged_quantity": 10}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Iota Automotive SAS", "destination_city": "Lyon", "priority_level": "Critical", "line_items": [{"sku": "TECH-BATT-Q17", "quantity": 10}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "UPS"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "TECH-BATT-Q17"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="log_audit_trail", kwargs={"audit_event": "HAZMAT_RETURN_REPLACE", "subject_id": "ORD-0009", "outcome_code": "SUCCESS", "outcome_details": {"replacement_order_id": "ORD-0017"}})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_26",
        instruction="You are a data integrity auditor. You must perform a consistency check on orders 'ORD-0001' and 'ORD-0002'. For each order, you must retrieve its details and the details of the carrier that handled it. Verify that the 'carrier_name' listed on each order record exactly matches the 'carrier_name' in the official carrier master record. After checking both orders, log a single audit event with the code 'ORDER_DATA_CONSISTENCY_CHECK', detailing your findings for each order. Finally, report the SCAC code for the carrier that handled order 'ORD-0002'.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0001"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "UPS"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0002"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "DHL Express"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "ORDER_DATA_CONSISTENCY_CHECK", "subject_id": "ORD-0001;ORD-0002", "outcome_code": "ALL_RECORDS_CONSISTENT",
                    "outcome_details": {
                        "ORD-0001": {"status": "MATCH"},
                        "ORD-0002": {"status": "MATCH"}
                    }
                }
            )
        ],
        outputs=["DHLG"]
    ),
    Task(
        annotator="0",
        user_id="task_27",
        instruction="You are a logistics coordinator. Optimize shipping efficiency by consolidating two Denver-bound orders: existing order 'ORD-0003' for 'Gamma Construction Ltd.' and a new high-priority order for 'Denver Heavy Equipment Yard' requesting 5 'Diamond Core Drill Bits'. Achieve cost-effective consolidated shipment with appropriate truck carrier selection based on insurance coverage for total combined value, and establish audit trail with 'CONSOLIDATED_SHIPMENT_PLANNED' event. Report the selected carrier's SCAC code.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Diamond Core Drill Bit"}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Denver Heavy Equipment Yard", "destination_city": "Denver", "priority_level": "High", "line_items": [{"sku": "HEVY-DRIL-I9", "quantity": 5}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Truck"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "CONSOLIDATED_SHIPMENT_PLANNED", "subject_id": "ORD-0003;ORD-0017", "outcome_code": "CARRIER_SELECTED",
                    "outcome_details": {"chosen_carrier_scac": "UPSN", "total_value": 99500}
                }
            )
        ],
        outputs=["UPSN"]
    ),
    Task(
        annotator="0",
        user_id="task_28",
        instruction="You are an auditor verifying the returns process. Your objective is to first process a complete return for 50 '8-bit Microcontroller' units from sales order 'SO-2024-0001' for 'Alpha Electronics LLC', using the specific reason code 'AUDIT_TEST_CASE'. Immediately after, you must audit your work by retrieving the newly created RMA and Credit Memo records to verify their details. After confirming, log a successful audit using the event type 'RETURN_PROCESS_AUDIT' and outcome code 'VERIFIED_OK'. Finally, report the created RMA ID.",    actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0001"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0001", "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}], "reason": "AUDIT_TEST_CASE"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0001", "customer_id": "CUST-2001", "returned_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}]}),
            Action(name="get_return_authorization_details", kwargs={"rma_id": "RMA-1001"}),
            Action(name="get_credit_memo_details", kwargs={"credit_memo_id": "CM-0001"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "RETURN_PROCESS_AUDIT", "subject_id": "RMA-1001", "outcome_code": "VERIFIED_OK"
                }
            )
        ],
        outputs=["RMA-1001"]
    ),
    Task(
        annotator="0",
        user_id="task_29",
        instruction="You are an outbound planner optimizing shipments for 'Epsilon Fashion Co.'. You need to handle their pending order 'ORD-0005' shipping from the 'Detroit Apparel Hub'. In addition, you must create and dispatch a new 'High' priority order for the same customer to Toronto for 100 'Organic Cotton T-Shirts' via 'Truck' transport. After shipping both orders, log an audit event with the exact event type 'CONSOLIDATED_CUSTOMER_FULFILLMENT' and outcome code 'BOTH_ORDERS_SHIPPED' confirming the fulfillment. Finally, report the tracking numbers for both shipments, joined by a semicolon.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0005"}),
            Action(name="get_product_details", kwargs={"product_name": "Organic Cotton T-Shirt"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "priority_level": "High",
                    "line_items": [{"sku": "APRL-TSHT-O15", "quantity": 100}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Truck"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0005", "warehouse_id": "WH-04", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-04", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "CONSOLIDATED_CUSTOMER_FULFILLMENT",
                    "subject_id": "ORD-0005;ORD-0017",
                    "outcome_code": "BOTH_ORDERS_SHIPPED"
                }
            ),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0005"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0005;UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_30",
        instruction="You are a compliance manager. Rectify the compliance breach where Purchase Order 'PO-2024-0016' containing 'Articulated Robotic Arm' was incorrectly received at 'Chicago Parts Depot' instead of the required high-security facility. Achieve regulatory compliance by relocating all 20 units to the appropriate secure warehouse, updating shipment status to 'Received' with note code 'REDIRECTED_TO_SECURE_WAREHOUSE', and documenting corrective action. Report the correct secure facility's warehouse ID.",
        actions=[
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2024-0016"}),
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="list_warehouses_by_capability", kwargs={"certification": "UL Certified Vault"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-ROBO-N14", "warehouse_id": "WH-03"}),
            Action(name="initiate_warehouse_transfer", kwargs={"sku": "TECH-ROBO-N14", "quantity": 20, "from_warehouse_id": "WH-03", "to_warehouse_id": "WH-07"}),
            Action(
                name="update_shipment_status",
                kwargs={"shipment_id": "SHIP-0016", "new_status": "Received", "notes": "REDIRECTED_TO_SECURE_WAREHOUSE"}
            ),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "COMPLIANCE_CORRECTION", "subject_id": "SHIP-0016", "outcome_code": "INVENTORY_RELOCATED_TO_SECURE",
                    "outcome_details": {"moved_sku": "TECH-ROBO-N14", "new_warehouse": "WH-07"}
                }
            )
        ],
        outputs=["WH-07"]
    ),
    Task(
        annotator="0",
        user_id="task_31",
        instruction="You are a finance manager. Determine the complete financial impact of processing a return for 20 'Smartphone Model X' units from 'Beta Retail GmbH' on sales order 'SO-2024-0002'. Calculate the Net Financial Impact in USD (total credited value minus original shipping cost and inventory cost) using 1 EUR = 1.08 USD exchange rate, process the return with reason code 'FINANCIAL_AUDIT_RETURN', and document findings through 'RETURN_FINANCIAL_RECONCILIATION' audit event. Report the calculated Net Financial Impact.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0002"}),
            Action(name="get_product_details", kwargs={"product_name": "Smartphone Model X"}),
            Action(
                name="create_return_authorization",
                kwargs={"order_id": "ORD-0002", "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 20}], "reason": "FINANCIAL_AUDIT_RETURN"}
            ),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0002", "customer_id": "CUST-2002", "returned_items": [{"sku": "ELEC-SMART-W23", "quantity": 20}]}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-SMART-W23", "warehouse_id": "WH-02"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "RETURN_FINANCIAL_RECONCILIATION", "subject_id": "RMA-1001", "outcome_code": "RECONCILED_OK",
                    "outcome_details": {"credited_value_usd": 19980.00, "shipping_cost_usd": 3456.00, "inventory_cost_usd": 13000.00, "net_financial_impact_usd": 3524.00}
                }
            )
        ],
        outputs=["3524.00"]
    ),
    Task(
        annotator="0",
        user_id="task_32",
        instruction="You are a data integrity analyst. You must perform a consistency check on outbound orders 'ORD-0001' and 'ORD-0002'. For each order, you must retrieve its full details and the full details of the carrier that handled it. Verify that the 'carrier_name' listed on each order record exactly matches the 'carrier_name' in the official carrier master record. After checking both orders, log a single audit event with the code 'ORDER_DATA_CONSISTENCY_CHECK', detailing the pass/fail consistency status for each order. Finally, report the SCAC code for the carrier that handled order 'ORD-0002'.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0001"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "UPS"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0002"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "DHL Express"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "ORDER_DATA_CONSISTENCY_CHECK",
                    "subject_id": "ORD-0001;ORD-0002",
                    "outcome_code": "ALL_RECORDS_CONSISTENT",
                    "outcome_details": {
                        "ORD-0001": {"status": "MATCH"},
                        "ORD-0002": {"status": "MATCH"}
                    }
                }
            )
        ],
        outputs=["DHLG"]
    ),
    Task(
        annotator="0",
        user_id="task_33",
        instruction="You are a senior auditor testing the fulfillment system. Your objective is to first execute the fulfillment of a 15,000 unit order of '8-bit Microcontrollers' for 'Alpha Electronics LLC' to San Jose, which will require shipping from multiple warehouses under 'High' priority using 'Truck' transport. Your second objective is to immediately audit the transactions. You must verify that the correct warehouses and carrier were used according to policy. After verifying, log a consolidated audit event with the event code 'MULTI_WAREHOUSE_AUDIT' and the outcome code 'AUDIT_PASS'. Finally, report the name of the carrier used.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "ELEC-CHIP-A1"}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Alpha Electronics LLC", "destination_city": "San Jose", "priority_level": "High", "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 12500}]}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Alpha Electronics LLC", "destination_city": "San Jose", "priority_level": "High", "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 2500}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Truck"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0018"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "UPS"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "MULTI_WAREHOUSE_AUDIT", "subject_id": "ORD-0017;ORD-0018", "outcome_code": "AUDIT_PASS"
                }
            )
        ],
        outputs=["UPS"]
    ),
    Task(
        annotator="0",
        user_id="task_34",
        instruction="You are a compliance specialist who discovered that our entire stock of 'Lithium-Ion Battery Packs' is incorrectly stored at the 'Chicago Parts Depot', which is not certified for HAZMAT goods. Your objective is to correct this compliance breach immediately. You must initiate a transfer of the entire available stock of this product from Chicago to our certified facility, the 'Cleveland Chemical Storage'. After initiating the transfer, you must perform a verification by retrieving the updated inventory records for both warehouses. Finally, log the corrective action with the event code 'HAZMAT_COMPLIANCE_TRANSFER' and outcome code 'INVENTORY_RELOCATED' and report the new 'quantity_inbound' at the Cleveland facility.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Lithium-Ion Battery Pack"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Chicago Parts Depot"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-BATT-Q17", "warehouse_id": "WH-03"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Cleveland Chemical Storage"}),
            Action(
                name="initiate_warehouse_transfer",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                    "quantity": 1400,
                    "from_warehouse_id": "WH-03",
                    "to_warehouse_id": "WH-13"
                }
            ),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-BATT-Q17", "warehouse_id": "WH-03"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-BATT-Q17", "warehouse_id": "WH-13"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "HAZMAT_COMPLIANCE_TRANSFER",
                    "subject_id": "TECH-BATT-Q17",
                    "outcome_code": "INVENTORY_RELOCATED"
                }
            )
        ],
        outputs=["1400"]
    ),
    Task(
        annotator="0",
        user_id="task_35",
        instruction="You are an inventory accountant. Establish comprehensive financial accountability for all '8-bit Microcontroller' inventory across the entire warehouse network. Achieve complete system-wide inventory valuation including total quantities, financial values, and location distribution, with consolidated audit documentation using event code 'MULTI_WAREHOUSE_INVENTORY_AUDIT' and outcome 'AUDIT_COMPLETE'. Report the calculated system-wide total value.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "ELEC-CHIP-A1"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-03"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "MULTI_WAREHOUSE_INVENTORY_AUDIT",
                    "subject_id": "ELEC-CHIP-A1",
                    "outcome_code": "AUDIT_COMPLETE",
                    "outcome_details": {"total_quantity_on_hand": 23000, "total_value": 57500.00, "location_count": 2}
                }
            )
        ],
        outputs=["57500.00"]
    ),
    Task(
        annotator="0",
        user_id="task_36",
        instruction="You are a quality auditor. While preparing order 'ORD-0001' for 'Alpha Electronics LLC', you inspect the 300 '8-bit Microcontroller' units allocated for shipment. Your inspection reveals that 10 units are damaged. Your objective is to handle this quality failure before shipment. You must: 1) Update the inventory record to reflect the 10 newly discovered damaged units. 2) Cancel the original order with status 'Cancelled - Damaged Stock' so it can be re-processed correctly. 3) Calculate the inventory loss from the damaged goods. 4) Log a detailed audit with event code 'PRE_SHIPMENT_QUALITY_FAIL' and outcome code 'ORDER_CANCELLED'. Finally, report the calculated inventory loss.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0001"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0001", "damaged_quantity": 10}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0001", "new_status": "Cancelled - Damaged Stock"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "PRE_SHIPMENT_QUALITY_FAIL",
                    "subject_id": "ORD-0001",
                    "outcome_code": "ORDER_CANCELLED",
                    "outcome_details": {"scrapped_qty": 10, "inventory_loss_usd": 25.00}
                }
            )
        ],
        outputs=["25.00"]
    ),
    Task(
        annotator="0",
        user_id="task_37",
        instruction="You are a fulfillment specialist handling a 'Critical' priority order for 'Alpha Electronics LLC' for 13,000 '8-bit Microcontrollers' to be shipped to San Jose. The 'Los Angeles Distribution Center' only has 12,500 units available. Your objective is to fulfill the order by creating split shipments from multiple warehouses. The final state must show: 1. An outbound order for 12,500 units is created and shipped from Los Angeles (WH-01). 2. A second order for the remaining 500 units is created and shipped from the 'Chicago Parts Depot' (WH-03). 3. Both shipments use the best 'Air' carrier per policy. Finally, report the tracking numbers for both shipments.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "ELEC-CHIP-A1"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Critical",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 12500}]
                }
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Critical",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 500}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "ORDER_FULFILLMENT_SPLIT", "subject_id": "ORD-0017;ORD-0018", "outcome_code": "FULFILLED_FROM_MULTIPLE_WAREHOUSES",
                    "outcome_details": {"original_request_qty": 13000, "wh1_qty": 12500, "wh2_qty": 500}
                }
            )
        ],
        outputs=["UPSN-0017", "UPSN-0018"]
    ),
    Task(
        annotator="0",
        user_id="task_38",
        instruction="You are a transport analyst. For a 'High' priority shipment of 1,000 'Organic Cotton T-Shirts' to Toronto for 'Epsilon Fashion Co.', determine the optimal carrier between UPS and FedEx. Your objective is a comparative analysis based on policy. You must: 1) Create and ship two identical test orders (one UPS, one FedEx). 2) As the shipping costs are identical, apply the policy's tie-breaker rule by comparing the carriers' 'on_time_delivery_percentage'. 3) Log an audit event with event code 'CARRIER_PROFITABILITY_ANALYSIS' and outcome code 'TIEBREAKER_APPLIED'. The 'Organic Cotton T-Shirts' are primarily stocked at the Newark Apparel Hub (WH-04). Finally, report the name of the superior carrier.",
        actions=[
            Action(name="create_outbound_order", kwargs={"customer_name": "Epsilon Fashion Co.", "destination_city": "Toronto", "priority_level": "High", "line_items": [{"sku": "APRL-TSHT-O15", "quantity": 1000}]}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Epsilon Fashion Co.", "destination_city": "Toronto", "priority_level": "High", "line_items": [{"sku": "APRL-TSHT-O15", "quantity": 1000}]}),
            Action(name="get_product_details", kwargs={"product_name": "Organic Cotton T-Shirt"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Newark Apparel Hub"}),
            Action(name="get_inventory_details", kwargs={"sku": "APRL-TSHT-O15", "warehouse_id": "WH-04"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-04", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-04", "carrier_scac": "FDEG"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "UPS"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "FedEx"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "CARRIER_PROFITABILITY_ANALYSIS", "subject_id": "APRL-TSHT-O15", "outcome_code": "TIEBREAKER_APPLIED",
                    "outcome_details": {"most_profitable_carrier": "UPS", "tiebreaker_metric": "ON_TIME_DELIVERY_PERCENTAGE"}
                }
            )
        ],
        outputs=["UPS"]
    ),
    Task(
        annotator="0",
        user_id="task_39",
        instruction="You are an international auditor verifying our returns process. Your first objective is to execute a complete return for 'Beta Retail GmbH' in Hamburg, Germany, for 15 'Smartphone Model X' units from their sales order 'SO-2024-0002', using the reason code 'AUDIT_SCENARIO'. Your second objective is to immediately audit this transaction. You must verify that: 1) The credit memo value correctly matches the product's unit price. 2) The correct international return carrier ('DHL Express') was used. After verifying, log a successful audit using the event code 'INTERNATIONAL_RETURN_AUDIT' and outcome code 'RETURN_AUDIT_PASS', with the outcome details {\"financial_check\": \"PASS\", \"logistics_check\": \"PASS\"}. Finally, report the ID of the inbound return shipment created.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0002"}),
            Action(name="get_product_details", kwargs={"product_name": "Smartphone Model X"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0002", "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 15}], "reason": "AUDIT_SCENARIO"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0002", "customer_id": "CUST-2002", "returned_items": [{"sku": "ELEC-SMART-W23", "quantity": 15}]}),
            Action(name="create_inbound_return_shipment", kwargs={"rma_id": "RMA-1001", "from_customer_id": "CUST-2002", "to_warehouse_id": "WH-02", "carrier_scac": "DHLG"}),
            Action(name="get_credit_memo_details", kwargs={"credit_memo_id": "CM-0002"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "DHL Express"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "INTERNATIONAL_RETURN_AUDIT", "subject_id": "RMA-1001", "outcome_code": "RETURN_AUDIT_PASS",
                    "outcome_details": {"financial_check": "PASS", "logistics_check": "PASS"}
                }
            )
        ],
        outputs=["SHIP-0031"]
    ),
    Task(
        annotator="0",
        user_id="task_40",
        instruction="You are a priority fulfillment manager. You have a new 'Critical' priority order for 10,000 '8-bit Microcontrollers' for 'Zeta Tech Solutions', located in Yokohama, that must ship from the 'Los Angeles Distribution Center'. Upon checking, you see the warehouse has stock on hand, but none is available. The entire stock is allocated to a 'Low' priority order, 'ORD-0001'. Your objective is to resolve this deadlock. You must cancel the low-priority order ('ORD-0001') to free up the inventory. Then, create and ship the new 'Critical' order for Zeta Tech Solutions. This new order will be assigned the ID 'ORD-0017'. Log the resolution event. Finally, report the tracking number for the new critical shipment.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0001", "new_status": "Cancelled"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Zeta Tech Solutions", "destination_city": "Yokohama", "priority_level": "Critical",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 10000}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "DEADLOCK_RESOLUTION", "subject_id": "ORD-0017", "outcome_code": "FULFILLED_BY_CANCELLING_ORD-0001"
                }
            ),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_41",
        instruction="You are a finance auditor verifying inventory data integrity. For the 'Teak Wood Dining Chair' at the 'Dallas Home Goods DC', your objective is to perform a full financial reconciliation of its inventory record. You must retrieve the inventory record to get the system's 'quantity_on_hand' and 'unit_cost', then manually recalculate the correct 'total_value'. You must then compare your calculated value with the 'total_value' currently stored in the system. Log an audit event with the code 'INVENTORY_FINANCIAL_AUDIT' detailing both the system value and your calculated value. Finally, report your calculated total value.",
        actions=[
        Action(name="get_product_details", kwargs={"product_name": "Teak Wood Dining Chair"}),
        Action(name="get_warehouse_details", kwargs={"warehouse_name": "Dallas Home Goods DC"}),
        Action(
            name="get_inventory_details",
            kwargs={
                "sku": "FURN-CHAIR-M13",
                "warehouse_id": "WH-14"
            }
        ),
        Action(
            name="log_audit_trail",
            kwargs={
                "audit_event": "INVENTORY_FINANCIAL_AUDIT",
                "subject_id": "INV-0013",
                "outcome_code": "VALUES_RECONCILED",
                "outcome_details": {
                    "system_total_value": 72000.00,
                    "calculated_total_value": 72000.00,
                    "discrepancy": 0.00
                }
            }
        )
    ],
        outputs=["72000.00"]
    ),
    Task(
        annotator="0",
        user_id="task_42",
        instruction="You are a logistics planner handling a consolidated order for 'Epsilon Fashion Co.' to be sent to Toronto with 'High' priority. The order consists of 20 'Teak Wood Dining Chairs' and 10 'Raw Cotton Bales'. The items must be shipped from their respective source warehouses via 'Truck' transport. Your objective is to execute this fulfillment. The final state must show: 1) A shipment for the chairs is created from their source warehouse (WH-14). 2) A separate shipment for the cotton bales is created from their source warehouse (WH-04). 3) Both shipments use the best-performing 'Truck' carrier. Finally, report the tracking numbers for both shipments, joined by a semicolon.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Teak Wood Dining Chair"}),
            Action(name="get_product_details", kwargs={"product_name": "Raw Cotton Bale"}),
            Action(name="get_inventory_details", kwargs={"sku": "FURN-CHAIR-M13", "warehouse_id": "WH-14"}),
            Action(name="get_inventory_details", kwargs={"sku": "MATR-COTT-R18", "warehouse_id": "WH-04"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Epsilon Fashion Co.", "destination_city": "Toronto", "priority_level": "High",
                    "line_items": [{"sku": "FURN-CHAIR-M13", "quantity": 20}]
                }
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Epsilon Fashion Co.", "destination_city": "Toronto", "priority_level": "High",
                    "line_items": [{"sku": "MATR-COTT-R18", "quantity": 10}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Truck"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-14", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-04", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0018"})
        ],
        outputs=["UPSN-0017;UPSN-0018"]
    ),
    Task(
        annotator="0",
        user_id="task_43",
        instruction="You are a priority fulfillment manager. You have a new 'Critical' priority order for 10,000 '8-bit Microcontrollers' for 'Zeta Tech Solutions' that must ship from the 'Los Angeles Distribution Center' to Yokohama. Upon checking, you see the warehouse has stock on hand, but none is available. The entire stock is allocated to a 'Low' priority order, 'ORD-0001'. Your objective is to resolve this deadlock. You must cancel the low-priority order ('ORD-0001') to free up the inventory, then create and ship the new 'Critical' order. Log the resolution event. Finally, report the tracking number for the new critical shipment.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Los Angeles Distribution Center"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0001", "new_status": "Cancelled"}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Zeta Tech Solutions", "destination_city": "Yokohama", "priority_level": "Critical", "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 10000}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(name="log_audit_trail", kwargs={"audit_event": "DEADLOCK_RESOLUTION", "subject_id": "ORD-0017", "outcome_code": "FULFILLED_BY_CANCELLING_ORD-0001"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_44",
        instruction="You are a kitting specialist. Ensure successful fulfillment of a high-priority 'Basic Robotic Starter Kit' order for 'Gamma Construction Ltd.' destined for Denver from 'Chicago Parts Depot'. Achieve complete pre-fulfillment compliance verification for all kit components, successful order creation and shipment execution, and audit confirmation of fulfillment success. The audit must show that the 'Articulated Robotic Arm' compliance check is 'FAIL' and the 'Lithium-Ion Battery Pack' compliance check is 'FAIL'. Report the tracking number.",
        actions=[
            Action(name="get_kit_components", kwargs={"kit_sku": "KIT-ROBO-S1"}),
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="get_product_details", kwargs={"product_name": "Lithium-Ion Battery Pack"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-ROBO-N14", "warehouse_id": "WH-03"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-BATT-Q17", "warehouse_id": "WH-03"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Chicago Parts Depot"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Gamma Construction Ltd.", "destination_city": "Denver", "priority_level": "High",
                    "line_items": [{"sku": "TECH-ROBO-N14", "quantity": 1}, {"sku": "TECH-BATT-Q17", "quantity": 2}]
                }
            ),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "KIT_FULFILLMENT_AUDIT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "STOCK_VERIFIED_AND_SHIPPED",
                    "outcome_details": {
                        "robotic_arm_compliance_check": "FAIL",
                        "battery_compliance_check": "FAIL"
                    }
                }
            ),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_45",
        instruction="You are a returns inspector. Process a partial-damage return of 100 'Ceramic Floor Tile' from 'Gamma Construction Ltd.' order 'SO-2024-0003' at 'Miami Building Materials' warehouse, where 85 tiles are perfect and 15 are broken. Achieve complete return processing with full customer credit, proper inventory disposition separating sellable from damaged stock, and documentation of split-disposition outcomes. Log an audit trail with the exact audit event 'RETURN_INSPECTION_AUDIT' and outcome code 'DISPOSITION_COMPLETED_SUCCESSFULLY'. Report the new quantity_damaged for this product at Miami warehouse.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0003", "line_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}], "reason": "PARTIAL_DAMAGE_RETURN"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0003", "customer_id": "CUST-2003", "returned_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}]}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": -85}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": 15}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "RETURN_INSPECTION_AUDIT",
                    "subject_id": "RMA-1001",
                    "outcome_code": "DISPOSITION_COMPLETED_SUCCESSFULLY",
                    "outcome_details": {"restocked_qty": 85, "damaged_qty": 15}
                }
            ),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"})
        ],
        outputs=["180"]
    ),
    Task(
        annotator="0",
        user_id="task_46",
        instruction="You are a carrier relations manager. Address the performance deficiency of ocean carrier 'Maersk' which has fallen below acceptable company standards. Achieve complete risk mitigation by reassigning all active 'Shipped' orders to best-performing alternative ocean carriers and implementing carrier suspension to prevent future assignments. Report the total number of orders reassigned.",
        actions=[
            Action(name="get_carrier_details", kwargs={"carrier_name": "Maersk"}),
            Action(name="find_orders_by_carrier", kwargs={"carrier_name": "Maersk", "status": "Shipped"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Sea"}),
            Action(
                name="reassign_order_carrier",
                kwargs={"order_id": "ORD-0006", "new_carrier_scac": "KNLU"}
            ),
            Action(name="update_carrier_status", kwargs={"carrier_name": "Maersk", "status": "Suspended"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "CARRIER_SUSPENSION", "subject_id": "MAEU", "outcome_code": "ORDERS_REASSIGNED",
                    "outcome_details": {"reassigned_order_count": 1, "new_carrier": "KNLU"}
                }
            )
        ],
        outputs=["1"]
    ),
    Task(
        annotator="0",
        user_id="task_47",
        instruction="You are a logistics planner. Execute a complex multi-modal international shipment of 700 'Ceramic Brake Pad Sets' for 'Iota Automotive SAS' from 'Chicago Parts Depot' to Lyon, France. This shipment has 'High' priority and requires domestic rail and international ocean transport legs. Achieve optimal carrier selection for both rail and ocean segments based on company policy, establish comprehensive planning documentation with 'MULTI_LEG_PLAN_CREATED' audit event, and initiate first-leg transportation. Report the tracking number for the rail segment.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Brake Pad Set"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Iota Automotive SAS", "destination_city": "Lyon", "priority_level": "High",
                    "line_items": [{"sku": "AUTO-PAD-B2", "quantity": 700}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Rail"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Sea"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Chicago Parts Depot"}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "MULTI_LEG_PLAN_CREATED", "subject_id": "ORD-0017", "outcome_code": "CARRIERS_SELECTED",
                "outcome_details": {"rail_carrier": "KNLU", "sea_carrier": "KNLU"}}
            ),
            Action(
                name="ship_outbound_order",
                kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "KNLU"}
            ),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["KNLU-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_48",
        instruction="You are a returns specialist. Manage the safe return of 20 'Smartphone Model X' units from 'Beta Retail GmbH' order 'SO-2024-0002' damaged in transit, ensuring hazardous materials compliance. Achieve complete return resolution with reason code 'DAMAGED_IN_TRANSIT', customer credit, compliant international return shipment via 'DHL Express', and hazmat compliance documentation through 'HAZMAT_RETURN_AUDIT' with 'CARRIER_COMPLIANT' outcome. Report the RMA ID.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0002"}),
            Action(name="get_product_details", kwargs={"product_name": "Smartphone Model X"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "DHL Express"}),
            Action(
                name="create_return_authorization",
                kwargs={"order_id": "ORD-0002", "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 20}], "reason": "DAMAGED_IN_TRANSIT"}
            ),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0002", "customer_id": "CUST-2002", "returned_items": [{"sku": "ELEC-SMART-W23", "quantity": 20}]}),
            Action(name="create_inbound_return_shipment", kwargs={"rma_id": "RMA-1001", "from_customer_id": "CUST-2002", "to_warehouse_id": "WH-02", "carrier_scac": "DHLG"}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "HAZMAT_RETURN_AUDIT", "subject_id": "RMA-1001", "outcome_code": "CARRIER_COMPLIANT"}
            )
        ],
        outputs=["RMA-1001"]
    ),
    Task(
        annotator="0",
        user_id="task_49",
        instruction="You are a returns inspector. Complete the processing of 100 'Ceramic Floor Tile' returned from order 'SO-2024-0003' at 'Miami Building Materials' warehouse, with 85 tiles in perfect condition and 15 broken. Achieve comprehensive return resolution including full customer credit authorization, appropriate inventory disposition for both good and damaged stock, and complete event documentation. Report the new quantity_damaged for this product at Miami warehouse.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0003", "line_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}], "reason": "PARTIAL_DAMAGE_RETURN"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0003", "customer_id": "CUST-2003", "returned_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}]}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": -85}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": 15}),
            Action(name="log_audit_trail", kwargs={"audit_event": "PARTIAL_DAMAGE_RETURN", "subject_id": "RMA-1001", "outcome_code": "SPLIT_DISPOSITION_COMPLETE"}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"})
        ],
        outputs=["180"]
    ),
    Task(
        annotator="0",
        user_id="task_50",
        instruction="You are a Logistics Manager. A 'Critical' priority order for 2 'Basic Robotic Starter Kits' has been placed by 'Alpha Electronics LLC' for delivery to San Jose, USA. This kit contains HAZMAT components (Lithium-Ion Battery Packs). The fulfillment warehouse is 'Chicago Parts Depot' (WH-03). Your objective is to ensure this order is fulfilled compliantly. The final state must show: 1. The individual components of the kit are identified. 2. The order is created. 3. The order is shipped using the best available 'Air' carrier, ensuring HAZMAT compliance. 4. A 'HAZMAT_KIT_FULFILLMENT_AUDIT' event is logged with outcome code 'HAZMAT_ORDER_SHIPPED_COMPLIANT', including the total value, total weight, and carrier SCAC in the outcome details. Finally, report the final tracking number.",
        actions=[
            Action(name="get_kit_components", kwargs={"kit_name": "Basic Robotic Starter Kit"}),
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="get_product_details", kwargs={"product_name": "Lithium-Ion Battery Pack"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-ROBO-N14", "warehouse_id": "WH-03"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-BATT-Q17", "warehouse_id": "WH-03"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Critical",
                    "line_items": [
                        {"sku": "TECH-ROBO-N14", "quantity": 2},
                        {"sku": "TECH-BATT-Q17", "quantity": 4}
                    ]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "HAZMAT_KIT_FULFILLMENT_AUDIT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "HAZMAT_ORDER_SHIPPED_COMPLIANT",
                    "outcome_details": {
                        "total_value_usd": 50359.96,
                        "total_weight_kg": 502.8,
                        "carrier_scac": "UPSN"
                    }
                }
            )
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_51",
        instruction="You are a risk manager. Assess and address potential performance risks for order 'ORD-0006' shipped to 'Zeta Tech Solutions' via 'Maersk'. Determine if carrier performance meets company standards (OTD ≥ 95%) and achieve risk mitigation through carrier reassignment to best-performing 'Sea' carrier if needed, with comprehensive audit documentation and verification of successful changes. The audit log must include the exact reason code 'CARRIER_OTD_BELOW_THRESHOLD' for reassignment. Report the performance rating of the final assigned carrier.",
        actions=[
            Action(name="get_carrier_details", kwargs={"carrier_name": "Maersk"}),
            Action(name="find_orders_by_carrier", kwargs={"carrier_name": "Maersk", "status": "Shipped"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Sea"}),
            Action(name="reassign_order_carrier", kwargs={"order_id": "ORD-0006", "new_carrier_scac": "KNLU"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "Kuehne + Nagel"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0006"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "PROACTIVE_CARRIER_REASSIGNMENT", "subject_id": "ORD-0006", "outcome_code": "SUCCESS_AND_VERIFIED",
                    "outcome_details": {"original_carrier": "MAEU", "new_carrier": "KNLU", "reason": "CARRIER_OTD_BELOW_THRESHOLD"}
                }
            )
        ],
        outputs=["4.8"]
    ),
    Task(
        annotator="0",
        user_id="task_52",
        instruction="You are a returns auditor. Quantify the complete financial impact of processing 100 'Ceramic Floor Tile' returned from order 'SO-2024-0003', where 85 tiles are sellable and 15 are damaged. Achieve comprehensive financial accounting including full customer credit processing, proper inventory disposition, accurate inventory loss calculation for damaged goods, and detailed audit documentation. Report the calculated inventory loss.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0003", "customer_id": "CUST-2003", "returned_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}]}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": -85}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": 15}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "PARTIAL_DAMAGE_RETURN", "subject_id": "ORD-0003", "outcome_code": "SPLIT_DISPOSITION_COMPLETE",
                    "outcome_details": {"restocked_qty": 85, "scrapped_qty": 15, "inventory_loss": 52.50}
                }
            )
        ],
        outputs=["52.50"]
    ),
    Task(
        annotator="0",
        user_id="task_53",
        instruction="You are a quality manager. Address the critical stock issue involving expired 'Organic Arabica Coffee Beans' (Lot 'LOT202405C') at 'Houston Food-Grade Warehouse' that affects pending order 'ORD-0012'. Achieve complete incident resolution including order cancellation with 'Cancelled - Expired Stock' status, safe disposal of expired inventory through damage marking, financial loss quantification, and incident documentation with 'EXPIRING_STOCK_INCIDENT' event code. Report the total calculated financial loss.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0012"}),
            Action(name="get_product_details", kwargs={"product_name": "Organic Arabica Coffee Beans"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Houston Food-Grade Warehouse"}),
            Action(name="get_inventory_details", kwargs={"sku": "FOOD-COFF-C3", "warehouse_id": "WH-05"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0012", "new_status": "Cancelled - Expired Stock"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0003", "damaged_quantity": 5000}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "EXPIRING_STOCK_INCIDENT", "subject_id": "FOOD-COFF-C3", "outcome_code": "INVENTORY_SCRAPPED_ORDERS_CANCELLED",
                    "outcome_details": {"cancelled_order_count": 1, "total_financial_loss": 110000.00}
                }
            )
        ],
        outputs=["110000.00"]
    ),
    Task(
        annotator="0",
        user_id="task_54",
        instruction="You are a quality manager. Prevent shipment of potentially expired 'Organic Arabica Coffee Beans' for a new high-priority order from 'Theta Foods SA' requesting 100kg delivery to São Paulo from 'Houston Food-Grade Warehouse'. If stock is expired, achieve complete safety compliance by canceling the customer order with the exact status 'CANCELLED_EXPIRED_STOCK', marking expired inventory for disposal, and documenting the critical incident with 'CRITICAL_STOCK_ISSUE' event type and 'ORDER_CANCELLED_DUE_TO_EXPIRED_STOCK' outcome. Report the Order ID that was cancelled.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Organic Arabica Coffee Beans"}),
            Action(name="get_inventory_details", kwargs={"sku": "FOOD-COFF-C3", "warehouse_id": "WH-05"}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Theta Foods SA", "destination_city": "São Paulo", "priority_level": "High", "line_items": [{"sku": "FOOD-COFF-C3", "quantity": 100}]}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0017", "new_status": "CANCELLED_EXPIRED_STOCK"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0003", "damaged_quantity": 5000}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "CRITICAL_STOCK_ISSUE", "subject_id": "FOOD-COFF-C3", "outcome_code": "ORDER_CANCELLED_DUE_TO_EXPIRED_STOCK"
                }
            )
        ],
        outputs=["ORD-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_55",
        instruction="You are a kitting specialist. Address compliance failure for a high-priority 'Basic Robotic Starter Kit' order from 'Gamma Construction Ltd.' shipping to Denver from 'Chicago Parts Depot'. Upon identifying that the kit contains HAZMAT components requiring certified warehouse capabilities not available at the current location, achieve compliance resolution by placing the order on hold with 'On Hold - Compliance Failure' status and documenting the violation with 'KIT_FULFILLMENT_COMPLIANCE_FAIL' event and 'INVALID_HAZMAT_WAREHOUSE' outcome. Report the SKU of the non-compliant component.",
        actions=[
            Action(name="create_outbound_order", kwargs={"customer_name": "Gamma Construction Ltd.", "destination_city": "Denver", "priority_level": "High", "line_items": [{"sku": "KIT-ROBO-S1", "quantity": 1}]}),
            Action(name="get_kit_components", kwargs={"kit_sku": "KIT-ROBO-S1"}),
            Action(name="get_product_details", kwargs={"product_name": "Lithium-Ion Battery Pack"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Chicago Parts Depot"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0017", "new_status": "On Hold - Compliance Failure"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "KIT_FULFILLMENT_COMPLIANCE_FAIL", "subject_id": "ORD-0017", "outcome_code": "INVALID_HAZMAT_WAREHOUSE",
                    "outcome_details": {"non_compliant_sku": "TECH-BATT-Q17", "warehouse_id": "WH-03"}
                }
            )
        ],
        outputs=["TECH-BATT-Q17"]
    ),
    Task(
        annotator="0",
        user_id="task_56",
        instruction="You are an auditor. Conduct comprehensive audit validation for multi-warehouse order 'ORD-0003' fulfilled for 'Gamma Construction Ltd.' with 100 'Ceramic Floor Tiles' from 'Miami Building Materials' and 10 'Industrial Paper Rolls' from 'Detroit Packaging Supplies'. Achieve complete logistics verification including total inventory cost calculation, warehouse capability validation for cross-docking operations, carrier performance assessment for 'FedEx', and consolidated audit documentation with 'MULTI_WAREHOUSE_SHIPMENT_AUDIT' and 'AUDIT_COMPLETE' codes. Report the carrier's average rating.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(name="get_product_details", kwargs={"product_name": "Industrial Paper Roll"}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Detroit Packaging Supplies"}),
            Action(name="get_inventory_details", kwargs={"sku": "MANU-PAPR-F6", "warehouse_id": "WH-08"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "FedEx"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Miami Building Materials"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "MULTI_WAREHOUSE_SHIPMENT_AUDIT", "subject_id": "ORD-0003", "outcome_code": "AUDIT_COMPLETE",
                    "outcome_details": {
                        "total_inventory_cost": 2850.00,
                        "wh_capability_check": {"WH-12": "PASS", "WH-08": "FAIL"}
                    }
                }
            )
        ],
        outputs=["4.8"]
    ),
    Task(
        annotator="0",
        user_id="task_57",
        instruction="You are a specialist. Process a quality-related financial return for 'Alpha Electronics LLC' returning 50 defective '8-bit Microcontroller' units from order 'SO-2024-0001'. Achieve complete return resolution including RMA creation with 'DEFECTIVE_RETURN' reason code, customer credit issuance, inventory adjustment marking returned units as damaged at 'Los Angeles Distribution Center', and comprehensive transaction documentation. Report the credit memo ID.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0001"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0001", "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}], "reason": "DEFECTIVE_RETURN"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0001", "customer_id": "CUST-2001", "returned_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}]}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0001", "damaged_quantity": 50}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "DEFECTIVE_RETURN_PROCESSED", "subject_id": "RMA-1001", "outcome_code": "INVENTORY_SCRAPPED_AND_CREDITED"
                }
            )
        ],
        outputs=["CM-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_58",
        instruction="You are an auditor. Perform a data integrity audit on sales order 'SO-2024-0003'. Your objective is to verify that the warehouse and carrier listed on the order record are consistent with their master data files. You must: 1) Retrieve the order details. 2) Retrieve the master data for the origin warehouse ('Miami Building Materials') and the carrier ('FedEx'). 3) Log a consolidated audit of your findings using the event code 'DATA_INTEGRITY_AUDIT' and outcome code 'VALIDATION_PASS'. Finally, report the average rating of the carrier.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Miami Building Materials"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "FedEx"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "DATA_INTEGRITY_AUDIT", "subject_id": "ORD-0003", "outcome_code": "VALIDATION_PASS",
                    "outcome_details": {"customer": "CUST-2003", "carrier": "FDEG", "warehouse": "WH-12"}
                }
            )
        ],
        outputs=["4.8"]
    ),
    Task(
        annotator="0",
        user_id="task_59",
        instruction="You are a returns specialist. Overcome carrier unavailability to process a return of 50 '8-bit Microcontrollers' for 'Alpha Electronics LLC' from order 'SO-2024-0001' when standard return carrier 'Hanjin' is inactive. Achieve complete return resolution despite carrier constraints by selecting best alternative 'Parcel' carrier based on highest average rating policy, creating return authorization with the exact reason code 'UNAVAILABLE_CARRIER_ISSUE', and inbound shipment with new carrier, and issuing customer credit. Log an audit trail with the exact event 'RETURN_CARRIER_EXCEPTION_AUDIT' and outcome code 'ALTERNATIVE_CARRIER_ASSIGNED'. Report the selected carrier's SCAC code.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0001"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0001", "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}], "reason": "UNAVAILABLE_CARRIER_ISSUE"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "Hanjin"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Parcel"}),
            Action(name="create_inbound_return_shipment", kwargs={"rma_id": "RMA-1001", "from_customer_id": "CUST-2001", "to_warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0001", "customer_id": "CUST-2001", "returned_items": [{"sku": "ELEC-CHIP-A1", "quantity": 50}]}),
            Action(name="log_audit_trail", kwargs={"audit_event": "RETURN_CARRIER_EXCEPTION_AUDIT", "subject_id": "RMA-1001", "outcome_code": "ALTERNATIVE_CARRIER_ASSIGNED"})
        ],
        outputs=["UPSN"]
    ),
    Task(
        annotator="0",
        user_id="task_60",
        instruction="You are a carrier auditor. The performance of 'Maersk' has fallen below the acceptable threshold. Your first objective is to execute a full suspension: find all their 'Shipped' orders, reassign each to the best alternative 'Sea' carrier, and then update Maersk's status to 'Suspended'. Your second objective is to immediately audit this action. You must retrieve the updated order ('ORD-0006') and the updated master record for 'Maersk' to confirm the changes were applied correctly. After verifying, log the successful audit and report the new status of Maersk.",
        actions=[
            Action(name="get_carrier_details", kwargs={"carrier_name": "Maersk"}),
            Action(name="find_orders_by_carrier", kwargs={"carrier_name": "Maersk", "status": "Shipped"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Sea"}),
            Action(name="reassign_order_carrier", kwargs={"order_id": "ORD-0006", "new_carrier_scac": "KNLU"}),
            Action(name="update_carrier_status", kwargs={"carrier_name": "Maersk", "status": "Suspended"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0006"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "Maersk"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "CARRIER_SUSPENSION_AUDIT", "subject_id": "MAEU", "outcome_code": "SUSPENSION_AND_REASSIGNMENT_VERIFIED"
                }
            )
        ],
        outputs=["Suspended"]
    ),
    Task(
        annotator="0",
        user_id="task_61",
        instruction="You are a kitting specialist. A 'High' priority order for a 'Super Starter Kit' (one 'Teak Wood Dining Chair' and ten 'Organic Cotton T-Shirts') is placed for 'Epsilon Fashion Co.' in Toronto. The components are in separate warehouses. Your objective is to fulfill the order by shipping from each location. The final state must show: 1. An outbound order for the chair is created and shipped from its warehouse (WH-14). 2. A separate outbound order for the t-shirts is created and shipped from its warehouse (WH-04). 3. Both shipments must use the best-performing 'Truck' carrier. Finally, report both tracking numbers.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Teak Wood Dining Chair"}),
            Action(name="get_product_details", kwargs={"product_name": "Organic Cotton T-Shirt"}),
            Action(name="get_inventory_details", kwargs={"sku": "FURN-CHAIR-M13", "warehouse_id": "WH-14"}),
            Action(name="get_inventory_details", kwargs={"sku": "APRL-TSHT-O15", "warehouse_id": "WH-04"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Epsilon Fashion Co.", "destination_city": "Toronto", "priority_level": "High",
                    "line_items": [{"sku": "FURN-CHAIR-M13", "quantity": 1}]
                }
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Epsilon Fashion Co.", "destination_city": "Toronto", "priority_level": "High",
                    "line_items": [{"sku": "APRL-TSHT-O15", "quantity": 10}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Truck"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-14", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-04", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0018"})
        ],
        outputs=["UPSN-0017", "UPSN-0018"]
    ),
    Task(
        annotator="0",
        user_id="task_62",
        instruction="You are a logistics corrections specialist. Resolve the fulfillment error for 'Gamma Construction Ltd.' order 'SO-2024-0003' where 10 'Industrial Paper Roll' were shipped instead of 100 'Ceramic Floor Tile'. Achieve complete error correction including return processing with 'INCORRECT_ITEM_SHIPPED' reason code, critical priority replacement order dispatch, inventory cost quantification of the error, and comprehensive audit documentation with 'SHIPMENT_ERROR_CORRECTION' event and 'RETURN_AND_REPLACE_COMPLETE' outcome. Report the calculated inventory cost of the error.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Industrial Paper Roll"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(
                name="create_return_authorization",
                kwargs={"order_id": "ORD-0003", "line_items": [{"sku": "MANU-PAPR-F6", "quantity": 10}], "reason": "INCORRECT_ITEM_SHIPPED"}
            ),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0003", "customer_id": "CUST-2003", "returned_items": [{"sku": "MANU-PAPR-F6", "quantity": 10}]}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "MANU-PAPR-F6"}),
            Action(name="get_inventory_details", kwargs={"sku": "MANU-PAPR-F6", "warehouse_id": "WH-08"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0006", "damaged_quantity": -10}),
            Action(
                name="create_outbound_order",
                kwargs={"customer_name": "Gamma Construction Ltd.", "destination_city": "Denver", "priority_level": "Critical", "line_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}]}
            ),
            Action(name="get_inventory_by_sku", kwargs={"sku": "BLDG-TILE-J10"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-12", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "SHIPMENT_ERROR_CORRECTION", "subject_id": "ORD-0003", "outcome_code": "RETURN_AND_REPLACE_COMPLETE",
                    "outcome_details": {"replacement_order_id": "ORD-0017", "error_inventory_cost": 2500.00}
                }
            )
        ],
        outputs=["2500.00"]
    ),
    Task(
        annotator="0",
        user_id="task_63",
        instruction="You are a priority fulfillment manager. Resolve inventory allocation conflict where a critical priority order for 10,000 '8-bit Microcontrollers' for 'Zeta Tech Solutions' shipping from 'Los Angeles Distribution Center' to Yokohama cannot be fulfilled due to stock being allocated to low-priority order 'ORD-0001'. Achieve priority-based resolution by reallocating inventory to the critical order, ensuring successful shipment execution, and documenting the resolution including affected order details. Report the tracking number for the critical shipment.",
        actions=[
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0001", "new_status": "Cancelled"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Zeta Tech Solutions", "destination_city": "Yokohama", "priority_level": "Critical", "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 10000}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "DEADLOCK_RESOLUTION", "subject_id": "ORD-0017", "outcome_code": "FULFILLED_BY_CANCELLING_ORD-0001",
                    "outcome_details": {"cancelled_order_id": "ORD-0001", "new_order_id": "ORD-0017"}
                }
            ),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_64",
        instruction="You are a fulfillment auditor testing the 'Chicago Parts Depot' process. Your objective is to execute and audit a new 'High' priority order for 'Gamma Construction Ltd.' in Denver via 'Truck' transport. The order must contain 5 'Articulated Robotic Arms' and 20 'Lithium-Ion Battery Packs'. After creating and shipping the order, you must perform a full audit: 1) Retrieve the final order details. 2) Retrieve inventory records to verify stock was correctly decremented. 3) Log your findings with the event code 'FULFILLMENT_PROCESS_AUDIT' and outcome code 'FULFILLMENT_AUDIT_PASS'. Finally, report the tracking number for the shipment.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="get_product_details", kwargs={"product_name": "Lithium-Ion Battery Pack"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Chicago Parts Depot"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Gamma Construction Ltd.", "destination_city": "Denver", "priority_level": "High",
                    "line_items": [{"sku": "TECH-ROBO-N14", "quantity": 5}, {"sku": "TECH-BATT-Q17", "quantity": 20}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Truck"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-ROBO-N14", "warehouse_id": "WH-03"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-BATT-Q17", "warehouse_id": "WH-03"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "FULFILLMENT_PROCESS_AUDIT", "subject_id": "ORD-0017", "outcome_code": "FULFILLMENT_AUDIT_PASS",
                    "outcome_details": {"carrier_policy_check": "PASS", "inventory_deduction_check": "PASS"}
                }
            )
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_65",
        instruction="You are a quality auditor at the 'Chicago Parts Depot'. While preparing order 'ORD-0014' for 10 'Articulated Robotic Arms', your inspection reveals that 2 units are damaged beyond repair. Your objective is to handle this quality failure before shipment. You must: 1) Update the inventory record to reflect the 2 newly discovered damaged units. 2) Cancel the original order using the status 'Cancelled - Damaged Stock'. 3) Calculate the inventory loss from the damaged goods. 4) Log a detailed audit with the event code 'PRE_SHIPMENT_QUALITY_FAIL' and outcome code 'ORDER_CANCELLED'. Finally, report the calculated inventory loss.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0014"}),
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Chicago Parts Depot"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-ROBO-N14", "warehouse_id": "WH-03"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0014", "damaged_quantity": 2}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0014", "new_status": "Cancelled - Damaged Stock"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "PRE_SHIPMENT_QUALITY_FAIL", "subject_id": "ORD-0014", "outcome_code": "ORDER_CANCELLED",
                    "outcome_details": {"scrapped_qty": 2, "inventory_loss": 24000.00}
                }
            )
        ],
        outputs=["24000.00"]
    ),
    Task(
        annotator="0",
        user_id="task_66",
        instruction="You are a kitting auditor. Execute and validate a complex multi-component kit fulfillment for 'Epsilon Fashion Co.' requesting a 'Super Starter Kit' (one 'Teak Wood Dining Chair', ten 'Organic Cotton T-Shirts') shipping to Toronto via truck transport from separate source warehouses. This is a 'High' priority fulfillment. Achieve comprehensive fulfillment execution with separate component shipments, complete financial audit including revenue calculation ($25.00/unit for t-shirts per policy), cost analysis, gross profit determination, and audit documentation with 'MULTI_SHIP_KIT_AUDIT' event. Report the calculated gross profit.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Teak Wood Dining Chair"}),
            Action(name="get_product_details", kwargs={"product_name": "Organic Cotton T-Shirt"}),
            Action(name="get_inventory_details", kwargs={"sku": "FURN-CHAIR-M13", "warehouse_id": "WH-14"}),
            Action(name="get_inventory_details", kwargs={"sku": "APRL-TSHT-O15", "warehouse_id": "WH-04"}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Epsilon Fashion Co.", "destination_city": "Toronto", "priority_level": "High", "line_items": [{"sku": "FURN-CHAIR-M13", "quantity": 1}]}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Epsilon Fashion Co.", "destination_city": "Toronto", "priority_level": "High", "line_items": [{"sku": "APRL-TSHT-O15", "quantity": 10}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Truck"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-14", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-04", "carrier_scac": "UPSN"}),
            Action(name="log_audit_trail", kwargs={"audit_event": "MULTI_SHIP_KIT_AUDIT", "subject_id": "ORD-0017;ORD-0018", "outcome_code": "PROFIT_CALCULATED", "outcome_details": {"profit": 44.99}})
        ],
        outputs=["44.99"]
    ),
    Task(
        annotator="0",
        user_id="task_67",
        instruction="You are a returns auditor. Determine the complete financial impact of processing 100 'Ceramic Floor Tile' returned from order 'SO-2024-0003', where 85 tiles are sellable and 15 are damaged. Achieve comprehensive financial reconciliation including full customer credit processing, proper inventory disposition separating good from damaged stock, accurate inventory loss calculation for damaged goods, and detailed audit documentation with the exact audit event 'RETURN_AUDIT_SPLIT_DISPOSITION' and outcome code 'DISPOSITION_COMPLETE'. Report the calculated inventory loss.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0003", "customer_id": "CUST-2003", "returned_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}]}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": -85}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": 15}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "RETURN_AUDIT_SPLIT_DISPOSITION", # Audit event agora é explicitado na instrução
                    "subject_id": "ORD-0003",
                    "outcome_code": "DISPOSITION_COMPLETE", # Outcome code agora é explicitado na instrução
                    "outcome_details": {"restocked_qty": 85, "scrapped_qty": 15, "inventory_loss": 52.50}
                }
            )
        ],
        outputs=["52.50"]
    ),
    Task(
        annotator="0",
        user_id="task_68",
        instruction="You are a specialist in financial returns auditing a return from 'Gamma Construction Ltd.' on order 'SO-2024-0003'. The return consists of 100 'Ceramic Floor Tile', of which 15 are reported as broken. Your objective is to achieve a fully reconciled state for this incident. The final state must show that: 1) A full credit for all 100 tiles has been issued. 2) The 85 undamaged tiles have been returned to available stock. 3) The 15 broken tiles have been marked as damaged. 4) A detailed audit log with the exact audit event 'FINANCIAL_RETURN_RECONCILIATION' and the outcome code 'PARTIAL_DAMAGE_RECONCILED' has been created, including the calculated inventory loss (cost of damaged goods). The return authorization must use the exact reason code 'PARTIAL_DAMAGE_REPORTED'. Finally, you must report the calculated inventory loss.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0003", "line_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}], "reason": "PARTIAL_DAMAGE_REPORTED"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0003", "customer_id": "CUST-2003", "returned_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}]}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": -85}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": 15}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "FINANCIAL_RETURN_RECONCILIATION",
                    "subject_id": "RMA-1001",
                    "outcome_code": "PARTIAL_DAMAGE_RECONCILED",
                    "outcome_details": {"credited_value": 600.00, "inventory_loss": 52.50}
                }
            )
        ],
        outputs=["52.50"]
    ),
    Task(
        annotator="0",
        user_id="task_69",
        instruction="You are an inventory planner. A 'Critical' priority order has been placed for 14,500 '8-bit Microcontrollers' for 'Alpha Electronics LLC' in San Jose. A key requirement is that the entire order must be shipped from the 'Los Angeles Distribution Center'. Currently, that warehouse has 12,500 units available. Your objective is to ensure the order can be fulfilled from Los Angeles as requested. The final state must show that the necessary 2,000 units have been transferred from our 'Chicago Parts Depot', the customer order has been created, and the full shipment has been dispatched from Los Angeles. Finally, report the tracking number for the customer's shipment.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "ELEC-CHIP-A1"}),
            Action(name="initiate_warehouse_transfer", kwargs={"sku": "ELEC-CHIP-A1", "quantity": 2000, "from_warehouse_id": "WH-03", "to_warehouse_id": "WH-01"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC", "destination_city": "San Jose", "priority_level": "Critical",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 14500}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(name="log_audit_trail", kwargs={"audit_event": "CONSOLIDATION_FULFILLMENT", "subject_id": "ORD-0017", "outcome_code": "TRANSFER_PREREQUISITE_MET"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_70",
        instruction="You are a returns auditor. A return from 'Gamma Construction Ltd.' on order 'SO-2024-0003' for 100 'Ceramic Floor Tile' has been inspected, revealing that 85 tiles are in perfect condition while 15 are broken. Your objective is to achieve a fully reconciled state for this incident. The final state must show that: 1) A full credit memo for all 100 tiles has been issued. 2) The 85 undamaged tiles are reflected in the available inventory. 3) The 15 broken tiles are reflected in the damaged inventory. 4) A detailed audit log with the event code 'PARTIAL_DAMAGE_RECONCILED' and outcome code 'SPLIT_DISPOSITION_COMPLETE' has been created, including the calculated inventory loss. Finally, you must report the calculated inventory loss.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0003", "customer_id": "CUST-2003", "returned_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}]}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": -85}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": 15}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "PARTIAL_DAMAGE_RECONCILED", "subject_id": "ORD-0003", "outcome_code": "SPLIT_DISPOSITION_COMPLETE",
                    "outcome_details": {"restocked_qty": 85, "scrapped_qty": 15, "inventory_loss": 52.50}
                }
            )
        ],
        outputs=["52.50"]
    ),
    Task(
        annotator="0",
        user_id="task_71",
        instruction="You are a kitting planner. A 'Critical' priority order for a 'Super Kit' (one 'Teak Wood Dining Chair', one 'Articulated Robotic Arm') is placed for 'Gamma Construction Ltd.' in Denver. The components must ship from their respective warehouses via 'Air' transport, as required for Critical orders. Your objective is to fulfill this order. The final state must show: 1) A separate order is created and shipped for each component from its source warehouse. 2) An audit log with the event code 'MULTI_SHIP_KIT_FULFILLMENT' and outcome code 'FULFILLMENT_COMPLETE' is created. Finally, report both tracking numbers.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Teak Wood Dining Chair"}),
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "FURN-CHAIR-M13"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "TECH-ROBO-N14"}),
            Action(
                name="create_outbound_order",
                kwargs={"customer_name": "Gamma Construction Ltd.", "destination_city": "Denver", "priority_level": "Critical", "line_items": [{"sku": "FURN-CHAIR-M13", "quantity": 1}]}
            ),
            Action(
                name="create_outbound_order",
                kwargs={"customer_name": "Gamma Construction Ltd.", "destination_city": "Denver", "priority_level": "Critical", "line_items": [{"sku": "TECH-ROBO-N14", "quantity": 1}]}
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-14", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "MULTI_SHIP_KIT_FULFILLMENT", "subject_id": "ORD-0017;ORD-0018", "outcome_code": "FULFILLMENT_COMPLETE"}
            )
        ],
        outputs=["UPSN-0017", "UPSN-0018"]
    ),
    Task(
        annotator="0",
        user_id="task_72",
        instruction="You are a specialist in financial returns auditing a return from 'Gamma Construction Ltd.' on order 'SO-2024-0003'. The return contains 100 'Ceramic Floor Tile' to be restocked at WH-12, and 10 'Industrial Paper Roll' to be restocked at WH-08. Use the reason code 'UNUSED_MATERIAL_RETURN'. Your objective is to achieve a fully reconciled state. The final state must show that: 1) A full credit has been issued. 2) For the tiles, 85 are restocked and 15 are marked as damaged. 3) The 10 paper rolls are restocked. 4) A detailed audit log with code 'MULTI_ITEM_RETURN_RECONCILED' is created, including the calculated inventory loss. Finally, report the calculated inventory loss.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(name="get_product_details", kwargs={"product_name": "Industrial Paper Roll"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0003", "line_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}, {"sku": "MANU-PAPR-F6", "quantity": 10}], "reason": "UNUSED_MATERIAL_RETURN"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0003", "customer_id": "CUST-2003", "returned_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}, {"sku": "MANU-PAPR-F6", "quantity": 10}]}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="get_inventory_details", kwargs={"sku": "MANU-PAPR-F6", "warehouse_id": "WH-08"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": -85}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": 15}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0006", "damaged_quantity": -10}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "FINANCIAL_RECONCILIATION", "subject_id": "RMA-1001", "outcome_code": "MULTI_ITEM_RETURN_RECONCILED",
                    "outcome_details": {"inventory_loss": 52.50}
                }
            )
        ],
        outputs=["52.50"]
    ),
    Task(
        annotator="0",
        user_id="task_73",
        instruction="You are an inventory rebalancing specialist. A new 'Critical' priority order has arrived for 'Zeta Tech Solutions' for 10,000 '8-bit Microcontrollers' to be shipped to Yokohama from the 'Los Angeles Distribution Center' (WH-01). To ensure fulfillment, you must transfer 2,000 units of '8-bit Microcontroller' from 'Chicago Parts Depot' (WH-03) to 'Los Angeles Distribution Center' (WH-01). After the transfer, create and ship the 'Critical' priority order using the best 'Air' carrier. The final state must show: 1) The transfer is completed. 2) The new 'Critical' order is created and fully dispatched. 3) A 'STOCK_REBALANCE_AUDIT' event is logged with outcome code 'FULFILLMENT_TRANSFER_COMPLETE', detailing the quantities transferred and shipped. Report the tracking number for the new critical shipment.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-03"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(
                name="initiate_warehouse_transfer",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "quantity": 2000,
                    "from_warehouse_id": "WH-03",
                    "to_warehouse_id": "WH-01"
                }
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Zeta Tech Solutions",
                    "destination_city": "Yokohama",
                    "priority_level": "Critical",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 10000}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-03"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "UPS"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "STOCK_REBALANCE_AUDIT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "FULFILLMENT_TRANSFER_COMPLETE",
                    "outcome_details": {
                        "transferred_quantity": 2000,
                        "shipped_quantity": 10000,
                        "fulfillment_warehouse": "WH-01",
                        "carrier_scac": "UPSN"
                    }
                }
            )
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_74",
        instruction="You are a kitting specialist. A 'Critical' order for a 'Super Kit' (one 'Teak Wood Dining Chair', one 'Articulated Robotic Arm') is placed for 'Gamma Construction Ltd.' in Denver. The components must ship from their respective warehouses via 'Air' transport, as required for Critical priority orders. Your objective is to fulfill this order. The final state must show: 1) A shipment for the chair is created from its source warehouse in Dallas (WH-14). 2) A separate shipment for the robotic arm is created from its source warehouse in Chicago (WH-03). 3) An audit log with the event code 'MULTI_SHIP_KIT_FULFILLMENT' is created. Finally, report both tracking numbers, joined by a semicolon.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Teak Wood Dining Chair"}),
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="get_inventory_details", kwargs={"sku": "FURN-CHAIR-M13", "warehouse_id": "WH-14"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-ROBO-N14", "warehouse_id": "WH-03"}),
            Action(
                name="create_outbound_order",
                kwargs={"customer_name": "Gamma Construction Ltd.", "destination_city": "Denver", "priority_level": "Critical", "line_items": [{"sku": "FURN-CHAIR-M13", "quantity": 1}]}
            ),
            Action(
                name="create_outbound_order",
                kwargs={"customer_name": "Gamma Construction Ltd.", "destination_city": "Denver", "priority_level": "Critical", "line_items": [{"sku": "TECH-ROBO-N14", "quantity": 1}]}
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-14", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "MULTI_SHIP_KIT_FULFILLMENT", "subject_id": "ORD-0017;ORD-0018", "outcome_code": "FULFILLMENT_COMPLETE"}
            )
        ],
        outputs=["UPSN-0017;UPSN-0018"]
    ),
    Task(
            annotator="0",
            user_id="task_75",
            instruction="You are a corrections auditor. Order 'SO-2024-0003' for 'Gamma Construction Ltd.' was fulfilled with the wrong item: 10 'Industrial Paper Roll' instead of 100 'Ceramic Floor Tile'. Your objective is to achieve a fully corrected and reconciled state. This requires that: 1) A full return for the incorrect items is processed with a credit memo using reason code 'INCORRECT_ITEM_SHIPPED'. 2) The returned, undamaged paper rolls are restocked at their proper warehouse ('Detroit Packaging Supplies'). 3) A new 'Critical' replacement order for the correct items is dispatched. Finally, you must report the tracking number of the correct, new shipment.",
            actions=[
                Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0003"}),
                Action(name="get_product_details", kwargs={"product_name": "Industrial Paper Roll"}),
                Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
                Action(
                    name="create_return_authorization",
                    kwargs={"order_id": "ORD-0003", "line_items": [{"sku": "MANU-PAPR-F6", "quantity": 10}], "reason": "INCORRECT_ITEM_SHIPPED"}
                ),
                Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0003", "customer_id": "CUST-2003", "returned_items": [{"sku": "MANU-PAPR-F6", "quantity": 10}]}),
                Action(name="get_warehouse_details", kwargs={"warehouse_name": "Detroit Packaging Supplies"}),
                Action(name="get_inventory_details", kwargs={"sku": "MANU-PAPR-F6", "warehouse_id": "WH-08"}),
                Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0006", "damaged_quantity": -10}),
                Action(
                    name="create_outbound_order",
                    kwargs={"customer_name": "Gamma Construction Ltd.", "destination_city": "Denver", "priority_level": "Critical", "line_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}]}
                ),
                Action(name="get_inventory_by_sku", kwargs={"sku": "BLDG-TILE-J10"}),
                Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
                Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-12", "carrier_scac": "UPSN"}),
                Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"})
            ],
            outputs=["UPSN-0017"]
        ),
    Task(
        annotator="0",
        user_id="task_103",
        instruction="You are a Supply Chain Compliance Auditor. Conduct an urgent audit for 'Influenza Vaccine' (SKU PHRM-VACC-D4) at the 'Atlanta Cold Chain Center' (WH-06). Your objective is to: 1) Verify its stock status, expiration date (assume current date is 2025-07-23), and temperature storage requirements. The inventory currently has a batch of 'Influenza Vaccine' with an expiration date of '2025-01-01'. 2) If the product is non-compliant (e.g., expired), immediately mark all 18,000 available units of this batch as damaged in inventory. 3) Log a performance issue against 'Mumbai Pharma Supplies' (SUP-1006) for 'EXPIRED_GOODS_RECEIVED' related to purchase order 'PO-2024-0006' and specific shipment 'SHIP-0006'. 4) Create a new 'Critical' priority purchase order for 18,000 units of 'Influenza Vaccine' from 'Mumbai Pharma Supplies' (SUP-1006). 5) Update the new inbound shipment (which will be 'SHIP-0031') to 'Expedited' status with the note 'URGENT_REPLENISHMENT_AFTER_DISPOSAL'. 6) Log an audit event with event 'COMPLIANCE_AUDIT_AND_REPLENISHMENT', outcome 'NON_COMPLIANT_STOCK_HANDLED', and details including 'disposed_quantity' (18000), 'new_po_number' ('PO-2025-0001'), and 'replenishment_shipment_id' ('SHIP-0031'). Report the new Purchase Order number.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Influenza Vaccine"}),
            Action(name="get_warehouse_details", kwargs={"warehouse_name": "Atlanta Cold Chain Center"}),
            Action(name="get_inventory_details", kwargs={"sku": "PHRM-VACC-D4", "warehouse_id": "WH-06"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0004", "damaged_quantity": 18000}),
            Action(name="log_supplier_performance_issue", kwargs={"supplier_id": "SUP-1006", "issue_code": "EXPIRED_GOODS_RECEIVED", "shipment_id": "SHIP-0006"}),
            Action(name="create_purchase_order", kwargs={"supplier_id": "SUP-1006", "line_items": [{"sku": "PHRM-VACC-D4", "quantity": 18000}], "priority": "Critical"}),
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2025-0001"}),
            Action(name="update_shipment_status", kwargs={"shipment_id": "SHIP-0031", "new_status": "Expedited", "notes": "URGENT_REPLENISHMENT_AFTER_DISPOSAL"}),
            Action(name="get_product_details", kwargs={"product_name": "Influenza Vaccine"}),
            Action(name="get_inventory_details", kwargs={"sku": "PHRM-VACC-D4", "warehouse_id": "WH-06"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "COMPLIANCE_AUDIT_AND_REPLENISHMENT",
                    "subject_id": "PHRM-VACC-D4;WH-06",
                    "outcome_code": "NON_COMPLIANT_STOCK_HANDLED",
                    "outcome_details": {
                        "disposed_quantity": 18000,
                        "new_po_number": "PO-2025-0001",
                        "replenishment_shipment_id": "SHIP-0031"
                    }
                }
            )
        ],
        outputs=["PO-2025-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_77",
        instruction="You are a kitting specialist. A 'Critical' priority order for a 'Home & Auto Combo' (one 'Ceramic Brake Pad Set' and four 'Teak Wood Dining Chairs') is placed for 'Iota Automotive SAS' in Lyon. The components are in different warehouses. Your objective is to fulfill this order by shipping the components from their respective locations via 'Air' transport. The final state must show: 1) A separate order is created and shipped for each component from its source warehouse. 2) Both shipments use the best-performing 'Air' carrier per policy. Finally, report both tracking numbers.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Brake Pad Set"}),
            Action(name="get_product_details", kwargs={"product_name": "Teak Wood Dining Chair"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "AUTO-PAD-B2"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "FURN-CHAIR-M13"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Iota Automotive SAS", "destination_city": "Lyon", "priority_level": "Critical",
                    "line_items": [{"sku": "AUTO-PAD-B2", "quantity": 1}]
                }
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Iota Automotive SAS", "destination_city": "Lyon", "priority_level": "Critical",
                    "line_items": [{"sku": "FURN-CHAIR-M13", "quantity": 4}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-14", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0018"})
        ],
        outputs=["UPSN-0017", "UPSN-0018"]
    ),
    Task(
        annotator="0",
        user_id="task_78",
        instruction="You are a Quality Assurance Lead. A critical fulfillment error occurred with order SO-2024-0002 for 'Beta Retail GmbH'. The warehouse shipped 1,200 units of '8-bit Microcontroller' instead of 'Smartphone Model X'. Your objective is a full recovery. The final state must show: 1. A complete return authorization using the reason code 'INCORRECT_ITEM_SHIPPED' and a full credit memo are issued. 2. A new, 'Critical' priority replacement order for the correct quantity of 'Smartphone Model X' is created and shipped from the original warehouse ('WH-02'). 3. A detailed audit log with the event code 'FULFILLMENT_CORRECTION' and outcome code 'RECOVERY_COMPLETE' is created. Finally, report the new tracking number and the ID of the issued credit memo.",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0002"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_product_details", kwargs={"product_name": "Smartphone Model X"}),
            Action(
                name="create_return_authorization",
                kwargs={"order_id": "ORD-0002", "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 1200}], "reason": "INCORRECT_ITEM_SHIPPED"}
            ),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0002", "customer_id": "CUST-2002", "returned_items": [{"sku": "ELEC-CHIP-A1", "quantity": 1200}]}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Beta Retail GmbH", "destination_city": "Hamburg", "priority_level": "Critical", "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 1200}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-02", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "FULFILLMENT_CORRECTION", "subject_id": "ORD-0002", "outcome_code": "RECOVERY_COMPLETE", "outcome_details": {"replacement_order_id": "ORD-0017", "rma_id": "RMA-1001", "credit_memo_id": "CM-0002"}}
            )
        ],
        outputs=["UPSN-0017", "CM-0002"]
    ),
    Task(
        annotator="0",
        user_id="task_79",
        instruction="You are a Returns Manager. Customer 'Alpha Electronics LLC' is processing a partial return against order 'ORD-0001'. They are returning 25 units of '8-bit Microcontroller'. Your inspection reveals that 10 of these units are damaged and must be written off, while 15 are in perfect condition. Your objective is to process this complex return. The final state must show: 1. An RMA is created for all 25 units using the reason code 'SPLIT_RETURN_DAMAGED_OVERSTOCK'. 2. Inventory at WH-01 is updated to move 10 units to 'damaged' and return 15 to 'available' stock. 3. A credit memo is issued for only the 15 undamaged items. 4. A 'PARTIAL_RETURN_AUDIT' log is created with outcome code 'PROCESSED_WITH_SPLIT'. Finally, report the RMA ID and the Credit Memo ID.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0001"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(
                name="create_return_authorization",
                kwargs={"order_id": "ORD-0001", "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 25}], "reason": "SPLIT_RETURN_DAMAGED_OVERSTOCK"}
            ),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0001", "damaged_quantity": 10}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0001", "damaged_quantity": -15}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0001", "customer_id": "CUST-2001", "returned_items": [{"sku": "ELEC-CHIP-A1", "quantity": 15}]}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "PARTIAL_RETURN_AUDIT", "subject_id": "RMA-1001", "outcome_code": "PROCESSED_WITH_SPLIT", "outcome_details": {"original_order_id": "ORD-0001", "damaged_quantity": 10, "restocked_quantity": 15, "credited_quantity": 15, "credit_memo_id": "CM-0001"}}
            )
        ],
        outputs=["RMA-1001", "CM-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_80",
        instruction="You are a Risk & Compliance Officer. An urgent alert has been raised for inbound shipment 'SHIP-0013', a 'High' priority shipment of 'Industrial Solvent' from 'Helsinki Chemicals Oy'. The assigned carrier, 'Hapag-Lloyd', is not certified for this HAZMAT class. This is a major compliance breach. Your objective is to mitigate this risk. The final state must show: 1. The inbound shipment 'SHIP-0013' is updated to a status of 'On Hold - Compliance Review' with the note code 'NOTE:NON_COMPLIANT_CARRIER_HLCU'. 2. The carrier 'Hapag-Lloyd' is set to 'Under Review'. 3. A new, 'Critical' priority purchase order is created for the same items. 4. An audit trail is logged with the event code 'HAZMAT_COMPLIANCE_BREACH' and outcome code 'MITIGATION_INITIATED'. 5. A supplier performance issue is logged using the issue code 'NON_COMPLIANT_CARRIER'. Finally, report the new Purchase Order ID and the audited shipment ID.",
        actions=[
            Action(name="find_inbound_shipment", kwargs={"supplier_name": "Helsinki Chemicals Oy", "origin_city": "Helsinki"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "Hapag-Lloyd"}),
            Action(name="get_product_details", kwargs={"product_name": "Industrial Solvent"}),
            Action(
                name="update_shipment_status",
                kwargs={"shipment_id": "SHIP-0013", "new_status": "On Hold - Compliance Review", "notes": "NOTE:NON_COMPLIANT_CARRIER_HLCU"}
            ),
            Action(name="update_carrier_status", kwargs={"carrier_name": "Hapag-Lloyd", "status": "Under Review"}),
            Action(name="log_supplier_performance_issue", kwargs={"supplier_id": "SUP-1013", "issue_code": "NON_COMPLIANT_CARRIER", "shipment_id": "SHIP-0013"}),
            Action(name="create_purchase_order", kwargs={"supplier_id": "SUP-1013", "line_items": [{"sku": "CHEM-SOLV-K11", "quantity": 400}], "priority": "Critical"}),
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2025-0001"}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "HAZMAT_COMPLIANCE_BREACH", "subject_id": "SHIP-0013", "outcome_code": "MITIGATION_INITIATED", "outcome_details": {"non_compliant_carrier": "HLCU", "new_po_number": "PO-2025-0001"}}
            )
        ],
        outputs=["PO-2025-0001", "SHIP-0013"]
    ),
    Task(
        annotator="0",
        user_id="task_81",
        instruction="You are a Supply Chain Analyst. You've determined that 'Johannesburg Mining Equipment' (SUP-1011) is an underperforming supplier. Your objective is to mitigate future risk. Find their large 'In Transit' shipment ('SHIP-0011'). Update its status with the note code 'FLAG_INSPECT_PERFORMANCE'. Then, create a new, 'High' priority Purchase Order for 20 'Diamond Core Drill Bits' with 'Berlin Auto Parts GmbH' (SUP-1003), our designated alternate for this category. Finally, log the performance issue against the original supplier using the issue code 'BELOW_OTD_THRESHOLD' and audit the mitigation action with the exact audit event 'SUPPLIER_RISK_MITIGATION_AUDIT' and outcome code 'ORDER_DIVERSIFICATION_SUCCESS'. Report the new Purchase Order number.",
        actions=[
            Action(name="find_inbound_shipment", kwargs={"supplier_name": "Johannesburg Mining Equipment", "origin_city": "Johannesburg", "status": "In Transit"}),
            Action(name="get_product_details", kwargs={"product_name": "Diamond Core Drill Bit"}),
            Action(name="update_shipment_status", kwargs={"shipment_id": "SHIP-0011", "new_status": "In Transit", "notes": "FLAG_INSPECT_PERFORMANCE"}),
            Action(name="log_supplier_performance_issue", kwargs={"supplier_id": "SUP-1011", "issue_code": "BELOW_OTD_THRESHOLD", "shipment_id": "SHIP-0011"}),
            Action(name="create_purchase_order", kwargs={"supplier_id": "SUP-1003", "line_items": [{"sku": "HEVY-DRIL-I9", "quantity": 20}], "priority": "High"}),
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2025-0001"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "SUPPLIER_RISK_MITIGATION_AUDIT",
                    "subject_id": "SUP-1011",
                    "outcome_code": "ORDER_DIVERSIFICATION_SUCCESS",
                    "outcome_details": {"underperforming_supplier": "SUP-1011", "flagged_shipment": "SHIP-0011", "new_supplier": "SUP-1003", "new_po": "PO-2025-0001"}
                }
            )
        ],
        outputs=["PO-2025-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_82",
        instruction="You are a Logistics Coordinator handling a critical service failure. Order 'ORD-0007', a shipment containing 50 units of 'Diamond Core Drill Bit' for 'Eta Mining Pty Ltd.', was returned due to incorrect customs documentation filed by the carrier, 'COSCO'. The customer requires an immediate reshipment. Your objective is to manage this incident completely. The final state must show: 1. The original order 'ORD-0007' is updated to 'Returned'. 2. The carrier 'COSCO' is placed 'Under Review'. 3. The 50 returned items are restocked into inventory at the origin warehouse 'WH-11'. 4. A new 'Critical' priority order is created for the 50 units. 5. The new order is shipped using the best available 'Air' carrier. 6. An audit log with the event 'RESHIPMENT_HAZMAT_FAILURE', outcome code 'RESHIPMENT_COMPLETED', and outcome details specifying the new order ID 'ORD-0017', original carrier SCAC 'COSU', and new carrier SCAC 'UPSN' is created. Finally, report the new tracking number.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Diamond Core Drill Bit"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0007"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0007", "new_status": "Returned"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "COSCO"}),
            Action(name="update_carrier_status", kwargs={"carrier_name": "COSCO", "status": "Under Review"}),
            Action(name="get_inventory_details", kwargs={"sku": "HEVY-DRIL-I9", "warehouse_id": "WH-11"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0009", "damaged_quantity": -50}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Eta Mining Pty Ltd.", "destination_city": "Perth", "priority_level": "Critical", "line_items": [{"sku": "HEVY-DRIL-I9", "quantity": 50}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-11", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "RESHIPMENT_HAZMAT_FAILURE",
                    "subject_id": "ORD-0007",
                    "outcome_code": "RESHIPMENT_COMPLETED",
                    "outcome_details": {"new_order_id": "ORD-0017", "original_carrier_scac": "COSU", "new_carrier_scac": "UPSN"}
                }
            )
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_83",
        instruction="You are an Inventory Manager responsible for stock rotation. You must audit our stock of 'Influenza Vaccine' (SKU PHRM-VACC-D4). Per policy, any batch expiring within the next 12 months must be written off for disposal. Your objective is to execute this policy. The final state must show: 1. You have identified the batch of vaccines at the 'Atlanta Cold Chain Center' (WH-06) that meets the expiration criteria. 2. The entire available quantity of this expiring batch has been moved to the 'damaged' category. 3. A new 'High' priority purchase order has been created for the exact quantity of disposed units from our critical pharma supplier, 'Mumbai Pharma Supplies' (SUP-1006). 4. The new inbound shipment created from this PO has been updated to 'Expedited' status with the note 'REPLENISHMENT_FOR_DISPOSED_STOCK'. 5. An audit log with the event 'EXPIRING_STOCK_DISPOSAL' is created. Finally, report the new Purchase Order number.",
        actions=[
            Action(name="get_inventory_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0004", "damaged_quantity": 18000}),
            Action(name="create_purchase_order", kwargs={"supplier_id": "SUP-1006", "line_items": [{"sku": "PHRM-VACC-D4", "quantity": 18000}], "priority": "High"}),
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2025-0001"}),
            Action(name="update_shipment_status", kwargs={"shipment_id": "SHIP-0031", "new_status": "Expedited", "notes": "REPLENISHMENT_FOR_DISPOSED_STOCK"}),
            Action(name="get_inventory_details", kwargs={"sku": "PHRM-VACC-D4", "warehouse_id": "WH-06"}),
            Action(name="log_audit_trail", kwargs={"audit_event": "EXPIRING_STOCK_DISPOSAL", "subject_id": "PHRM-VACC-D4", "outcome_code": "DISPOSED_AND_REORDERED", "outcome_details": {"inventory_id": "INV-0004", "disposed_quantity": 18000, "new_po_number": "PO-2025-0001", "replenishment_shipment_id": "SHIP-0031"}})
        ],
        outputs=["PO-2025-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_84",
        instruction="You are a Customs Broker preparing an international shipment. A 'Critical' priority order for 5 units of the 'Basic Robotic Starter Kit' has been placed by 'Beta Retail GmbH' for delivery to Hamburg, Germany, shipping from warehouse WH-03. This is a multi-component kit containing batteries (Hazmat Class 9). Your objective is to prepare and ship this order correctly. The final state must show: 1. The individual components of the kit have been identified. 2. The total weight and total value of the entire order have been calculated for the customs declaration. 3. The order has been created. 4. The order has been shipped using the best available 'Air' carrier. 5. A 'CUSTOMS_PREP' audit log has been created containing the final calculated weight, value, and the new order ID for documentation purposes. Finally, report the final tracking number.",
        actions=[
            Action(name="get_kit_components", kwargs={"kit_name": "Basic Robotic Starter Kit"}),
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="get_product_details", kwargs={"product_name": "Lithium-Ion Battery Pack"}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Beta Retail GmbH", "destination_city": "Hamburg", "priority_level": "Critical", "line_items": [{"sku": "TECH-ROBO-N14", "quantity": 5}, {"sku": "TECH-BATT-Q17", "quantity": 10}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(name="log_audit_trail", kwargs={"audit_event": "CUSTOMS_PREP", "subject_id": "ORD-0017", "outcome_code": "DATA_AGGREGATED", "outcome_details": {"total_weight_kg": 1257.0, "total_value_usd": 125899.9, "carrier_scac": "UPSN"}})
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_85",
        instruction="You are a Receiving Manager at WH-03. You've just received inbound shipment 'SHIP-0003' from 'Berlin Auto Parts GmbH', which corresponds to PO 'PO-2024-0003'. The PO was for 'Ceramic Brake Pad Set', but the shipment contained 300 units of 'Automotive Windshield' instead. This is a critical error. Your objective is to document and rectify this situation. The final state must show: 1. The inbound shipment 'SHIP-0003' is updated to a status of 'Received Incorrectly' with the exact note 'INCORRECT_SKU_RECEIVED'. 2. A performance issue is logged against the supplier using the code 'WRONG_ITEM_RECEIVED'. 3. A new 'Critical' priority purchase order is created with the same supplier for the correct item (800 units of 'Ceramic Brake Pad Set'). 4. The total value of the 300 incorrectly received goods is calculated and included in a final audit log with the exact audit event 'RECEIVING_ERROR_CORRECTION' and outcome code 'REPLACEMENT_ORDERED_AND_LOGGED'. Finally, report the new PO number.",
        actions=[
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2024-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Brake Pad Set"}),
            Action(name="get_product_details", kwargs={"product_name": "Automotive Windshield"}),
            Action(name="update_shipment_status", kwargs={"shipment_id": "SHIP-0003", "new_status": "Received Incorrectly", "notes": "INCORRECT_SKU_RECEIVED"}),
            Action(name="log_supplier_performance_issue", kwargs={"supplier_id": "SUP-1003", "issue_code": "WRONG_ITEM_RECEIVED", "shipment_id": "SHIP-0003"}),
            Action(name="create_purchase_order", kwargs={"supplier_id": "SUP-1003", "line_items": [{"sku": "AUTO-PAD-B2", "quantity": 800}], "priority": "Critical"}),
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2025-0001"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "RECEIVING_ERROR_CORRECTION",
                    "subject_id": "SHIP-0003",
                    "outcome_code": "REPLACEMENT_ORDERED_AND_LOGGED",
                    "outcome_details": {"supplier_id": "SUP-1003", "incorrect_shipment_value_usd": 75000, "new_po_number": "PO-2025-0001"}
                }
            )
        ],
        outputs=["PO-2025-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_86",
        instruction="You are a Fulfillment Optimizer. Order 'ORD-0002' for 'Beta Retail GmbH', containing 1200 units of 'Smartphone Model X' (SKU ELEC-SMART-W23), is 'In Transit' via 'DHL Express'. The customer wants to split the shipment: 400 units to Hamburg and the remaining 800 to a new hub in Berlin. Your objective is to resolve this. The final state must show: 1. The original order 'ORD-0002' is cancelled. 2. The 1200 units are explicitly released back to available stock at WH-02. 3. Two new 'High' priority orders are created. 4. Both new orders are shipped using the best 'Air' carrier. 5. An audit log with event 'ORDER_SPLIT_AND_REDIRECT' is created. Report both new tracking numbers.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0002"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-SMART-W23", "warehouse_id": "WH-02"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0002", "new_status": "Cancelled"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0023", "damaged_quantity": -1200}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Beta Retail GmbH", "destination_city": "Hamburg", "priority_level": "High", "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 400}]}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Beta Retail GmbH", "destination_city": "Berlin", "priority_level": "High", "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 800}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-02", "carrier_scac": "UPSN"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-02", "carrier_scac": "UPSN"}),
            Action(name="log_audit_trail", kwargs={"audit_event": "ORDER_SPLIT_AND_REDIRECT", "subject_id": "ORD-0002", "outcome_code": "SPLIT_COMPLETE", "outcome_details": {"new_order_hamburg": "ORD-0017", "new_order_berlin": "ORD-0018"}})
        ],
        outputs=["UPSN-0017", "UPSN-0018"]
    ),
    Task(
        annotator="0",
        user_id="task_87",
        instruction="You are an International Logistics Specialist resolving a major shipping error. Our high-value order of 5 'Articulated Robotic Arms' for 'Iota Automotive SAS' was mistakenly shipped to 'Alpha Electronics LLC' under order ID 'ORD-0001'. You must recall the incorrect shipment and fulfill the correct order. The final state must show: 1. The incorrect order 'ORD-0001' is updated to 'Returned'. 2. A full return and credit memo have been processed using the reason code 'INCORRECT_RECIPIENT'. 3. The recalled robotic arms are returned to available inventory at WH-03. 4. A new 'Critical' priority order for the correct items is created for 'Iota Automotive SAS' in Lyon. 5. This new order is shipped using the best available 'Air' carrier. 6. A detailed audit trail with event code 'MISSHIPMENT_RECOVERY' and outcome code 'RECOVERY_COMPLETE' is logged. Report the new tracking number and the credit memo ID.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0001"}),
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0001", "new_status": "Returned"}),
            Action(
                name="create_return_authorization",
                kwargs={"order_id": "ORD-0001", "line_items": [{"sku": "TECH-ROBO-N14", "quantity": 5}], "reason": "INCORRECT_RECIPIENT"}
            ),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0001", "customer_id": "CUST-2001", "returned_items": [{"sku": "TECH-ROBO-N14", "quantity": 5}]}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-ROBO-N14", "warehouse_id": "WH-03"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0014", "damaged_quantity": -5}),
            Action(name="create_outbound_order", kwargs={"customer_name": "Iota Automotive SAS", "destination_city": "Lyon", "priority_level": "Critical", "line_items": [{"sku": "TECH-ROBO-N14", "quantity": 5}]}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "MISSHIPMENT_RECOVERY", "subject_id": "ORD-0001", "outcome_code": "RECOVERY_COMPLETE", "outcome_details": {"incorrect_customer_id": "CUST-2001", "correct_customer_name": "Iota Automotive SAS", "new_order_id": "ORD-0017", "credit_memo_id": "CM-0001"}}
            )
        ],
        outputs=["UPSN-0017", "CM-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_88",
        instruction="You are a Supply Chain Risk Manager. An analysis has flagged two suppliers for underperformance: 'Global Components Inc.' (SUP-1001) and 'Shanghai Electronics Co.' (SUP-1025). You must cancel their key in-transit shipments ('SHIP-0001' and 'SHIP-0025' respectively) and re-source the products from our top-rated supplier, 'Tokyo Electronics Ltd.' (SUP-1002). The final state must show: 1. Both shipments are marked 'Cancelled' with the exact note 'SUPPLIER_UNDERPERFORMANCE_CANCEL'. 2. A performance issue is logged against each respective supplier for each cancelled shipment using the code 'SUPPLIER_PERFORMANCE_FAIL'. 3. Two new, 'High' priority purchase orders are created with 'Tokyo Electronics Ltd.' for the products '8-bit Microcontroller' (15000 units) and 'Smartphone Model X' (4000 units). 4. An audit trail is logged. Report both new purchase order numbers.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_product_details", kwargs={"product_name": "Smartphone Model X"}),
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2024-0001"}),
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2024-0025"}),
            Action(name="update_shipment_status", kwargs={"shipment_id": "SHIP-0001", "new_status": "Cancelled", "notes": "SUPPLIER_UNDERPERFORMANCE_CANCEL"}),
            Action(name="update_shipment_status", kwargs={"shipment_id": "SHIP-0025", "new_status": "Cancelled", "notes": "SUPPLIER_UNDERPERFORMANCE_CANCEL"}),
            Action(name="log_supplier_performance_issue", kwargs={"supplier_id": "SUP-1001", "issue_code": "SUPPLIER_PERFORMANCE_FAIL", "shipment_id": "SHIP-0001"}),
            Action(name="log_supplier_performance_issue", kwargs={"supplier_id": "SUP-1025", "issue_code": "SUPPLIER_PERFORMANCE_FAIL", "shipment_id": "SHIP-0025"}),
            Action(name="create_purchase_order", kwargs={"supplier_id": "SUP-1002", "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 15000}], "priority": "High"}),
            Action(name="create_purchase_order", kwargs={"supplier_id": "SUP-1002", "line_items": [{"sku": "ELEC-SMART-W23", "quantity": 4000}], "priority": "High"}),
            Action(name="log_audit_trail", kwargs={"audit_event": "SUPPLIER_RESOURCING", "subject_id": "SUP-1001;SUP-1025", "outcome_code": "ORDERS_REPLACED", "outcome_details": {"cancelled_shipments": "SHIP-0001;SHIP-0025", "new_supplier_id": "SUP-1002", "new_po_numbers": "PO-2025-0001;PO-2025-0002"}})
        ],
        outputs=["PO-2025-0001", "PO-2025-0002"]
    ),
    Task(
        annotator="0",
        user_id="task_89",
        instruction="You are a Cold Chain Auditor. Process a spoilage incident for PO 'PO-2024-0010', a shipment of 'Frozen Tuna Loin'. Temperature logs show a critical failure. The final state must show: 1. The shipment status is updated to 'Received - Damaged' with note code 'LOSS_TEMP_BREACH'. 2. The entire available quantity (2400 units) of the stock at WH-10 is marked as damaged. 3. A performance issue is logged against the supplier with code 'COLD_CHAIN_BREACH'. 4. A new 'Critical' priority PO is created to replenish the disposed quantity. 5. The new inbound shipment is marked 'Expedited' with note code 'URGENT_REPLACEMENT'. 6. An audit is logged with the exact audit event 'COLD_CHAIN_SPOILAGE_AUDIT', and the exact outcome code 'STOCK_REPLENISHED'. The outcome details must specify 'disposed_inventory_id' as 'INV-0008' and 'new_po_number' as 'PO-2025-0001'. Report the new PO number.",
        actions=[
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2024-0010"}),
            Action(name="get_product_details", kwargs={"product_name": "Frozen Tuna Loin"}),
            Action(name="update_shipment_status", kwargs={"shipment_id": "SHIP-0010", "new_status": "Received - Damaged", "notes": "LOSS_TEMP_BREACH"}),
            Action(name="get_inventory_details", kwargs={"sku": "FOOD-FISH-H8", "warehouse_id": "WH-10"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0008", "damaged_quantity": 2400}),
            Action(name="log_supplier_performance_issue", kwargs={"supplier_id": "SUP-1010", "issue_code": "COLD_CHAIN_BREACH", "shipment_id": "SHIP-0010"}),
            Action(name="create_purchase_order", kwargs={"supplier_id": "SUP-1010", "line_items": [{"sku": "FOOD-FISH-H8", "quantity": 2400}], "priority": "Critical"}),
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2025-0001"}),
            Action(name="update_shipment_status", kwargs={"shipment_id": "SHIP-0031", "new_status": "Expedited", "notes": "URGENT_REPLACEMENT"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "COLD_CHAIN_SPOILAGE_AUDIT",
                    "subject_id": "SHIP-0010",
                    "outcome_code": "STOCK_REPLENISHED",
                    "outcome_details": {"disposed_inventory_id": "INV-0008", "new_po_number": "PO-2025-0001"}
                }
            )
        ],
        outputs=["PO-2025-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_90",
        instruction="You are a Fraud Analyst. Customer 'Alpha Electronics LLC' (CUST-2001) has reported that order 'ORD-0001', which contained 300 units of '8-bit Microcontroller', is fraudulent. You must process this as a high-priority security incident. The final state must show: 1. The order status is updated to 'On Hold - Fraud Investigation'. 2. A provisional credit memo is issued for the fraudulent items. 3. A security note is added to the origin warehouse (WH-01) with the exact text: 'SECURITY_ALERT:ORD-0001_FRAUD_INVESTIGATION'. 4. A security audit is logged using the audit event 'FRAUDULENT_ORDER_REPORTED' and outcome code 'INVESTIGATION_OPENED'. Report the ID of the credit memo issued.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0001"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0001", "new_status": "On Hold - Fraud Investigation"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0001", "customer_id": "CUST-2001", "returned_items": [{"sku": "ELEC-CHIP-A1", "quantity": 300}]}),
            Action(name="update_warehouse_notes", kwargs={"warehouse_id": "WH-01", "notes": "SECURITY_ALERT:ORD-0001_FRAUD_INVESTIGATION"}),
            Action(name="get_credit_memo_details", kwargs={"credit_memo_id": "CM-0001"}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "FRAUDULENT_ORDER_REPORTED", "subject_id": "ORD-0001", "outcome_code": "INVESTIGATION_OPENED", "outcome_details": {"customer_id": "CUST-2001", "credit_memo_id": "CM-0001"}}
            )
        ],
        outputs=["CM-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_91",
        instruction="You are a Product Manager launching a new 'Robotics Pro Kit'. The kit consists of one 'Articulated Robotic Arm' and four 'Lithium-Ion Battery Packs'. Customer 'Osaka Robotics Corp.' wants to place a 'High' priority order for 3 of these new kits, to be shipped from 'Chicago Parts Depot' (WH-03) to Osaka via 'Air' transport. Your objective is to process this first-ever order. The final state must show: 1) You have verified the component SKUs and checked available stock. 2) A new outbound order is created. 3) The order is shipped using the best available 'Air' carrier. 4) An audit trail with event 'NEW_KIT_FULFILLMENT' and outcome code 'PRO_KIT_LAUNCH_ORDER_SHIPPED' is logged. Report the final tracking number.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="get_product_details", kwargs={"product_name": "Lithium-Ion Battery Pack"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-ROBO-N14", "warehouse_id": "WH-03"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-BATT-Q17", "warehouse_id": "WH-03"}),
            Action(
                name="create_outbound_order",
                kwargs={"customer_name": "Osaka Robotics Corp.", "destination_city": "Osaka", "priority_level": "High", "line_items": [{"sku": "TECH-ROBO-N14", "quantity": 3}, {"sku": "TECH-BATT-Q17", "quantity": 12}]}
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0017"}),
            Action(
                name="log_audit_trail",
                kwargs={"audit_event": "NEW_KIT_FULFILLMENT", "subject_id": "ORD-0017", "outcome_code": "PRO_KIT_LAUNCH_ORDER_SHIPPED", "outcome_details": {"customer_name": "Osaka Robotics Corp.", "carrier_scac": "UPSN"}}
            )
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_92",
        instruction="You are a Returns Manager. Customer 'Theta Foods SA' has reported a complete spoilage of their 'Frozen Tuna Loin' shipment from sales order 'SO-2024-0008' due to a critical temperature breach in transit, linked to inbound shipment 'SHIP-0010' from 'Sydney Seafood Exporters'. The original outbound shipment departed from the 'Buenos Aires Cold Chain' warehouse, but the return destination is the 'San Francisco Fresh Foods DC' (WH-10). Your objective is to process this international return and replenish the stock. The final state must show: 1. A return authorization is created for the 2400 spoiled units using the reason code 'SPOILAGE_TEMP_BREACH'. 2. A credit memo is issued for these 2400 units. 3. All 2400 currently available units of 'Frozen Tuna Loin' are explicitly marked as damaged in inventory at WH-10. 4. A performance issue is logged against the supplier ('Sydney Seafood Exporters', SUP-1010) using the issue code 'COLD_CHAIN_FAILURE_RETURN' for shipment 'SHIP-0010'. 5. A new 'Critical' priority purchase order for the exact quantity (2400 units) of 'Frozen Tuna Loin' is created with 'Sydney Seafood Exporters' (SUP-1010). 6. The new inbound shipment created from this PO (which will be 'SHIP-0031') is updated to 'Expedited' status with the note 'URGENT_SPOILAGE_REPLENISHMENT'. 7. The entire incident is logged in the audit trail with the event 'SPOILAGE_RETURN_RECOVERY' and outcome code 'REPLENISHMENT_INITIATED'. Report the ID of the credit memo and the new Purchase Order number (which will be 'PO-2025-0001').",
        actions=[
            Action(name="get_outbound_order_details_by_so", kwargs={"sales_order_number": "SO-2024-0008"}),
            Action(name="get_product_details", kwargs={"product_name": "Frozen Tuna Loin"}),
            Action(
                name="create_return_authorization",
                kwargs={
                    "order_id": "ORD-0008",
                    "line_items": [{"sku": "FOOD-FISH-H8", "quantity": 2400}],
                    "reason": "SPOILAGE_TEMP_BREACH"
                }
            ),
            Action(
                name="issue_customer_credit_memo",
                kwargs={
                    "order_id": "ORD-0008",
                    "customer_id": "CUST-2008",
                    "returned_items": [{"sku": "FOOD-FISH-H8", "quantity": 2400}]
                }
            ),
            Action(name="get_inventory_details", kwargs={"sku": "FOOD-FISH-H8", "warehouse_id": "WH-10"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0008", "damaged_quantity": 2400}),
            Action(name="log_supplier_performance_issue", kwargs={"supplier_id": "SUP-1010", "issue_code": "COLD_CHAIN_FAILURE_RETURN", "shipment_id": "SHIP-0010"}),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1010",
                    "line_items": [{"sku": "FOOD-FISH-H8", "quantity": 2400}],
                    "priority": "Critical"
                }
            ),
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2025-0001"}),
            Action(name="update_shipment_status", kwargs={"shipment_id": "SHIP-0031", "new_status": "Expedited", "notes": "URGENT_SPOILAGE_REPLENISHMENT"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "SPOILAGE_RETURN_RECOVERY",
                    "subject_id": "ORD-0008;RMA-1001",
                    "outcome_code": "REPLENISHMENT_INITIATED",
                    "outcome_details": {"credit_memo_id": "CM-0008", "new_po_number": "PO-2025-0001", "damaged_qty": 2400}
                }
            )
        ],
        outputs=["CM-0008", "PO-2025-0001"]
    ),
    Task(
        annotator="0",
        user_id="task_93",
        instruction="You are a Returns Supervisor. Order 'ORD-0005' to 'Epsilon Fashion Co.' is being returned due to 'Incorrect Size'. The order contained 1500 units of 'Organic Cotton T-Shirt'. Per policy, the return must go back to the origin warehouse, 'Newark Apparel Hub' (WH-04). This is a domestic return. You must use 'UPS' carrier. The final state must show: 1. An RMA is created. 2. A credit memo is issued. 3. An inbound return shipment is created for the correct warehouse and carrier. 4. The 1500 units are explicitly returned to available stock at WH-04. 5. The original order is updated to 'Returned'. Report the RMA and inbound shipment IDs.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0005"}),
            Action(name="get_product_details", kwargs={"product_name": "Organic Cotton T-Shirt"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0005", "line_items": [{"sku": "APRL-TSHT-O15", "quantity": 1500}], "reason": "Incorrect Size"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0005", "customer_id": "CUST-2005", "returned_items": [{"sku": "APRL-TSHT-O15", "quantity": 1500}]}),
            Action(name="create_inbound_return_shipment", kwargs={"rma_id": "RMA-1001", "from_customer_id": "CUST-2005", "to_warehouse_id": "WH-04", "carrier_scac": "UPSN"}),
            Action(name="get_inventory_details", kwargs={"sku": "APRL-TSHT-O15", "warehouse_id": "WH-04"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0015", "damaged_quantity": -1500}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0005", "new_status": "Returned"}),
            Action(name="log_audit_trail", kwargs={"audit_event": "DOMESTIC_RETURN_PROCESSING", "subject_id": "ORD-0005", "outcome_code": "RETURN_COMPLETE", "outcome_details": {"rma_id": "RMA-1001", "inbound_shipment_id": "SHIP-0031", "credit_memo_id": "CM-0005"}})
        ],
        outputs=["RMA-1001", "SHIP-0031"]
    ),
    Task(
        annotator="0",
        user_id="task_94",
        instruction="You are an Inventory Auditor tasked with a major inventory write-off. Two perishable products have expired: all available 'Organic Arabica Coffee Beans' (SKU FOOD-COFF-C3) at WH-05 and all available 'Frozen Tuna Loin' (SKU FOOD-FISH-H8) at WH-10. Your objective is to process this disposal and reorder replacements. The final state must show: 1. The entire available quantity of both expired products has been moved to the 'damaged' category in their respective warehouses. 2. A single new 'High' priority purchase order has been created for replacement products from our top-rated grocery supplier, 'São Paulo Coffee Exporters' (SUP-1005). The replacements are 1500 units of 'Extra Virgin Olive Oil' and 800 units of 'Argentinian Malbec Wine'. 3. A 'FINANCIAL_WRITE_OFF' audit event is logged, containing the total calculated value of the inventory loss and the new PO number. Report the new PO number and the total loss value.",
        actions=[
            Action(name="get_inventory_details", kwargs={"sku": "FOOD-COFF-C3", "warehouse_id": "WH-05"}),
            Action(name="get_inventory_details", kwargs={"sku": "FOOD-FISH-H8", "warehouse_id": "WH-10"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0003", "damaged_quantity": 5000}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0008", "damaged_quantity": 2400}),
            Action(name="get_product_details", kwargs={"product_name": "Extra Virgin Olive Oil"}),
            Action(name="get_product_details", kwargs={"product_name": "Argentinian Malbec Wine"}),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1005",
                    "line_items": [
                        {"sku": "FOOD-OLIV-V22", "quantity": 1500},
                        {"sku": "BEVG-WINE-P16", "quantity": 800}
                    ],
                    "priority": "High"
                }
            ),
            Action(name="get_purchase_order_details", kwargs={"po_number": "PO-2025-0001"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "FINANCIAL_WRITE_OFF",
                    "subject_id": "FOOD-COFF-C3;FOOD-FISH-H8",
                    "outcome_code": "DISPOSED_AND_REPLACED",
                    "outcome_details": {
                        "total_loss_value_usd": 194000.00,
                        "new_po_number": "PO-2025-0001",
                        "replenishment_shipment_id": "SHIP-0031"
                    }
                }
            )
        ],
        outputs=["PO-2025-0001", "194000.00"]
    ),
    Task(
        annotator="0",
        user_id="task_95",
        instruction="You are a Risk Manager. We've received a critical alert that 'DHL Express' has a temporary lapse in their international insurance coverage. Order 'ORD-0002', a high-value shipment to 'Beta Retail GmbH' currently 'In Transit' with this carrier, is at risk. Your objective is to mitigate this immediately. The final state must show: 1. The carrier 'DHL Express' has its status updated to 'On Hold - Insurance Lapse'. 2. The at-risk order 'ORD-0002' is reassigned mid-transit to the best-performing alternative 'Air' carrier. 3. The order's status is updated to 'In Transit - Carrier Reassigned'. 4. A note with the code 'ALERT:ORD-0002_CARRIER_REASSIGNED_TO_UPSN' is added to the origin warehouse ('Seattle Fulfillment Center'). 5. The entire incident is logged in the audit trail with the event code 'CARRIER_RISK_MITIGATION', outcome code 'CARRIER_REASSIGNED_SUCCESS', and reason code 'INSURANCE_LAPSE'. Report the new tracking number for the shipment.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0002"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "DHL Express"}),
            Action(name="update_carrier_status", kwargs={"carrier_name": "DHL Express", "status": "On Hold - Insurance Lapse"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="reassign_order_carrier", kwargs={"order_id": "ORD-0002", "new_carrier_scac": "UPSN"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0002", "new_status": "In Transit - Carrier Reassigned"}),
            Action(name="update_warehouse_notes", kwargs={"warehouse_id": "WH-02", "notes": "ALERT:ORD-0002_CARRIER_REASSIGNED_TO_UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "CARRIER_RISK_MITIGATION",
                    "subject_id": "ORD-0002",
                    "outcome_code": "CARRIER_REASSIGNED_SUCCESS",
                    "outcome_details": {
                        "original_carrier_scac": "DHLG",
                        "new_carrier_scac": "UPSN",
                        "reason_code": "INSURANCE_LAPSE"
                    }
                }
            )
        ],
        outputs=["UPSN-0002"]
    ),
    Task(
        annotator="0",
        user_id="task_96",
        instruction="You are a Fulfillment Manager resolving a stock deadlock. A 'Critical' priority order has arrived from 'Zeta Tech Solutions' located in Yokohama for 10,000 '8-bit Microcontrollers' to ship from WH-01. However, 12,500 units at WH-01 are currently allocated to a 'Low' priority order, 'ORD-0001', for 'Alpha Electronics LLC'. Policy dictates you must cancel the low-priority order to free up stock. You must then ensure the original quantity of 12,500 units from 'ORD-0001' is re-fulfilled: 10,000 units for 'Zeta Tech Solutions' as the new 'Critical' order, and the remaining 2,500 units as a new 'Low' priority order for 'Alpha Electronics LLC' shipped from the next best warehouse (WH-03) using the best 'Truck' carrier. The new 'Critical' order for 'Zeta Tech Solutions' must be shipped from WH-01 using the best 'Air' carrier. The final state must show: 1. Order 'ORD-0001' is 'Cancelled'. 2. A new 'Low' priority order for 'Alpha Electronics' of 2,500 units is created and shipped from WH-03. 3. The new 'Critical' order for 'Zeta Tech Solutions' of 10,000 units is created and shipped from WH-01. 4. An audit trail with event 'DEADLOCK_RESOLUTION_REASSIGN' is logged. Report the tracking numbers for the new Critical order and the new Low-priority order.",
        actions=[
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0001"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0001", "new_status": "Cancelled"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-03"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Low",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 2500}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Truck"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Zeta Tech Solutions",
                    "destination_city": "Yokohama",
                    "priority_level": "Critical",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 10000}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0018", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "DEADLOCK_RESOLUTION_REASSIGN",
                    "subject_id": "ORD-0018",
                    "outcome_code": "SUCCESS",
                    "outcome_details": {
                        "cancelled_order_id": "ORD-0001",
                        "reassigned_order_id": "ORD-0017"
                    }
                }
            )
        ],
        outputs=["UPSN-0018", "UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_97",
        instruction="You are a Carrier Relations Manager. A critical service alert has been issued for 'DB Schenker': their 'EuroCargo' rail service has been suspended. Order 'ORD-0009' for 'Iota Automotive SAS' is currently 'In Transit' to Lyon using this exact service. Your objective is to mitigate this disruption. The final state must show: 1. The 'DB Schenker' carrier status is updated to 'Partial Service Suspension'. 2. The order is reassigned to the best-performing alternative 'Rail' carrier. 3. The order's status is updated to 'In Transit - Reassigned'. 4. A detailed audit is logged with the event code 'SERVICE_DISRUPTION_MITIGATION' and outcome code 'CARRIER_REASSIGNED'. Report the new tracking number.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0009"}),
            Action(name="get_carrier_details", kwargs={"carrier_name": "DB Schenker"}),
            Action(name="update_carrier_status", kwargs={"carrier_name": "DB Schenker", "status": "Partial Service Suspension"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Rail"}),
            Action(name="reassign_order_carrier", kwargs={"order_id": "ORD-0009", "new_carrier_scac": "KNLU"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0009", "new_status": "In Transit - Reassigned"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "SERVICE_DISRUPTION_MITIGATION",
                    "subject_id": "ORD-0009",
                    "outcome_code": "CARRIER_REASSIGNED",
                    "outcome_details": {
                        "original_carrier_scac": "DBSK",
                        "new_carrier_scac": "KNLU",
                        "reason": "SERVICE_SUSPENSION"
                    }
                }
            )
        ],
        outputs=["KNLU-0009"]
    ),
    Task(
        annotator="0",
        user_id="task_98",
        instruction="You are a Kitting Fulfillment Lead. A 'Critical' priority order for 20 'Basic Robotic Starter Kits' is placed for 'Alpha Electronics LLC' to be shipped to San Jose. The fulfillment warehouse, 'Chicago Parts Depot' (WH-03), has all 20 required 'Articulated Robotic Arms' but only 30 of the 40 required 'Lithium-Ion Battery Packs'. Per policy for critical orders, you must ship what is available immediately and backorder the rest. The shipment must use 'Air' transport. Your objective is to manage this split fulfillment. The final state must show: 1. An outbound order for the partial kit (20 arms, 30 batteries) is created and shipped. 2. A separate backorder for the remaining 10 batteries is created with status 'Pending - Awaiting Stock'. 3. An audit log is created with event code 'KIT_FULFILLMENT_SPLIT' and the exact outcome code 'PARTIAL_KIT_SHIPPED'. Report the tracking number for the partial shipment and the ID for the backorder.",
        actions=[
            Action(name="get_kit_components", kwargs={"kit_name": "Basic Robotic Starter Kit"}),
            Action(name="get_product_details", kwargs={"product_name": "Articulated Robotic Arm"}),
            Action(name="get_product_details", kwargs={"product_name": "Lithium-Ion Battery Pack"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-ROBO-N14", "warehouse_id": "WH-03"}),
            Action(name="get_inventory_details", kwargs={"sku": "TECH-BATT-Q17", "warehouse_id": "WH-03"}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC", "destination_city": "San Jose", "priority_level": "Critical",
                    "line_items": [{"sku": "TECH-ROBO-N14", "quantity": 20}, {"sku": "TECH-BATT-Q17", "quantity": 30}]
                }
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Alpha Electronics LLC", "destination_city": "San Jose", "priority_level": "Critical",
                    "line_items": [{"sku": "TECH-BATT-Q17", "quantity": 10}]
                }
            ),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0018", "new_status": "Pending - Awaiting Stock"}),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-03", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "KIT_FULFILLMENT_SPLIT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "PARTIAL_KIT_SHIPPED",
                    "outcome_details": {"backorder_id": "ORD-0018"}
                }
            )
        ],
        outputs=["UPSN-0017", "ORD-0018"]
    ),
    Task(
        annotator="0",
        user_id="task_99",
        instruction="You are a Proactive Risk Manager. A general port strike has been announced for all of California, affecting all 'Sea' freight. Order 'ORD-0006' for 'Zeta Tech Solutions' (containing 900 units of '8-bit Microcontroller') is 'Shipped' from San Francisco (WH-05) via 'Maersk' but has not yet departed. Your objective is to proactively prevent a delay. The final state must show: 1. The original order 'ORD-0006' is cancelled using the status 'Cancelled - Force Majeure'. 2. The 900 units are returned to available stock at the Los Angeles Distribution Center (WH-01). 3. A new 'Critical' priority order is created for the same items. 4. The new order is shipped via the best available 'Air' carrier. 5. An audit is logged with event 'PROACTIVE_REROUTE' and outcome 'SUCCESS'. Report the new tracking number.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0006"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0006", "new_status": "Cancelled - Force Majeure"}),
            Action(name="get_product_details", kwargs={"product_name": "8-bit Microcontroller"}),
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0001", "damaged_quantity": -900}),
            Action(
                name="create_outbound_order",
                kwargs={
                    "customer_name": "Zeta Tech Solutions", "destination_city": "Yokohama", "priority_level": "Critical",
                    "line_items": [{"sku": "ELEC-CHIP-A1", "quantity": 900}]
                }
            ),
            Action(name="list_carriers_by_mode", kwargs={"mode": "Air"}),
            Action(name="ship_outbound_order", kwargs={"order_id": "ORD-0017", "warehouse_id": "WH-01", "carrier_scac": "UPSN"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "PROACTIVE_REROUTE", "subject_id": "ORD-0006", "outcome_code": "SUCCESS",
                    "outcome_details": {"new_order_id": "ORD-0017"}
                }
            )
        ],
        outputs=["UPSN-0017"]
    ),
    Task(
        annotator="0",
        user_id="task_100",
        instruction="You are a Finance Returns Auditor for an incident with 'Gamma Construction Ltd.' and order 'ORD-0003'. They returned 100 'Ceramic Floor Tiles'. Inspection revealed 85 are undamaged and 15 are broken. Per policy, credit is issued only for undamaged items. Your objective is to process this split return and its full financial impact. The final state must show: 1. An RMA is created with reason 'SPLIT_RETURN_DAMAGED'. 2. A credit memo is issued for only the 85 undamaged tiles. 3. Inventory is updated at WH-12 (85 restocked, 15 damaged). 4. A 'FINANCIAL_RECONCILIATION' audit is logged with outcome 'RETURN_PROCESSED', detailing the credited value and the inventory loss value (cost of damaged goods). Report the total credited value and the inventory loss value.",
        actions=[
            Action(name="get_outbound_order_details", kwargs={"order_id": "ORD-0003"}),
            Action(name="get_product_details", kwargs={"product_name": "Ceramic Floor Tile"}),
            Action(name="create_return_authorization", kwargs={"order_id": "ORD-0003", "line_items": [{"sku": "BLDG-TILE-J10", "quantity": 100}], "reason": "SPLIT_RETURN_DAMAGED"}),
            Action(name="issue_customer_credit_memo", kwargs={"order_id": "ORD-0003", "customer_id": "CUST-2003", "returned_items": [{"sku": "BLDG-TILE-J10", "quantity": 85}]}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": -85}),
            Action(name="update_inventory_damage_status", kwargs={"inventory_id": "INV-0010", "damaged_quantity": 15}),
            Action(name="get_credit_memo_details", kwargs={"credit_memo_id": "CM-0003"}),
            Action(
                name="log_audit_trail",
                kwargs={
                    "audit_event": "FINANCIAL_RECONCILIATION",
                    "subject_id": "CM-0003",
                    "outcome_code": "RETURN_PROCESSED",
                    "outcome_details": {"credited_value_usd": 510.00, "inventory_loss_usd": 52.50}
                }
            )
        ],
        outputs=["510.00", "52.50"]
    )
]
