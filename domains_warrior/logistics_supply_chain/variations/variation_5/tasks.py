from domains.dto import Action, Task
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
time_now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

TASKS = [

        Task(
        annotator="0",
        user_id="V5TSK_USR_1",
        instruction="""Korean textile quality audit for supplier SUP-1004. Get supplier performance rating,
        get inventory details for SKU MATR-COTT-R18 in warehouse WH-04, quarantine inventory lot LOT202404D in WH-04 for reason
        "quality_audit", perform physical count, create inventory adjustment with quantity -5 and reason "audit_samples",
        create incident report with type "quality_audit" and severity "low" for shipment SHIP-0004, notify supplier with type "audit_notification",
        calculate financial impact with textile value 160000 and audit cost 4200. Get notification status and incident ID,""",
        actions=[
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1004"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202404D",
                    "warehouse_id": "WH-04",
                    "reason": "quality_audit"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-04",
                    "sku": "MATR-COTT-R18"
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "adjustment_quantity": -5,
                    "reason": "audit_samples"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0004",
                    "incident_type": "quality_audit",
                    "severity": "low"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1004",
                    "notification_type": "audit_notification"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 160000,
                    "liability_estimate": 4200
                }
            )
        ],
        outputs=[
            '"incident_id": "INC-SHIP-0004-low"',
            '"notification_status": "Sent"',
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_2",
        instruction="""Critical electronics shortage alert: Our main customer Apple has increased their Q4 order by 40%,
        requiring immediate restocking of 8-bit microcontrollers. Current LA warehouse stock shows only 2 weeks remaining.
        Evaluate supplier SUP-1001 performance, expedite 5000 units of ELEC-CHIP-A1 to WH-01 with medium priority.
        Our supplier relationship manager reports they're offering a 10% volume bonus (500 extra units) due to our loyalty.
        Conduct full inventory verification including physical count and warehouse
        utilization analysis to ensure we can handle the increased volume. Calculate total investment including the $22,500
        chip value and $2,750 rush processing fees.""",
        actions=[
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1001"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1001",
                    "sku": "ELEC-CHIP-A1",
                    "quantity": 5000,
                    "destination_warehouse": "WH-01",
                    "priority": "Medium"
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
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                }
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "adjustment_quantity": 500,
                    "reason": "supplier_bonus"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 22500,
                    "liability_estimate": 2750
                }
            )
        ],
        outputs=[
            '"supplier_performance_rating": 4.6',
            '"total_chip_investment": 25250'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_3",
        instruction="""Quality crisis escalation: BMW Munich has rejected our latest brake pad shipment of SKU AUTO-PAD-B2 due
        to inconsistent friction coefficients. They're threatening to source from our competitor unless we provide immediate
        quality verification. Our supplier SUP-1003 in Berlin claims the issue is with storage conditions, not manufacturing.
        Quarantine all brake pads from lot LOT202403B in our Chicago facility WH-03 immediately with reason "BMW quality verification pending".
        Take 8 sets for comprehensive testing labs with physical count 792 and verify our storage meets automotive standards with compliance required.
        Document everything for the BMW audit next week. Total brake pad inventory value is $36000 with $1200 in emergency testing costs.""",

        actions=[
            Action(name="get_supplier_performance", kwargs={"supplier_id": "SUP-1003"}),
            Action(name="get_inventory_details", kwargs={"sku": "AUTO-PAD-B2", "warehouse_id": "WH-03"}),
            Action(name="quarantine_inventory", kwargs={"lot_number": "LOT202403B", "warehouse_id": "WH-03", "reason": "BMW quality verification pending"}),
            Action(name="perform_physical_count", kwargs={"sku": "AUTO-PAD-B2", "warehouse_id": "WH-03", "instruction_amount": 792}),
            Action(name="create_inventory_adjustment", kwargs={"sku": "AUTO-PAD-B2", "warehouse_id": "WH-03", "adjustment_quantity": -8}),
            Action(name="verify_storage_compliance", kwargs={"warehouse_id": "WH-03", "storage_type": "automotive", "compliant_flag": True}),
            Action(name="update_accuracy_metrics", kwargs={"warehouse_id": "WH-03"}),
            Action(name="calculate_financial_impact", kwargs={"product_value": 36000, "liability_estimate": 1200})
        ],

        outputs=[
            '"supplier_performance_rating": 4.7',
            '"total_quality_cost": 37200'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_4",
        instruction="""Electronics shortage crisis: SKU ELEC-CHIP-A1 critically low at Los Angeles WH-01 with only 15000 available units.
        Get inventory details for SKU ELEC-CHIP-A1 in warehouse WH-01. Get warehouse capacity for WH-01 to assess space constraints.
        Search inbound shipments for SKU ELEC-CHIP-A1 to destination warehouse WH-01 to check incoming stock. Get approved suppliers
        for SKU ELEC-CHIP-A1. Get supplier SUP-1001 performance rating. Create emergency purchase order for quantity 25000 units
        to supplier SUP-1001 for warehouse WH-01 with priority Critical and notes "Emergency replenishment - customer backorders critical".
        Get carrier performance for MAEU. Select optimal carrier for destination Los Angeles, USA with priority Critical and weight 5000 kg.
        Request shipping quote from MAEU for 5000 kg shipment to Los Angeles. Generate shipping labels for existing order ORD-0001
        using carrier MAEU. Perform physical count for SKU ELEC-CHIP-A1 in warehouse WH-01. Calculate inventory variance using system
        count 15000 and physical count 14888. Create inventory adjustment for quantity -112 with reason "Emergency count correction
        for accurate reordering". Update accuracy metrics for warehouse WH-01. Get order details for ORD-0001 to verify customer impact.
        Update order status for ORD-0001 to "Backordered". Report emergency order status, variance percentage, and estimated delivery cost.""",

        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="search_inbound_shipments",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "destination_warehouse_id": "WH-01"
                }
            ),
            Action(
                name="get_approved_suppliers",
                kwargs={"sku": "ELEC-CHIP-A1"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1001"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "quantity": 25000,
                    "supplier_id": "SUP-1001",
                    "sku": "ELEC-CHIP-A1",
                    "destination_warehouse": "WH-01",
                    "priority": "Critical",
                    "notes": "Emergency replenishment - customer backorders critical"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "MAEU"}
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_city": "Los Angeles",
                    "destination_country": "USA",
                    "priority_level": "Critical",
                    "total_weight_kg": 5000
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "MAEU",
                    "weight_kg": 5000,
                    "destination": "Los Angeles"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0001",
                    "carrier_scac": "MAEU"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "system_count": 15000,
                    "physical_count": 14888
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "adjustment_quantity": -112,
                    "reason": "Emergency count correction for accurate reordering"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0001"}
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0001",
                    "new_status": "Backordered"
                }
            )
        ],

        outputs=[
            '"emergency_order_status": "Created"',
            '"variance_percentage": 0.75',
            '"estimated_delivery_cost": 12500'
        ]
    ),

    Task(
            annotator="0",
            user_id="V5TSK_USR_5",
            instruction="""Process critical stock shortage alert for pharmaceutical SKU PHRM-DRUG-S19 in warehouse WH-06.
            Get current inventory details, verify supplier SUP-1021 performance rating, create urgent purchase order for 1000
            units with High priority and note "Critical patient medication shortage - expedite processing".
            Check incoming shipments for this SKU to WH-06, quarantine existing inventory with lot number LOT202405H for
            reason "Batch verification pending regulatory approval", create incident report with severity "high", notify
            supplier SUP-1021 about quality concern, and calculate total financial impact with product value 600000 and '
            liability estimate 100000. Report purchase order number and total financial impact.""",

            actions=[
                Action(name="get_inventory_details", kwargs={"sku": "PHRM-DRUG-S19", "warehouse_id": "WH-06"}),
                Action(name="get_supplier_performance", kwargs={"supplier_id": "SUP-1021"}),
                Action(name="create_purchase_order", kwargs={"supplier_id": "SUP-1021", "sku": "PHRM-DRUG-S19", "quantity": 1000,
                                                            "destination_warehouse": "WH-06", "priority": "High",
                                                            "notes": "Critical patient medication shortage - expedite processing"}),
                Action(name="search_inbound_shipments", kwargs={"sku": "PHRM-DRUG-S19", "destination_warehouse_id": "WH-06"}),
                Action(name="quarantine_inventory", kwargs={"lot_number": "LOT202405H", "warehouse_id": "WH-06", "reason": "Batch verification pending regulatory approval"}),
                Action(name="create_incident_report", kwargs={"id": "PHRM-DRUG-S19", "incident_type": "quality_concern", "severity": "high"}),
                Action(name="notify_supplier", kwargs={"supplier_id": "SUP-1021", "notification_type": "quality_incident"}),
                Action(name="calculate_financial_impact", kwargs={"product_value": 600000, "liability_estimate": 100000})
            ],

            outputs=['"purchase_order_number": "PO-SUP-1021-PHRM-DRUG-S19-001"',
                    '"total_financial_impact": 700000']
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_6",
        instruction="""Process temperature-sensitive shipment emergency for SHIP-0006 containing SKU
        PHRM-VACC-D4 from supplier SUP-1006 to warehouse WH-06. Get shipment details, check temperature logs against
        required range 2-8C, quarantine inventory with lot number LOT202406A in warehouse WH-06 for reason
        "Cold chain verification pending investigation". Get supplier SUP-1006 performance rating, create supplier
        improvement plan with review cycle 60 days, create incident report type "cold_chain_breach" with severity "high",
        notify supplier SUP-1006 with notification type "quality_incident", and calculate financial impact with product
        value 310000 and liability estimate 25000. Report incident ID and total financial exposure.""",

        actions=[
            Action(name="get_shipment_details", kwargs={"shipment_id": "SHIP-0006"}),
            Action(name="check_temperature_logs", kwargs={"shipment_id": "SHIP-0006", "required_temp_range": "2-8C"}),
            Action(name="quarantine_inventory", kwargs={"lot_number": "LOT202406A", "warehouse_id": "WH-06", "reason":
                                                        "Cold chain verification pending investigation"}),
            Action(name="get_supplier_performance", kwargs={"supplier_id": "SUP-1006"}),
            Action(name="create_supplier_improvement_plan", kwargs={"supplier_id": "SUP-1006", "review_cycle_days": 60}),
            Action(name="create_incident_report", kwargs={"id": "SHIP-0006", "incident_type": "cold_chain_breach", "severity": "high"}),
            Action(name="notify_supplier", kwargs={"supplier_id": "SUP-1006", "notification_type": "quality_incident"}),
            Action(name="calculate_financial_impact", kwargs={"product_value": 310000, "liability_estimate": 25000})
        ],

        outputs=[
            '"incident_id": "INC-SHIP-0006-high"',
            '"total_financial_impact": 335000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_7",
        instruction="""Emergency procurement for critical shortage of SKU TECH-SOLR-G7 in warehouse WH-09.
        Get inventory details for SKU TECH-SOLR-G7 in warehouse WH-09, get supplier SUP-1009 performance rating,
        create purchase order for 500 units with Critical priority and note "Solar panel emergency replenishment for grid project".
        Check incoming shipments for this SKU to WH-09, update accuracy metrics for warehouse WH-09, calculate financial
        impact with product value 149995 and liability estimate 5000. Report purchase order ID and current incoming inventory.""",

        actions=[
            Action(name="get_inventory_details", kwargs={"sku": "TECH-SOLR-G7", "warehouse_id": "WH-09"}),
            Action(name="get_supplier_performance", kwargs={"supplier_id": "SUP-1009"}),
            Action(name="create_purchase_order", kwargs={"supplier_id": "SUP-1009", "sku": "TECH-SOLR-G7",
                                                         "quantity": 500, "destination_warehouse": "WH-09",
                                                         "priority": "Critical", "notes": "Solar panel emergency replenishment for grid project"}),
            Action(name="search_inbound_shipments", kwargs={"sku": "TECH-SOLR-G7", "destination_warehouse_id": "WH-09"}),
            Action(name="update_accuracy_metrics", kwargs={"warehouse_id": "WH-09"}),
            Action(name="calculate_financial_impact", kwargs={"product_value": 149995, "liability_estimate": 5000})
        ],

        outputs=[
            '"po_id": "PO-SUP-1009-TECH-SOLR-G7-001"',
            '"current_incoming_inventory": 600'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_8",
        instruction="""Process building materials order ORD-0003 containing SKU BLDG-TILE-J10 from warehouse WH-12.
        Get order details, get inventory details for SKU BLDG-TILE-J10 in warehouse WH-12, quarantine inventory with lot number LOT202404A
        in warehouse WH-12 for reason "Customer return quality investigation". Create incident report for order ORD-0003 with
        incident type "customer_return" and severity "medium", get supplier SUP-1012 performance rating, notify supplier SUP-1012
        with notification type "quality_incident". Report incident ID and quarantine confirmation.""",

        actions=[
            Action(name="get_order_details", kwargs={"order_id": "ORD-0003"}),
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="quarantine_inventory", kwargs={"lot_number": "LOT202404A", "warehouse_id": "WH-12", "reason":
                                                        "Customer return quality investigation"}),
            Action(name="create_incident_report", kwargs={"id": "ORD-0003", "incident_type": "customer_return", "severity": "medium"}),
            Action(name="get_supplier_performance", kwargs={"supplier_id": "SUP-1012"}),
            Action(name="notify_supplier", kwargs={"supplier_id": "SUP-1012", "notification_type": "quality_incident"})
        ],

        outputs=[
            '"incident_id": "INC-ORD-0003-medium"',
            '"quarantine_confirmation": "Quarantined"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_9",
        instruction="""Process damaged inventory discovery for SKU BLDG-TILE-J10 in warehouse WH-12 from supplier SUP-1012.
        Get inventory details for SKU BLDG-TILE-J10 in warehouse WH-12, quarantine inventory with lot number LOT202404A in
        warehouse WH-12 for reason "Damage assessment pending quality inspection". Get supplier SUP-1012 performance rating,
        create supplier improvement plan with review cycle 90 days, create incident report with severity "medium" with incident type "product_damage",
        notify supplier SUP-1012 with notification type "quality_incident", calculate financial impact with product value 63000 and liability estimate 8000.
        Report quarantine status and total financial impact.""",

        actions=[
            Action(name="get_inventory_details", kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}),
            Action(name="quarantine_inventory", kwargs={"lot_number": "LOT202404A", "warehouse_id": "WH-12", "reason": "Damage assessment pending quality inspection"}),
            Action(name="get_supplier_performance", kwargs={"supplier_id": "SUP-1012"}),
            Action(name="create_supplier_improvement_plan", kwargs={"supplier_id": "SUP-1012", "review_cycle_days": 90}),
            Action(name="create_incident_report", kwargs={"id": "BLDG-TILE-J10", "incident_type": "product_damage", "severity": "medium"}),
            Action(name="notify_supplier", kwargs={"supplier_id": "SUP-1012", "notification_type": "quality_incident"}),
            Action(name="calculate_financial_impact", kwargs={"product_value": 63000, "liability_estimate": 8000})
        ],

        outputs=[
            '"quarantine_status": "Quarantined"',
            '"total_financial_impact": 71000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_10",
        instruction="""Critical inventory adjustment required for SKU CHEM-SOLV-K11 in warehouse WH-13 after
            physical count discrepancy. Get inventory details for SKU CHEM-SOLV-K11 in warehouse WH-13, create inventory
            adjustment with quantity -20 for reason "Physical count correction after audit variance", get supplier SUP-1013
            performance rating, create incident report with severity "low", incident type "inventory_variance" and id 'CHEM-SOLV-K11',
            notify supplier SUP-1013 with notification type "quality_incident",
            search inbound shipments for SKU CHEM-SOLV-K11 to warehouse WH-13, update accuracy metrics for warehouse WH-13, calculate
            financial impact with product value 60000 and liability estimate 1500. Report adjustment value and updated quantity.""",

        actions=[
            Action(name="get_inventory_details", kwargs={"sku": "CHEM-SOLV-K11", "warehouse_id": "WH-13"}),
            Action(name="create_inventory_adjustment", kwargs={"sku": "CHEM-SOLV-K11", "warehouse_id": "WH-13", "adjustment_quantity": -20, "reason": "Physical count correction after audit variance"}),
            Action(name="get_supplier_performance", kwargs={"supplier_id": "SUP-1013"}),
            Action(name="create_incident_report", kwargs={"id": "CHEM-SOLV-K11", "incident_type": "inventory_variance", "severity": "low"}),
            Action(name="notify_supplier", kwargs={"supplier_id": "SUP-1013", "notification_type": "quality_incident"}),
            Action(name="search_inbound_shipments", kwargs={"sku": "CHEM-SOLV-K11", "destination_warehouse_id": "WH-13"}),
            Action(name="update_accuracy_metrics", kwargs={"warehouse_id": "WH-13"}),
            Action(name="calculate_financial_impact", kwargs={"product_value": 60000, "liability_estimate": 1500})
        ],

        outputs=[
            '"adjustment_value": 3000',
            '"updated_quantity": 380'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_11",
        instruction="""Critical pharmaceutical cold chain emergency for shipment SHIP-0006 containing SKU PHRM-VACC-D4 from
        supplier SUP-1006 to warehouse WH-06. Get shipment details, check temperature logs against required range 2-8C with excursions
        flag true, verify cold chain integrity with carrier UAE, quarantine inventory with lot number LOT202406A in warehouse WH-06 for
        reason "Cold chain breach investigation pending", get supplier SUP-1006 performance rating, create supplier improvement
        plan with review cycle 90 days, initiate product recall for lot number LOT202406A with recall type "precautionary",
        create incident report with severity "critical" with incident type "cold_chain_breach", notify supplier SUP-1006 with notification type "quality_incident",
        calculate financial impact with product value 310000 and liability estimate 50000, escalate to quality team
        with priority "critical". Report recall ID and total financial impact.""",

        actions=[
            Action(name="get_shipment_details", kwargs={"shipment_id": "SHIP-0006"}),
            Action(name="check_temperature_logs", kwargs={"shipment_id": "SHIP-0006", "required_temp_range": "2-8C", "excursions_flag": True}),
            Action(name="verify_cold_chain_integrity", kwargs={"shipment_id": "SHIP-0006", "carrier_scac": "UAE"}),
            Action(name="quarantine_inventory", kwargs={"lot_number": "LOT202406A", "warehouse_id": "WH-06", "reason": "Cold chain breach investigation pending"}),
            Action(name="get_supplier_performance", kwargs={"supplier_id": "SUP-1006"}),
            Action(name="create_supplier_improvement_plan", kwargs={"supplier_id": "SUP-1006", "review_cycle_days": 90}),
            Action(name="initiate_product_recall", kwargs={"lot_number": "LOT202406A", "recall_type": "precautionary"}),
            Action(name="create_incident_report", kwargs={"id": "SHIP-0006", "incident_type": "cold_chain_breach", "severity": "critical"}),
            Action(name="notify_supplier", kwargs={"supplier_id": "SUP-1006", "notification_type": "quality_incident"}),
            Action(name="calculate_financial_impact", kwargs={"product_value": 310000, "liability_estimate": 50000}),
            Action(name="escalate_to_quality_team", kwargs={"incident_id": "INC-SHIP-0006-critical", "priority": "critical"})
        ],

        outputs=[
            '"recall_id": "RCL-LOT202406A-precautionary"',
            '"total_financial_impact": 360000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_12",
        instruction="""Complex international customs processing for shipment
        SHIP-0023 containing SKU AUTO-GLAS-U21 from supplier SUP-1023 to warehouse WH-03.
        Get shipment details, verify customs documentation completeness, calculate customs duty for total
        value 95000 from origin country Mexico, process duty payment amount of 0, update customs status to "Cleared",
        update shipment status to "Ready for Receipt", get supplier SUP-1023 performance rating, verify storage compliance
        for warehouse WH-03 with storage type "fragile" and compliant flag true, get carrier performance for UPSN, update
        accuracy metrics for warehouse WH-03, calculate financial impact with product value 95000 and liability estimate 3000. Report
        customs status and storage compliance status.""",

        actions=[
            Action(name="get_shipment_details", kwargs={"shipment_id": "SHIP-0023"}),
            Action(name="verify_customs_documentation", kwargs={"shipment_id": "SHIP-0023"}),
            Action(name="calculate_customs_duty", kwargs={"shipment_id": "SHIP-0023", "total_value": 95000, "country_of_origin": "Mexico"}),
            Action(name="process_duty_payment", kwargs={"shipment_id": "SHIP-0023", "duty_amount": 0}),
            Action(name="update_customs_status", kwargs={"shipment_id": "SHIP-0023", "status": "Cleared"}),
            Action(name="update_shipment_status", kwargs={"shipment_id": "SHIP-0023", "status": "Ready for Receipt"}),
            Action(name="get_supplier_performance", kwargs={"supplier_id": "SUP-1023"}),
            Action(name="verify_storage_compliance", kwargs={"warehouse_id": "WH-03", "storage_type": "fragile", "compliant_flag": True}),
            Action(name="get_carrier_performance", kwargs={"carrier_scac": "UPSN"}),
            Action(name="update_accuracy_metrics", kwargs={"warehouse_id": "WH-03"}),
            Action(name="calculate_financial_impact", kwargs={"product_value": 95000, "liability_estimate": 3000})
        ],

        outputs=[
            '"customs_status": "Cleared"',
            '"storage_compliance_status": "compliant"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_13",
        instruction="""Multi-phase inventory management crisis for SKU ELEC-CHIP-A1 in warehouse WH-01 from supplier SUP-1001.
        Get inventory details for SKU ELEC-CHIP-A1 in warehouse WH-01, perform physical count with sku ELEC-CHIP-A1,
        warehouse WH-01, and physical count 14500, calculate inventory variance for sku ELEC-CHIP-A1 with system count 15000
        and physical count 14500, create inventory adjustment with sku ELEC-CHIP-A1, warehouse WH-01, adjustment quantity -500,
        and reason "Physical count variance correction", search inbound shipments for sku ELEC-CHIP-A1 to warehouse WH-01,
        get supplier SUP-1001 performance rating, create supplier improvement plan with review cycle 60 days,
        create incident report with severity "medium" with reason "inventory_variance",
        notify supplier SUP-1001 with notification type "quality_incident",
        update accuracy metrics for warehouse WH-01, calculate financial impact with product value 37500 and liability estimate
        2500, get approved suppliers for sku ELEC-CHIP-A1. Report adjustment value and total expected stock.""",

        actions=[
            Action(name="get_inventory_details", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}),
            Action(name="perform_physical_count", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01",
                                                          "instruction_amount": 14500}),
            Action(name="calculate_inventory_variance", kwargs={"sku": "ELEC-CHIP-A1", "system_count": 15000, "physical_count": 14500}),
            Action(name="create_inventory_adjustment", kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01", "adjustment_quantity": -500, "reason": "Physical count variance correction"}),
            Action(name="search_inbound_shipments", kwargs={"sku": "ELEC-CHIP-A1", "destination_warehouse_id": "WH-01"}),
            Action(name="get_supplier_performance", kwargs={"supplier_id": "SUP-1001"}),
            Action(name="create_supplier_improvement_plan", kwargs={"supplier_id": "SUP-1001", "review_cycle_days": 60}),
            Action(name="create_incident_report", kwargs={"id": "ELEC-CHIP-A1", "incident_type": "inventory_variance", "severity": "medium"}),
            Action(name="notify_supplier", kwargs={"supplier_id": "SUP-1001", "notification_type": "quality_incident"}),
            Action(name="update_accuracy_metrics", kwargs={"warehouse_id": "WH-01"}),
            Action(name="calculate_financial_impact", kwargs={"product_value": 37500, "liability_estimate": 2500}),
            Action(name="get_approved_suppliers", kwargs={"sku": "ELEC-CHIP-A1"})
        ],

        outputs=[
            '"adjustment_value": 1250',
            '"total_expected_stock": 17000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_14",
        instruction="""Food safety inspection alert for coffee inventory at Houston warehouse WH-05.
        Check current inventory levels for SKU FOOD-COFF-C3 in warehouse WH-05. Get supplier SUP-1024 performance rating.
        Perform physical count with instruction amount 4980. Calculate inventory variance between system count 5000 and physical count 4980.
        Create inventory adjustment with quantity -20 for reason "Food safety inspection variance".
        Create purchase order from supplier SUP-1024 for 1000 units at $35 FOOD-COFF-C3 to warehouse WH-05 with priority Medium.
        Report adjustment value and supplier rating.""",

        actions=[
            Action(
                name="get_inventory_by_sku_warehouse",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={
                    "supplier_id": "SUP-1024"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "instruction_amount": 4980
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "system_count": 5000,
                    "physical_count": 4980
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "adjustment_quantity": -20,
                    "reason": "Food safety inspection variance"
                }
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1024",
                    "sku": "FOOD-COFF-C3",
                    "quantity": 1000,
                    "destination_warehouse": "WH-05",
                    "priority": "Medium",
                    "unit_price": 35.00
                }
            )
        ],

        outputs=[
            '"adjustment_value": 440.00',
            '"supplier_rating": 4.7'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_15",
        instruction="""Critical pharmaceutical shipment inspection for vaccine storage at Atlanta cold chain center WH-06.
        Check inventory levels for SKU PHRM-VACC-D4 in warehouse WH-06. Get supplier SUP-1020 performance rating. Request
        shipping quotes from carriers FDEG and UAE for weight 1800 kg to destination Atlanta, USA. Select UAE as carrier
        for destination country USA with priority Critical and weight 1800 kg. Perform physical count with instruction amount 19980 against system baseline 20000.
        Calculate inventory variance between system count 20000 and physical count 19980. Create inventory adjustment with quantity -20 for
        reason "Cold chain verification variance" with unit cost 15.50 per unit. Report selected carrier and monetary adjustment value.""",

        actions=[
            Action(
                name="get_inventory_by_sku_warehouse",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={
                    "supplier_id": "SUP-1020"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "FDEG",
                    "weight_kg": 1800,
                    "destination": "Atlanta, USA"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "UAE",
                    "weight_kg": 1800,
                    "destination": "Atlanta, USA"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "USA",
                    "priority_level": "Critical",
                    "total_weight_kg": 1800,
                    "carriers_list": ["FDEG", "UAE"]
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "instruction_amount": 19980
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "system_count": 20000,
                    "physical_count": 19980
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "adjustment_quantity": -20,
                    "reason": "Cold chain verification variance"
                }
            )
        ],

        outputs=[
            '"selected_carrier": "UAE"',
            '"adjustment_value": 310.00'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_16",
        instruction="""Process construction materials order ORD-0003 for Denver customer Gamma
        Construction Ltd. Get order details showing 6200 kg shipment from Miami warehouse WH-12. Verify inventory allocation for order.
        Get warehouse capacity status for WH-12. Get supplier SUP-1012 performance rating. Request shipping quote from FDEG carrier for
        6200 kg to destination Denver, USA. Generate shipping labels using FDEG carrier. Update order status to Shipped.
        Report customer name and shipping cost estimate.""",

        actions=[
            Action(
                name="get_order_details",
                kwargs={
                    "order_id": "ORD-0003"
                }
            ),
            Action(
                name="verify_inventory_allocation",
                kwargs={
                    "order_id": "ORD-0003"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={
                    "warehouse_id": "WH-12"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={
                    "supplier_id": "SUP-1012"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "FDEG",
                    "weight_kg": 6200,
                    "destination": "Denver, USA"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0003",
                    "carrier_scac": "FDEG"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0003",
                    "new_status": "Shipped"
                }
            )
        ],

        outputs=[
            '"customer_name": "Gamma Construction Ltd."',
            '"shipping_cost_estimate": 27900'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_17",
        instruction="""Handle critical pharmaceutical order ORD-0004 temperature-sensitive shipment from Chicago cold storage
        WH-03 to Boston customer Delta Pharma Inc. Get order details showing 180 kg weight. Verify inventory allocation status.
        Get supplier SUP-1021 performance rating. Request shipping quotes from carriers FDEG and UAE for weight 180 kg to destination Boston, USA.
        Select UAE as carrier for destination country USA with priority High and weight 180 kg.
        Get inventory details for SKU PHRM-VACC-D4 in warehouse WH-06. Quarantine inventory with lot number LOT202406A in warehouse
        WH-06 for reason "Temperature compliance inspection". Generate shipping labels using selected carrier. Update order status to "For Return".
        Report customer details and quarantine confirmation.""",

        actions=[
            Action(
                name="get_order_details",
                kwargs={
                    "order_id": "ORD-0004"
                }
            ),
            Action(
                name="verify_inventory_allocation",
                kwargs={
                    "order_id": "ORD-0004"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={
                    "supplier_id": "SUP-1021"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "FDEG",
                    "weight_kg": 180,
                    "destination": "Boston, USA"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "UAE",
                    "weight_kg": 180,
                    "destination": "Boston, USA"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "USA",
                    "priority_level": "High",
                    "total_weight_kg": 180,
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202406A",
                    "warehouse_id": "WH-06",
                    "reason": "Temperature compliance inspection"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0004",
                    "carrier_scac": "UAE"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0004",
                    "new_status": "For Return"
                }
            )
        ],

        outputs=[
            '"customer_name": "Delta Pharma Inc."',
            '"quarantine_confirmation": "Quarantined"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_18",
        instruction="""Complex international electronics shipment ORD-0006 from San Francisco to Japan customer Zeta Tech Solutions.
        Get order details showing 550 kg weight and fragile electronics. Verify inventory allocation status. Get supplier SUP-1025
        performance rating. Check warehouse WH-05 capacity utilization. Get inventory details for SKU ELEC-CHIP-A1 in warehouse WH-01.
        Perform physical count with instruction amount 12450. Calculate inventory variance between system count 15000 and physical count 12450.
        Create inventory adjustment with quantity -2550 for reason "International shipment preparation count".
        Request shipping quotes from carriers MAEU and NPEX for weight 550 kg to destination Yokohama, Japan.
        Select MAEU as preferred carrier for destination country Japan with priority Medium and weight 550 kg.
        Generate shipping labels using selected carrier MAEU. Update order status to Shipped.
        Create incident report with id "INTL-SHIP-006" and incident type "international_compliance" and severity "low".
        Report customer details and incident id + status.""",

        actions=[
            Action(
                name="get_order_details",
                kwargs={
                    "order_id": "ORD-0006"
                }
            ),
            Action(
                name="verify_inventory_allocation",
                kwargs={
                    "order_id": "ORD-0006"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={
                    "supplier_id": "SUP-1025"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={
                    "warehouse_id": "WH-05"
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
                name="perform_physical_count",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "instruction_amount": 12450
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "system_count": 15000,
                    "instruction_count": 12450
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "adjustment_quantity": -2550,
                    "reason": "International shipment preparation count"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "MAEU",
                    "weight_kg": 550,
                    "destination": "Yokohama, Japan"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "NPEX",
                    "weight_kg": 550,
                    "destination": "Yokohama, Japan"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "Japan",
                    "priority_level": "Medium",
                    "total_weight_kg": 550,
                    "preferred_carrier": "MAEU"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0006",
                    "carrier_scac": "MAEU"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0006",
                    "new_status": "Shipped"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "INTL-SHIP-006",
                    "incident_type": "international_compliance",
                    "severity": "low"
                }
            )
        ],

        outputs=[
            '"customer_name": "Zeta Tech Solutions"',
            '"incident_status": "Created"',
            '"incident_id": "INC-INTL-SHIP-006-low"',
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_19",
        instruction="""Quality control process for raw cotton inventory at Newark apparel facility WH-04.
        Get inventory details for SKU MATR-COTT-R18 in warehouse WH-04. Quarantine inventory with lot number
        LOT202404D in warehouse WH-04 for reason "Quality inspection hold pending certification". Get supplier SUP-1020 performance rating.
        Get warehouse capacity for WH-04. Perform physical count with instruction amount 195. Calculate inventory variance between system
        count 200 and physical count 195. Create inventory adjustment with quantity -5 for reason "Quality control shrinkage".
        Request shipping quotes from carriers UPSN and CMDU for weight 1135 kg to destination Newark, USA. Select optimal carrier for
        destination country USA with priority Medium and weight 1135 kg. Report quarantine status and carrier selection.""",

        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202404D",
                    "warehouse_id": "WH-04",
                    "reason": "Quality inspection hold pending certification"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={
                    "supplier_id": "SUP-1020"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={
                    "warehouse_id": "WH-04"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "instruction_amount": 195
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "system_count": 200,
                    "physical_count": 195
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "adjustment_quantity": -5,
                    "reason": "Quality control shrinkage"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "UPSN",
                    "weight_kg": 1135,
                    "destination": "Newark, USA"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "CMDU",
                    "weight_kg": 1135,
                    "destination": "Newark, USA"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "USA",
                    "priority_level": "Medium",
                    "total_weight_kg": 1135,
                    "carriers_list": ["UPSN", "CMDU"]
                }
            )
        ],

        outputs=[
            '"quarantine_status": "Quarantined"',
            '"selected_carrier": "UPSN"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_20",
        instruction="""Critical inventory shortage analysis for automotive glass SKU AUTO-GLAS-U21 at
        Chicago parts depot WH-03. Get inventory details for SKU AUTO-GLAS-U21 in warehouse WH-03.
        Get supplier SUP-1023 performance rating. Create purchase order from supplier SUP-1023 for 300 units AUTO-GLAS-U21 to
        warehouse WH-03 with priority High. Request shipping quotes from carriers FDEG and DBSG for weight 1500 kg to destination
        Chicago, USA. Select optimal carrier for destination country USA with priority High and weight 1500 kg.
        Create incident report with id "AUTO-SHORTAGE-001" and incident type "inventory_shortage" and severity "medium".
        Report supplier rating and incident status.""",

        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={
                    "supplier_id": "SUP-1023"
                }
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1023",
                    "sku": "AUTO-GLAS-U21",
                    "quantity": 300,
                    "destination_warehouse": "WH-03",
                    "priority": "High"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "FDEG",
                    "weight_kg": 1500,
                    "destination": "Chicago, USA"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "DBSG",
                    "weight_kg": 1500,
                    "destination": "Chicago, USA"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "USA",
                    "priority_level": "High",
                    "total_weight_kg": 1500,
                    "carriers_list": ["FDEG", "DBSG"]
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "AUTO-SHORTAGE-001",
                    "incident_type": "inventory_shortage",
                    "severity": "medium"
                }
            )
        ],

        outputs=[
            '"supplier_rating": 4.5',
            '"incident_status": "Created"'
        ]
    ),


    Task(
        annotator="0",
        user_id="V5TSK_USR_21",
        instruction="""As the LA warehouse manager, verify available stock levels for ELEC-CHIP-A1 in WH-01. When available inventory is
        below 15,000 units, urgently order 10,000 units from supplier SUP-1001 for WH-01. Mark as high priority.
        Also check incoming shipments for this item and report total expected inventory after arrivals.""",
        actions=[
            Action(
                name="get_inventory_by_sku_warehouse",
                kwargs={"sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1001",
                    "sku": "ELEC-CHIP-A1",
                    "quantity": 10000,
                    "destination_warehouse": "WH-01",
                    "priority": "High",
                }
            ),
            Action(
                name="search_inbound_shipments",
                kwargs={"sku": "ELEC-CHIP-A1",
                        "destination_warehouse_id": "WH-01"}
            )
        ],
        outputs=[
            '"quantity_available": 12500',
            '"quantity_inbound": 5000',
            '"total_expected_stock": 17500',
            '"status": "Created"',
            '"total_cost": 45000',
            '"priority": "High"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_22",
        instruction="""Handle customs clearance for shipment SHIP-0001 currently awaiting processing.
        Confirm all required paperwork is complete including customs entry number and duty payment status.
        For unpaid duties, compute amount and process payment. Update status to Cleared and ready for warehouse receipt.
        Report total duty paid.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0001"}
            ),
            Action(
                name="verify_customs_documentation",
                kwargs={"shipment_id": "SHIP-0001"}
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={"shipment_id": "SHIP-0001",
                        "total_value": 350000, "country_of_origin": "China"}
            ),
            Action(
                name="process_duty_payment",
                kwargs={"shipment_id": "SHIP-0001", "duty_amount": 17500}
            ),
            Action(
                name="update_customs_status",
                kwargs={"shipment_id": "SHIP-0001", "status": "Cleared"}
            ),
            Action(
                name="update_shipment_status",
                kwargs={"shipment_id": "SHIP-0001",
                        "status": "Ready for Receipt"}
            )
        ],
        outputs=[
            '"duty_amount": 17500'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_23",
        instruction="""Conduct comprehensive supplier risk assessment for SUP-1004 following quality incidents and delivery delays.
        Review current performance metrics including rating and on-time delivery statistics. Analyze delayed purchase orders to assess financial exposure
        and delivery risk. If performance rating less than or equal to 4.5, create detailed 90-day improvement plan with the recommendation
        'Focus on improving on-time delivery'. Evaluate impact on critical inventory levels for affected SKUs including
        APRL-TSHT-O15. Check current warehouse stock levels and assess reorder needs. Check SUP-1020 capabilities and performance metrics.
        Create emergency purchase orders of 1100 (MATR-COTT-R18) with high priority if inventory levels are critical to SUP-1020.
        Notify initial supplier of concerns.""",
        actions=[
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1004"}
            ),
            Action(
                name="search_purchase_orders",
                kwargs={"supplier_id": "SUP-1004", "status": "Delayed"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "APRL-TSHT-O15", "warehouse_id": "WH-04"}
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={"sku": "APRL-TSHT-O15", "system_count": 25000, "physical_count": 22000}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1004"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1020"}
            ),
            Action(
                name="create_supplier_improvement_plan",
                kwargs={
                    "supplier_id": "SUP-1004",
                    "review_cycle_days": 90,
                    "recommendation": "Focus on improving on-time"
                }
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1020",
                    "sku": "MATR-COTT-R18",
                    "quantity": 1100,
                    "destination_warehouse": "WH-04",
                    "priority": "High"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={"supplier_id": "SUP-1004", "notification_type": "performance_review"}
            )
        ],
        outputs=[
            '"supplier_name": "Seoul Textiles Co."',
            '"performance_rating": 4.5',
            '"on_time_delivery_percentage": 96.8',
            '"relationship_status": "Active"',
            '"pending_orders_count": 1',
            '"tshirt_quantity_available": 22000',
            '"system_count": 25000',
            '"physical_count": 22000',
            '"variance": -3000',
            '"variance_percentage": 12',
            '"alternative_supplier_1": "Cairo Cotton Co.."',
            '"improvement_plan_created": true',
            '"emergency_order_quantity": 1100',
            '"emergency_order_created": true',
            '"supplier_notification_sent": true',
            '"supplier_status_recommendation": "maintain_active"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_24",
        instruction="""Ship outbound order ORD-0010 using a medium-priority international carrier.
        Select an optimal carrier that supports global shipping with reliable on-time delivery regardless of the route since the selected carrier will
        support global shipping. Generate shipping labels for the selected carrier and update the order status to 'Shipped'.""",
        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0010"}
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_city": "Mumbai",
                    "destination_country": "India",
                    "priority_level": "Medium",
                    "total_weight_kg": 2000
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0010",
                    "carrier_scac": "UAE"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0010",
                    "new_status": "Shipped"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={
                    "carrier_scac": "UAE",
                }
            )
        ],
        outputs=[
            '"optimal_carrier": "Emirates SkyCargo"',
            '"carrier_scac": "UAE"',
            '"on_time_delivery_percentage": 98.1',
            '"tracking_number":"UAE-ORD-0010"',
            '"label_id": "LBL-UAE"',
            '"order_status": "Shipped"',
            '"estimated_delivery_date": "2024-06-18"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_25",
        instruction="""Check space utilization at Phoenix facility WH-10. If utilization is equal or greater than 90%,
        find overflow options that has a required capacity with a minimum 5000 cubic meters. Then use 'redistribute_slow_moving'
        strategy to develop a capacity optimization plan. Analyze inventory by category and compute remaining space in cubic meters.
        Create incident report with id 'WH-10-CAPACITY-00' and incident type 'for_monitoring' and severity low'""",
        actions=[
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="analyze_inventory_by_category",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="identify_overflow_options",
                kwargs={"warehouse_id": "WH-10", "required_capacity": 5000}
            ),
            Action(
                name="create_capacity_plan",
                kwargs={"warehouse_id": "WH-10", "optimization_strategy": "redistribute_slow_moving"}
            ),
            Action(
                name="create_incident_report",
                kwargs={"id": "WH-10-CAPACITY-00", "incident_type": "for_monitoring", "severity": "low"}
            ),
        ],
        outputs=[
            '"remaining_capacity_cbm": 990.0',
            '"utilization_percentage": 95.5',
            '"plan_created": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_26",
        instruction="""Handle critical frozen seafood shipment SHIP-0010 from Sydney containing premium
        fish products (FOOD-FISH-H8). Verify temperature logs show compliance with below -5°C requirements, confirm carrier
        QFA maintained cold chain integrity, check inventory allocation in WH-10 cold storage, and since temperature excursions detected at -2°C,
        quarantine product LOT202406B with the following reason 'Temperature monitoring verification - seafood quality check' and create quality incident tagged as high severity.
        Calculate financial exposure including $15,000 liability estimate and escalate incident INC-SHIP-0010-high.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0010"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0010",
                    "required_temp_range": "below_-5C",
                    "excursions_flag": True
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0010",
                    "carrier_scac": "QFA"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202406B",
                    "warehouse_id": "WH-10",
                    "reason": "Temperature monitoring verification - seafood quality check"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0010",
                    "incident_type": "temperature_monitoring",
                    "severity": "high"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 180000,
                    "liability_estimate": 15000
                }
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={
                    "incident_id": "INC-SHIP-0010-high",
                    "priority": "high"
                }
            )
        ],
        outputs=[
            '"temperature_compliance": "non-compliant"',
            '"quarantined_lot": "LOT202406B"',
            '"total_financial_impact": 195000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_27",
        instruction="""Emergency: Customer reports damaged vaccine shipment SHIP-0006 carrying INV-0004 (PHRM-VACC-D4).
        Customer received compromised vials with visible crystallization and broken seals in lot LOT202406A.
        Immediately quarantine all affected inventory LOT202406A in WH-06 stating 'Customer damage report - compromised vials investigation' as primary reason,
        verify temperature logs were maintained at 2-8°C, confirm carrier UAE handling procedures, create critical incident report for product damage investigation,
        notify supplier SUP-1006 of quality concerns, calculate financial impact including $50,000 liability estimate,
        and initiate precautionary product recall pending investigation.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0006"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "PHRM-VACC-D4", "warehouse_id": "WH-06"}
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202406A",
                    "warehouse_id": "WH-06",
                    "reason": "Customer damage report - compromised vials investigation"
                }
            ),
            Action(
                name="check_temperature_logs",
                kwargs={"shipment_id": "SHIP-0006", "required_temp_range": "2-8"}
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={"shipment_id": "SHIP-0006", "carrier_scac": "UAE"}
            ),
            Action(
                name="initiate_product_recall",
                kwargs={"lot_number": "LOT202406A", "recall_type": "precautionary"}
            ),
            Action(
                name="create_incident_report",
                kwargs={"id": "SHIP-0006", "incident_type": "product_damage", "severity": "critical"}
            ),
            Action(
                name="notify_supplier",
                kwargs={"supplier_id": "SUP-1006", "notification_type": "quality_incident"}
            ),
            Action(
                name="update_shipment_status",
                kwargs={"shipment_id": "SHIP-0006", "status": "Quarantined"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={"product_value": 450000, "liability_estimate": 50000}
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={"incident_id": f"INC-SHIP-0006-critical", "priority": "critical"}
            )
        ],
        outputs=[
            '"quarantined_lot": "LOT202406A"',
            '"incident_id": f"INC-SHIP-0006-critical"',
            '"recall_id": "RCL-LOT202406A-precautionary"',
            '"temperature_excursion_detected": false',
            '"total_financial_impact": 500000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_28",
        instruction="""Monitor chemical inventory levels for CHEM-SOLV-K11 in WH-13. Current stock is running low and requires
        immediate replenishment from SUP-1013. Create purchase order for 200 at $250 per unit with expedited delivery.
        Check physical inventory count.
        Create incident report with low severity and incident type 'for_monitoring'.
        Check supplier performance metrics before confirming order.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={"sku": "CHEM-SOLV-K11", "warehouse_id": "WH-13"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1013"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={"sku": "CHEM-SOLV-K11", "warehouse_id": "WH-13"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "CHEM-SOLV-K11",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                }
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1013",
                    "sku": "CHEM-SOLV-K11",
                    "quantity": 200,
                    "destination_warehouse": "WH-13",
                    "priority": "High",
                    "unit_price": 250

                }
            )
        ],
        outputs=[
            '"quantity_available": 380',
            '"performance_rating": 4.8',
            '"status": "Created"'
        ]
    ),


    Task(
        annotator="0",
        user_id="V5TSK_USR_29",
        instruction="""Ship outbound order ORD-0005 to Toronto, Canada using UAE as carrier.
        Create incident report with low severity and incident type 'for monitoring'.
        for a 750kg load. Generate shipping labels using UAE as carrier with medium priority and update the order status to 'Shipped'.""",
        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0005"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "ORD-0005",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_city": "Toronto",
                    "destination_country": "Canada",
                    "priority_level": "Medium",
                    "total_weight_kg": 750,
                    "preferred_carrier": "UAE"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0005",
                    "carrier_scac": "UAE"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0005",
                    "new_status": "Shipped"
                }
            )
        ],
        outputs=[
            '"carrier": "UAE"',
            '"tracking_number": "UAE-ORD-0005"',
            '"estimated_delivery_date": "2024-06-09"'
        ]
    ),


    Task(
        annotator="0",
        user_id="V5TSK_USR_30",
        instruction="""Process complex customs clearance for international shipment SHIP-0001 from China worth $350,000.
        During documentation review, discover missing customs entry number requiring supplier SUP-1001 coordination.
        Calculate standard duty at 5% rate ($17,500), but supplier performance review shows rating below 4.7 requiring notification.
        If documentation issues cause delays exceeding 24 hours, create incident report with medium severity and calculate financial impact including
        $25,000 demurrage costs. Process duty payment, update customs status to cleared, coordinate with WH-01 and update shipment status.
        Report total financial impact, supplier rating and customs status.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0001"}
            ),
            Action(
                name="verify_customs_documentation",
                kwargs={"shipment_id": "SHIP-0001"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1001"}
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1001",
                    "notification_type": "documentation_required"
                }
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "total_value": 350000,
                    "country_of_origin": "China"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0001",
                    "incident_type": "documentation_delay",
                    "severity": "medium"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 350000,
                    "liability_estimate": 25000
                }
            ),
            Action(
                name="process_duty_payment",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "duty_amount": 17500
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="update_customs_status",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "status": "Cleared"
                }
            ),
            Action(
                name="update_shipment_status",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "status": "Ready for Receipt"
                }
            )
        ],
        outputs=[
            '"duty_amount": 17500',
            '"total_financial_impact": 375000',
            '"documentation_complete": false',
            '"incident_created": true',
            '"shipment_status": Ready for Receipt',
            '"supplier_performance_rating": 4.6',
            '"customs_status": Cleared'

        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_31",
        instruction="""Emergency: Customer reports damaged vaccine shipment SHIP-0006. Immediately quarantine related inventory
        containing lot number LOT202406A in WH-06. Check shipment temperature logs and verify temperature range 2-8°C with carrier UAE.
        Temperature deviations occurred with excursions detected as true. Create critical incident report
        INC-SHIP-0006-critical with reason being the damaged vaccine shipment, notify supplier SUP-1006 with quality incident notification,
        calculate financial impact with product value $450000 and liability estimate $50000, and escalate incident
        INC-SHIP-0006-critical to quality team for urgent investigation.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0006"}
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "warehouse_id": "WH-06",
                    "lot_number": "LOT202406A",
                    "reason": "Damaged vaccine shipment"
                }
            ),
            Action(
                name="check_temperature_logs",
                kwargs={"shipment_id": "SHIP-0006", "required_temp_range": "2-8", "excursions_flag": True}
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={"shipment_id": "SHIP-0006", "carrier_scac": "UAE"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0006",
                    "incident_type": "product_damage",
                    "severity": "critical"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={"supplier_id": "SUP-1006", "notification_type": "quality_incident"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={"product_value": 450000, "liability_estimate": 50000}
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={"incident_id": "INC-SHIP-0006-critical", "priority": "critical"}
            )
        ],
        outputs=[
            '"excursions_detected": true',
            '"incident_id": "INC-SHIP-0006-critical"',
            '"total_financial_impact": 500000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_32",
        instruction="""Review supplier SUP-1028 steel works performance following delivery delays and quality concerns.
        Analyze current performance metrics and delivery statistics. Since performance rating 4.2 is below 4.5 threshold,
        examine all pending purchase orders for risk assessment and provide recommendation of "conditional approval" on
        90-day improvement plan for supplier relationship status.
        An incident report with medium severity should be created using SHIP-0028 as reference.
        Create inventory adjustment for affected heavy equipment SKU HEVY-DRIL-I9 in warehouse WH-11 with quantity adjustment
        of -5 units due to quality defects from supplier delivery issues under the reason 'quality defects from SUP-1028 delivery delays'.
        The financial impact calculations should include $2,000
        liability estimate. Research alternative suppliers including SUP-1011 and
        validate there is a alternative_suppliers_available for HEVY-DRIL-I9.""",
        actions=[
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1028"}
            ),
            Action(
                name="search_purchase_orders",
                kwargs={
                    "supplier_id": "SUP-1028",
                    "status": "In Transit"
                }
            ),
            Action(
                name="search_inbound_shipments",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "destination_warehouse_id": "WH-11"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11"
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "adjustment_quantity": -5,
                    "reason": "quality defects from SUP-1028 delivery delays"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 11000,
                    "liability_estimate": 2000
                }
            ),
            Action(
                name="create_supplier_improvement_plan",
                kwargs={
                    "supplier_id": "SUP-1028",
                    "review_cycle_days": 90,
                    "recommendation": "conditional_approval"
                }
            ),
            Action(
                name="get_approved_suppliers",
                kwargs={"sku": "HEVY-DRIL-I9"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0028",
                    "incident_type": "quality_defect",
                    "severity": "medium"
                }
            )
        ],
        outputs=[
            '"performance_rating": 4.2',
            '"current_inventory": 40',
            '"adjustment_value": 11000',
            '"total_financial_impact": 13000',
            '"alternative_suppliers_available": 1',
            '"improvement_plan_id": "SIP-SUP-1028"',
            '"supplier_status_recommendation": "conditional_approval"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_33",
        instruction="""Investigate inventory discrepancy for luxury watch components LUX-WATCH-L12 in WH-07 security vault.
        System shows 500 units but physical count reveals exactly 497 units, indicating a -3 unit variance. Calculate inventory variance using
        system count 500 and physical count 497. Create inventory adjustment for the -3 unit discrepancy due to security audit findings because of potential theft (variance) with reason "Security audit findings - luxury goods variance".
        When calculating the financial impact=it should be noted that the product value is $300 per unit, resulting in a total financial impact of $1400 including $500 liability estimate.
        Update warehouse accuracy metrics and create medium incident report for shipment SHIP-0014 related to luxury goods security protocol. Notify supplier
        of the incident using data for SUP-1014 stating 'quality_incident' as the reason""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={"sku": "LUX-WATCH-L12", "warehouse_id": "WH-07"}
            ),
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0014"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={"sku": "LUX-WATCH-L12", "warehouse_id": "WH-07"}
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "system_count": 500,
                    "physical_count": 497
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202403E",
                    "warehouse_id": "WH-07",
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "adjustment_quantity": -3,
                    "reason": "Security audit findings - luxury goods variance"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 900,
                    "liability_estimate": 500
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-07"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0014",
                    "incident_type": "inventory_variance",
                    "severity": "medium"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1014",
                    "notification_type": "quality_incident"
                }
            )
        ],
        outputs=[
            '"variance_units": -3',
            '"variance_percentage": 0.6',
            '"quarantine_id": "QTN-LOT202403E-WH-07"',
            '"total_financial_impact": 1400',
            '"incident_id": "INC-SHIP-0014-medium"',
            '"supplier_notified": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_34",
        instruction="""Emergency: Luxury goods shipment SHIP-0014 containing Swiss watch parts from Zurich, Switzerland worth
        CHF 50000 shows potential damage based on carrier inspection report. Prepare damage assessment protocol (Calculate potential financial impact) for when shipment arrives at WH-07.
        Create preventive incident report about the potential damage with medium severity, improvement plan with 60-day review cycle,
        notify supplier SUP-1014 of potential quality concerns,
        calculate financial impact with product value CHF 50000 (approximately $45450 USD) and liability estimate $10000 for
        potential customer claims with the reason 'Quality incident - damaged luxury goods'""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0014"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1014"}
            ),
            Action(
                name="verify_customs_documentation",
                kwargs={"shipment_id": "SHIP-0014"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-07"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0014",
                    "incident_type": "potential_damage",
                    "severity": "medium"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 45450,
                    "liability_estimate": 10000
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={"supplier_id": "SUP-1014", "notification_type": "quality_incident"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "UPSN",
                    "weight_kg": 15,
                    "destination": "Zurich"
                }
            ),
            Action(
                name="create_supplier_improvement_plan",
                kwargs={
                    "supplier_id": "SUP-1014",
                    "review_cycle_days": 60,
                    "reason": "Quality incident - damaged luxury goods"
                }
            ),
            Action(
                name="update_shipment_status",
                kwargs={"shipment_id": "SHIP-0014", "status": "Inspection Required"}
            )
        ],
        outputs=[
            '"supplier_rating": 4.9',
            '"customs_status": "Pending"',
            '"warehouse_utilization": 60.0',
            '"incident_id": "INC-SHIP-0014-medium"',
            '"total_financial_impact": 55450',
            '"return_shipping_cost": 48',
            '"improvement_plan_created": true',
            '"shipment_status": "Inspection Required"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_35",
        instruction="""Execute shipment coordination for critical electronics order ORD-0006 to Yokohama, Japan going to WH-05.
        Verify complete inventory allocation across multiple SKUs, analyze warehouse capacity at origin San Francisco Electronics Hub (WH-05),
        select carrier MAEU for international electronics transport with destination Yokohama, Japan, priority Medium, weight 550kg.
        Generate shipping documentation with MAEU carrier, request shipping quote for cost analysis and finalize shipment processing.""",
        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0006"}
            ),
            Action(
                name="verify_inventory_allocation",
                kwargs={"order_id": "ORD-0006"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-05"}
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_city": "Yokohama",
                    "destination_country": "Japan",
                    "priority_level": "Medium",
                    "total_weight_kg": 550,
                    "preferred_carrier": "MAEU"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={"order_id": "ORD-0006", "carrier_scac": "MAEU"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "MAEU",
                    "weight_kg": 550,
                    "destination": "Yokohama, Japan"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={"order_id": "ORD-0006", "new_status": "Shipped"}
            ),
        ],
        outputs=[
            '"selected_carrier": "MAEU"',
            '"tracking_number": "MAEU-ORD-0006"',
            '"current_status": "Shipped"',
            '"estimated_delivery_date": "2024-06-15"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_36",
        instruction="""Check current stock levels for TECH-SOLR-G7 solar panels in WH-09 Phoenix facility. Perform inventory recount
        verification following cycle count discrepancies. Review supplier SUP-1009 performance metrics to
        ensure continued reliability. Create inventory adjustment for TECH-SOLR-G7 in WH-09 with adjustment quantity of +500 units
        due to inventory recount findings showing system undercount with the reason 'Inventory recount findings - system undercount correction',
        and update warehouse accuracy metrics.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={"sku": "TECH-SOLR-G7", "warehouse_id": "WH-09"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1009"}
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "adjustment_quantity": 500,
                    "reason": "Inventory recount findings - system undercount correction"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-09"}
            )
        ],
        outputs=[
            '"quantity_before_adjustment": 1200',
            '"quantity_after_adjustment": 1700',
            '"performance_rating": 4.5',
            '"adjustment_value": 90000',
            '"accuracy_updated": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_38",
        instruction="""Re-process customs clearance for electronics shipment SHIP-0030 from Dubai containing smartphones worth $380,000.
        Initial duty payment was made under DDP terms, but customs audit revealed duty underpayment requiring adjustment.
        Verify all documentation completeness, calculate correct import duties based on revised classification,
        process additional duty payment of $13,300, update customs status to cleared, and prepare shipment for warehouse receipt.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0030"}
            ),
            Action(
                name="verify_customs_documentation",
                kwargs={"shipment_id": "SHIP-0030"}
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={"shipment_id": "SHIP-0030", "total_value": 380000, "country_of_origin": "UAE"}
            ),
            Action(
                name="process_duty_payment",
                kwargs={"shipment_id": "SHIP-0030", "duty_amount": 13300}
            ),
            Action(
                name="update_customs_status",
                kwargs={"shipment_id": "SHIP-0030", "status": "Cleared"}
            ),
            Action(
                name="update_shipment_status",
                kwargs={"shipment_id": "SHIP-0030", "status": "Ready for Receipt"}
            )
        ],
            outputs=[
            '"duty_amount": 13300',
            '"customs_entry_number": "US-SHIP-0030"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_39",
        instruction="""Investigate potential contamination issue with chemical shipment SHIP-0013 with required temperature range of 4-20C
        from Helsinki containing industrial solvents (LOT202405E). Check temperature logs for proper storage conditions,
        verify cold chain maintenance, quarantine affected inventory in WH-13 hazmat area with reason being 'Contamination investigation - chemical safety protocol',
        create detailed incident report with type 'contamination_suspected' and severity 'high',
        notify supplier SUP-1013 with notification type 'quality_incident', and initiate product recall
        with recall type value of 'precautionary'.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0013"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={"shipment_id": "SHIP-0013", "required_temp_range": "4-20C"}
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={"shipment_id": "SHIP-0013", "carrier_scac": "HLCU"}
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405E",
                    "warehouse_id": "WH-13",
                    "reason": "Contamination investigation - chemical safety protocol"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={"id": "SHIP-0013", "incident_type": "contamination_suspected", "severity": "high"}
            ),
            Action(
                name="notify_supplier",
                kwargs={"supplier_id": "SUP-1013", "notification_type": "quality_incident"}
            ),
            Action(
                name="initiate_product_recall",
                kwargs={"lot_number": "LOT202405E", "recall_type": "precautionary"}
            )
        ],
        outputs=[
            '"temperature_compliance": "compliant"',
            '"recall_initiated": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_40",
        instruction="""Conduct comprehensive carrier performance analysis for Asian and Global routes.
        Evaluate MAEU, NPEX, and DHLG carriers for critical 2800kg electronics shipment to Tokyo requiring delivery within 12 days.
        Generate shipping quotes from all carriers, perform cost-benefit analysis, select optimal carrier based on performance and cost,
        generate shipping labels for order ORD-0006 with selected carrier, and update order status to Shipped.""",
        actions=[
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "MAEU", "route": "Japan"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "NPEX", "route": "Japan"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "DHLG", "route": "Global"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "MAEU",
                    "weight_kg": 2800,
                    "destination": "Tokyo, Japan"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "NPEX",
                    "weight_kg": 2800,
                    "destination": "Tokyo, Japan"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "DHLG",
                    "weight_kg": 2800,
                    "destination": "Tokyo, Japan"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "Japan",
                    "destination_city": "Tokyo",
                    "weight_kg": 2800,
                    "priority_level": "Critical",
                    "carriers_list": ["MAEU", "NPEX", "DHLG"]
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0006",
                    "carrier_scac": "DHLG"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0006",
                    "new_status": "Shipped"
                }
            )
        ],
        outputs=[
            '"recommended_carrier": "DHLG"',
            '"maeu_on_time_percentage": 94.5',
            '"npex_on_time_percentage": 96.2',
            '"dhlg_on_time_percentage": 97.9',
            '"maeu_estimated_cost": 7000',
            '"npex_estimated_cost": 8400',
            '"dhlg_estimated_cost": 8400',
            '"tracking_number": "DHLG-ORD-0006"',
            '"order_status": "Shipped"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_41",
        instruction="""Perform cycle count audit for luxury watch components LUX-WATCH-L12
        in WH-07 high-security vault which currently shows 500 units in system. Physical count reveals 497 units.
        Calculate variance percentage, create inventory adjustment since discrepancy exists, using reason code
        "Cycle count variance correction", and update warehouse accuracy metrics per standard calculation methodology.
        Report percentage variance""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "instruction_amount": 497
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "system_count": 500,
                    "physical_count": 497
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "adjustment_quantity": -3,
                    "reason": "Cycle count variance correction"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-07"}
            )
        ],
        outputs=[
            '"variance_percentage": 0.6',
            '"inventory_accuracy_percentage": 100.0'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_42",
        instruction="""As operations manager for Los Angeles facility,
        conduct stock assessment for 8-bit microcontroller component ELEC-CHIP-A1 in warehouse WH-01. Current system indicates low
        inventory requiring immediate replenishment action. Place emergency procurement order for 10,000 units from primary
        supplier SUP-1001 with high priority designation in addition to existing stock of 12,500 units.
        Create incident report with incident type 'for_monitoring' with low severity.
        Review all pending inbound deliveries for this component to understand current pipeline status.""",
        actions=[
            Action(
                name="get_inventory_by_sku_warehouse",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                }
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "quantity": 10000,
                    "destination_warehouse": "WH-01",
                    "supplier_id": "SUP-1001",
                    "sku": "ELEC-CHIP-A1",
                    "priority": "High"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "ELEC-CHIP-A1",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                }
            ),
            Action(
                name="search_inbound_shipments",
                kwargs={
                    "destination_warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                }
            )
        ],
        outputs=[
            '"quantity_available": 12500',
            '"quantity_inbound": 5000',
            '"total_expected_stock": 17500',
            '"status": "Created"',
            '"total_cost": 45000',
            '"priority": "High"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_43",
        instruction="""As international trade compliance specialist, process import clearance for
        electronics container SHIP-0001 from Shenzhen manufacturing facility that has arrived at Los Angeles port.
        Review import documentation completeness, validate customs entry requirements, calculate applicable tariff obligations for
        Chinese electronics valued at $350,000, execute duty settlement, and advance clearance status to enable warehouse delivery.
        Document final tariff payment amount.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0001"}
            ),
            Action(
                name="verify_customs_documentation",
                kwargs={"shipment_id": "SHIP-0001"}
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "total_value": 350000,
                    "country_of_origin": "China"
                }
            ),
            Action(
                name="process_duty_payment",
                kwargs={"shipment_id": "SHIP-0001", "duty_amount": 17500}
            ),
            Action(
                name="update_customs_status",
                kwargs={"shipment_id": "SHIP-0001", "status": "Cleared"}
            ),
            Action(
                name="update_shipment_status",
                kwargs={"shipment_id": "SHIP-0001", "status": "Ready for Receipt"}
            )
        ],
        outputs=[
            '"duty_amount": 17500'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_44",
        instruction="""Review supplier SUP-1028 Moscow Steel Works performance following quality concerns and shipment monitoring needs.
        Current performance rating of 4.2 is below company standards requiring formal improvement plan with 60-day review cycle.
        Analyze active shipment SHIP-0028 steel delivery status,
        create incident report with low severity with incident type 'for_monitoring',
        examine all in-transit deliveries from this supplier,
        and assess warehouse WH-11 capacity impact.""",
        actions=[
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1028"}
            ),
            Action(
                name="create_supplier_improvement_plan",
                kwargs={
                    "supplier_id": "SUP-1028",
                    "review_cycle_days": 60
                }
            ),
            Action(
                name="search_purchase_orders",
                kwargs={"supplier_id": "SUP-1028", "status": "In Transit"}
            ),
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0028"}
            ),
            Action(
                name="search_inbound_shipments",
                kwargs={"destination_warehouse_id": "WH-11"}
            ),
            Action(
                name="create_incident_report",
                kwargs={"id": "SHIP-0028", "incident_type": "for_monitoring", "severity": "low"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-11"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-11"}
            )
        ],
        outputs=[
            '"performance_rating": 4.2',
            '"on_time_delivery_percentage": 92.5',
            '"supplier_status_recommendation": "maintain_active"',
            '"warehouse_utilization": 55.8',
            '"total_capacity_cbm": 120000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_45",
        instruction="""Monitor inventory levels for FOOD-FISH-H8 frozen tuna in WH-10 cold storage facility.
        Stock levels appear critically low for upcoming restaurant orders.
        Check inbound shipments to avoid duplicate ordering, verify warehouse cold storage capacity utilization,
        evaluate supplier SUP-1010 performance for seafood deliveries, create urgent purchase order for 1000 units with Critical priority
        level and notes "Emergency seafood inventory replenishment", and update inventory accuracy metrics after procurement action.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={"sku": "FOOD-FISH-H8", "warehouse_id": "WH-10"}
            ),
            Action(
                name="search_inbound_shipments",
                kwargs={"sku": "FOOD-FISH-H8", "destination_warehouse_id": "WH-10"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1010"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1010",
                    "sku": "FOOD-FISH-H8",
                    "quantity": 1000,
                    "destination_warehouse": "WH-10",
                    "priority": "Critical",
                    "notes": "Emergency seafood inventory replenishment"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-10"}
            )
        ],
        outputs=[
            '"quantity_available": 2400',
            '"current_inbound": 1000',
            '"total_capacity_cbm": 22000',
            '"current_utilization_percentage": 95.5',
            '"performance_rating": 4.9',
            '"po_created": "PO-SUP-1010-FOOD-FISH-H8-001"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_46",
        instruction="""Manage critical pharmaceutical inventory for vaccine SKU PHRM-VACC-D4 in warehouse WH-06.
        Check current inventory levels and storage requirements, verify warehouse capacity and utilization for staging,
        search for incoming pharmaceutical shipments to assess supply pipeline, perform mandatory cycle count showing
        150 units variance requiring inventory adjustment with reason "Cycle count variance correction",
        update warehouse accuracy metrics, check supplier SUP-1006 performance for vaccine supply chain reliability,
        and search for any pending purchase orders from this pharmaceutical supplier.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={"sku": "PHRM-VACC-D4", "warehouse_id": "WH-06"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-06"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-06"}
            ),
            Action(
                name="search_inbound_shipments",
                kwargs={"sku": "PHRM-VACC-D4", "destination_warehouse_id": "WH-06"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={"sku": "PHRM-VACC-D4", "warehouse_id": "WH-06"}
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={"sku": "PHRM-VACC-D4", "system_count": 20000, "physical_count": 19850}
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "adjustment_quantity": -150,
                    "reason": "Cycle count variance correction"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-06"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1006"}
            ),
            Action(
                name="search_purchase_orders",
                kwargs={"supplier_id": "SUP-1006", "status": "Pending"}
            )
        ],
        outputs=[
            '"vaccine_quantity_available": 18000',
            '"warehouse_utilization": 81.2',
            '"physical_count": 19850',
            '"variance_percentage": 0.75',
            '"total_adjustment_value": 2325.00',
            '"supplier_performance_rating": 4.9',
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_47",
        instruction="""Handle emergency contamination alert for textile shipment SHIP-0020 containing Egyptian cotton from Cairo valued at $210,000.
        Immediately quarantine all affected inventory lot LOT202404D in WH-04 with reason "Emergency quarantine - contamination investigation",
        review shipment documentation which shows pending customs clearance requiring immediate attention, create comprehensive incident report for "contamination_alert" with "high" severity level,
        notify supplier SUP-1020 using "quality_incident" notification type, calculate financial exposure including $30,000 liability
        estimate, and initiate voluntary product recall for affected lot.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0020"}
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202404D",
                    "warehouse_id": "WH-04",
                    "reason": "Emergency quarantine - contamination investigation"
                }
            ),
            Action(
                name="verify_customs_documentation",
                kwargs={"shipment_id": "SHIP-0020"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1020"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0020",
                    "incident_type": "contamination_alert",
                    "severity": "high"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1020",
                    "notification_type": "quality_incident"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 210000,
                    "liability_estimate": 30000
                }
            ),
            Action(
                name="initiate_product_recall",
                kwargs={
                    "lot_number": "LOT202404D",
                    "recall_type": "voluntary"
                }
            )
        ],
        outputs=[
            '"total_financial_impact": 240000',
            '"recall_initiated": true',
            '"supplier_performance_rating": 4.5',
            '"customs_documentation_complete": false'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_48",
        instruction="""Coordinate customs clearance for heavy mining equipment shipment SHIP-0011
        from Johannesburg containing specialized drill components valued at $1,200,000. Verify all international documentation,
        calculate import duties and taxes for South African origin, process duty payment for calculated amount, update customs
        clearance status, verify warehouse WH-11 capacity for heavy equipment, check supplier SUP-1011 performance, and prepare
        equipment for delivery to Denver facility.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0011"}
            ),
            Action(
                name="verify_customs_documentation",
                kwargs={"shipment_id": "SHIP-0011"}
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={
                    "shipment_id": "SHIP-0011",
                    "total_value": 1200000,
                    "country_of_origin": "South Africa"
                }
            ),
            Action(
                name="process_duty_payment",
                kwargs={"shipment_id": "SHIP-0011", "duty_amount": 42000}
            ),
            Action(
                name="update_customs_status",
                kwargs={"shipment_id": "SHIP-0011", "status": "Cleared"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-11"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1011"}
            ),
            Action(
                name="update_shipment_status",
                kwargs={"shipment_id": "SHIP-0011", "status": "Ready for Receipt"}
            )
        ],
        outputs=[
            '"duty_amount": 42000',
            '"total_capacity_cbm": 120000',
            '"supplier_performance_rating": 4.3',
            '"customs_entry_number": "US-SHIP-0011"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_49",
        instruction="""Analyze warehouse capacity constraints at WH-15 Los Angeles beverage distribution center.
        Current wine inventory is approaching storage limits with cork shipment SHIP-0022 from supplier SUP-1022 delayed causing bottleneck.
        Evaluate space utilization, check delayed shipment impact, assess supplier performance for reliability,
        identify overflow warehouse options requiring 8000 cbm capacity, analyze beverage category breakdown,
        search for pending beverage orders that may need redistribution to other warehouses, check current wine inventory BEVG-WINE-P16 levels,
        verify cork inventory MATR-CORK-T20 availability, calculate optimal redistribution to nearby WH-01,
        create inventory adjustment to transfer 300 units of BEVG-WINE-P16 from WH-15 to WH-01 for capacity optimization
        with reason "Transfer to WH-01 for capacity optimization", create comprehensive capacity plan using beverage_optimization strategy,
        and update warehouse metrics.""",
        actions=[
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-15"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-15"}
            ),
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0022"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1022"}
            ),
            Action(
                name="identify_overflow_options",
                kwargs={"warehouse_id": "WH-15", "required_capacity": 8000}
            ),
            Action(
                name="analyze_inventory_by_category",
                kwargs={"warehouse_id": "WH-15"}
            ),
            Action(
                name="search_inbound_shipments",
                kwargs={"destination_warehouse_id": "WH-15", "status": "pending"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "BEVG-WINE-P16", "warehouse_id": "WH-15"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "MATR-CORK-T20", "warehouse_id": "WH-15"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "BEVG-WINE-P16",
                    "warehouse_id": "WH-15",
                    "adjustment_quantity": -300,
                    "reason": "Transfer to WH-01 for capacity optimization"
                }
            ),
            Action(
                name="create_capacity_plan",
                kwargs={"warehouse_id": "WH-15", "optimization_strategy": "beverage_optimization"}
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-15"}
            )
        ],
        outputs=[
            '"utilization_percentage": 82.0',
            '"remaining_capacity_cbm": 5400',
            '"delayed_shipment_value": 75000',
            '"supplier_rating": 4.6',
            '"overflow_warehouse": "WH-01"',
            '"wine_inventory_available": 4500',
            '"cork_inventory_available": 450000',
            '"optimization_plan_id": "CAP-WH-15"',
            '"transfer_units": 300'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_50",
        instruction="""Investigate quality issues with furniture shipment SHIP-0015 from Bangkok containing teak dining chairs lot LOT202402B.
            Check shipping conditions and carrier performance, quarantine affected inventory lot LOT202402B in WH-14 with reason "Quality investigation required",
            create quality_issues incident documentation, notify supplier SUP-1015 with quality_incident notification,
            assess financial impact of $250,000 shipment value including potential customer claims.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0015"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "EGLV", "route": "Thailand"}
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202402B",
                    "warehouse_id": "WH-14",
                    "reason": "Quality investigation required"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={"id": "SHIP-0015", "incident_type": "quality_issues"}
            ),
            Action(
                name="notify_supplier",
                kwargs={"supplier_id": "SUP-1015", "notification_type": "quality_incident"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={"product_value": 250000}
            )
        ],
        outputs=[
            '"total_financial_impact": 250000',
            '"carrier_rating": 4.4'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_51",
        instruction="""Execute comprehensive carrier evaluation for European automotive parts distribution.
        Analyze performance metrics for DBSG, HLCU, and MAEU carriers including cost efficiency, delivery reliability, and damage rates.
        Select optimal carrier from these three options for critical 4200kg automotive glass shipment to Germany requiring delivery within 10 days.
        Generate detailed cost comparisons by requesting shipping quotes: DBSG for Hamburg, Germany,
        HLCU for Rotterdam, Netherlands, and MAEU for multiple European cities distribution.
        Check current inventory levels for AUTO-GLAS-U21 in warehouse WH-03, perform physical count showing system count 200 but physical count 196,
        calculate variance and create inventory adjustment with reason "Carrier evaluation count verification".
        Create emergency purchase order for 500 units of AUTO-GLAS-U21 automotive windshields from supplier SUP-1023
        for destination warehouse WH-03 with high priority due to European distribution demand.
        Generate shipping labels for existing order ORD-0003 using selected optimal carrier and update order status to shipped.
        Assess warehouse capacity at WH-03 for incoming automotive glass inventory, identify overflow options requiring 1000 cbm capacity,
        create capacity optimization plan using automotive_consolidation strategy.""",

        actions=[
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "DBSG", "route": "Europe"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "HLCU", "route": "Europe"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "MAEU", "route": "Europe"}
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "Germany",
                    "weight_kg": 4200,
                    "priority_level": "Critical",
                    "max_transit_days": 10,
                    "carriers_list": ["DBSG", "HLCU", "MAEU"]
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "DBSG",
                    "weight_kg": 4200,
                    "destination": "Hamburg, Germany"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "HLCU",
                    "weight_kg": 4200,
                    "destination": "Rotterdam, Netherlands"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "MAEU",
                    "weight_kg": 4200,
                    "destination": "Multiple European Cities"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "AUTO-GLAS-U21", "warehouse_id": "WH-03"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={"sku": "AUTO-GLAS-U21", "warehouse_id": "WH-03", "instruction_amount": 196}
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={"sku": "AUTO-GLAS-U21", "system_count": 200, "physical_count": 196}
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "adjustment_quantity": -4,
                    "reason": "Carrier evaluation count verification"
                }
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1023",
                    "sku": "AUTO-GLAS-U21",
                    "quantity": 500,
                    "destination_warehouse": "WH-03",
                    "priority": "High",
                    "notes": "Emergency order for European automotive glass distribution"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0003",
                    "carrier_scac": "DBSG"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0003",
                    "new_status": "Shipped"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-03"}
            ),
            Action(
                name="identify_overflow_options",
                kwargs={"warehouse_id": "WH-03", "required_capacity": 1000}
            ),
            Action(
                name="create_capacity_plan",
                kwargs={"warehouse_id": "WH-03", "optimization_strategy": "automotive_consolidation"}
            )
        ],
        outputs=[
            '"recommended_carrier": "DBSG"',
            '"estimated_cost": 7560',
            '"delivery_reliability": 95.8',
            '"current_inventory": 200',
            '"physical_count": 196',
            '"variance_percentage": 2.0',
            '"adjustment_id": "ADJ-WH-03"',
            '"purchase_order_id": "PO-SUP-1023-AUTO-GLAS-U21-001"',
            '"tracking_number": "DBSG-ORD-0003"',
            '"warehouse_utilization": 65.0',
            '"overflow_warehouse": "WH-01"',
            '"capacity_plan_id": "CAP-WH-03"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_52",
        instruction="""Perform inventory accuracy audit for building materials BLDG-TILE-J10 ceramic tiles in WH-12 Miami facility.
        Conduct physical count verification, calculate variance against system records, create inventory adjustment with reason 'Physical count variance - building materials audit',
        and update warehouse accuracy metrics for compliance reporting.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={"sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={"sku": "BLDG-TILE-J10", "system_count": 18000, "physical_count": 17865}
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                    "adjustment_quantity": -135,
                    "reason": "Physical count variance - building materials audit",
                    "variance_percentage": 0.75
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-12"}
            )
        ],
        outputs=[
            '"variance_percentage": 0.75',
            '"total_adjustment_value": 472.50'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_53",
        instruction="""Coordinate complex emergency response for multiple pharmaceutical shipments SHIP-0006 and SHIP-0021
        showing temperature deviations during transit. Verify temperature logs for both shipments using required pharmaceutical
        cold chain range 2-8°C with excursions_flag true to detect deviations, check cold chain integrity with respective carriers UAE and SAS,
        quarantine affected vaccine inventory for SHIP-0021 lot LOT202405H in WH-06 with reason
        "Temperature deviation - multi-shipment pharmaceutical investigation",
        create comprehensive incident reports for each shipment documenting temperature_deviation incidents with critical
        severity due to pharmaceutical temperature violations, notify both suppliers SUP-1006 and SUP-1021 about quality incidents,
        calculate combined financial exposure using shipment values 450000 and 550000 with liability estimate 100000,
        escalate both incident reports INC-SHIP-0006-critical and INC-SHIP-0021-critical with critical priority due to patient safety concerns,
        and initiate mandatory product recalls for lot LOT202405H due to temperature compromise requiring immediate market withdrawal.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0006"}
            ),
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0021"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "required_temp_range": "2-8",
                    "excursions_flag": True
                }
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0021",
                    "required_temp_range": "2-8",
                    "excursions_flag": True
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "carrier_scac": "UAE"
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0021",
                    "carrier_scac": "SAS"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405H",
                    "warehouse_id": "WH-06",
                    "reason": "Temperature deviation - multi-shipment pharmaceutical investigation"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0006",
                    "incident_type": "temperature_deviation",
                    "severity": "critical"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0021",
                    "incident_type": "temperature_deviation",
                    "severity": "critical"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1006",
                    "notification_type": "quality_incident"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "notification_type": "quality_incident"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 1000000,
                    "liability_estimate": 100000
                }
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={
                    "incident_id": "INC-SHIP-0006-critical",
                    "priority": "critical"
                }
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={
                    "incident_id": "INC-SHIP-0021-critical",
                    "priority": "critical"
                }
            ),
            Action(
                name="initiate_product_recall",
                kwargs={
                    "lot_number": "LOT202405H",
                    "recall_type": "mandatory"
                }
            )
        ],
        outputs=[
            '"temperature_excursion_detected": true',
            '"total_financial_impact": 1100000',
            '"affected_shipments": 2'
        ]
    ),
    Task(
        annotator="0",
        user_id="V5TSK_USR_54",
        instruction="""Review supplier SUP-1026 (Kuala Lumpur Rubber Exports) performance following recent delivery
        inconsistencies and quality concerns. Analyze current performance metrics including delivery
        reliability and quality ratings, create structured improvement plan with 45-day review milestones due to delivery
        inconsistencies and quality concerns requiring intensive monitoring with recommendation "enhanced_monitoring", examine pending purchase orders for risk assessment,
        review recent shipments from this supplier by searching for shipments with destination warehouse WH-14 which is where
        SUP-1026 delivers, examine specific shipment SHIP-0026 details from this supplier,
        create incident report of low severity stating the type 'for_monitoring', and recommend enhanced monitoring
        as the supplier relationship adjustment due to the performance concerns identified.""",
        actions=[
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1026"}
            ),
            Action(
                name="create_supplier_improvement_plan",
                kwargs={
                    "supplier_id": "SUP-1026",
                    "review_cycle_days": 45,
                    "reason": "Delivery inconsistencies and quality concerns requiring intensive monitoring",
                    "recommendation": "enhanced_monitoring"
                }
            ),
            Action(
                name="search_purchase_orders",
                kwargs={
                    "supplier_id": "SUP-1026",
                    "status": "pending"
                }
            ),
            Action(
                name="search_inbound_shipments",
                kwargs={"destination_warehouse_id": "WH-14"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SUP-1026",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                }
            ),
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0026"}
            )
        ],
        outputs=[
            '"performance_rating": 4.5',
            '"on_time_delivery_percentage": 96.0',
            '"supplier_status_recommendation": "enhanced_monitoring"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_55",
        instruction="""Process shipment for order ORD-0002. First confirm order details and customer needs. Verify stock allocation for all items.
        If fully allocated, choose DHLG as shipping provider based on the destination Germany and priority High for order ORD-0002
        with total weight 980 kg. Assess performance metrics for carrier DHLG on the Hamburg, Germany route.
        Create shipping labels, create incident report with low severity and incident type "for_monitoring" and mark the order as shipped.
        Provide tracking number and delivery estimate.""",
        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0002"}
            ),
            Action(
                name="verify_inventory_allocation",
                kwargs={"order_id": "ORD-0002"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "DHLG", "route": "Hamburg, Germany"}
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "Germany",
                    "priority_level": "High",
                    "total_weight_kg": 980,
                    "preferred_carrier": "DHLG",
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={"order_id": "ORD-0002", "carrier_scac": "DHLG"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "ORD-0002",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={"order_id": "ORD-0002", "new_status": "Shipped"}
            )
        ],
        outputs=[
            '"tracking_number": "DHLG-ORD-0002"',
            '"estimated_delivery_date": "2024-06-05"',
            '"status": "Shipped"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_56",
        instruction="""Investigate critical battery shipment SHIP-0019 from Warsaw containing lithium-ion batteries potentially in violation of hazmat handling protocols.
        Review temperature logs to ensure storage stayed within 15°C to 25°C during transit. Document cold chain integrity status with carrier LOT for hazmat transport compliance.
        Affected inventory under lot number LOT202405G is stored at WH-03 and must be quarantined for inspection due to safety concerns. Quarantine this inventory immediately with reason being "Quarantine required pending hazmat compliance inspection for lithium-ion batteries".
        Initiate an incident report for this hazmat compliance issue with severity set to high. Notify supplier SUP-1019 of the compliance breach under a quality incident classification.
        Estimate financial exposure based on product value of 200000 and projected liability of 50000 due to potential non-conformance.
        Escalate the issue to the quality assurance team using the generated incident report ID with critical priority.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0019"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0019",
                    "required_temp_range": "15-25"
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0019",
                    "carrier_scac": "LOT"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405G",
                    "warehouse_id": "WH-03",
                    "reason": "Quarantine required pending hazmat compliance inspection for lithium-ion batteries"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0019",
                    "incident_type": "hazmat_nonconformance",
                    "severity": "high"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1019",
                    "notification_type": "quality_incident"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 200000,
                    "liability_estimate": 50000
                }
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={
                    "incident_id": "INC-SHIP-0019-high",
                    "priority": "critical"
                }
            )
        ],
        outputs=[
            '"cold_chain_integrity": "maintained"',
            '"total_financial_impact": 250000',
            '"incident_id": "INC-SHIP-0019-high"'
        ]
    ),


    Task(
        annotator="0",
        user_id="V5TSK_USR_57",
        instruction="""Clear customs for ceramic tile shipment SHIP-0012 from Madrid containing premium building materials.
        Verify all import documentation is complete, calculate applicable duties and fees for the total shipment value of 220000 from Spain,
        process duty payment of 7700, update customs clearance status to Cleared, create incident report with low severity and incident type as "for_monitoring"
        and prepare shipment for delivery to WH-12 Miami
        facility by updating status to Ready for Receipt.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0012"}
            ),
            Action(
                name="verify_customs_documentation",
                kwargs={"shipment_id": "SHIP-0012"}
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={"shipment_id": "SHIP-0012", "total_value": 220000, "country_of_origin": "Spain"}
            ),
            Action(
                name="process_duty_payment",
                kwargs={"shipment_id": "SHIP-0012", "duty_amount": 7700}
            ),
            Action(
                name="update_customs_status",
                kwargs={"shipment_id": "SHIP-0012", "status": "Cleared"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0012",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                }
            ),
            Action(
                name="update_shipment_status",
                kwargs={"shipment_id": "SHIP-0012", "status": "Ready for Receipt"}
            )
        ],
        outputs=[
            '"duty_amount": 7700',
            '"customs_status": "Cleared"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_58",
        instruction="""Conduct comprehensive supplier assessment for SUP-1004 (Seoul Textiles Co.) due to declining performance metrics.
        First retrieve their current performance data and rating status. Since their rating is below our 4.5 threshold,
        create a 90-day improvement plan immediately. Search for all pending purchase orders with this supplier to assess impact.
        Next, analyze current inventory levels for textile SKU APRL-TSHT-O15 at warehouse WH-04 where Seoul Textiles delivers.
        Perform a physical count to verify accuracy against the system count of 25000 units. The physical count revealed 24880 units.
        Calculate the variance between system count of 25000 and physical count of 24880.
        Since the variance is 0.48% which is below our 2% threshold, create an inventory adjustment of -120 units with reason being cycle
        count variance correction to align system with actual counts. Finally, update warehouse WH-04 accuracy metrics to reflect the audit results.""",
        actions=[
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1004"}
            ),
            Action(
                name="create_supplier_improvement_plan",
                kwargs={
                    "supplier_id": "SUP-1004",
                    "review_cycle_days": 90
                }
            ),
            Action(
                name="search_purchase_orders",
                kwargs={
                    "supplier_id": "SUP-1004",
                    "status": "pending"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                    "instruction_amount": 24880
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "system_count": 25000,
                    "physical_count": 24880
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                    "adjustment_quantity": -120,
                    "reason": "cycle count variance correction"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-04"}
            )
        ],
        outputs=[
            '"performance_rating": 4.5',
            '"variance_percentage": 0.48',
            '"total_adjustment_value": 960.00'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_59",
        instruction="""Investigate temperature excursion alert for pharmaceutical shipment SHIP-0021 from Stockholm containing life-saving
        drugs valued at 550000. The shipment was transported by SAS Cargo and requires immediate assessment due to cold chain integrity concerns.
        First get detailed shipment information, then check temperature logs to verify if storage remained within required 2-8C range during
        transit with excursions flag set to true due to reported deviations. Document that carrier SAS maintained standard cold chain protocols
        for this critical pharmaceutical cargo. The physical inspection revealed temperature deviations, so immediately quarantine
        the affected lot LOT202405H at destination warehouse WH-06 with reason "Temperature excursion detected - pharmaceutical cold chain
        breach requiring quality review". Create a high severity incident report with incident type cold_chain_failure for this
        temperature control breach. Notify supplier SUP-1021 of this quality incident requiring immediate corrective action.
        Calculate financial exposure including the full shipment value of 550000 plus estimated liability of 100000 for potential product loss.
        Finally, escalate this critical quality issue to the quality assurance team using the generated incident report ID with
        critical priority level.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0021"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0021",
                    "required_temp_range": "2-8C",
                    "excursions_flag": True
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0021",
                    "carrier_scac": "SAS"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405H",
                    "warehouse_id": "WH-06",
                    "reason": "Temperature excursion detected - pharmaceutical cold chain breach requiring quality review"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0021",
                    "incident_type": "cold_chain_failure",
                    "severity": "high"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "notification_type": "quality_incident"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 550000,
                    "liability_estimate": 100000
                }
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={
                    "incident_id": "INC-SHIP-0021-high",
                    "priority": "critical"
                }
            )
        ],
        outputs=[
            '"shipment_value": 550000',
            '"temperature_compliance": "non-compliant"',
            '"cold_chain_integrity": "maintained"',
            '"quarantine_status": "Quarantined"',
            '"incident_id": "INC-SHIP-0021-high"',
            '"total_financial_impact": 650000',
            '"escalation_priority": "critical"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_60",
        instruction="""Address capacity crisis at WH-10 San Francisco Fresh Foods DC which is currently at 95.5% utilization approaching
        maximum safe limits. The facility is receiving high-value frozen seafood including shipment SHIP-0010 from
        Sydney Seafood Exporters (SUP-1010) containing premium tuna valued at 180000. First assess current warehouse capacity and utilization
        levels at WH-10. Check details of the incoming seafood shipment SHIP-0010 to understand space requirements.
        Review supplier SUP-1010 performance metrics to ensure reliable delivery scheduling. Since utilization exceeds 95%,
        identify up to 2 overflow warehouse options that can accommodate at least 2500 cbm of frozen storage and support frozen seafood handling.
        Analyze current inventory breakdown by category to identify optimization opportunities, ensuring frozen seafood is accounted for.
        The critical frozen tuna inventory FOOD-FISH-H8 requires immediate verification - perform physical count with instruction amount of 2400 units.
        Calculate inventory variance between system count of 2500 and the physical count of 2400 units. Due to the shortage of 100 units,
        create inventory adjustment of -100 units with reason 'Physical count variance correction for frozen seafood'.
        Create capacity management plan using frozen_goods_optimization strategy to address the space constraints.
        Finally, update warehouse accuracy metrics to reflect the inventory audit results.""",

        actions=[
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0010"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1010"}
            ),
            Action(
                name="identify_overflow_options",
                kwargs={"warehouse_id": "WH-10", "required_capacity": 2500}
            ),
            Action(
                name="analyze_inventory_by_category",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                    "instruction_amount": 2400
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "system_count": 2500,
                    "physical_count": 2400
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                    "adjustment_quantity": -100,
                    "reason": "Physical count variance correction for frozen seafood"
                }
            ),
            Action(
                name="create_capacity_plan",
                kwargs={
                    "warehouse_id": "WH-10",
                    "optimization_strategy": "frozen_goods_optimization"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-10"}
            )
        ],

        outputs=[
            '"current_utilization_percentage": 95.5',
            '"remaining_capacity_cbm": 990',
            '"shipment_value": 180000',
            '"supplier_rating": 4.9',
            '"overflow_options_found": 2',
            '"system_count": 2500',
            '"physical_count": 2400',
            '"variance_percentage": 4.0',
            '"adjustment_amount": -100',
            '"plan_id": "CAP-WH-10"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_61",
        instruction="""Execute comprehensive supply chain recovery following disruption to Asian electronics suppliers.
        Critical smartphone inventory ELEC-SMART-W23 at WH-02 Seattle shows only 3500 units available against reorder point of 1000,
        but major customer orders require 5000 units minimum. Simultaneously, delayed shipment SHIP-0002 from supplier SUP-1002
        Tokyo Electronics valued at 125000 is impacting production schedules. Begin by checking current smartphone inventory levels at WH-02,
        then verify details of the delayed Tokyo shipment. Assess supplier SUP-1002 performance metrics.
        Since inventory is critically low, use SUP-1002 as primary supplier for ELEC-SMART-W23.
        Create emergency purchase order with primary supplier SUP-1002 for 2000
        units to WH-02 with Critical priority and note "Emergency procurement for customer fulfillment - supply chain disruption recovery".
        Verify carrier performance for NPEX Nippon Express to ensure reliable delivery.
        Request shipping quote for 800 kg smartphone shipment from Tokyo to Seattle with rate 3.20 per kg.
        Calculate total financial exposure including product value of 1998000 for the emergency order plus liability estimate of 150000 for potential delays.
        Perform physical count of current smartphone stock revealing 3450 units against system count of 3500.
        Calculate variance between system count 3500 and physical count 3450.
        Create inventory adjustment of -50 units with reason "Cycle count correction for smartphone inventory discrepancy".
        Search for any pending purchase orders from SUP-1002 to assess supply pipeline impact.
        Finally, create comprehensive capacity management plan using electronics_optimization strategy and update WH-02 accuracy metrics.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={"sku": "ELEC-SMART-W23", "warehouse_id": "WH-02"}
            ),
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0002"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1002"}
            ),
            Action(
                name="get_approved_suppliers",
                kwargs={"sku": "ELEC-SMART-W23", "preferred_supplier": "SUP-1002"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "sku": "ELEC-SMART-W23",
                    "quantity": 2000,
                    "destination_warehouse": "WH-02",
                    "priority": "Critical",
                    "notes": "Emergency procurement for customer fulfillment - supply chain disruption recovery"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "NPEX", "route": "Japan-USA"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "NPEX",
                    "weight_kg": 800,
                    "destination": "Seattle"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 1998000,
                    "liability_estimate": 150000
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "instruction_amount": 3450
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "instruction_system_count": 3500,
                    "physical_count": 3450
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "adjustment_quantity": -50,
                    "reason": "Cycle count correction for smartphone inventory discrepancy"
                }
            ),
            Action(
                name="search_purchase_orders",
                kwargs={"supplier_id": "SUP-1002", "status": "pending"}
            ),
            Action(
                name="create_capacity_plan",
                kwargs={
                    "warehouse_id": "WH-02",
                    "optimization_strategy": "electronics_optimization"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-02"}
            )
        ],
        outputs=[
            '"quantity_available": 3500',
            '"delayed_shipment_value": 125000',
            '"supplier_rating": 4.9',
            '"primary_supplier_found": "SUP-1002"',
            '"po_id": "PO-SUP-1002-ELEC-SMART-W23-001"',
            '"carrier_performance": 96.2',
            '"shipping_quote": 2400',
            '"total_financial_impact": 2148000',
            '"physical_count": 3450',
            '"variance_percentage": 1.43',
            '"adjustment_created": true',
            '"pending_orders_count": 0',
            '"optimization_plan_id": "CAP-WH-02"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_62",
        instruction="""Manage complex international shipment SHIP-0013 containing hazmat chemicals from Helsinki supplier SUP-1013
        with delivery delays causing supply chain bottlenecks. The shipment contains flammable industrial solvents valued at 600000
        requiring special handling protocols. First retrieve detailed shipment information for SHIP-0013, then check temperature logs
        to ensure hazmat storage remained within required range of 4-20C during transit. Verify that carrier HLCU Hapag-Lloyd maintained
        proper cold chain integrity for this chemical cargo. Since this involves hazmat class 3 materials, immediately quarantine the
        affected lot LOT202405E at destination warehouse WH-13 with reason "Hazmat inspection required for flammable chemical shipment
        pending safety clearance". Review supplier SUP-1013 performance including their rating.
        Calculate customs duty for the shipment value of 600000 from country of origin Finland with duty rate of 3.5 percent.
        Process duty payment of 21000 to clear customs. Update customs clearance status to Cleared for the shipment.
        Create high severity incident report with incident type chemical_handling for this hazmat compliance review.
        Calculate total financial exposure including product value of 600000 plus liability estimate of 75000 for handling delays.
        Search for any pending purchase orders from SUP-1013 to assess supply chain impact. Finally, escalate this chemical handling issue to
        quality team using incident ID INC-SHIP-0013-high with critical priority.""",

        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0013"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "required_temp_range": "4-20C"
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "carrier_scac": "HLCU"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405E",
                    "warehouse_id": "WH-13",
                    "reason": "Hazmat inspection required for flammable chemical shipment pending safety clearance"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1013"}
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "total_value": 600000,
                    "country_of_origin": "Finland"
                }
            ),
            Action(
                name="process_duty_payment",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "duty_amount": 21000
                }
            ),
            Action(
                name="update_customs_status",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "status": "Cleared"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0013",
                    "incident_type": "chemical_handling",
                    "severity": "high"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 600000,
                    "liability_estimate": 75000
                }
            ),
            Action(
                name="search_purchase_orders",
                kwargs={
                    "supplier_id": "SUP-1013",
                    "status": "pending"
                }
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={
                    "incident_id": "INC-SHIP-0013-high",
                    "priority": "critical"
                }
            )
        ],
        outputs=[
            '"shipment_value": 600000',
            '"temperature_compliance": "compliant"',
            '"cold_chain_integrity": "maintained"',
            '"quarantine_status": "active"',
            '"supplier_rating": 4.8',
            '"calculated_duty": 21000',
            '"duty_paid": 21000',
            '"customs_status": "Cleared"',
            '"incident_id": "INC-SHIP-0013-high"',
            '"total_financial_impact": 675000',
            '"pending_orders_found": 0',
            '"escalation_priority": "critical"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_64",
        instruction="""Process hazmat battery shipment SHIP-0019 from Warsaw containing lithium-ion batteries valued at 200000 requiring special handling protocols. Get shipment details, then check temperature logs to ensure storage stayed within safe operating range of 15-25C during transit. Verify carrier LOT maintained proper hazmat handling procedures for this Class 9 dangerous goods shipment. Since batteries contain hazmat materials, quarantine affected lot LOT202405G at warehouse WH-03 with reason "Hazmat safety inspection required for lithium-ion battery shipment compliance review". Review supplier SUP-1019 Warsaw IT Components performance including their 4.8 rating and 98.9% delivery record. Create high severity incident report with incident type battery_safety for this hazmat handling review. Calculate financial exposure including product value 200000 plus liability estimate 25000 for safety compliance costs. Check current battery inventory TECH-BATT-Q17 levels at WH-03 showing system count of 1500 units. Perform physical count revealing 1485 units. Calculate variance between system count 1500 and physical count 1485. Create inventory adjustment of -15 units with reason "Battery inventory audit correction for hazmat compliance". Finally, escalate this safety issue to quality team using incident ID INC-SHIP-0019-high with critical priority.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0019"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0019",
                    "required_temp_range": "15-25C"
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0019",
                    "carrier_scac": "LOT"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405G",
                    "warehouse_id": "WH-03",
                    "reason": "Hazmat safety inspection required for lithium-ion battery shipment compliance review"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1019"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0019",
                    "incident_type": "battery_safety",
                    "severity": "high"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 200000,
                    "liability_estimate": 25000
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03",
                    "instruction_amount": 1485
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                    "system_count": 1500,
                    "physical_count": 1485
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03",
                    "adjustment_quantity": -15,
                    "reason": "Battery inventory audit correction for hazmat compliance"
                }
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={
                    "incident_id": "INC-SHIP-0019-high",
                    "priority": "critical"
                }
            )
        ],
        outputs=[
            '"shipment_value": 200000',
            '"temperature_compliance": "compliant"',
            '"quarantine_status": "active"',
            '"supplier_rating": 4.8',
            '"incident_id": "INC-SHIP-0019-high"',
            '"total_financial_impact": 225000',
            '"physical_count": 1485',
            '"variance_percentage": 1.0',
            '"adjustment_amount": -15'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_65",
        instruction="""Coordinate furniture shipment SHIP-0015 from Bangkok containing teak dining chairs valued at 250000
        with delivery scheduling challenges. Retrieve shipment details first, then review supplier SUP-1015 Bangkok Furniture
        performance including their 4.4 rating and 95.0% delivery rate. Since delivery performance is below 96% threshold,
        create 60-day improvement plan for intensive monitoring due to scheduling inconsistencies. Verify carrier EGLV Evergreen maintained
        proper handling for this furniture cargo. Check current furniture inventory FURN-CHAIR-M13 at destination WH-14 showing 520 units available.
        Perform physical count revealing 515 units against system count of 520. Calculate variance between system count 520 and physical count 515.
        Since variance is 0.96%, create inventory adjustment of -5 units with reason "Furniture inventory cycle count adjustment for teak chair stock".
        Request shipping quote from EGLV for 19000 kg furniture shipment to Dallas.
        Calculate total logistics cost including shipment value 250000 plus additional handling fees of 15000.
        Search for pending furniture orders with this supplier to assess delivery pipeline.
        Finally, create capacity plan for WH-14 using furniture_optimization strategy to address space utilization.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0015"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1015"}
            ),
            Action(
                name="create_supplier_improvement_plan",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "review_cycle_days": 60,
                    "reason": "Scheduling inconsistencies requiring intensive monitoring"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "EGLV", "route": "Thailand-USA"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "FURN-CHAIR-M13", "warehouse_id": "WH-14"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "instruction_amount": 515
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "system_count": 520,
                    "physical_count": 515
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "adjustment_quantity": -5,
                    "reason": "Furniture inventory cycle count adjustment for teak chair stock"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "EGLV",
                    "weight_kg": 19000,
                    "destination": "Dallas"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 250000,
                    "liability_estimate": 15000
                }
            ),
            Action(
                name="search_purchase_orders",
                kwargs={"supplier_id": "SUP-1015", "status": "pending"}
            ),
            Action(
                name="create_capacity_plan",
                kwargs={
                    "warehouse_id": "WH-14",
                    "optimization_strategy": "furniture_optimization"
                }
            )
        ],
        outputs=[
            '"shipment_value": 250000',
            '"supplier_rating": 4.4',
            '"improvement_plan_created": true',
            '"carrier_performance": 93.5',
            '"quantity_available": 520',
            '"physical_count": 515',
            '"variance_percentage": 0.96',
            '"adjustment_amount": -5',
            '"shipping_quote": 57000',
            '"total_cost": 265000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_66",
        instruction="""Handle textile shipment SHIP-0020 from Cairo containing cotton bales valued at 210000 with quality concerns requiring inspection. Get shipment details, then review supplier SUP-1020 Cairo Cotton performance including their 4.5 rating and 97.1% delivery rate. Since quality concerns exist, quarantine lot LOT202404D at warehouse WH-04 with reason "Quality inspection required for cotton bale shipment pending fiber analysis". Check temperature logs to ensure cotton storage remained within safe range of 20-25C during transport. Verify carrier MAEU Maersk maintained proper cargo handling for this textile shipment. Check current cotton inventory MATR-COTT-R18 levels at WH-04. Perform physical count revealing 198 units. Calculate variance between the system inventory count and the physical count of 198. Create inventory adjustment based on the calculated variance with reason "Cotton inventory audit for textile quality control process". Calculate customs duty for shipment value 210000 from country of origin Egypt. Process the calculated duty payment amount for customs clearance. Update customs status to Cleared for the shipment. Finally, calculate total financial impact including product value 210000 plus quality inspection costs of 12000.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0020"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1020"}
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202404D",
                    "warehouse_id": "WH-04",
                    "reason": "Quality inspection required for cotton bale shipment pending fiber analysis"
                }
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0020",
                    "required_temp_range": "20-25C"
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0020",
                    "carrier_scac": "MAEU"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "MATR-COTT-R18", "warehouse_id": "WH-04"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "instruction_amount": 198
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "system_count": 200,
                    "physical_count": 198
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "adjustment_quantity": -2,
                    "reason": "Cotton inventory audit for textile quality control process"
                }
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={
                    "shipment_id": "SHIP-0020",
                    "total_value": 210000,
                    "country_of_origin": "Egypt"
                }
            ),
            Action(
                name="process_duty_payment",
                kwargs={
                    "shipment_id": "SHIP-0020",
                    "duty_amount": 7350
                }
            ),
            Action(
                name="update_customs_status",
                kwargs={
                    "shipment_id": "SHIP-0020",
                    "status": "Cleared"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 210000,
                    "liability_estimate": 12000
                }
            )
        ],
        outputs=[
            '"shipment_value": 210000',
            '"supplier_rating": 4.5',
            '"quarantine_status": "active"',
            '"temperature_compliance": "compliant"',
            '"quantity_on_hand": 200',
            '"physical_count": 198',
            '"variance_percentage": 1.0',
            '"duty_amount": 7350',
            '"customs_status": "Cleared"',
            '"total_financial_impact": 222000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_67",
        instruction="""Handle critical temperature excursion for pharmaceutical shipment SHIP-0021 containing life-saving drugs from Stockholm.
        Check shipment details showing 500 units valued at 550000. Review supplier SUP-1021 Stockholm Pharma performance with their 4.9
        rating and 99.7% delivery rate. Check temperature logs for required range 2-8C and verify SAS carrier maintained cold chain integrity.
        Current inventory shows PHRM-DRUG-S19 in WH-06 has 500 units available. Perform physical count revealing 398 units.
        Calculate variance between system count 500 and physical count 398. Create inventory adjustment of -102 units with reason
        "Temperature monitoring audit for pharmaceutical compliance". Since temperature excursion detected, quarantine lot LOT202405H at WH-06
        with reason "Cold chain breach investigation pending regulatory review". Create incident report for product damage with high severity.
        Notify supplier SUP-1021 about quality incident. Calculate financial impact including product value 550000 plus regulatory
        investigation costs of 25000. Finally escalate incident INC-SHIP-0021-high to quality team with critical priority.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0021"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1021"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0021",
                    "required_temp_range": "2-8C",
                    "excursions_flag": True
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0021",
                    "carrier_scac": "SAS"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "PHRM-DRUG-S19", "warehouse_id": "WH-06"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06",
                    "instruction_amount": 398
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                    "system_count": 500,
                    "physical_count": 398
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06",
                    "adjustment_quantity": -102,
                    "reason": "Temperature monitoring audit for pharmaceutical compliance"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405H",
                    "warehouse_id": "WH-06",
                    "reason": "Cold chain breach investigation pending regulatory review"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0021",
                    "incident_type": "product_damage",
                    "severity": "high"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "notification_type": "quality_incident"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 550000,
                    "liability_estimate": 25000
                }
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={
                    "incident_id": "INC-SHIP-0021-high",
                    "priority": "critical"
                }
            )
        ],
        outputs=[
            '"shipment_value": 550000',
            '"supplier_rating": 4.9',
            '"excursions_detected": true',
            '"variance_percentage": 20.4',
            '"quarantine_status": "active"',
            '"total_financial_impact": 575000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_68",
        instruction="""Optimize inventory distribution for ELEC-SMART-W23 smartphones across West Coast facilities.
        Check current inventory at WH-02 Seattle showing 3500 units available. Review WH-02 Seattle capacity showing 92.1% utilization
        approaching limits. Check single primary supplier SUP-1030 Dubai Electronics performance with 4.7 rating for potential emergency replenishment.
        Analyze inventory by category at WH-09 Phoenix warehouse to identify overflow capacity. Calculate current utilization at WH-09
        showing 85.0% usage. Since WH-02 is over 90% capacity, identify overflow options requiring 2000 units additional capacity.
        Create capacity optimization plan for WH-09 using redistribute_slow_moving strategy.
        Check warehouse capacity at WH-01 showing 78.5% utilization with remaining space available.
        Generate emergency purchase order for 1500 units from SUP-1030 to WH-01 with High priority and note about West Coast inventory
        rebalancing requirements. Get primary supplier status for ELEC-SMART-W23 to verify single supplier qualification. Request shipping quote from
        Emirates SkyCargo UAE for 1500kg shipment to Los Angeles, USA. Get carrier performance for UAE carrier including their 98.1% delivery rate.
        Select optimal carrier for Los Angeles, USA destination with High priority considering 1500kg weight, preferring UAE carrier.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={"sku": "ELEC-SMART-W23", "warehouse_id": "WH-02"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-02"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1030"}
            ),
            Action(
                name="analyze_inventory_by_category",
                kwargs={"warehouse_id": "WH-09"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-09"}
            ),
            Action(
                name="identify_overflow_options",
                kwargs={"warehouse_id": "WH-02", "required_capacity": 2000}
            ),
            Action(
                name="create_capacity_plan",
                kwargs={"warehouse_id": "WH-09", "optimization_strategy": "redistribute_slow_moving"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1030",
                    "sku": "ELEC-SMART-W23",
                    "quantity": 1500,
                    "destination_warehouse": "WH-01",
                    "priority": "High",
                    "notes": "West Coast inventory rebalancing requirements"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1030"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "UAE",
                    "weight_kg": 1500,
                    "destination": "Los Angeles"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "UAE"}
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_city": "Los Angeles",
                    "destination_country": "USA",
                    "priority_level": "High",
                    "total_weight_kg": 1500,
                    "preferred_carrier": "UAE"
                }
            )
        ],
        outputs=[
            '"quantity_available": 3500',
            '"current_utilization_percentage": 92.1',
            '"supplier_rating": 4.7',
            '"utilization_percentage": 85.0',
            '"total_cost": 1498500',
            '"primary_supplier_verified": "SUP-1030"',
            '"estimated_cost": 4500',
            '"on_time_delivery_percentage": 98.1'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_69",
        instruction="""Process temperature-sensitive pharmaceutical shipment SHIP-0006 containing vaccines from Mumbai.
        Get shipment details showing 150 packages valued at 450000. Review supplier SUP-1006 Mumbai Pharma performance with their 4.9
        rating and 99.8% delivery rate. Check temperature logs for required range 2-8C to ensure vaccine integrity.
        Verify UAE Emirates SkyCargo maintained cold chain during transport. Check current vaccine inventory PHRM-VACC-D4 at
        destination WH-06 showing 18000 units available. Perform physical count revealing 17950 units. Calculate variance between
        system count 18000 and physical count 17950. Create inventory adjustment of -50 units with reason "Pre-receipt vaccine inventory verification
        for quality compliance". Calculate customs duty for shipment value 450000 from country India. Process duty payment of 15750 for
        customs clearance. Update customs status to Cleared. Create incident report for temperature monitoring with medium severity.
        Calculate financial impact including product value 450000 plus compliance verification costs of 8000.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0006"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1006"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "required_temp_range": "2-8C"
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "carrier_scac": "UAE"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "PHRM-VACC-D4", "warehouse_id": "WH-06"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "instruction_amount": 17950
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "system_count": 18000,
                    "physical_count": 17950
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "adjustment_quantity": -50,
                    "reason": "Pre-receipt vaccine inventory verification for quality compliance"
                }
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "total_value": 450000,
                    "country_of_origin": "India"
                }
            ),
            Action(
                name="process_duty_payment",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "duty_amount": 15750
                }
            ),
            Action(
                name="update_customs_status",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "status": "Cleared"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0006",
                    "incident_type": "temperature_monitoring",
                    "severity": "medium"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 450000,
                    "liability_estimate": 8000
                }
            )
        ],
        outputs=[
            '"number_of_packages": 150',
            '"supplier_rating": 4.9',
            '"temperature_compliance": "compliant"',
            '"quantity_available": 18000',
            '"variance_percentage": 0.28',
            '"duty_amount": 15750',
            '"total_financial_impact": 458000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_70",
        instruction="""Handle hazmat chemical shipment SHIP-0013 containing
        flammable liquids from Helsinki. Get shipment details showing 400 packages valued at 600000.
        Review supplier SUP-1013 Helsinki Chemicals performance with their 4.8 rating and 99.2% delivery rate.
        Check temperature logs for required range 4-20C for chemical stability. Verify Hapag-Lloyd HLCU carrier maintained proper
        hazmat handling procedures. Check current chemical inventory CHEM-SOLV-K11 at WH-13 showing 380 units available.
        Calculate warehouse utilization at WH-13 to ensure hazmat storage capacity. Perform physical count revealing 378 units.
        Calculate variance between system count 380 and physical count 378. Create inventory adjustment of -2 units with reason
        "Hazmat inventory audit for regulatory compliance verification". Since this is hazmat class 3 shipment, quarantine lot LOT202405E at
        WH-13 with reason "Hazmat class 3 inspection required per OSHA regulations". Calculate customs duty for shipment value 600000 from
        country Finland. Update customs status to Cleared. Calculate total financial impact including product value 600000 plus hazmat
        compliance costs of 15000.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0013"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1013"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "required_temp_range": "4-20C"
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "carrier_scac": "HLCU"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "CHEM-SOLV-K11", "warehouse_id": "WH-13"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-13"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "instruction_amount": 378
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "system_count": 380,
                    "physical_count": 378
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "adjustment_quantity": -2,
                    "reason": "Hazmat inventory audit for regulatory compliance verification"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405E",
                    "warehouse_id": "WH-13",
                    "reason": "Hazmat class 3 inspection required per OSHA regulations"
                }
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "total_value": 600000,
                    "country_of_origin": "Finland"
                }
            ),
            Action(
                name="update_customs_status",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "status": "Cleared"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 600000,
                    "liability_estimate": 15000
                }
            )
        ],
        outputs=[
            '"hazmat_class": "3"',
            '"supplier_rating": 4.8',
            '"quantity_available": 378',
            '"utilization_percentage": 70.0',
            '"variance_percentage": 0.53',
            '"duty_amount": 21000',
            '"total_financial_impact": 615000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_71",
        instruction="""Check solar panel inventory TECH-SOLR-G7 at WH-09 Phoenix showing 1100 units available.
        Since available stock 1100 is below reorder point 250, create purchase order for 600 units priced at $299.99 from SUP-1009 Beijing Solar
        Tech with Medium priority and note about renewable energy project requirements. Review supplier SUP-1009 performance including
        their 4.5 rating and 96.5% delivery rate. Search for existing inbound shipments of TECH-SOLR-G7 to WH-09 to check pipeline inventory.
        Get warehouse capacity at WH-09 showing 85.0% utilization to confirm space availability.
        Finally calculate total cost for the 600-unit purchase order.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={"sku": "TECH-SOLR-G7", "warehouse_id": "WH-09"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1009",
                    "sku": "TECH-SOLR-G7",
                    "quantity": 600,
                    "destination_warehouse": "WH-09",
                    "priority": "Medium",
                    "notes": "Renewable energy project requirements",
                    "unit_price": 299.99
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1009"}
            ),
            Action(
                name="search_inbound_shipments",
                kwargs={"sku": "TECH-SOLR-G7", "destination_warehouse_id": "WH-09"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-09"}
            )
        ],
        outputs=[
            '"quantity_available": 1100',
            '"supplier_rating": 4.5',
            '"current_inbound": 600',
            '"total_cost": 179994'
        ]
    ),

     Task(
        annotator="0",
        user_id="V5TSK_USR_72",
        instruction="""Inspect luxury handbag shipment SHIP-0007 from Paris containing designer goods.
        Get shipment details showing 12 packages valued at 90000. Review supplier SUP-1007 Paris Luxury Goods performance with their 4.7
        rating and 98.5% delivery rate. Check current handbag inventory APRL-BAG-E5 at destination WH-07 showing 120 units available.
        Perform physical count revealing 119 units against system baseline of 120 units with quantity available flag set to true. Calculate variance between system count 120 and physical count 119.
        Create inventory adjustment of -1 unit with reason "Luxury goods quality inspection discrepancy".
        Verify FedEx FDEG carrier performance.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0007"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1007"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "APRL-BAG-E5", "warehouse_id": "WH-07"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                    "instruction_amount": 119,
                    "quantity_available_flag": True
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "system_count": 120,
                    "instruction_count": 119
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                    "adjustment_quantity": -1,
                    "reason": "Luxury goods quality inspection discrepancy"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "FDEG"}
            )
        ],
        outputs=[
            '"number_of_packages": 12',
            '"supplier_rating": 4.7',
            '"quantity_available": 120',
            '"on_time_delivery_percentage": 97.5'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_73",
        instruction="""Process textile order ORD-0005 for Canadian fashion retailer. Get order details showing shipment to Toronto with
        750kg total weight. Verify inventory allocation status for the order. Check current t-shirt inventory APRL-TSHT-O15 at source WH-04
        showing 22000 units available. Select UPSN as carrier for Canada destination with Medium priority considering 750kg weight.
        Generate shipping labels using UPS UPSN carrier for the order. Update order status to Shipped. Request shipping quote from UPS
        for 750kg shipment to Toronto to confirm shipping costs.""",
        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0005"}
            ),
            Action(
                name="verify_inventory_allocation",
                kwargs={"order_id": "ORD-0005"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "APRL-TSHT-O15", "warehouse_id": "WH-04"}
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_city": "Toronto",
                    "destination_country": "Canada",
                    "priority_level": "Medium",
                    "total_weight_kg": 750,
                    "preferred_carrier": "UPSN"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={"order_id": "ORD-0005", "carrier_scac": "UPSN"}
            ),
            Action(
                name="update_order_status",
                kwargs={"order_id": "ORD-0005", "new_status": "Shipped"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "UPSN",
                    "weight_kg": 750,
                    "destination": "Toronto"
                }
            )
        ],
        outputs=[
            '"customer_name": "Epsilon Fashion Co."',
            '"allocation_status": "fully_allocated"',
            '"quantity_available": 22000',
            '"selected_carrier": "UPSN"',
            '"estimated_cost": 2400'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_74",
        instruction="""Process urgent international shipment SHIP-0013 from supplier SUP-1013
        containing hazmat SKU CHEM-SOLV-K11 bound for warehouse WH-13. Verify customs documentation completeness,
        calculate customs duty for total value 600000 from origin country Finland. Process duty payment amount 15000,
        update customs status to "Cleared", then update shipment status to "Ready for Delivery". Get performance data for carrier MAEU,
        request shipping quote for weight 16000 kg to destination "Cleveland, USA" from MAEU carrier. Report customs clearance completion and
        estimated shipping cost.""",

        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0013"}
            ),
            Action(
                name="verify_customs_documentation",
                kwargs={"shipment_id": "SHIP-0013"}
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "total_value": 600000,
                    "country_of_origin": "Finland"
                }
            ),
            Action(
                name="process_duty_payment",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "duty_amount": 15000
                }
            ),
            Action(
                name="update_customs_status",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "status": "Cleared"
                }
            ),
            Action(
                name="update_shipment_status",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "status": "Ready for Delivery"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "MAEU"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "MAEU",
                    "weight_kg": 16000,
                    "destination": "Cleveland, USA"
                }
            )
        ],

        outputs=[
            '"customs_clearance_status": "Cleared"',
            '"estimated_cost": 40000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_75",
        instruction="""Emergency mining equipment shortage detected: SKU HEVY-DRIL-I9
        in warehouse WH-11 has fallen to critical levels. Check current inventory details,
        perform physical count with instruction amount 32, calculate inventory variance between system count 40 and physical count 32.
        Create inventory adjustment with quantity -8 for reason "Physical count discrepancy correction".
        Get approved suppliers for SKU HEVY-DRIL-I9, assess supplier SUP-1011 performance rating.
        Since rating below threshold, create 90-day improvement plan with reason "Performance below 4.5 threshold requires improvement".
        Create emergency purchase order for quantity 25 units to supplier SUP-1011 for warehouse WH-11 with priority "Critical" and
        notes "Emergency replenishment for mining operations". Report total adjustment value and improvement plan status.""",

        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "instruction_amount": 32
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "system_count": 40,
                    "physical_count": 32
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "adjustment_quantity": -8,
                    "reason": "Physical count discrepancy correction"
                }
            ),
            Action(
                name="get_approved_suppliers",
                kwargs={"sku": "HEVY-DRIL-I9"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1011"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1011",
                    "sku": "HEVY-DRIL-I9",
                    "quantity": 25,
                    "destination_warehouse": "WH-11",
                    "priority": "Critical",
                    "notes": "Emergency replenishment for mining operations"
                }
            ),
            Action(
                name="create_supplier_improvement_plan",
                kwargs={
                    "supplier_id": "SUP-1011",
                    "review_cycle_days": 90,
                    "reason": "Performance below 4.5 threshold requires improvement"
                }
            ),
        ],
        outputs=[
            '"total_adjustment_value": 17600',
            '"improvement_plan_status": "Created"',
            '"po_id": "PO-SUP-1011-HEVY-DRIL-I9-001"',
            '"total_cost": 87500'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_76",
        instruction="""Critical pharmaceutical shipment SHIP-0006 containing vaccines SKU PHRM-VACC-D4 from
        supplier SUP-1006 requires cold chain verification for warehouse WH-06. Get shipment details, check temperature logs for
        required range "2-8C", verify cold chain integrity with carrier UAE, get supplier SUP-1006 performance rating,
        update shipment status to "Cleared for Receipt", update customs status to "Cleared", and
        create incident report with low severity and incident type 'for_monitoring'.
        calculate financial impact with product value 125000 and liability estimate 25000.
        Report temperature compliance and total financial exposure.""",

        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0006"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "required_temp_range": "2-8C"
                }
            ),
            Action(
                name="verify_cold_chain_integrity",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "carrier_scac": "UAE"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1006"}
            ),
            Action(
                name="update_shipment_status",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "status": "Cleared for Receipt"
                }
            ),
            Action(
                name="update_customs_status",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "status": "Cleared"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0006",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 125000,
                    "liability_estimate": 25000
                }
            )
        ],

        outputs=[
            '"temperature_compliance": "maintained"',
            '"total_financial_exposure": 150000',
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_77",
        instruction="""Process high-value luxury shipment SHIP-0007 containing SKU APRL-BAG-E5 from supplier SUP-1007 bound
        for secure warehouse WH-07. Get shipment details, verify customs documentation completeness, calculate customs duty
        for total value 90000 from origin country France. Process duty payment amount 3150, update customs status to "Cleared",
        get supplier SUP-1007 performance rating, and quarantine inventory with lot number LOT202403E in warehouse WH-07 for reason
        "High-value security verification". Report customs clearance status and supplier rating.""",

        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0007"}
            ),
            Action(
                name="verify_customs_documentation",
                kwargs={"shipment_id": "SHIP-0007"}
            ),
            Action(
                name="calculate_customs_duty",
                kwargs={
                    "shipment_id": "SHIP-0007",
                    "total_value": 90000,
                    "country_of_origin": "France"
                }
            ),
            Action(
                name="process_duty_payment",
                kwargs={
                    "shipment_id": "SHIP-0007",
                    "duty_amount": 3150
                }
            ),
            Action(
                name="update_customs_status",
                kwargs={
                    "shipment_id": "SHIP-0007",
                    "status": "Cleared"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1007"}
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202403E",
                    "warehouse_id": "WH-07",
                    "reason": "High-value security verification"
                }
            )
        ],

        outputs=[
            '"customs_clearance_status": "Cleared"',
            '"supplier_rating": 4.7',
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_78",
        instruction="""Optimize shipping for urgent international order ORD-0002 from warehouse WH-02 to
        destination Hamburg, Germany. Get order details, verify inventory allocation, get performance data for carriers MAEU and DBSG,
        request shipping quotes for weight 980 kg to destination "Hamburg, Germany" from both carriers MAEU and DBSG.
        Select DBSG as carrier to Germany, priority level High, and weight 980 kg.
        Generate shipping labels for selected carrier DBSG and update order status to "Shipped".
        Report selected carrier, performance between MAEU and DBSG, and estimated shipping cost.""",

        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0002"}
            ),
            Action(
                name="verify_inventory_allocation",
                kwargs={"order_id": "ORD-0002"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "MAEU"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "DBSG"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "MAEU",
                    "weight_kg": 980,
                    "destination": "Hamburg, Germany"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "DBSG",
                    "weight_kg": 980,
                    "destination": "Hamburg, Germany"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "Germany",
                    "priority_level": "High",
                    "total_weight_kg": 980,
                    "preferred_carrier": "DBSG"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0002",
                    "carrier_scac": "DBSG"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0002",
                    "new_status": "Shipped"
                }
            )
        ],

        outputs=[
            '"selected_carrier": "DBSG"',
            '"estimated_cost": 1764',
            '"ontime_delivery_percentage_maeu": 94.5',
            '"ontime_delivery_percentage_dbsg": 95.8',
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_79",
        instruction="""Warehouse WH-09 approaching capacity limits with solar panel inventory.
        Check warehouse WH-09 capacity and utilization percentage, get inventory details for SKU TECH-SOLR-G7
        in warehouse WH-09, perform physical count with instruction amount 1050 against system count 1200,
        calculate inventory variance between system count 1200 and physical count 1050.
        Create inventory adjustment with quantity -150 for reason "Physical count correction for transfer preparation"
        with unit cost 180.00 per panel, then create capacity plan with optimization strategy "inventory_redistribution"
        for WH-09. Report adjustment value.""",

        actions=[
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-09"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-09"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "instruction_amount": 1050
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "system_count": 1200,
                    "physical_count": 1050
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "adjustment_quantity": -150,
                    "reason": "Physical count correction for transfer preparation",
                    "unit_cost": 180.00
                }
            ),
            Action(
                name="create_capacity_plan",
                kwargs={
                    "warehouse_id": "WH-09",
                    "optimization_strategy": "inventory_redistribution",
                }
            )
        ],

        outputs=[
            '"adjustment_value": 27000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_80",
        instruction="""Damaged goods discovered in warehouse WH-12 for SKU BLDG-TILE-J10 from supplier SUP-1012.
        Get inventory details for SKU BLDG-TILE-J10 in warehouse WH-12, quarantine inventory with lot number
        LOT202404A in warehouse WH-12 for reason "Damaged goods quality control hold". Get supplier SUP-1012 performance rating,
        create supplier improvement plan with review cycle 90 days and reason "Quality issues require immediate attention".
        Notify supplier SUP-1012 with notification type "quality_incident", create incident report for
        shipment SHIP-0012 with incident type "product_damage" and severity "medium".
        Report quarantine status and supplier improvement plan ID.""",

        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202404A",
                    "warehouse_id": "WH-12",
                    "reason": "Damaged goods quality control hold"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1012"}
            ),
            Action(
                name="create_supplier_improvement_plan",
                kwargs={
                    "supplier_id": "SUP-1012",
                    "review_cycle_days": 90,
                    "reason": "Quality issues require immediate attention"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1012",
                    "notification_type": "quality_incident"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0012",
                    "incident_type": "product_damage",
                    "severity": "medium"
                }
            )
        ],

        outputs=[
            '"quarantine_status": "Quarantined"',
            '"improvement_plan_id": "SIP-SUP-1012"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_81",
        instruction="""Critical shortage detected for SKU AUTO-GLAS-U21 in warehouse WH-03 below safety stock.
        Get inventory details for SKU AUTO-GLAS-U21 in warehouse WH-03, get approved suppliers for SKU AUTO-GLAS-U21,
        get supplier SUP-1023 performance rating, create emergency purchase order for quantity 100 units to supplier SUP-1023 for
        warehouse WH-03 with priority "Critical" and notes "Emergency replenishment - safety stock breach". Get carrier performance
        for UPSN, select optimal carrier for destination country USA, priority level Critical, and weight 1400 kg.
        Report emergency order status and selected carrier.""",

        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03"
                }
            ),
            Action(
                name="get_approved_suppliers",
                kwargs={"sku": "AUTO-GLAS-U21"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1023"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "quantity": 100,
                    "supplier_id": "SUP-1023",
                    "sku": "AUTO-GLAS-U21",
                    "destination_warehouse": "WH-03",
                    "priority": "Critical",
                    "notes": "Emergency replenishment - safety stock breach"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "UPSN"}
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "USA",
                    "priority_level": "Critical",
                    "total_weight_kg": 1400
                }
            )
        ],

        outputs=[
            '"emergency_order_status": "Created"',
            '"selected_carrier": "UPSN"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_82",
        instruction="""Customer return received for order ORD-0003 due to quality defect. Get order details for ORD-0003, get inventory details for SKU BLDG-TILE-J10 in warehouse WH-12, quarantine inventory with lot number LOT202404A in warehouse WH-12 for reason "Customer return quality investigation". Create incident report for order ORD-0003 with incident type "customer_return" and severity "medium", get supplier SUP-1012 performance rating, notify supplier SUP-1012 with notification type "quality_incident". Report incident ID and quarantine confirmation.""",

        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0003"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202404A",
                    "warehouse_id": "WH-12",
                    "reason": "Customer return quality investigation"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "ORD-0003",
                    "incident_type": "customer_return",
                    "severity": "medium"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1012"}
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1012",
                    "notification_type": "quality_incident"
                }
            )
        ],

        outputs=[
            '"incident_id": "INC-ORD-0003-medium"',
            '"quarantine_confirmation": "Quarantined"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_83",
        instruction="""Urgent perishable shipment SHIP-0010 containing SKU FOOD-FISH-H8 from supplier SUP-1010 requires
        immediate processing for warehouse WH-10. Get shipment details, check temperature logs for required range "-5C to 0C",
        get supplier SUP-1010 performance rating, get carrier performance for QFA and UAE, request shipping quotes for weight 1200 kg
        to destination "San Francisco, USA" from both QFA and UAE carriers. Select optimal carrier for destination country USA,
        priority level High, and weight 1200 kg. Update shipment status to "Expedited Processing".
        Report temperature compliance and selected carrier.""",

        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0010"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0010",
                    "required_temp_range": "-5C to 0C"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1010"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "QFA"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "UAE"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "QFA",
                    "weight_kg": 1200,
                    "destination": "San Francisco, USA"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "UAE",
                    "weight_kg": 1200,
                    "destination": "San Francisco, USA"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "USA",
                    "priority_level": "High",
                    "total_weight_kg": 1200
                }
            ),
            Action(
                name="update_shipment_status",
                kwargs={
                    "shipment_id": "SHIP-0010",
                    "status": "Expedited Processing"
                }
            )
        ],

        outputs=[
            '"temperature_compliance": "maintained"',
            '"selected_carrier": "UAE"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_84",
        instruction="""Food safety alert for shipment SHIP-0005 containing SKU FOOD-COFF-C3 from supplier SUP-1005 bound
        for warehouse WH-05. Get shipment details, check temperature logs for required range "Cool, Dry",
        get supplier SUP-1005 performance rating, quarantine inventory with lot number LOT202405C in warehouse WH-05 for reason
        "Food safety investigation - temperature deviation". Create incident report for shipment SHIP-0005 with incident type
        "food_safety_alert" and severity "high", notify supplier SUP-1005 with notification type "quality_incident",
        calculate financial impact with product value 110000 and liability estimate 15000.
        Report quarantine status and total financial exposure.""",

        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0005"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0005",
                    "required_temp_range": "Cool, Dry"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1005"}
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405C",
                    "warehouse_id": "WH-05",
                    "reason": "Food safety investigation - temperature deviation"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0005",
                    "incident_type": "food_safety_alert",
                    "severity": "high"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1005",
                    "notification_type": "quality_incident"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 110000,
                    "liability_estimate": 15000
                }
            )
        ],

        outputs=[
            '"quarantine_status": "Quarantined"',
            '"total_financial_exposure": 125000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_85",
        instruction="""Security investigation for delivered order ORD-0001 containing high-value SKU ELEC-CHIP-A1 from warehouse WH-01.
        Get order details, get inventory details for SKU ELEC-CHIP-A1 in warehouse WH-01, get supplier SUP-1001 performance rating,
        get carrier performance for UPSN and FDEG, request shipping quotes for weight 450 kg to destination "San Jose, USA" from both
        UPSN and FDEG carriers. Select optimal carrier for destination country USA, priority level High, and weight 450 kg.
        Create incident report for order ORD-0001 with incident type "security_investigation" and severity "medium".
        Report selected carrier and incident ID.""",

        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0001"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1001"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "UPSN"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "FDEG"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "UPSN",
                    "weight_kg": 450,
                    "destination": "San Jose, USA"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "FDEG",
                    "weight_kg": 450,
                    "destination": "San Jose, USA"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_country": "USA",
                    "priority_level": "High",
                    "total_weight_kg": 450,
                    "carriers_list": ["UPSN", "FDEG"]
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "ORD-0001",
                    "incident_type": "security_investigation",
                    "severity": "medium"
                }
            )
        ],

        outputs=[
            '"selected_carrier": "UPSN"',
            '"incident_id": "INC-ORD-0001-medium"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_86",
        instruction="""Pharmaceutical compliance audit for SKU PHRM-DRUG-S19 in warehouse WH-06 from supplier SUP-1020 Cairo Cotton Co.
        Get inventory details for SKU PHRM-DRUG-S19 in warehouse WH-06, quarantine inventory with lot number LOT202405H
        in warehouse WH-06 for reason "GDP compliance audit verification". Get supplier SUP-1020 performance rating,
        create supplier improvement plan with review cycle 60 days and reason "Regulatory compliance enhancement required"
        returning improvement plan ID SIP-SUP-1020. Update accuracy metrics for warehouse WH-06, calculate financial impact with product value 600000 and liability estimate 50000.
        Create incident report with low severity and incident type 'compliance_monitoring'.
        Report supplier improvement plan id and financial exposure.""",

        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405H",
                    "warehouse_id": "WH-06",
                    "reason": "GDP compliance audit verification"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1020"}
            ),
            Action(
                name="create_supplier_improvement_plan",
                kwargs={
                    "supplier_id": "SUP-1020",
                    "review_cycle_days": 60,
                    "reason": "Regulatory compliance enhancement required"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-06"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 600000,
                    "liability_estimate": 50000
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "PHRM-DRUG-S19",
                    "incident_type": "compliance_monitoring",
                    "severity": "low"
                }
            )
        ],

        outputs=[
            '"improvement_plan_id": "SIP-SUP-1020"',
            '"total_financial_exposure": 650000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_87",
        instruction="""Hazmat emergency for shipment SHIP-0013 containing SKU CHEM-SOLV-K11 from supplier SUP-1013 bound for warehouse WH-13.
        Get shipment details, check temperature logs for required range "4-20C", quarantine inventory with lot number LOT202405E in
        warehouse WH-13 for reason "Hazmat emergency containment protocol". Create incident report for shipment SHIP-0013 with
        incident type "hazmat_emergency" and severity "critical", notify supplier SUP-1013 with notification type "quality_incident",
        escalate to quality team with priority "critical". Report incident status and escalation confirmation via escalation id.""",

        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0013"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "required_temp_range": "4-20C"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405E",
                    "warehouse_id": "WH-13",
                    "reason": "Hazmat emergency containment protocol"
                }
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0013",
                    "incident_type": "hazmat_emergency",
                    "severity": "critical"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1013",
                    "notification_type": "quality_incident"
                }
            ),
            Action(
                name="escalate_to_quality_team",
                kwargs={
                    "incident_id": "INC-SHIP-0013-critical",
                    "priority": "critical"
                }
            )
        ],

        outputs=[
            '"incident_status": "Created"',
            '"escalation_id": "ESC-INC-SHIP-0013-critical"'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_88",
        instruction="""Automotive quality control for SKU AUTO-GLAS-U21 in warehouse WH-03 from supplier SUP-1023.
        Get inventory details for SKU AUTO-GLAS-U21 in warehouse WH-03, perform physical count with instruction amount 175,
        calculate inventory variance between system count 180 and physical count 175. Create inventory adjustment with quantity -5 for reason
        "Quality control precision adjustment", get supplier SUP-1023 performance rating, create purchase order for quantity 50 units at unit price of $250
        to supplier SUP-1023 for warehouse WH-03 with priority "Medium" and notes "Quality-verified replacement stock".
        Report adjustment value and purchase order status plus total cost.""",

        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "instruction_amount": 175
                }
            ),
            Action(
                name="calculate_inventory_variance",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "system_count": 180,
                    "physical_count": 175
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "adjustment_quantity": -5,
                    "reason": "Quality control precision adjustment"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1023"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "quantity": 50,
                    "supplier_id": "SUP-1023",
                    "sku": "AUTO-GLAS-U21",
                    "destination_warehouse": "WH-03",
                    "priority": "Medium",
                    "notes": "Quality-verified replacement stock",
                    "unit_price": 250.00
                }
            )
        ],

        outputs=[
            '"adjustment_value": 750',
            '"purchase_order_status": "Created"',
            '"total_cost": 12500'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_89",
        instruction="""Process high-priority order ORD-0005 for Toronto destination.
        Get order details, verify inventory allocation for SKU MATR-COTT-R18 in warehouse WH-04,
        perform physical count, create inventory adjustment with quantity -20 and reason "picking damage",
        get carrier performance for UPSN, request shipping quote for 750 kg to destination "Toronto, Canada",
        generate shipping labels using UPSN, update order status to "Shipped", calculate financial impact with shipping value 120000
        and processing cost 2500.""",
        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0005"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-04",
                    "sku": "MATR-COTT-R18"
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "adjustment_quantity": -20,
                    "reason": "picking damage"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "UPSN"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "UPSN",
                    "weight_kg": 750,
                    "destination": "Toronto, Canada"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0005",
                    "carrier_scac": "UPSN"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0005",
                    "new_status": "Shipped"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 120000,
                    "liability_estimate": 2500
                }
            )
        ],
        outputs=[
            '"tracking_number": "UPSN-ORD-0005"',
            '"total_financial_cost": 122500'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_90",
        instruction="""Monitor temperature-controlled shipment SHIP-0010 containing SKU FOOD-FISH-H8
        from supplier SUP-1010. Get shipment details, check temperature logs for required range "-5C to 0C",
        get supplier performance rating, get warehouse capacity for destination WH-10, calculate utilization percentage for WH-10,
        create incident report with type "temperature_monitoring" and severity "low", update accuracy metrics for WH-10,
        calculate financial impact with product value 180000 and liability cost 5000.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0010"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0010",
                    "required_range": "-5C to 0C"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1010"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0010",
                    "incident_type": "temperature_monitoring",
                    "severity": "low"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 180000,
                    "liability_estimate": 5000
                }
            )
        ],
        outputs=[
            '"temperature_compliance": "compliant"',
            '"total_monitoring_cost": 185000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_91",
        instruction="""Process international electronics shipment for order ORD-0006 to Japan. Get order details,
        analyze inventory by category for warehouse WH-05, get carrier performance for MAEU and HLCU, request shipping quotes for
        550 kg to destination "Yokohama, Japan", select MAEU as carrier for destination Japan priority "Medium", generate shipping
        labels, update order status to "International Processing", calculate financial impact with order value 180000 and shipping cost 2800.""",
        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0006"}
            ),
            Action(
                name="analyze_inventory_by_category",
                kwargs={"warehouse_id": "WH-05"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "MAEU"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "HLCU"}
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "MAEU",
                    "weight_kg": 550,
                    "destination": "Yokohama, Japan"
                }
            ),
            Action(
                name="request_shipping_quote",
                kwargs={
                    "carrier_scac": "HLCU",
                    "weight_kg": 550,
                    "destination": "Yokohama, Japan"
                }
            ),
            Action(
                name="select_optimal_carrier",
                kwargs={
                    "destination_city": "Yokohama",
                    "destination_country": "Japan",
                    "priority_level": "Medium",
                    "preferred_carrier": "MAEU"
                }
            ),
            Action(
                name="generate_shipping_labels",
                kwargs={
                    "order_id": "ORD-0006",
                    "carrier_scac": "MAEU"
                }
            ),
            Action(
                name="update_order_status",
                kwargs={
                    "order_id": "ORD-0006",
                    "new_status": "International Processing"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 180000,
                    "liability_estimate": 2800
                }
            )
        ],
        outputs=[
            '"selected_carrier": "MAEU"',
            '"total_shipment_value": 182800'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_93",
        instruction="""Conduct cycle count audit for high-value electronics in warehouse WH-02.
        Get inventory details for SKU ELEC-SMART-W23 in WH-02, perform physical count, create inventory adjustment with
        quantity 100 and reason "cycle count correction", calculate utilization percentage for WH-02, get warehouse capacity,
        update accuracy metrics, create incident report with type "inventory_variance" and severity "medium" using "ELEC-SMART-W23" as id,
        calculate financial impact with variance value 65000 and audit cost 3500.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-02",
                    "sku": "ELEC-SMART-W23"
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "adjustment_quantity": 100,
                    "reason": "cycle count correction"
                }
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-02"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-02"}
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-02"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "ELEC-SMART-W23",
                    "incident_type": "inventory_variance",
                    "severity": "medium"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 65000,
                    "liability_estimate": 3500
                }
            )
        ],
        outputs=[
            '"inventory_accuracy": 100',
            '"total_audit_cost": 68500'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_94",
        instruction="""Monitor perishable goods approaching expiration in Houston food warehouse.
        Get inventory details for SKU FOOD-COFF-C3 in warehouse WH-05, perform physical count, calculate utilization percentage,
        create inventory adjustment with quantity -12 and reason "damaged_expired", quarantine inventory lot LOT202405C in
        WH-05 for reason "expiration_review", get warehouse capacity, create incident report with type "expiration_alert"
        and severity "medium", update accuracy metrics. Report incident and utilization percentage.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-05",
                    "sku": "FOOD-COFF-C3"
                }
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-05"}
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "adjustment_quantity": -12,
                    "reason": "damaged_expired"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405C",
                    "warehouse_id": "WH-05",
                    "reason": "expiration_review"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-05"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "FOOD-COFF-C3",
                    "incident_type": "expiration_alert",
                    "severity": "medium"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-05"}
            )
        ],
        outputs=[
            '"incident_id": INC-FOOD-COFF-C3-medium',
            '"warehouse_utilization": 75.0'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_95",
        instruction="""Process delayed textile shipment SHIP-0004 from Seoul supplier SUP-1004 to warehouse WH-04.
        Get shipment details, get supplier performance rating, create incident report with type "weather_delay" and severity "medium",
        get warehouse capacity for WH-04, calculate utilization percentage, create purchase order with SKU MATR-COTT-R18 quantity
        300 priority "High" for WH-04, get carrier performance for HJSC, calculate financial impact with delay cost 25000 and
        inventory impact 75000.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0004"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1004"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0004",
                    "incident_type": "weather_delay",
                    "severity": "medium"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-04"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-04"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1004",
                    "sku": "MATR-COTT-R18",
                    "quantity": 300,
                    "destination_warehouse": "WH-04",
                    "priority": "High"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "HJSC"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 75000,
                    "liability_estimate": 25000
                }
            )
        ],
        outputs=[
            '"incident_id": "INC-SHIP-0004-medium"',
            '"total_delay_impact": 100000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_96",
        instruction="""Coordinate auto parts shipment SHIP-0003 from Berlin supplier SUP-1003 to Chicago depot WH-03.
        Get shipment details, get supplier performance rating, get warehouse capacity, calculate utilization percentage,
        get inventory details for SKU AUTO-PAD-B2 in WH-03, perform physical count, create inventory adjustment with quantity 25 and
        reason "receiving_bonus", get carrier performance for DBSG, calculate financial impact with parts value 200000 and
        rail transport cost 12000. Report shipment arrival date and total shipment value.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0003"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1003"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-03"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-03"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "adjustment_quantity": 25,
                    "reason": "receiving_bonus"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "DBSG"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 200000,
                    "liability_estimate": 12000
                }
            )
        ],
        outputs=[
            '"delivery_date": "2024-06-15"',
            '"total_shipment_value": 212000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_97",
        instruction="""Process high-value watch parts shipment SHIP-0014 from Zurich supplier SUP-1014 to NYC vault WH-07.
        Get shipment details, verify storage compliance for high-security requirements, get supplier performance rating,
        create incident report with type "high_value_receipt" and severity "low", quarantine inventory lot LOT202406E in WH-07 for
        reason "security_verification", get carrier performance for UPSN, update accuracy metrics, calculate financial impact with parts
        value 50000 and security cost 5500. Report incident ID and total luxury value.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0014"}
            ),
            Action(
                name="verify_storage_compliance",
                kwargs={
                    "warehouse_id": "WH-07",
                    "storage_type": "high_security"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1014"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0014",
                    "incident_type": "high_value_receipt",
                    "severity": "low"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202406E",
                    "warehouse_id": "WH-07",
                    "reason": "security_verification"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "UPSN"}
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-07"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 50000,
                    "liability_estimate": 5500
                }
            )
        ],
        outputs=[
            '"incident_id": "INC-SHIP-0014-low"',
            '"total_luxury_value": 55500'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_98",
        instruction="""Manage furniture shipment SHIP-0015 from Bangkok supplier SUP-1015 arriving at Dallas warehouse WH-14.
        Get shipment details, get warehouse capacity, calculate utilization percentage, get supplier performance rating, analyze
        inventory by category, perform physical count for furniture items with SKU FURN-CHAIR-M13, create inventory adjustment with
        quantity -10 and reason "shipping_damage", notify supplier with type "damage_report", calculate financial
        impact with furniture value 250000 and damage cost 15000. Report warehouse utilization and physical count""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0015"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-14"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-14"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1015"}
            ),
            Action(
                name="analyze_inventory_by_category",
                kwargs={"warehouse_id": "WH-14"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "adjustment_quantity": -10,
                    "reason": "shipping_damage"
                }
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "notification_type": "damage_report"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 250000,
                    "liability_estimate": 15000
                }
            )
        ],
        outputs=[
            '"physical_count": "596"',
            '"utilization_percentage": 88.9'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_99",
        instruction="""Process in-transit electronics shipment SHIP-0001 from Shenzhen supplier SUP-1001 to LA center WH-01.
        Get shipment details showing expected arrival 2024-06-20, get supplier performance rating, get inventory details for SKU ELEC-CHIP-A1 in WH-01,
        perform physical count with 16000 units counted, create inventory adjustment with quantity 1000 and reason "bulk_receipt",
        get warehouse capacity showing 78.5% utilization, get carrier performance for MAEU Maersk, update accuracy metrics for WH-01,
        calculate financial impact with electronics value 350000 and import duty 28000. Report expected arrival date and total import cost.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0001"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1001"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1",
                    "instruction_amount": 16000
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "adjustment_quantity": 1000,
                    "reason": "bulk_receipt"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "MAEU"}
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-01"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 350000,
                    "liability_estimate": 28000
                }
            )
        ],
        outputs=[
            '"expected_arrival_date": "2024-06-20"',
            '"total_import_cost": 378000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_100",
        instruction="""Monitor critical seafood shipment SHIP-0027 from Reykjavik supplier SUP-1027
        requiring ultra-cold storage. Get shipment details, check temperature logs for required range
        "-18C to -15C" with excursion flag set true, get supplier performance rating, verify storage compliance for frozen requirements,
        quarantine inventory lot LOT202406F for reason "cold_chain_verification", get warehouse capacity for destination,
        create incident report with type "cold_chain_receipt" and severity "low", calculate financial impact with seafood value 180000
        and cold storage cost 9500. Report temperature compliance, incident id and total seafood investment.""",
        actions=[
            Action(
                name="get_shipment_details",
                kwargs={"shipment_id": "SHIP-0027"}
            ),
            Action(
                name="check_temperature_logs",
                kwargs={
                    "shipment_id": "SHIP-0027",
                    "required_range": "-18C to -15C",
                    "excursions_flag": True
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1027"}
            ),
            Action(
                name="verify_storage_compliance",
                kwargs={
                    "warehouse_id": "WH-10",
                    "storage_type": "frozen"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202406F",
                    "warehouse_id": "WH-10",
                    "reason": "cold_chain_verification"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-10"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "SHIP-0027",
                    "incident_type": "cold_chain_receipt",
                    "severity": "low"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 180000,
                    "liability_estimate": 9500
                }
            )
        ],
        outputs=[
            '"temperature_compliance": "non-compliant"',
            '"incident_id": "INC-SHIP-0027-low"',
            '"total_seafood_investment": 189500'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_101",
        instruction="""Process customer return for order ORD-0015 from Middle East shipment. Get order details,
        create incident report with type "customer_return" and severity "low",
        analyze category by inventory for returned items in warehouse WH-14, perform physical count for SKU FURN-CHAIR-M13, quarantine inventory lot LOT202402B
        in WH-14 for reason "return_inspection", calculate utilization percentage, get supplier performance for associated supplier SUP-1015,
        calculate financial impact with return value 45000 and processing cost 2200. Report incident id, incident status and total financial cost.""",
        actions=[
            Action(
                name="get_order_details",
                kwargs={"order_id": "ORD-0015"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "ORD-0015",
                    "incident_type": "customer_return",
                    "severity": "low"
                }
            ),
            Action(
                name="analyze_inventory_by_category",
                kwargs={"warehouse_id": "WH-14"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202402B",
                    "warehouse_id": "WH-14",
                    "reason": "return_inspection"
                }
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-14"}
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1015"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 45000,
                    "liability_estimate": 2200
                }
            )
        ],
        outputs=[
            '"incident_id": "INC-ORD-0015-low"',
            '"incident_status": "Created"',
            '"total_financial_impact": 47200'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_102",
        instruction="""Premium coffee procurement from São Paulo supplier SUP-1005.
        Get supplier performance rating, create purchase order with SKU FOOD-COFF-C3 quantity 1200 priority "Medium" for warehouse WH-05,
        get inventory details for SKU FOOD-COFF-C3 in WH-05, perform physical count,
        create inventory adjustment with quantity -12 and reason "quality_samples", get warehouse capacity, calculate utilization percentage,
        update accuracy metrics, calculate financial impact with coffee value 264000 and quality testing cost 6800. Report supplier performance rating and total cost.""",
        actions=[
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1005"}
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1005",
                    "sku": "FOOD-COFF-C3",
                    "quantity": 1200,
                    "destination_warehouse": "WH-05",
                    "priority": "Medium"
                }
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-05",
                    "sku": "FOOD-COFF-C3"
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "adjustment_quantity": -12,
                    "reason": "quality_samples"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-05"}
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-05"}
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-05"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 264000,
                    "liability_estimate": 6800
                }
            )
        ],
        outputs=[
            '"supplier_performance": "4.8"',
            '"total_commodity_investment": 270800'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_103",
        instruction="""High-value electronics assessment in Seattle facility. Get inventory details for SKU ELEC-SMART-W23 in warehouse WH-02,
        calculate utilization percentage, perform physical count, create inventory adjustment with quantity -10 and
        reason "shrinkage_investigation", verify storage compliance for electronics requirements, get warehouse capacity,
        create incident report with type "inventory_shrinkage" and severity "medium", update accuracy metrics, calculate financial
        impact with electronics value 2600000 and investigation cost 12000. Provide reports on utilization, count and financial impact.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02"
                }
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-02"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-02",
                    "sku": "ELEC-SMART-W23"
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "adjustment_quantity": -10,
                    "reason": "shrinkage_investigation"
                }
            ),
            Action(
                name="verify_storage_compliance",
                kwargs={
                    "warehouse_id": "WH-02",
                    "storage_type": "electronics"
                }
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-02"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "ELEC-SMART-W23",
                    "incident_type": "inventory_shrinkage",
                    "severity": "medium"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-02"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 2600000,
                    "liability_estimate": 12000
                }
            )
        ],
        outputs=[
            '"count": "3970"',
            '"utilization_percentage": 92.1',
            '"total_investigation_cost": 2612000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_104",
        instruction="""Lithium battery safety compliance check in Chicago depot with non-compliant hazmat storage. Get inventory details for SKU TECH-BATT-Q17 in warehouse WH-03,
        verify hazmat storage compliance expecting non-compliant status for WH-03, quarantine inventory lot LOT202405G in WH-03 for reason "safety_verification",
        perform physical count with 1450 units found, get supplier SUP-1020 performance rating showing 4.5 rating, create incident report with type "safety_compliance" and severity "low",
        update accuracy metrics for WH-03, calculate financial impact with battery value 82500 and compliance cost 5500.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                }
            ),
            Action(
                name="verify_storage_compliance",
                kwargs={
                    "warehouse_id": "WH-03",
                    "storage_type": "hazmat",
                    "compliant_flag": False
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202405G",
                    "warehouse_id": "WH-03",
                    "reason": "safety_verification"
                }
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17",
                    "instruction_amount": 1450
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1020"}
            ),
            Action(
                name="create_incident_report",
                kwargs={
                    "id": "TECH-BATT-Q17",
                    "incident_type": "safety_compliance",
                    "severity": "low"
                }
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-03"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 82500,
                    "liability_estimate": 5500
                }
            )
        ],
        outputs=[
            '"safety_compliance_status": "non_compliant"',
            '"incident_id": "INC-TECH-BATT-Q17-low"',
            '"total_battery_compliance_cost": 88000'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_105",
        instruction="""Ceramic tile inventory verification for construction project.
        Get inventory details for SKU BLDG-TILE-J10 in warehouse WH-12, get supplier SUP-1012 performance rating,
        perform physical count, create inventory adjustment with quantity 75 and reason "construction_delivery",
        quarantine inventory lot LOT202404A in WH-12 for reason "project_allocation", calculate utilization percentage,
        get warehouse capacity, update accuracy metrics, calculate financial impact with tile value 225000 and delivery cost 7800.
        Provide feedback on quarantine id and total construction cost.""",
        actions=[
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                }
            ),
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1012"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-12",
                    "sku": "BLDG-TILE-J10"
                }
            ),
            Action(
                name="create_inventory_adjustment",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                    "adjustment_quantity": 75,
                    "reason": "construction_delivery"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202404A",
                    "warehouse_id": "WH-12",
                    "reason": "project_allocation"
                }
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-12"}
            ),
            Action(
                name="get_warehouse_capacity",
                kwargs={"warehouse_id": "WH-12"}
            ),
            Action(
                name="update_accuracy_metrics",
                kwargs={"warehouse_id": "WH-12"}
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 225000,
                    "liability_estimate": 7800
                }
            )
        ],
        outputs=[
            '"quarantine_id": "QTN-LOT202404A-WH-12"',
            '"total_construction_cost": 232800'
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_106",
        instruction="""Urgent automotive parts sourcing from Berlin supplier SUP-1003.
        Get supplier performance rating, get inventory details for SKU AUTO-PAD-B2 in warehouse WH-03,
        calculate utilization percentage for WH-03, perform physical count, quarantine inventory lot
        LOT202403B in WH-03 for reason "batch_testing", create purchase order with SKU AUTO-PAD-B2 quantity 400 priority
        "High" for WH-03, get carrier performance for DBSG, notify supplier with type "urgent_order", calculate financial
        impact with parts value 180000 and testing cost 8500. Report purchase order ID and total automotive cost.""",
        actions=[
            Action(
                name="get_supplier_performance",
                kwargs={"supplier_id": "SUP-1003"}
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03"
                }
            ),
            Action(
                name="calculate_utilization_percentage",
                kwargs={"warehouse_id": "WH-03"}
            ),
            Action(
                name="perform_physical_count",
                kwargs={
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                }
            ),
            Action(
                name="quarantine_inventory",
                kwargs={
                    "lot_number": "LOT202403B",
                    "warehouse_id": "WH-03",
                    "reason": "batch_testing"
                }
            ),
            Action(
                name="create_purchase_order",
                kwargs={
                    "supplier_id": "SUP-1003",
                    "sku": "AUTO-PAD-B2",
                    "quantity": 400,
                    "destination_warehouse": "WH-03",
                    "priority": "High"
                }
            ),
            Action(
                name="get_carrier_performance",
                kwargs={"carrier_scac": "DBSG"}
            ),
            Action(
                name="notify_supplier",
                kwargs={
                    "supplier_id": "SUP-1003",
                    "notification_type": "urgent_order"
                }
            ),
            Action(
                name="calculate_financial_impact",
                kwargs={
                    "product_value": 180000,
                    "liability_estimate": 8500
                }
            )
        ],
        outputs=[
            '"purchase_order_id": "PO-SUP-1003-AUTO-PAD-B2-001"',
            '"total_automotive_cost": 188500'
        ]
    ),
]
