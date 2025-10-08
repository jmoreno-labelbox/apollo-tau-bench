# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_1",
        "instruction": "\n        Manage the Korean textile quality audit for supplier SUP-1004.\n        Retrieve supplier performance rating and acquire inventory details for SKU MATR-COTT-R18 in warehouse WH-04.\n        Quarantine inventory EAC LOT202404D in WH-04 due to \"quality_audit\".\n        Carry out a physical count and establish an inventory adjustment with quantity -5 for reason \"audit_samples\".\n        Draft an incident report with type \"quality_audit\" and severity \"low\" for shipment SHIP-0004.\n        Notify supplier using type \"audit_notification\".\n        Compute financial impact using textile value 160000 and audit cost 4200.\n        Obtain notification status and incident ID.\n    ",
        "actions": [
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1004"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202404D",
                    "warehouse_id": "WH-04",
                    "reason": "quality_audit"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "MATR-COTT-R18"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "adjustment_quantity": -5,
                    "reason": "audit_samples"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0004",
                    "incident_type": "quality_audit",
                    "severity": "low"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1004",
                    "notification_type": "audit_notification"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 160000,
                    "liability_estimate": 4200
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"INC-SHIP-0004-low\"",
                "\"notification_status\": \"Sent\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_2",
        "instruction": "\n        Address critical electronics shortage alert: Main customer Apple has increased their Q4 order by 40%, necessitating immediate restocking of 8-bit microcontrollers.\n        Present LA warehouse stock indicates only 2 weeks supply left.\n        Assess supplier SUP-1001 performance and expedite 5000 units of ELEC-CHIP-A1 to WH-01 with medium priority.\n        Our supplier relationship manager reports a 10% volume bonus (500 additional units) as a loyalty offer.\n        Conduct comprehensive inventory verification, including a physical count and warehouse utilization analysis, to ensure capability to manage increased volume.\n        Estimate total investment comprising the $22,500 chip value and $2,750 rush processing charges.\n    ",
        "actions": [
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1001"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1001",
                    "sku": "ELEC-CHIP-A1",
                    "quantity": 5000,
                    "destination_warehouse": "WH-01",
                    "priority": "Medium"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "adjustment_quantity": 500,
                    "reason": "supplier_bonus"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 22500,
                    "liability_estimate": 2750
                }
            }
        ],
        "outputs": [
                "\"supplier_performance_rating\": 4.6",
                "\"total_chip_investment\": 25250"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_3",
        "instruction": "\n        Handle quality crisis escalation: BMW Munich has refused our latest brake pad shipment of SKU AUTO-PAD-B2 citing inconsistent friction coefficients.\n        They may switch to a competitor without immediate quality verification.\n        Supplier SUP-1003 in Frankfurt attributes the issue to storage conditions, not manufacturing.\n        Immediately quarantine all brake pads from EAC LOT202403B in the Milwaukee facility WH-03 with reason \"BMW quality verification pending\".\n        Allocate 8 sets for comprehensive testing labs, perform a physical count of 792, and ensure our storage complies with automotive standards.\n        Document all actions for the BMW audit scheduled next week.\n        The total brake pad inventory value stands at $36000, with $1200 allocated for emergency testing.\n    ",
        "actions": [
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1003"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202403B",
                    "warehouse_id": "WH-03",
                    "reason": "BMW quality verification pending"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "instruction_amount": 792
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "adjustment_quantity": -8
                },
            },
            {
                "name": "VerifyStorageCompliance",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "storage_type": "automotive",
                    "compliant_flag": true
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 36000,
                    "liability_estimate": 1200
                }
            }
        ],
        "outputs": [
                "\"supplier_performance_rating\": 4.7",
                "\"total_quality_cost\": 37200"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_4",
        "instruction": "\n        Address electronics shortage crisis: SKU ELEC-CHIP-A1 is critically low at San Diego WH-01 with only 15000 units available.\n        Obtain inventory details for SKU ELEC-CHIP-A1 in warehouse WH-01.\n        Ascertain warehouse capacity for WH-01 to evaluate space constraints.\n        Investigate inbound shipments for SKU ELEC-CHIP-A1 to warehouse WH-01 for incoming stock checks.\n        Retrieve approved suppliers for SKU ELEC-CHIP-A1.\n        Review supplier SUP-1001 performance rating.\n        Initiate an emergency purchase order for 25000 units with supplier SUP-1001 for warehouse WH-01, prioritizing Critical, with notes \"Emergency replenishment - customer backorders critical\".\n        Assess carrier performance for NSTS.\n        Choose the optimal carrier for San Diego, United States, with Critical priority and weight 5000 kg.\n        Request a shipping quote from NSTS for 5000 kg shipment to San Diego.\n        Create shipping labels for current order ORD-0001 using carrier NSTS.\n        Conduct a physical count for SKU ELEC-CHIP-A1 in warehouse WH-01.\n        Determine inventory variance using system count 15000 and physical count 14888.\n        Make an inventory adjustment for quantity -112 because of \"Emergency count correction for accurate reordering\".\n        Update accuracy metrics for warehouse WH-01.\n        Retrieve order details for ORD-0001 to verify customer effect.\n        Change order status for ORD-0001 to \"Backordered\".\n        Report emergency order status, variance percentage, and expected delivery cost.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "destination_warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetApprovedSuppliers",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1001"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "quantity": 25000,
                    "supplier_id": "SUP-1001",
                    "sku": "ELEC-CHIP-A1",
                    "destination_warehouse": "WH-01",
                    "priority": "Critical",
                    "notes": "Emergency replenishment - customer backorders critical"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_city": "San Diego",
                    "destination_country": "United States",
                    "priority_level": "Critical",
                    "total_weight_kg": 5000
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "weight_kg": 5000,
                    "destination": "San Diego"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0001",
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "system_count": 15000,
                    "physical_count": 14888
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "adjustment_quantity": -112,
                    "reason": "Emergency count correction for accurate reordering"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0001"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "Backordered"
                }
            }
        ],
        "outputs": [
                "\"emergency_order_status\": \"Created\"",
                "\"variance_percentage\": 0.75",
                "\"estimated_delivery_cost\": 12500"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_5",
        "instruction": "\n            Handle critical stock shortage alert for pharmaceutical SKU PHRM-DRUG-S19 in warehouse WH-06.\n            Acquire current inventory details, confirm supplier SUP-1021 performance rating, and generate an urgent purchase order for 1000 units, assigning High priority with note \"Critical patient medication shortage - expedite processing\".\n            Verify incoming shipments for this SKU to WH-06, quarantine current inventory with EAC number LOT202405H due to \"Batch verification pending regulatory approval\", create an incident report with severity \"high\", inform supplier SUP-1021 of quality concern, and compute total financial impact with product value 600000 and liability estimate 100000.\n            Document purchase order number and total financial impact.\n        ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1021"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1021",
                    "sku": "PHRM-DRUG-S19",
                    "quantity": 1000,
                    "destination_warehouse": "WH-06",
                    "priority": "High",
                    "notes": "Critical patient medication shortage - expedite processing"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "sku": "PHRM-DRUG-S19",
                    "destination_warehouse_id": "WH-06"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405H",
                    "warehouse_id": "WH-06",
                    "reason": "Batch verification pending regulatory approval"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "PHRM-DRUG-S19",
                    "incident_type": "quality_concern",
                    "severity": "high"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1021",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 600000,
                    "liability_estimate": 100000
                }
            }
        ],
        "outputs": [
                "\"purchase_order_number\": \"PO-SUP-1021-PHRM-DRUG-S19-001\"",
                "\"total_financial_impact\": 700000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_6",
        "instruction": "\n        Handle the emergency for a temperature-sensitive shipment SHIP-0006 containing SKU PHRM-VACC-D4 from supplier SUP-1006 to warehouse WH-06.\n        Obtain shipment details, verify temperature logs against the required range 2-8C, place inventory with EAC number LOT202406A in quarantine at warehouse WH-06 for the reason \"Cold chain verification pending investigation\".\n        Obtain the performance rating for supplier SUP-1006, develop a supplier improvement plan with a review cycle of 60 days, create an incident report of type \"cold_chain_breach\" with a severity of \"high\", alert supplier SUP-1006 with a notification type \"quality_incident\", and compute the financial impact with a product value of 310000 and a liability estimate of 25000.\n        Report the incident ID and total financial exposure.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "required_temp_range": "2-8C"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202406A",
                    "warehouse_id": "WH-06",
                    "reason": "Cold chain verification pending investigation"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1006"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "review_cycle_days": 60
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0006",
                    "incident_type": "cold_chain_breach",
                    "severity": "high"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 310000,
                    "liability_estimate": 25000
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"INC-SHIP-0006-high\"",
                "\"total_financial_impact\": 335000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_7",
        "instruction": "\n        Coordinate emergency procurement due to a critical shortage of SKU TECH-SOLR-G7 in warehouse WH-09.\n        Retrieve inventory details for SKU TECH-SOLR-G7 in warehouse WH-09, check the performance rating of supplier SUP-1009, create a purchase order for 500 units with Critical priority, noting \"Solar panel emergency replenishment for grid project\".\n        Examine incoming shipments for this SKU to WH-09, update accuracy metrics for warehouse WH-09, assess the financial impact with a product value of 149995 and a liability estimate of 5000.\n        Report the purchase order ID and current incoming inventory status.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1009"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1009",
                    "sku": "TECH-SOLR-G7",
                    "quantity": 500,
                    "destination_warehouse": "WH-09",
                    "priority": "Critical",
                    "notes": "Solar panel emergency replenishment for grid project"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "sku": "TECH-SOLR-G7",
                    "destination_warehouse_id": "WH-09"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 149995,
                    "liability_estimate": 5000
                }
            }
        ],
        "outputs": [
                "\"po_id\": \"PO-SUP-1009-TECH-SOLR-G7-001\"",
                "\"current_incoming_inventory\": 600"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_8",
        "instruction": "\n        Coordinate the handling of order ORD-0003 containing SKU BLDG-TILE-J10 from warehouse WH-12.\n        Gather order details, retrieve inventory details for SKU BLDG-TILE-J10 in warehouse WH-12, place inventory with EAC number LOT202404A under quarantine in warehouse WH-12 for the reason \"Customer return quality investigation\".\n        Generate an incident report for order ORD-0003 with incident type \"customer_return\" and severity \"medium\", acquire the performance rating of supplier SUP-1012, notify supplier SUP-1012 using notification type \"quality_incident\".\n        Report the incident ID along with quarantine confirmation.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0003"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202404A",
                    "warehouse_id": "WH-12",
                    "reason": "Customer return quality investigation"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "ORD-0003",
                    "incident_type": "customer_return",
                    "severity": "medium"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1012"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1012",
                    "notification_type": "quality_incident"
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"INC-ORD-0003-medium\"",
                "\"quarantine_confirmation\": \"Quarantined\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_9",
        "instruction": "\n        Manage the discovery of damaged inventory for SKU BLDG-TILE-J10 in warehouse WH-12 from supplier SUP-1012.\n        Gather inventory details for SKU BLDG-TILE-J10 in warehouse WH-12, isolate inventory with EAC number LOT202404A in warehouse WH-12 for the reason \"Damage assessment pending quality inspection\".\n        Check supplier SUP-1012 performance rating, formulate a supplier improvement plan with a 90-day review cycle, prepare an incident report marked with severity \"medium\" and incident type \"product_damage\", inform supplier SUP-1012 with notification type \"quality_incident\", and determine the financial impact with product value 63000 and liability estimate 8000.\n        Deliver a report on quarantine status and total financial impact.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202404A",
                    "warehouse_id": "WH-12",
                    "reason": "Damage assessment pending quality inspection"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1012"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1012",
                    "review_cycle_days": 90
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "BLDG-TILE-J10",
                    "incident_type": "product_damage",
                    "severity": "medium"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1012",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 63000,
                    "liability_estimate": 8000
                }
            }
        ],
        "outputs": [
                "\"quarantine_status\": \"Quarantined\"",
                "\"total_financial_impact\": 71000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_10",
        "instruction": "\n            Coordinate a critical inventory adjustment required for SKU CHEM-SOLV-K11 in warehouse WH-13 following a discrepancy in physical count.\n            Retrieve inventory details for SKU CHEM-SOLV-K11 in warehouse WH-13, establish an inventory adjustment with a quantity of -20 for the reason \"Physical count correction after audit variance\", get the performance rating for supplier SUP-1013, compile an incident report with severity \"low\", incident type \"inventory_variance\" and id 'CHEM-SOLV-K11', alert supplier SUP-1013 with notification type \"quality_incident\", inspect inbound shipments for SKU CHEM-SOLV-K11 to warehouse WH-13, refresh accuracy metrics for warehouse WH-13, evaluate financial impact with product value 60000 and liability estimate 1500.\n            Report adjustment value and updated quantity.\n        ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "adjustment_quantity": -20,
                    "reason": "Physical count correction after audit variance"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1013"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "CHEM-SOLV-K11",
                    "incident_type": "inventory_variance",
                    "severity": "low"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "destination_warehouse_id": "WH-13"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 60000,
                    "liability_estimate": 1500
                }
            }
        ],
        "outputs": [
                "\"adjustment_value\": 3000",
                "\"updated_quantity\": 380"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_11",
        "instruction": "\n        Handle a critical pharmaceutical cold chain emergency for shipment SHIP-0006, which includes SKU PHRM-VACC-D4 from supplier SUP-1006 to warehouse WH-06.\n        Retrieve shipment details, ensure temperature logs align with the required range of 2-8C considering excursions flag true, and confirm cold chain integrity with carrier DFC.\n        Quarantine stock with EAC number LOT202406A at warehouse WH-06 due to \"Cold chain breach investigation pending\".\n        Obtain supplier SUP-1006's performance rating and develop a supplier improvement plan with a review every 90 days.\n        Initiate a precautionary product recall for EAC LOT202406A, create an incident report marked as \"critical\" for \"cold_chain_breach\", and inform supplier SUP-1006 using notification type \"quality_incident\".\n        Compute the financial impact using a product value of 310000 and a liability estimate of 50000.\n        Escalate to the quality team with \"critical\" priority.\n        Report recall ID and total financial impact.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "required_temp_range": "2-8C",
                    "excursions_flag": true
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202406A",
                    "warehouse_id": "WH-06",
                    "reason": "Cold chain breach investigation pending"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1006"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "review_cycle_days": 90
                },
            },
            {
                "name": "InitiateProductRecall",
                "arguments": {
                    "lot_number": "LOT202406A",
                    "recall_type": "precautionary"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0006",
                    "incident_type": "cold_chain_breach",
                    "severity": "critical"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 310000,
                    "liability_estimate": 50000
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0006-critical",
                    "priority": "critical"
                }
            }
        ],
        "outputs": [
                "\"recall_id\": \"RCL-LOT202406A-precautionary\"",
                "\"total_financial_impact\": 360000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_12",
        "instruction": "\n        Coordinate complex international customs processing for shipment SHIP-0023 containing SKU AUTO-GLAS-U21 from supplier SUP-1023 to warehouse WH-03.\n        Gather shipment details, ensure customs documentation is complete, calculate the customs duty for a total value of 95000 originating from Mexico, and process the duty payment amount of 0.\n        Update the customs status to \"Cleared\" and change the shipment status to \"Ready for Receipt\".\n        Retrieve supplier SUP-1023's performance rating, verify storage compliance in warehouse WH-03 for storage type \"fragile\" with compliant flag true, and assess carrier performance for GPLS.\n        Update accuracy metrics for warehouse WH-03 and assess financial impact with a product value of 95000 and liability estimate of 3000.\n        Deliver reports on customs status and storage compliance.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0023"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0023"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0023",
                    "total_value": 95000,
                    "country_of_origin": "Mexico"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0023",
                    "duty_amount": 0
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0023",
                    "status": "Cleared"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0023",
                    "status": "Ready for Receipt"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1023"
                },
            },
            {
                "name": "VerifyStorageCompliance",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "storage_type": "fragile",
                    "compliant_flag": true
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 95000,
                    "liability_estimate": 3000
                }
            }
        ],
        "outputs": [
                "\"customs_status\": \"Cleared\"",
                "\"storage_compliance_status\": \"compliant\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_13",
        "instruction": "\n        Handle a multi-phase inventory management crisis for SKU ELEC-CHIP-A1 in warehouse WH-01 from supplier SUP-1001.\n        Retrieve inventory details for SKU ELEC-CHIP-A1 in warehouse WH-01, and conduct a physical count for SKU ELEC-CHIP-A1 at warehouse WH-01, with a physical count of 14500.\n        Calculate inventory discrepancy for SKU ELEC-CHIP-A1 comparing system count 15000 with physical count 14500.\n        Prepare an inventory adjustment for SKU ELEC-CHIP-A1 in warehouse WH-01, adjusting by -500 due to \"Physical count variance correction\".\n        Look for inbound shipments of SKU ELEC-CHIP-A1 to warehouse WH-01, acquire supplier SUP-1001's performance rating, and form a supplier improvement plan reviewed every 60 days.\n        Draft an incident report with \"medium\" severity addressing \"inventory_variance\" and alert supplier SUP-1001 with a \"quality_incident\" notification.\n        Update accuracy metrics for warehouse WH-01, evaluate the financial impact with product value 37500 and liability estimate 2500, and identify approved suppliers for SKU ELEC-CHIP-A1.\n        Report adjustment value and predicted total stock.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "instruction_amount": 14500
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "system_count": 15000,
                    "physical_count": 14500
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "adjustment_quantity": -500,
                    "reason": "Physical count variance correction"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "destination_warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1001"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1001",
                    "review_cycle_days": 60
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "ELEC-CHIP-A1",
                    "incident_type": "inventory_variance",
                    "severity": "medium"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1001",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 37500,
                    "liability_estimate": 2500
                },
            },
            {
                "name": "GetApprovedSuppliers",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                }
            }
        ],
        "outputs": [
                "\"adjustment_value\": 1250",
                "\"total_expected_stock\": 17000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_14",
        "instruction": "\n        Address a food safety inspection alert for coffee inventory at the Dallas warehouse WH-05.\n        Assess current inventory levels for SKU FOOD-COFF-C3 in warehouse WH-05.\n        Retrieve supplier SUP-1024's performance rating.\n        Conduct a physical count resulting in 4980.\n        Compute inventory variance between the system's count of 5000 and the physical count of 4980.\n        Implement an inventory adjustment with a quantity of -20 due to \"Food safety inspection variance\".\n        Create a purchase order from supplier SUP-1024 for 1000 units at $35 for FOOD-COFF-C3 to warehouse WH-05 with Medium priority.\n        Present reports on adjustment value and supplier rating.\n    ",
        "actions": [
            {
                "name": "GetInventoryBySkuWarehouse",
                "arguments": {
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1024"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "instruction_amount": 4980
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "FOOD-COFF-C3",
                    "system_count": 5000,
                    "physical_count": 4980
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "adjustment_quantity": -20,
                    "reason": "Food safety inspection variance"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1024",
                    "sku": "FOOD-COFF-C3",
                    "quantity": 1000,
                    "destination_warehouse": "WH-05",
                    "priority": "Medium",
                    "unit_price": 35.0
                }
            }
        ],
        "outputs": [
                "\"adjustment_value\": 440.00",
                "\"supplier_rating\": 4.7"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_15",
        "instruction": "\n        Manage a critical pharmaceutical shipment inspection for vaccine storage at the Charlotte cold chain center WH-06.\n        Examine inventory levels for SKU PHRM-VACC-D4 in warehouse WH-06.\n        Obtain supplier SUP-1020's performance rating and request shipping quotes from carriers SWDL and DFC for a shipment weighing 1800 kg destined for Charlotte, United States.\n        Choose DFC as the carrier for the United States destination, prioritizing critical delivery for the 1800 kg shipment.\n        Conduct a physical count amounting to 19980 compared to a system baseline of 20000.\n        Assess inventory variance between the system's 20000 count and the physical count of 19980.\n        Execute an inventory adjustment with a reduction by -20 due to \"Cold chain verification variance\" costing 15.\n        50 per unit.\n        Report on the selected carrier and monetary adjustment value.\n    ",
        "actions": [
            {
                "name": "GetInventoryBySkuWarehouse",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1020"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "SWDL",
                    "weight_kg": 1800,
                    "destination": "Charlotte, United States"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "DFC",
                    "weight_kg": 1800,
                    "destination": "Charlotte, United States"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "United States",
                    "priority_level": "Critical",
                    "total_weight_kg": 1800,
                    "carriers_list": [
                        "SWDL",
                        "DFC"
                    ]
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "instruction_amount": 19980
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "system_count": 20000,
                    "physical_count": 19980
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "adjustment_quantity": -20,
                    "reason": "Cold chain verification variance"
                }
            }
        ],
        "outputs": [
                "\"selected_carrier\": \"DFC\"",
                "\"adjustment_value\": 310.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_16",
        "instruction": "\n        Handle the order for construction materials ORD-0003 for the customer in Denver, Gamma Construction Ltd.\n        Retrieve the order details indicating the shipment of 6200 kg from the Fort Lauderdale warehouse WH-12.\n        Confirm the inventory allocation for the order.\n        Obtain the warehouse capacity status of WH-12.\n        Check the performance rating of supplier SUP-1012.\n        Request a shipping quote from the SWDL carrier for 6200 kg to Denver, United States.\n        Produce shipping labels with the SWDL carrier.\n        Change the order status to Shipped.\n        Provide the customer's name and the estimated shipping cost.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0003"
                },
            },
            {
                "name": "VerifyInventoryAllocation",
                "arguments": {
                    "order_id": "ORD-0003"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1012"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "SWDL",
                    "weight_kg": 6200,
                    "destination": "Denver, United States"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0003",
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0003",
                    "new_status": "Shipped"
                }
            }
        ],
        "outputs": [
                "\"customer_name\": \"Gamma Construction Ltd.\"",
                "\"shipping_cost_estimate\": 27900"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_17",
        "instruction": "\n        Coordinate the processing of the critical pharmaceutical order ORD-0004, which involves a temperature-sensitive shipment from the Milwaukee cold storage WH-03 to the customer Delta Pharma Inc.\n        in Boston.\n        Retrieve the order details reflecting a weight of 180 kg.\n        Confirm the inventory allocation status.\n        Assess the performance rating of supplier SUP-1021.\n        Request shipping quotes from carriers SWDL and DFC for 180 kg destined for Boston, United States.\n        Choose DFC as the carrier for the United States destination with High priority for 180 kg.\n        Retrieve inventory information for SKU PHRM-VACC-D4 in warehouse WH-06.\n        Place the inventory with EAC number LOT202406A in warehouse WH-06 into quarantine for \"Temperature compliance inspection\".\n        Produce shipping labels with the selected carrier.\n        Alter the order status to \"For Return\".\n        Provide customer details and confirm quarantine.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0004"
                },
            },
            {
                "name": "VerifyInventoryAllocation",
                "arguments": {
                    "order_id": "ORD-0004"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1021"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "SWDL",
                    "weight_kg": 180,
                    "destination": "Boston, United States"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "DFC",
                    "weight_kg": 180,
                    "destination": "Boston, United States"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "United States",
                    "priority_level": "High",
                    "total_weight_kg": 180
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202406A",
                    "warehouse_id": "WH-06",
                    "reason": "Temperature compliance inspection"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0004",
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0004",
                    "new_status": "For Return"
                }
            }
        ],
        "outputs": [
                "\"customer_name\": \"Delta Pharma Inc.\"",
                "\"quarantine_confirmation\": \"Quarantined\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_18",
        "instruction": "\n        Manage the complex international electronics shipment ORD-0006 from San Francisco to the customer Zeta Tech Solutions in Nippon.\n        Retrieve order details reflecting a weight of 550 kg and fragile electronics.\n        Confirm the inventory allocation status.\n        Evaluate the performance rating of supplier SUP-1025.\n        Check the capacity utilization of warehouse WH-05.\n        Obtain inventory data for SKU ELEC-CHIP-A1 in warehouse WH-01.\n        Conduct a physical count with the required amount of 12450.\n        Determine the inventory variance between the system count of 15000 and the physical count of 12450.\n        Execute an inventory adjustment with a quantity of -2550 for the reason \"International shipment preparation count\".\n        Request shipping quotes from the carriers NSTS and SKEX for 550 kg to Yokohama, Nippon.\n        Elect NSTS as the preferred carrier for Nippon with Medium priority for 550 kg.\n        Create shipping labels using chosen carrier NSTS.\n        Update the order status to Shipped.\n        Generate an incident report with id \"INTL-SHIP-006\" citing incident type \"international_compliance\" and severity \"low\".\n        Provide the customer's details and the incident id plus status.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "VerifyInventoryAllocation",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1025"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "instruction_amount": 12450
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "system_count": 15000,
                    "instruction_count": 12450
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "adjustment_quantity": -2550,
                    "reason": "International shipment preparation count"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "weight_kg": 550,
                    "destination": "Yokohama, Nippon"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "SKEX",
                    "weight_kg": 550,
                    "destination": "Yokohama, Nippon"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "Nippon",
                    "priority_level": "Medium",
                    "total_weight_kg": 550,
                    "preferred_carrier": "NSTS"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0006",
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0006",
                    "new_status": "Shipped"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "INTL-SHIP-006",
                    "incident_type": "international_compliance",
                    "severity": "low"
                }
            }
        ],
        "outputs": [
                "\"customer_name\": \"Zeta Tech Solutions\"",
                "\"incident_status\": \"Created\"",
                "\"incident_id\": \"INC-INTL-SHIP-006-low\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_19",
        "instruction": "\n        Oversee the quality control process for raw cotton inventory at the Hoboken apparel facility WH-04.\n        Retrieve inventory details for SKU MATR-COTT-R18 in warehouse WH-04.\n        Place the inventory with the EAC number LOT202404D in warehouse WH-04 into quarantine for \"Quality inspection hold pending certification\".\n        Assess the performance rating of supplier SUP-1020.\n        Obtain the capacity of warehouse WH-04.\n        Conduct a physical count with the specified amount of 195.\n        Calculate the inventory variance between a system count of 200 and a physical count of 195.\n        Perform an inventory adjustment with a quantity of -5 for the reason \"Quality control shrinkage\".\n        Solicit shipping quotes from carriers GPLS and MEDL for 1135 kg to Hoboken, United States.\n        Select the best-suited carrier for the United States destination with Medium priority and 1135 kg.\n        Provide report on quarantine status and carrier choice.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202404D",
                    "warehouse_id": "WH-04",
                    "reason": "Quality inspection hold pending certification"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1020"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "instruction_amount": 195
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "system_count": 200,
                    "physical_count": 195
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "adjustment_quantity": -5,
                    "reason": "Quality control shrinkage"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "weight_kg": 1135,
                    "destination": "Hoboken, United States"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "MEDL",
                    "weight_kg": 1135,
                    "destination": "Hoboken, United States"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "United States",
                    "priority_level": "Medium",
                    "total_weight_kg": 1135,
                    "carriers_list": [
                        "GPLS",
                        "MEDL"
                    ]
                }
            }
        ],
        "outputs": [
                "\"quarantine_status\": \"Quarantined\"",
                "\"selected_carrier\": \"GPLS\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_20",
        "instruction": "\n        Conduct an analysis of the critical inventory shortage for automotive glass SKU AUTO-GLAS-U21 at the Midwest Parts Warehouse WH-03.\n        Retrieve inventory details for SKU AUTO-GLAS-U21 in warehouse WH-03.\n        Inspect the performance rating of supplier SUP-1023.\n        Create a purchase order from supplier SUP-1023 for 300 units of AUTO-GLAS-U21 to warehouse WH-03 with High priority.\n        Request shipping quotes from carriers SWDL and DLOG for 1500 kg destined for Milwaukee, United States.\n        Select the most optimal carrier for the United States destination with High priority and 1500 kg.\n        Generate an incident report with id \"AUTO-SHORTAGE-001\" mentioning incident type \"inventory_shortage\" and severity \"medium\".\n        Provide the report on supplier rating and incident status.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1023"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1023",
                    "sku": "AUTO-GLAS-U21",
                    "quantity": 300,
                    "destination_warehouse": "WH-03",
                    "priority": "High"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "SWDL",
                    "weight_kg": 1500,
                    "destination": "Milwaukee, United States"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "DLOG",
                    "weight_kg": 1500,
                    "destination": "Milwaukee, United States"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "United States",
                    "priority_level": "High",
                    "total_weight_kg": 1500,
                    "carriers_list": [
                        "SWDL",
                        "DLOG"
                    ]
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "AUTO-SHORTAGE-001",
                    "incident_type": "inventory_shortage",
                    "severity": "medium"
                }
            }
        ],
        "outputs": [
                "\"supplier_rating\": 4.5",
                "\"incident_status\": \"Created\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_21",
        "instruction": "\n        As the LA warehouse manager, ensure you verify available stock levels for ELEC-CHIP-A1 in WH-01.\n        Should inventory fall\n        below 15,000 units, proceed to urgently order 10,000 units from supplier SUP-1001 for WH-01 and categorize it as high priority.\n        Also, review incoming shipments for this item and report the total expected inventory after arrivals.\n    ",
        "actions": [
            {
                "name": "GetInventoryBySkuWarehouse",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1001",
                    "sku": "ELEC-CHIP-A1",
                    "quantity": 10000,
                    "destination_warehouse": "WH-01",
                    "priority": "High"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "destination_warehouse_id": "WH-01"
                }
            }
        ],
        "outputs": [
                "\"quantity_available\": 12500",
                "\"quantity_inbound\": 5000",
                "\"total_expected_stock\": 17500",
                "\"status\": \"Created\"",
                "\"total_cost\": 45000",
                "\"priority\": \"High\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_22",
        "instruction": "\n        Handle the customs clearance for shipment SHIP-0001 that is currently awaiting processing.\n        Ensure all necessary paperwork is complete, including customs entry number and duty payment status.\n        For duties that are unpaid, calculate the amount and complete the payment process.\n        Update the status to Cleared and ready for warehouse receipt.\n        Report the total duty paid.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "total_value": 350000,
                    "country_of_origin": "Middle Kingdom"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "duty_amount": 17500
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "status": "Cleared"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "status": "Ready for Receipt"
                }
            }
        ],
        "outputs": [
                "\"duty_amount\": 17500"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_23",
        "instruction": "\n        Facilitate a thorough supplier risk assessment for SUP-1004 following quality issues and delivery delays.\n        Examine current performance metrics, including rating and on-time delivery statistics.\n        Analyze delayed purchase orders to evaluate financial exposure\n        and delivery risk.\n        If the performance rating is less than or equal to 4.\n        5, develop a detailed 90-day improvement plan with the recommendation\n        'Focus on improving on-time delivery'.\n        Examine the impact on critical inventory levels for affected SKUs, including\n        APRL-TSHT-O15.\n        Check current warehouse stock and assess reorder requirements.\n        Check SUP-1020's capabilities and performance metrics.\n        Issue emergency purchase orders of 1100 (MATR-COTT-R18) with high priority if inventory levels are critical to SUP-1020.\n        Notify the initial supplier of the concerns.\n    ",
        "actions": [
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1004"
                },
            },
            {
                "name": "SearchPurchaseOrders",
                "arguments": {
                    "supplier_id": "SUP-1004",
                    "status": "Delayed"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "APRL-TSHT-O15",
                    "system_count": 25000,
                    "physical_count": 22000
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1004"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1020"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1004",
                    "review_cycle_days": 90,
                    "recommendation": "Focus on improving on-time"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1020",
                    "sku": "MATR-COTT-R18",
                    "quantity": 1100,
                    "destination_warehouse": "WH-04",
                    "priority": "High"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1004",
                    "notification_type": "performance_review"
                }
            }
        ],
        "outputs": [
                "\"supplier_name\": \"Busan Textiles Co.\"",
                "\"performance_rating\": 4.5",
                "\"on_time_delivery_percentage\": 96.8",
                "\"relationship_status\": \"Active\"",
                "\"pending_orders_count\": 1",
                "\"tshirt_quantity_available\": 22000",
                "\"system_count\": 25000",
                "\"physical_count\": 22000",
                "\"variance\": -3000",
                "\"variance_percentage\": 12",
                "\"alternative_supplier_1\": \"Cairo Cotton Co..\"",
                "\"improvement_plan_created\": true",
                "\"emergency_order_quantity\": 1100",
                "\"emergency_order_created\": true",
                "\"supplier_notification_sent\": true",
                "\"supplier_status_recommendation\": \"maintain_active\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_24",
        "instruction": "\n        Dispatch outbound order ORD-0010 using a medium-priority international carrier.\n        Choose an optimal carrier that provides reliable global shipping with on-time delivery, regardless of the route as the chosen carrier will\n        support global shipping.\n        Generate shipping labels for the chosen carrier and update the order status to 'Shipped'.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_city": "Mumbai",
                    "destination_country": "India",
                    "priority_level": "Medium",
                    "total_weight_kg": 2000
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0010",
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0010",
                    "new_status": "Shipped"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "DFC"
                }
            }
        ],
        "outputs": [
                "\"optimal_carrier\": \"Desert Falcon Cargo\"",
                "\"carrier_scac\": \"DFC\"",
                "\"on_time_delivery_percentage\": 98.1",
                "\"tracking_number\":\"DFC-ORD-0010\"",
                "\"label_id\": \"LBL-DFC\"",
                "\"order_status\": \"Shipped\"",
                "\"estimated_delivery_date\": \"2024-06-18\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_25",
        "instruction": "\n        Evaluate the space utilization at the Phoenix facility WH-10.\n        If utilization reaches or exceeds 90%,\n        identify overflow options with a required capacity of at least 5000 cubic meters.\n        Then apply the 'redistribute_slow_moving'\n        strategy to craft a capacity optimization plan.\n        Analyze inventory by category and calculate remaining space in cubic meters.\n        Create an incident report with id 'WH-10-CAPACITY-00' and incident type 'for_monitoring' with low severity.\n    ",
        "actions": [
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "AnalyzeInventoryByCategory",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "IdentifyOverflowOptions",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "required_capacity": 5000
                },
            },
            {
                "name": "CreateCapacityPlan",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "optimization_strategy": "redistribute_slow_moving"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "WH-10-CAPACITY-00",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                }
            }
        ],
        "outputs": [
                "\"remaining_capacity_cbm\": 990.0",
                "\"utilization_percentage\": 95.5",
                "\"plan_created\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_26",
        "instruction": "\n        Manage the crucial frozen seafood shipment SHIP-0010 from Melbourne containing premium\n        fish products (FOOD-FISH-H8).\n        Check that the temperature logs confirm adherence to the below -5\u00b0C requirement, ensure that carrier\n        SCF maintained proper cold chain procedures, verify inventory allocation within WH-10 cold storage, and due to the detected temperature excursions at -2\u00b0C,\n        set apart product LOT202406B with the reason 'Temperature monitoring verification - seafood quality check' and initiate a quality incident marked as high severity.\n        Determine the financial exposure including a $15,000 liability estimate and escalate incident INC-SHIP-0010-high.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0010",
                    "required_temp_range": "below_-5C",
                    "excursions_flag": true
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0010",
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202406B",
                    "warehouse_id": "WH-10",
                    "reason": "Temperature monitoring verification - seafood quality check"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0010",
                    "incident_type": "temperature_monitoring",
                    "severity": "high"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 180000,
                    "liability_estimate": 15000
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0010-high",
                    "priority": "high"
                }
            }
        ],
        "outputs": [
                "\"temperature_compliance\": \"non-compliant\"",
                "\"quarantined_lot\": \"LOT202406B\"",
                "\"total_financial_impact\": 195000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_27",
        "instruction": "\n        Urgent: Customer reports a damaged vaccine shipment SHIP-0006 carrying INV-0004 (PHRM-VACC-D4).\n        The customer received vials with visible crystallization and broken seals in EAC LOT202406A.\n        Instantly isolate all affected inventory LOT202406A in WH-06 stating 'Customer damage report - compromised vials investigation' as the main reason,\n        ensure temperature logs were maintained between 2-8\u00b0C, verify DFC carrier handling procedures, create a critical incident report for the product damage investigation,\n        inform the supplier SUP-1006 of the quality concerns, compute the financial impact including a $50,000 liability estimate,\n        and commence a precautionary product recall pending further investigation.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202406A",
                    "warehouse_id": "WH-06",
                    "reason": "Customer damage report - compromised vials investigation"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "required_temp_range": "2-8"
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "InitiateProductRecall",
                "arguments": {
                    "lot_number": "LOT202406A",
                    "recall_type": "precautionary"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0006",
                    "incident_type": "product_damage",
                    "severity": "critical"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "status": "Quarantined"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 450000,
                    "liability_estimate": 50000
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0006-critical",
                    "priority": "critical"
                }
            }
        ],
        "outputs": [
                "\"quarantined_lot\": \"LOT202406A\"",
                "\"incident_id\": f\"INC-SHIP-0006-critical\"",
                "\"recall_id\": \"RCL-LOT202406A-precautionary\"",
                "\"temperature_excursion_detected\": false",
                "\"total_financial_impact\": 500000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_28",
        "instruction": "\n        Oversee the chemical inventory levels for CHEM-SOLV-K11 in WH-13.\n        The current stock is low and needs\n        immediate replenishment from SUP-1013.\n        Initiate a purchase order for 200 at $250 per unit with expedited delivery.\n        Verify the physical inventory count.\n        Draft an incident report with low severity and incident type 'for_monitoring'.\n        Examine supplier performance metrics before confirming the order.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1013"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "CHEM-SOLV-K11",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "sku": "CHEM-SOLV-K11",
                    "quantity": 200,
                    "destination_warehouse": "WH-13",
                    "priority": "High",
                    "unit_price": 250
                }
            }
        ],
        "outputs": [
                "\"quantity_available\": 380",
                "\"performance_rating\": 4.8",
                "\"status\": \"Created\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_29",
        "instruction": "\n        Dispatch the outbound order ORD-0005 to Toronto, Maple Nation using DFC as the carrier.\n        Draft an incident report with low severity and incident type 'for monitoring'.\n        for a 750kg load.\n        Create shipping labels using DFC as the carrier with medium priority and adjust the order status to 'Shipped'.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "ORD-0005",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_city": "Toronto",
                    "destination_country": "Maple Nation",
                    "priority_level": "Medium",
                    "total_weight_kg": 750,
                    "preferred_carrier": "DFC"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0005",
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0005",
                    "new_status": "Shipped"
                }
            }
        ],
        "outputs": [
                "\"carrier\": \"DFC\"",
                "\"tracking_number\": \"DFC-ORD-0005\"",
                "\"estimated_delivery_date\": \"2024-06-09\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_30",
        "instruction": "\n        Complete the complex customs clearance for the international shipment SHIP-0001 from Middle Kingdom valued at $350,000.\n        During the documentation review, identify a missing customs entry number necessitating coordination with supplier SUP-1001.\n        Compute the standard duty at a 5% rate ($17,500), but note that supplier's performance review shows a rating below 4.\n        7 requiring notification.\n        If documentation errors cause delays of over 24 hours, record an incident report with medium severity and compute the financial impact including\n        $25,000 in demurrage costs.\n        Process the duty payment, update the customs status to cleared, coordinate with WH-01, and update the shipment status.\n        Report the total financial impact, supplier rating, and customs status.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1001"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1001",
                    "notification_type": "documentation_required"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "total_value": 350000,
                    "country_of_origin": "Middle Kingdom"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0001",
                    "incident_type": "documentation_delay",
                    "severity": "medium"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 350000,
                    "liability_estimate": 25000
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "duty_amount": 17500
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "status": "Cleared"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "status": "Ready for Receipt"
                }
            }
        ],
        "outputs": [
                "\"duty_amount\": 17500",
                "\"total_financial_impact\": 375000",
                "\"documentation_complete\": false",
                "\"incident_created\": true",
                "\"shipment_status\": Ready for Receipt",
                "\"supplier_performance_rating\": 4.6",
                "\"customs_status\": Cleared"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_31",
        "instruction": "\n        Handle emergency: Customer reports damaged vaccine shipment SHIP-0006.\n        Immediately quarantine related inventory containing EAC number LOT202406A in WH-06.\n        Inspect shipment temperature logs and confirm temperature range 2-8\u00b0C with carrier DFC.\n        Temperature deviations occurred with excursions detected as true.\n        Establish critical incident report INC-SHIP-0006-critical due to the damaged vaccine shipment, inform supplier SUP-1006 with quality incident notification, evaluate financial impact with product value $450000 and liability estimate $50000, and elevate incident INC-SHIP-0006-critical to quality team for urgent investigation.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "lot_number": "LOT202406A",
                    "reason": "Damaged vaccine shipment"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "required_temp_range": "2-8",
                    "excursions_flag": true
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0006",
                    "incident_type": "product_damage",
                    "severity": "critical"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 450000,
                    "liability_estimate": 50000
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0006-critical",
                    "priority": "critical"
                }
            }
        ],
        "outputs": [
                "\"excursions_detected\": true",
                "\"incident_id\": \"INC-SHIP-0006-critical\"",
                "\"total_financial_impact\": 500000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_32",
        "instruction": "\n        Conduct a review of supplier SUP-1028 steel works performance due to delivery delays and quality issues.\n        Scrutinize current performance metrics and delivery statistics.\n        Since performance rating 4.\n        2 is below the 4.\n        5 threshold, investigate all pending purchase orders for risk evaluation and offer a recommendation of \"conditional approval\" on a 90-day improvement plan for the supplier relationship status.\n        An incident report with medium severity should be created using SHIP-0028 as reference.\n        Adjust inventory for affected heavy equipment SKU HEVY-DRIL-I9 in warehouse WH-11 by -5 units due to quality defects from supplier delivery issues under the reason 'quality defects from SUP-1028 delivery delays'.\n        The financial impact calculations should account for a $2,000 liability estimate.\n        Explore alternative suppliers including SUP-1011 and verify there is an alternative_suppliers_available for HEVY-DRIL-I9.\n    ",
        "actions": [
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1028"
                },
            },
            {
                "name": "SearchPurchaseOrders",
                "arguments": {
                    "supplier_id": "SUP-1028",
                    "status": "In Transit"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "sku": "HEVY-DRIL-I9",
                    "destination_warehouse_id": "WH-11"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "adjustment_quantity": -5,
                    "reason": "quality defects from SUP-1028 delivery delays"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 11000,
                    "liability_estimate": 2000
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1028",
                    "review_cycle_days": 90,
                    "recommendation": "conditional_approval"
                },
            },
            {
                "name": "GetApprovedSuppliers",
                "arguments": {
                    "sku": "HEVY-DRIL-I9"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0028",
                    "incident_type": "quality_defect",
                    "severity": "medium"
                }
            }
        ],
        "outputs": [
                "\"performance_rating\": 4.2",
                "\"current_inventory\": 40",
                "\"adjustment_value\": 11000",
                "\"total_financial_impact\": 13000",
                "\"alternative_suppliers_available\": 1",
                "\"improvement_plan_id\": \"SIP-SUP-1028\"",
                "\"supplier_status_recommendation\": \"conditional_approval\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_33",
        "instruction": "\n        Investigate inventory discrepancy for luxury watch components LUX-WATCH-L12 in WH-07 security vault.\n        The system shows 500 units but the physical count indicates exactly 497 units, leading to a -3 unit variance.\n        Compute inventory variance using the system count 500 and physical count 497.\n        Create inventory adjustment for the -3 unit discrepancy due to security audit findings because of potential theft (variance) with reason \"Security audit findings - luxury goods variance\".\n        When calculating the financial impact, it should be noted that the product value is $300 per unit, resulting in a total financial impact of $1400 including $500 liability estimate.\n        Update warehouse accuracy metrics and create a medium incident report for shipment SHIP-0014 related to luxury goods security protocol.\n        Notify the supplier of the incident using data for SUP-1014 stating 'quality_incident' as the reason.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "LUX-WATCH-L12",
                    "system_count": 500,
                    "physical_count": 497
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202403E",
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "adjustment_quantity": -3,
                    "reason": "Security audit findings - luxury goods variance"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 900,
                    "liability_estimate": 500
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0014",
                    "incident_type": "inventory_variance",
                    "severity": "medium"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1014",
                    "notification_type": "quality_incident"
                }
            }
        ],
        "outputs": [
                "\"variance_units\": -3",
                "\"variance_percentage\": 0.6",
                "\"quarantine_id\": \"QTN-LOT202403E-WH-07\"",
                "\"total_financial_impact\": 1400",
                "\"incident_id\": \"INC-SHIP-0014-medium\"",
                "\"supplier_notified\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_34",
        "instruction": "\n        Urgently address: Luxury goods shipment SHIP-0014 containing Swiss watch parts from Zurich, Helvetia valued at CHF 50000 shows potential damage based on carrier inspection report.\n        Formulate damage assessment protocol (compute potential financial impact) for when shipment reaches WH-07.\n        Draft a preventive incident report concerning the potential damage with medium severity, a 60-day review cycle improvement plan, inform supplier SUP-1014 of potential quality issues, calculate financial impact with product value CHF 50000 (approximately $45450 USD) and liability estimate $10000 for possible customer claims with the reason 'Quality incident - damaged luxury goods'.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1014"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0014",
                    "incident_type": "potential_damage",
                    "severity": "medium"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 45450,
                    "liability_estimate": 10000
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1014",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "weight_kg": 15,
                    "destination": "Zurich"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1014",
                    "review_cycle_days": 60,
                    "reason": "Quality incident - damaged luxury goods"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0014",
                    "status": "Inspection Required"
                }
            }
        ],
        "outputs": [
                "\"supplier_rating\": 4.9",
                "\"customs_status\": \"Pending\"",
                "\"warehouse_utilization\": 60.0",
                "\"incident_id\": \"INC-SHIP-0014-medium\"",
                "\"total_financial_impact\": 55450",
                "\"return_shipping_cost\": 48",
                "\"improvement_plan_created\": true",
                "\"shipment_status\": \"Inspection Required\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_35",
        "instruction": "\n        Coordinate shipment for critical electronics order ORD-0006 to Yokohama, Nippon destined for WH-05.\n        Confirm complete inventory allocation across various SKUs, evaluate warehouse capacity at the source San Francisco Electronics Hub (WH-05), choose carrier NSTS for international electronics transport to Yokohama, Nippon, with priority Medium, weight 550kg.\n        Produce shipping documentation with NSTS carrier, request a shipping quote for cost analysis, and complete shipment processing.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "VerifyInventoryAllocation",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_city": "Yokohama",
                    "destination_country": "Nippon",
                    "priority_level": "Medium",
                    "total_weight_kg": 550,
                    "preferred_carrier": "NSTS"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0006",
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "weight_kg": 550,
                    "destination": "Yokohama, Nippon"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0006",
                    "new_status": "Shipped"
                }
            }
        ],
        "outputs": [
                "\"selected_carrier\": \"NSTS\"",
                "\"tracking_number\": \"NSTS-ORD-0006\"",
                "\"current_status\": \"Shipped\"",
                "\"estimated_delivery_date\": \"2024-06-15\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_36",
        "instruction": "\n        Handle the check of current stock levels for TECH-SOLR-G7 solar panels in WH-09 Phoenix facility.\n        Coordinate inventory recount verification following cycle count discrepancies.\n        Evaluate SUP-1009 supplier's performance metrics to ensure ongoing reliability.\n        Create an inventory adjustment for TECH-SOLR-G7 in WH-09 with an adjustment quantity of +500 units because inventory recount findings showed a system undercount with the reason 'Inventory recount findings - system undercount correction', and update warehouse accuracy metrics.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1009"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "adjustment_quantity": 500,
                    "reason": "Inventory recount findings - system undercount correction"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-09"
                }
            }
        ],
        "outputs": [
                "\"quantity_before_adjustment\": 1200",
                "\"quantity_after_adjustment\": 1700",
                "\"performance_rating\": 4.5",
                "\"adjustment_value\": 90000",
                "\"accuracy_updated\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_38",
        "instruction": "\n        Coordinate re-processing of customs clearance for electronics shipment SHIP-0030 from Abu Dhabi containing smartphones worth $380,000.\n        Initial duty payment was made under DDP terms, however, a customs audit revealed a duty underpayment necessitating adjustment.\n        Ensure completeness of all documentation, calculate the correct import duties based on the revised classification, process an additional duty payment of $13,300, update customs status to cleared, and prepare the shipment for warehouse receipt.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0030"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0030"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0030",
                    "total_value": 380000,
                    "country_of_origin": "DFC"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0030",
                    "duty_amount": 13300
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0030",
                    "status": "Cleared"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0030",
                    "status": "Ready for Receipt"
                }
            }
        ],
        "outputs": [
                "\"duty_amount\": 13300",
                "\"customs_entry_number\": \"US-SHIP-0030\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_39",
        "instruction": "\n        Handle the investigation of a potential contamination issue with chemical shipment SHIP-0013, which requires a temperature range of 4-20C, from Helsinki containing industrial solvents (LOT202405E).\n        Check temperature logs to ensure proper storage conditions, verify cold chain maintenance, quarantine affected inventory in WH-13 hazmat area with the reason being 'Contamination investigation - chemical safety protocol', create a detailed incident report with type 'contamination_suspected' and severity 'high', notify supplier SUP-1013 using notification type 'quality_incident', and initiate a product recall with recall type 'precautionary'.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "required_temp_range": "4-20C"
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405E",
                    "warehouse_id": "WH-13",
                    "reason": "Contamination investigation - chemical safety protocol"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0013",
                    "incident_type": "contamination_suspected",
                    "severity": "high"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "InitiateProductRecall",
                "arguments": {
                    "lot_number": "LOT202405E",
                    "recall_type": "precautionary"
                }
            }
        ],
        "outputs": [
                "\"temperature_compliance\": \"compliant\"",
                "\"recall_initiated\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_40",
        "instruction": "\n        Conduct a comprehensive analysis of carrier performance for Asian and Global routes.\n        Evaluate NSTS, SKEX, and EWDL carriers for a critical 2800kg electronics shipment to Osaka requiring delivery within 12 days.\n        Generate shipping quotes from all carriers, perform a cost-benefit analysis, select the optimal carrier based on performance and cost, generate shipping labels for order ORD-0006 with the selected carrier, and update the order status to Shipped.\n    ",
        "actions": [
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "route": "Nippon"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "SKEX",
                    "route": "Nippon"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "EWDL",
                    "route": "Global"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "weight_kg": 2800,
                    "destination": "Osaka, Nippon"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "SKEX",
                    "weight_kg": 2800,
                    "destination": "Osaka, Nippon"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "EWDL",
                    "weight_kg": 2800,
                    "destination": "Osaka, Nippon"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "Nippon",
                    "destination_city": "Osaka",
                    "weight_kg": 2800,
                    "priority_level": "Critical",
                    "carriers_list": [
                        "NSTS",
                        "SKEX",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0006",
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0006",
                    "new_status": "Shipped"
                }
            }
        ],
        "outputs": [
                "\"recommended_carrier\": \"EWDL\"",
                "\"maeu_on_time_percentage\": 94.5",
                "\"npex_on_time_percentage\": 96.2",
                "\"dhlg_on_time_percentage\": 97.9",
                "\"maeu_estimated_cost\": 7000",
                "\"npex_estimated_cost\": 8400",
                "\"dhlg_estimated_cost\": 8400",
                "\"tracking_number\": \"EWDL-ORD-0006\"",
                "\"order_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_41",
        "instruction": "\n        Arrange a cycle count audit for luxury watch components LUX-WATCH-L12 in the WH-07 high-security vault, which currently shows 500 units in the system.\n        A physical count reveals 497 units.\n        Calculate the variance percentage, create an inventory adjustment due to the discrepancy, using reason code \"Cycle count variance correction\", and update warehouse accuracy metrics per the standard calculation methodology.\n        Report the percentage variance.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "instruction_amount": 497
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "LUX-WATCH-L12",
                    "system_count": 500,
                    "physical_count": 497
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "adjustment_quantity": -3,
                    "reason": "Cycle count variance correction"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-07"
                }
            }
        ],
        "outputs": [
                "\"variance_percentage\": 0.6",
                "\"inventory_accuracy_percentage\": 100.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_42",
        "instruction": "\n        In your role as operations manager for the San Diego facility, handle an inventory review for the 8-bit microcontroller component ELEC-CHIP-A1 at warehouse WH-01.\n        The current system shows low stock levels, necessitating an immediate replenishment order.\n        Arrange an urgent procurement for 10,000 units from primary supplier SUP-1001 with high priority, in addition to the existing stock of 12,500 units.\n        Prepare an incident report with the incident type 'for_monitoring' marked as low severity.\n        Examine all pending inbound deliveries for this component to assess the current pipeline status.\n    ",
        "actions": [
            {
                "name": "GetInventoryBySkuWarehouse",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "quantity": 10000,
                    "destination_warehouse": "WH-01",
                    "supplier_id": "SUP-1001",
                    "sku": "ELEC-CHIP-A1",
                    "priority": "High"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "ELEC-CHIP-A1",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "destination_warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                }
            }
        ],
        "outputs": [
                "\"quantity_available\": 12500",
                "\"quantity_inbound\": 5000",
                "\"total_expected_stock\": 17500",
                "\"status\": \"Created\"",
                "\"total_cost\": 45000",
                "\"priority\": \"High\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_43",
        "instruction": "\n        As an international trade compliance specialist, handle the import clearance process for electronics container SHIP-0001 from the Guangzhou manufacturing facility that has arrived at the San Diego port.\n        Check the completeness of import documentation, validate customs entry requirements, calculate applicable tariff obligations for Chinese electronics valued at $350,000, execute duty settlement, and progress clearance status to enable warehouse delivery.\n        Record the final tariff payment amount.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "total_value": 350000,
                    "country_of_origin": "Middle Kingdom"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "duty_amount": 17500
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "status": "Cleared"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "status": "Ready for Receipt"
                }
            }
        ],
        "outputs": [
                "\"duty_amount\": 17500"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_44",
        "instruction": "\n        Examine the performance of supplier SUP-1028 Moscow Steel Works following quality concerns and the need for shipment monitoring.\n        The current performance rating of 4.\n        2 falls below company standards, necessitating a formal improvement plan with a 60-day review cycle.\n        Analyze the status of active shipment SHIP-0028 steel delivery, file an incident report with low severity noting incident type 'for_monitoring', review all in-transit deliveries from this supplier, and evaluate the impact on warehouse WH-11 capacity.\n    ",
        "actions": [
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1028"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1028",
                    "review_cycle_days": 60
                },
            },
            {
                "name": "SearchPurchaseOrders",
                "arguments": {
                    "supplier_id": "SUP-1028",
                    "status": "In Transit"
                },
            },
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0028"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "destination_warehouse_id": "WH-11"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0028",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-11"
                }
            }
        ],
        "outputs": [
                "\"performance_rating\": 4.2",
                "\"on_time_delivery_percentage\": 92.5",
                "\"supplier_status_recommendation\": \"maintain_active\"",
                "\"warehouse_utilization\": 55.8",
                "\"total_capacity_cbm\": 120000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_45",
        "instruction": "\n        Oversee inventory monitoring for FOOD-FISH-H8 frozen tuna in WH-10 cold storage facility.\n        Stock levels are critically low for upcoming restaurant demands.\n        Examine inbound shipments to prevent duplicate ordering, confirm warehouse cold storage capacity utilization, evaluate supplier SUP-1010 performance for seafood deliveries, generate an urgent purchase order for 1000 units with Critical priority level and include notes \"Emergency seafood inventory replenishment\", and revise inventory accuracy metrics post-procurement action.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "sku": "FOOD-FISH-H8",
                    "destination_warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1010"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1010",
                    "sku": "FOOD-FISH-H8",
                    "quantity": 1000,
                    "destination_warehouse": "WH-10",
                    "priority": "Critical",
                    "notes": "Emergency seafood inventory replenishment"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-10"
                }
            }
        ],
        "outputs": [
                "\"quantity_available\": 2400",
                "\"current_inbound\": 1000",
                "\"total_capacity_cbm\": 22000",
                "\"current_utilization_percentage\": 95.5",
                "\"performance_rating\": 4.9",
                "\"po_created\": \"PO-SUP-1010-FOOD-FISH-H8-001\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_46",
        "instruction": "\n        Supervise the management of critical pharmaceutical inventory for vaccine SKU PHRM-VACC-D4 in warehouse WH-06.\n        Verify current inventory levels and storage requirements, check warehouse capacity and utilization for staging, search for incoming pharmaceutical shipments to assess the supply pipeline, conduct a mandatory cycle count showing a 150 units variance that requires an inventory adjustment with the reason \"Cycle count variance correction\", update the warehouse accuracy metrics, check the performance of supplier SUP-1006 for vaccine supply chain reliability, and search for any pending purchase orders from this pharmaceutical supplier.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "destination_warehouse_id": "WH-06"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "system_count": 20000,
                    "physical_count": 19850
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "adjustment_quantity": -150,
                    "reason": "Cycle count variance correction"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1006"
                },
            },
            {
                "name": "SearchPurchaseOrders",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "status": "Pending"
                }
            }
        ],
        "outputs": [
                "\"vaccine_quantity_available\": 18000",
                "\"warehouse_utilization\": 81.2",
                "\"physical_count\": 19850",
                "\"variance_percentage\": 0.75",
                "\"total_adjustment_value\": 2325.00",
                "\"supplier_performance_rating\": 4.9"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_47",
        "instruction": "\n        Manage emergency contamination alert for textile shipment SHIP-0020 containing Egyptian cotton from Cairo valued at $210,000.\n        Instantly quarantine all affected inventory EAC LOT202404D in WH-04 indicating \"Emergency quarantine - contamination investigation\" as the reason,\n        examine shipment documentation which indicates pending customs clearance requiring immediate focus, formulate a detailed incident report for \"contamination_alert\" with \"high\" severity level,\n        alert supplier SUP-1020 using the \"quality_incident\" notification type, compute financial exposure including a $30,000 liability\n        estimate, and instigate a voluntary product recall for the impacted EAC.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0020"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202404D",
                    "warehouse_id": "WH-04",
                    "reason": "Emergency quarantine - contamination investigation"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0020"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1020"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0020",
                    "incident_type": "contamination_alert",
                    "severity": "high"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1020",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 210000,
                    "liability_estimate": 30000
                },
            },
            {
                "name": "InitiateProductRecall",
                "arguments": {
                    "lot_number": "LOT202404D",
                    "recall_type": "voluntary"
                }
            }
        ],
        "outputs": [
                "\"total_financial_impact\": 240000",
                "\"recall_initiated\": true",
                "\"supplier_performance_rating\": 4.5",
                "\"customs_documentation_complete\": false"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_48",
        "instruction": "\n        Organize customs clearance for heavy mining equipment shipment SHIP-0011\n        from Johannesburg containing specialized drill components valued at $1,200,000.\n        Confirm all international documentation,\n        determine import duties and taxes for South African origin, process duty payment for the calculated amount, refresh customs\n        clearance status, confirm warehouse WH-11 capacity for heavy equipment, evaluate supplier SUP-1011 performance, and plan\n        equipment delivery to the Denver facility.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0011"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0011"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0011",
                    "total_value": 1200000,
                    "country_of_origin": "South Africa"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0011",
                    "duty_amount": 42000
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0011",
                    "status": "Cleared"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1011"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0011",
                    "status": "Ready for Receipt"
                }
            }
        ],
        "outputs": [
                "\"duty_amount\": 42000",
                "\"total_capacity_cbm\": 120000",
                "\"supplier_performance_rating\": 4.3",
                "\"customs_entry_number\": \"US-SHIP-0011\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_49",
        "instruction": "\n        Review warehouse capacity constraints at WH-15 San Diego beverage distribution center.\n        The current wine inventory is nearing storage capacity with cork shipment SHIP-0022 from supplier SUP-1022 delayed, causing a bottleneck.\n        Appraise space utilization, understand delayed shipment impact, evaluate supplier performance for reliability,\n        determine overflow warehouse options requiring 8000 cbm capacity, analyze beverage category distribution,\n        locate pending beverage orders that might require redistribution to other warehouses, verify current wine inventory BEVG-WINE-P16 levels,\n        confirm cork inventory MATR-CORK-T20 availability, compute optimal redistribution to nearby WH-01,\n        execute inventory adjustment to relocate 300 units of BEVG-WINE-P16 from WH-15 to WH-01 for capacity optimization\n        quoting \"Transfer to WH-01 for capacity optimization\" as the reason, formulate a detailed capacity plan using beverage_optimization strategy,\n        and update warehouse statistics.\n    ",
        "actions": [
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0022"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1022"
                },
            },
            {
                "name": "IdentifyOverflowOptions",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "required_capacity": 8000
                },
            },
            {
                "name": "AnalyzeInventoryByCategory",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "destination_warehouse_id": "WH-15",
                    "status": "pending"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "BEVG-WINE-P16",
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MATR-CORK-T20",
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "BEVG-WINE-P16",
                    "warehouse_id": "WH-15",
                    "adjustment_quantity": -300,
                    "reason": "Transfer to WH-01 for capacity optimization"
                },
            },
            {
                "name": "CreateCapacityPlan",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "optimization_strategy": "beverage_optimization"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-15"
                }
            }
        ],
        "outputs": [
                "\"utilization_percentage\": 82.0",
                "\"remaining_capacity_cbm\": 5400",
                "\"delayed_shipment_value\": 75000",
                "\"supplier_rating\": 4.6",
                "\"overflow_warehouse\": \"WH-01\"",
                "\"wine_inventory_available\": 4500",
                "\"cork_inventory_available\": 450000",
                "\"optimization_plan_id\": \"CAP-WH-15\"",
                "\"transfer_units\": 300"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_50",
        "instruction": "\n            Examine quality issues with furniture shipment SHIP-0015 from Bangkok comprising teak dining chairs EAC LOT202402B.\n            Inspect shipping conditions and carrier performance, place affected inventory EAC LOT202402B in quarantine in WH-14 with \"Quality investigation required\" as the reason,\n            compile quality_issues incident documentation, inform supplier SUP-1015 with quality_incident notification,\n            evaluate financial impact of $250,000 shipment value including potential customer claims.\n        ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0015"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "PSLN",
                    "route": "Thailand"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202402B",
                    "warehouse_id": "WH-14",
                    "reason": "Quality investigation required"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0015",
                    "incident_type": "quality_issues"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1015",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 250000
                }
            }
        ],
        "outputs": [
                "\"total_financial_impact\": 250000",
                "\"carrier_rating\": 4.4"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_51",
        "instruction": "\n        Conduct a comprehensive carrier evaluation for European automotive parts distribution.\n        Evaluate performance metrics for DLOG, NRMC, and NSTS carriers encompassing cost efficiency, delivery reliability, and damage rates.\n        Choose the most suitable carrier from these three options for the crucial 4200kg automotive glass shipment to Deutschland needing delivery within 10 days.\n        Develop thorough cost comparisons by acquiring shipping quotes: DLOG for Munich, Deutschland,\n        NRMC for Rotterdam, Netherlands, and NSTS for distribution across multiple European cities.\n        Verify current inventory levels for AUTO-GLAS-U21 in warehouse WH-03, perform a physical count which shows a system count of 200 but a physical count of 196,\n        calculate the variance and execute inventory adjustment citing \"Carrier evaluation count verification\" as the reason.\n        Create an emergency purchase order for 500 units of AUTO-GLAS-U21 automotive windshields from supplier SUP-1023\n        meant for delivery to warehouse WH-03 with top priority due to European distribution demand.\n        Produce shipping labels for existing order ORD-0003 using the chosen optimal carrier and update the order's status to shipped.\n        Evaluate warehouse capacity at WH-03 for incoming automotive glass inventory, pinpoint overflow options requiring 1000 cbm capacity,\n        devise a capacity optimization plan using automotive_consolidation strategy.\n    ",
        "actions": [
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "DLOG",
                    "route": "Europe"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "NRMC",
                    "route": "Europe"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "route": "Europe"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "Deutschland",
                    "weight_kg": 4200,
                    "priority_level": "Critical",
                    "max_transit_days": 10,
                    "carriers_list": [
                        "DLOG",
                        "NRMC",
                        "NSTS"
                    ]
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "DLOG",
                    "weight_kg": 4200,
                    "destination": "Munich, Deutschland"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "NRMC",
                    "weight_kg": 4200,
                    "destination": "Rotterdam, Netherlands"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "weight_kg": 4200,
                    "destination": "Multiple European Cities"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "instruction_amount": 196
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "AUTO-GLAS-U21",
                    "system_count": 200,
                    "physical_count": 196
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "adjustment_quantity": -4,
                    "reason": "Carrier evaluation count verification"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1023",
                    "sku": "AUTO-GLAS-U21",
                    "quantity": 500,
                    "destination_warehouse": "WH-03",
                    "priority": "High",
                    "notes": "Emergency order for European automotive glass distribution"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0003",
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0003",
                    "new_status": "Shipped"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "IdentifyOverflowOptions",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "required_capacity": 1000
                },
            },
            {
                "name": "CreateCapacityPlan",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "optimization_strategy": "automotive_consolidation"
                }
            }
        ],
        "outputs": [
                "\"recommended_carrier\": \"DLOG\"",
                "\"estimated_cost\": 7560",
                "\"delivery_reliability\": 95.8",
                "\"current_inventory\": 200",
                "\"physical_count\": 196",
                "\"variance_percentage\": 2.0",
                "\"adjustment_id\": \"ADJ-WH-03\"",
                "\"purchase_order_id\": \"PO-SUP-1023-AUTO-GLAS-U21-001\"",
                "\"tracking_number\": \"DLOG-ORD-0003\"",
                "\"warehouse_utilization\": 65.0",
                "\"overflow_warehouse\": \"WH-01\"",
                "\"capacity_plan_id\": \"CAP-WH-03\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_52",
        "instruction": "\n        Handle an audit for inventory accuracy concerning building materials BLDG-TILE-J10 ceramic tiles at the WH-12 Fort Lauderdale facility.\n        Conduct a physical count verification, determine variance compared to system records, prepare an inventory adjustment citing 'Physical count variance - building materials audit', and update warehouse accuracy metrics for compliance reporting.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "system_count": 18000,
                    "physical_count": 17865
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                    "adjustment_quantity": -135,
                    "reason": "Physical count variance - building materials audit",
                    "variance_percentage": 0.75
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-12"
                }
            }
        ],
        "outputs": [
                "\"variance_percentage\": 0.75",
                "\"total_adjustment_value\": 472.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_53",
        "instruction": "\n        Coordinate an emergency response for multiple pharmaceutical shipments SHIP-0006 and SHIP-0021 displaying temperature deviations in transit.\n        Confirm temperature logs for each shipment against the required 2-8\u00b0C pharmaceutical cold chain range with excursions_flag set to true for detecting deviations.\n        Check cold chain integrity with carriers DFC and NAC.\n        Quarantine the affected vaccine inventory for SHIP-0021, EAC LOT202405H, in WH-06 due to \"Temperature deviation - multi-shipment pharmaceutical investigation\".\n        Compile detailed incident reports for each shipment, documenting temperature_deviation events with critical severity due to pharmaceutical temperature breaches.\n        Notify suppliers SUP-1006 and SUP-1021 about the quality incidents.\n        Calculate the combined financial exposure with shipment values 450000 and 550000, and a liability estimate of 100000.\n        Escalate both critical incident reports INC-SHIP-0006-critical and INC-SHIP-0021-critical due to patient safety concerns, and trigger mandatory recalls for EAC LOT202405H due to the compromised temperature, requiring immediate market withdrawal.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "required_temp_range": "2-8",
                    "excursions_flag": true
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "required_temp_range": "2-8",
                    "excursions_flag": true
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405H",
                    "warehouse_id": "WH-06",
                    "reason": "Temperature deviation - multi-shipment pharmaceutical investigation"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0006",
                    "incident_type": "temperature_deviation",
                    "severity": "critical"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0021",
                    "incident_type": "temperature_deviation",
                    "severity": "critical"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1021",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 1000000,
                    "liability_estimate": 100000
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0006-critical",
                    "priority": "critical"
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0021-critical",
                    "priority": "critical"
                },
            },
            {
                "name": "InitiateProductRecall",
                "arguments": {
                    "lot_number": "LOT202405H",
                    "recall_type": "mandatory"
                }
            }
        ],
        "outputs": [
                "\"temperature_excursion_detected\": true",
                "\"total_financial_impact\": 1100000",
                "\"affected_shipments\": 2"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_54",
        "instruction": "\n        Review the performance of the supplier SUP-1026 (Kuala Lumpur Rubber Exports) due to recent delivery inconsistencies and quality issues.\n        Assess current performance metrics, including delivery reliability and quality ratings.\n        Develop a structured improvement plan with 45-day review milestones to address delivery inconsistencies and quality issues, recommending 'enhanced_monitoring'.\n        Examine pending purchase orders for risk assessment and review shipments from this supplier, focusing on those destined for warehouse WH-14.\n        Look into the specific details of shipment SHIP-0026 from this supplier.\n        Prepare a low-severity incident report with the type 'for_monitoring' and propose enhanced monitoring as an adjustment in the supplier relationship due to the identified performance concerns.\n    ",
        "actions": [
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1026"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1026",
                    "review_cycle_days": 45,
                    "reason": "Delivery inconsistencies and quality concerns requiring intensive monitoring",
                    "recommendation": "enhanced_monitoring"
                },
            },
            {
                "name": "SearchPurchaseOrders",
                "arguments": {
                    "supplier_id": "SUP-1026",
                    "status": "pending"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "destination_warehouse_id": "WH-14"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SUP-1026",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                },
            },
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0026"
                }
            }
        ],
        "outputs": [
                "\"performance_rating\": 4.5",
                "\"on_time_delivery_percentage\": 96.0",
                "\"supplier_status_recommendation\": \"enhanced_monitoring\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_55",
        "instruction": "\n        Manage the processing of shipment for order ORD-0002.\n        Initially, confirm the order details and customer requirements.\n        Verify complete stock allocation for all items.\n        If fully allocated, select EWDL as the shipping provider considering the Deutschland destination and High priority for order ORD-0002, with a total weight of 980 kg.\n        Evaluate carrier EWDL's performance metrics on the Munich, Deutschland route.\n        Generate shipping labels, create a low-severity incident report with type \"for_monitoring\", and denote the order as shipped.\n        Provide a tracking number along with a delivery estimate.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0002"
                },
            },
            {
                "name": "VerifyInventoryAllocation",
                "arguments": {
                    "order_id": "ORD-0002"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "EWDL",
                    "route": "Munich, Deutschland"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "Deutschland",
                    "priority_level": "High",
                    "total_weight_kg": 980,
                    "preferred_carrier": "EWDL"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0002",
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "ORD-0002",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0002",
                    "new_status": "Shipped"
                }
            }
        ],
        "outputs": [
                "\"tracking_number\": \"EWDL-ORD-0002\"",
                "\"estimated_delivery_date\": \"2024-06-05\"",
                "\"status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_56",
        "instruction": "\n        Initiate an investigation into critical shipment SHIP-0019 from Krakow, containing lithium-ion batteries suspected of hazmat handling protocol violations.\n        Check temperature logs to confirm storage remained between 15\u00b0C and 25\u00b0C during transit.\n        Record cold chain integrity status with carrier EAC for compliance in hazmat transport.\n        Quarantine the affected inventory under EAC number LOT202405G at WH-03 immediately for inspection due to safety concerns, citing \"Quarantine required pending hazmat compliance inspection for lithium-ion batteries\".\n        Generate an incident report for this high-severity hazmat compliance issue.\n        Inform supplier SUP-1019 of the compliance breach, categorized under a quality incident.\n        Calculate financial exposure based on the product value of 200000 and a projected liability of 50000 due to likely non-conformance.\n        Escalate the matter to the quality assurance team using the incident report ID with critical priority.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0019"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0019",
                    "required_temp_range": "15-25"
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0019",
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405G",
                    "warehouse_id": "WH-03",
                    "reason": "Quarantine required pending hazmat compliance inspection for lithium-ion batteries"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0019",
                    "incident_type": "hazmat_nonconformance",
                    "severity": "high"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1019",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 200000,
                    "liability_estimate": 50000
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0019-high",
                    "priority": "critical"
                }
            }
        ],
        "outputs": [
                "\"cold_chain_integrity\": \"maintained\"",
                "\"total_financial_impact\": 250000",
                "\"incident_id\": \"INC-SHIP-0019-high\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_57",
        "instruction": "\n        Handle customs clearance for ceramic tile shipment SHIP-0012 from Madrid containing premium building materials.\n        Ensure completeness of all import documentation, compute the applicable duties and fees for the total shipment value of 220000 from Spain, process the duty payment of 7700, and update customs clearance status to Cleared.\n        Create an incident report with low severity and incident type as \"for_monitoring\", then prepare the shipment for delivery to WH-12 Fort Lauderdale facility by updating status to Ready for Receipt.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0012"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0012"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0012",
                    "total_value": 220000,
                    "country_of_origin": "Spain"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0012",
                    "duty_amount": 7700
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0012",
                    "status": "Cleared"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0012",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0012",
                    "status": "Ready for Receipt"
                }
            }
        ],
        "outputs": [
                "\"duty_amount\": 7700",
                "\"customs_status\": \"Cleared\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_58",
        "instruction": "\n        Execute thorough supplier assessment for SUP-1004 (Busan Textiles Co.\n        ) due to declining performance metrics.\n        First, retrieve their current performance data and rating status.\n        Given their rating is below our 4.\n        5 threshold, promptly create a 90-day improvement plan.\n        Locate all pending purchase orders with this supplier to determine impact.\n        Subsequently, analyze current inventory levels for textile SKU APRL-TSHT-O15 at warehouse WH-04 where Busan Textiles delivers.\n        Carry out a physical count to verify accuracy against the system count of 25000 units.\n        The physical count revealed 24880 units.\n        Determine the variance between system count of 25000 and physical count of 24880.\n        Since the variance of 0.\n        48% is within our 2% threshold, adjust inventory by -120 units due to cycle count variance correction to align system with actual counts.\n        Finally, update warehouse WH-04 accuracy metrics to reflect the audit results.\n    ",
        "actions": [
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1004"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1004",
                    "review_cycle_days": 90
                },
            },
            {
                "name": "SearchPurchaseOrders",
                "arguments": {
                    "supplier_id": "SUP-1004",
                    "status": "pending"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                    "instruction_amount": 24880
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "APRL-TSHT-O15",
                    "system_count": 25000,
                    "physical_count": 24880
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                    "adjustment_quantity": -120,
                    "reason": "cycle count variance correction"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-04"
                }
            }
        ],
        "outputs": [
                "\"performance_rating\": 4.5",
                "\"variance_percentage\": 0.48",
                "\"total_adjustment_value\": 960.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_59",
        "instruction": "\n        Conduct an investigation on the temperature excursion alert for pharmaceutical shipment SHIP-0021 from Stockholm containing life-saving drugs valued at 550000.\n        The shipment was transported by Nordic Air Cargo and demands immediate assessment due to cold chain integrity concerns.\n        First, gather detailed shipment information, then inspect temperature logs to confirm if storage remained within the required 2-8C range during transit with excursions flag set to true due to reported deviations.\n        Document that carrier NAC followed standard cold chain protocols for this critical pharmaceutical cargo.\n        The physical inspection exposed temperature deviations, thus immediately quarantine the affected EAC LOT202405H at destination warehouse WH-06 with reason \"Temperature excursion detected - pharmaceutical cold chain breach requiring quality review\".\n        Prepare a high severity incident report with incident type cold_chain_failure for this temperature control breach.\n        Notify supplier SUP-1021 of this quality incident demanding immediate corrective action.\n        Calculate financial exposure including the full shipment value of 550000 plus estimated liability of 100000 for potential product loss.\n        Finally, escalate this critical quality issue to the quality assurance team using the generated incident report ID with critical priority level.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "required_temp_range": "2-8C",
                    "excursions_flag": true
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405H",
                    "warehouse_id": "WH-06",
                    "reason": "Temperature excursion detected - pharmaceutical cold chain breach requiring quality review"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0021",
                    "incident_type": "cold_chain_failure",
                    "severity": "high"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1021",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 550000,
                    "liability_estimate": 100000
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0021-high",
                    "priority": "critical"
                }
            }
        ],
        "outputs": [
                "\"shipment_value\": 550000",
                "\"temperature_compliance\": \"non-compliant\"",
                "\"cold_chain_integrity\": \"maintained\"",
                "\"quarantine_status\": \"Quarantined\"",
                "\"incident_id\": \"INC-SHIP-0021-high\"",
                "\"total_financial_impact\": 650000",
                "\"escalation_priority\": \"critical\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_60",
        "instruction": "\n        Address the capacity crisis at WH-10 San Francisco Fresh Foods DC currently at 95.\n        5% utilization nearing maximum safe limits.\n        The facility is receiving high-value frozen seafood including shipment SHIP-0010 from Melbourne Seafood Exporters (SUP-1010) containing premium tuna valued at 180000.\n        Initially, assess current warehouse capacity and utilization levels at WH-10.\n        Examine details of the incoming seafood shipment SHIP-0010 to determine space requirements.\n        Review supplier SUP-1010 performance metrics to ensure reliable delivery scheduling.\n        Since utilization exceeds 95%, identify up to 2 overflow warehouse options that can house at least 2500 cbm of frozen storage and support frozen seafood handling.\n        Analyze current inventory breakdown by category for optimization opportunities, ensuring frozen seafood is included.\n        Verify the critical frozen tuna inventory FOOD-FISH-H8 immediately - carry out a physical count with instruction amount of 2400 units.\n        Determine inventory variance between system count of 2500 and the physical count of 2400 units.\n        Due to the shortage of 100 units, adjust inventory by -100 units with reason 'Physical count variance correction for frozen seafood'.\n        Develop a capacity management plan using frozen_goods_optimization strategy to address the space constraints.\n        Finally, update warehouse accuracy metrics to reflect the inventory audit results.\n    ",
        "actions": [
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1010"
                },
            },
            {
                "name": "IdentifyOverflowOptions",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "required_capacity": 2500
                },
            },
            {
                "name": "AnalyzeInventoryByCategory",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                    "instruction_amount": 2400
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "FOOD-FISH-H8",
                    "system_count": 2500,
                    "physical_count": 2400
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                    "adjustment_quantity": -100,
                    "reason": "Physical count variance correction for frozen seafood"
                },
            },
            {
                "name": "CreateCapacityPlan",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "optimization_strategy": "frozen_goods_optimization"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-10"
                }
            }
        ],
        "outputs": [
                "\"current_utilization_percentage\": 95.5",
                "\"remaining_capacity_cbm\": 990",
                "\"shipment_value\": 180000",
                "\"supplier_rating\": 4.9",
                "\"overflow_options_found\": 2",
                "\"system_count\": 2500",
                "\"physical_count\": 2400",
                "\"variance_percentage\": 4.0",
                "\"adjustment_amount\": -100",
                "\"plan_id\": \"CAP-WH-10\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_61",
        "instruction": "\n        Coordinate comprehensive supply chain recovery following disruption to Asian electronics suppliers.\n        Critical smartphone inventory ELEC-SMART-W23 at WH-02 Portland shows only 3500 units available against reorder point of 1000, but major customer orders require a minimum of 5000 units.\n        Concurrently, delayed shipment SHIP-0002 from supplier SUP-1002 Osaka Electronics valued at 125000 is affecting production schedules.\n        Start by checking current smartphone inventory levels at WH-02, then confirm details of the delayed Osaka shipment.\n        Evaluate supplier SUP-1002 performance metrics.\n        With inventory critically low, assign SUP-1002 as the primary supplier for ELEC-SMART-W23.\n        Initiate an emergency purchase order with primary supplier SUP-1002 for 2000 units to WH-02 with Critical priority and note \"Emergency procurement for customer fulfillment - supply chain disruption recovery\".\n        Validate carrier performance for SKEX Sakura Express to ensure reliable delivery.\n        Request shipping quote for 800 kg smartphone shipment from Osaka to Portland with rate 3.\n        20 per kg.\n        Compute total financial exposure including product value of 1998000 for the emergency order plus liability estimate of 150000 for potential delays.\n        Conduct a physical count of current smartphone stock revealing 3450 units against system count of 3500.\n        Determine variance between system count of 3500 and physical count of 3450.\n        Adjust inventory by -50 units with reason \"Cycle count correction for smartphone inventory discrepancy\".\n        Investigate any pending purchase orders from SUP-1002 to evaluate supply pipeline impact.\n        Finally, formulate a comprehensive capacity management plan using electronics_optimization strategy and update WH-02 accuracy metrics.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0002"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1002"
                },
            },
            {
                "name": "GetApprovedSuppliers",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "preferred_supplier": "SUP-1002"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1002",
                    "sku": "ELEC-SMART-W23",
                    "quantity": 2000,
                    "destination_warehouse": "WH-02",
                    "priority": "Critical",
                    "notes": "Emergency procurement for customer fulfillment - supply chain disruption recovery"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "SKEX",
                    "route": "Nippon-United States"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "SKEX",
                    "weight_kg": 800,
                    "destination": "Portland"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 1998000,
                    "liability_estimate": 150000
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "instruction_amount": 3450
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "instruction_system_count": 3500,
                    "physical_count": 3450
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "adjustment_quantity": -50,
                    "reason": "Cycle count correction for smartphone inventory discrepancy"
                },
            },
            {
                "name": "SearchPurchaseOrders",
                "arguments": {
                    "supplier_id": "SUP-1002",
                    "status": "pending"
                },
            },
            {
                "name": "CreateCapacityPlan",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "optimization_strategy": "electronics_optimization"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-02"
                }
            }
        ],
        "outputs": [
                "\"quantity_available\": 3500",
                "\"delayed_shipment_value\": 125000",
                "\"supplier_rating\": 4.9",
                "\"primary_supplier_found\": \"SUP-1002\"",
                "\"po_id\": \"PO-SUP-1002-ELEC-SMART-W23-001\"",
                "\"carrier_performance\": 96.2",
                "\"shipping_quote\": 2400",
                "\"total_financial_impact\": 2148000",
                "\"physical_count\": 3450",
                "\"variance_percentage\": 1.43",
                "\"adjustment_created\": true",
                "\"pending_orders_count\": 0",
                "\"optimization_plan_id\": \"CAP-WH-02\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_62",
        "instruction": "\n        Handle complex international shipment SHIP-0013 involving hazmat chemicals from Helsinki supplier SUP-1013 with delivery delays affecting the supply chain.\n        This shipment includes flammable industrial solvents valued at 600000 and requires special handling protocols.\n        Initially, obtain detailed shipment information for SHIP-0013, then examine temperature logs to confirm that hazmat storage adhered to the required range of 4-20C during transit.\n        Confirm that carrier NRMC Nordic Marine maintained appropriate cold chain integrity for this chemical cargo.\n        As this deals with hazmat class 3 materials, promptly quarantine the affected EAC LOT202405E at destination warehouse WH-13 with the reason \"Hazmat inspection required for flammable chemical shipment pending safety clearance\".\n        Evaluate supplier SUP-1013's performance, including their rating.\n        Calculate the customs duty based on the shipment value of 600000 from Finland with a duty rate of 3.\n        5 percent.\n        Process the duty payment of 21000 to facilitate customs clearance.\n        Update the customs clearance status to Cleared for the shipment.\n        Draft a high severity incident report with chemical_handling as the incident type for this hazmat compliance review.\n        Determine the total financial exposure, considering the product value of 600000 and a liability estimate of 75000 due to handling delays.\n        Search for any outstanding purchase orders from SUP-1013 to evaluate the supply chain impact.\n        Finally, escalate this chemical handling issue to the quality team using incident ID INC-SHIP-0013-high with critical priority.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "required_temp_range": "4-20C"
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405E",
                    "warehouse_id": "WH-13",
                    "reason": "Hazmat inspection required for flammable chemical shipment pending safety clearance"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1013"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "total_value": 600000,
                    "country_of_origin": "Finland"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "duty_amount": 21000
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "status": "Cleared"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0013",
                    "incident_type": "chemical_handling",
                    "severity": "high"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 600000,
                    "liability_estimate": 75000
                },
            },
            {
                "name": "SearchPurchaseOrders",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "status": "pending"
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0013-high",
                    "priority": "critical"
                }
            }
        ],
        "outputs": [
                "\"shipment_value\": 600000",
                "\"temperature_compliance\": \"compliant\"",
                "\"cold_chain_integrity\": \"maintained\"",
                "\"quarantine_status\": \"active\"",
                "\"supplier_rating\": 4.8",
                "\"calculated_duty\": 21000",
                "\"duty_paid\": 21000",
                "\"customs_status\": \"Cleared\"",
                "\"incident_id\": \"INC-SHIP-0013-high\"",
                "\"total_financial_impact\": 675000",
                "\"pending_orders_found\": 0",
                "\"escalation_priority\": \"critical\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_64",
        "instruction": "\nCoordinate hazmat battery shipment SHIP-0019 from Krakow, which includes lithium-ion batteries valued at 200000 and requiring special handling protocols.\nAccess shipment details, then verify temperature logs to ensure storage remained within the safe operating range of 15-25C during transit.\nConfirm that the carrier EAC upheld proper hazmat handling procedures for this Class 9 dangerous goods shipment.\nDue to the batteries containing hazmat materials, quarantine the affected EAC LOT202405G at warehouse WH-03 with the reason \"Hazmat safety inspection required for lithium-ion battery shipment compliance review\".\nAssess supplier SUP-1019 Krakow IT Components' performance, including their 4.\n8 rating and 98.\n9% delivery record.\nCompose a high severity incident report with battery_safety as the incident type for this hazmat handling review.\nDetermine the financial exposure by adding the product value of 200000 and a liability estimate of 25000 for safety compliance costs.\nReview current battery inventory TECH-BATT-Q17 levels at WH-03, which show a system count of 1500 units.\nConduct a physical count, revealing 1485 units.\nCalculate the variance between the system count of 1500 and the physical count of 1485.\nImplement an inventory adjustment of -15 units with the reason \"Battery inventory audit correction for hazmat compliance\".\nLastly, escalate this safety concern to the quality team using incident ID INC-SHIP-0019-high with critical priority.\n",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0019"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0019",
                    "required_temp_range": "15-25C"
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0019",
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405G",
                    "warehouse_id": "WH-03",
                    "reason": "Hazmat safety inspection required for lithium-ion battery shipment compliance review"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1019"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0019",
                    "incident_type": "battery_safety",
                    "severity": "high"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 200000,
                    "liability_estimate": 25000
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03",
                    "instruction_amount": 1485
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "system_count": 1500,
                    "physical_count": 1485
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03",
                    "adjustment_quantity": -15,
                    "reason": "Battery inventory audit correction for hazmat compliance"
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0019-high",
                    "priority": "critical"
                }
            }
        ],
        "outputs": [
                "\"shipment_value\": 200000",
                "\"temperature_compliance\": \"compliant\"",
                "\"quarantine_status\": \"active\"",
                "\"supplier_rating\": 4.8",
                "\"incident_id\": \"INC-SHIP-0019-high\"",
                "\"total_financial_impact\": 225000",
                "\"physical_count\": 1485",
                "\"variance_percentage\": 1.0",
                "\"adjustment_amount\": -15"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_65",
        "instruction": "\n        Oversee furniture shipment SHIP-0015 from Bangkok, which includes teak dining chairs valued at 250000, with delivery scheduling issues.\n        Start by retrieving shipment details, then review supplier SUP-1015 Bangkok Furniture's performance, focusing on their 4.\n        4 rating and 95.\n        0% delivery rate.\n        As their delivery performance is below a 96% threshold, formulate a 60-day improvement plan to enforce intensive monitoring due to scheduling irregularities.\n        Confirm that carrier PSLN Pacific Sea Lines provided proper handling for this furniture cargo.\n        Inspect the current furniture inventory FURN-CHAIR-M13 at the destination WH-14, showing 520 units in stock.\n        Carry out a physical count, which reveals 515 units compared to the system count of 520.\n        Compute the variance between the system count of 520 and the physical count of 515.\n        Given the variance of 0.\n        96%, prepare an inventory adjustment of -5 units with the reason \"Furniture inventory cycle count adjustment for teak chair stock\".\n        Request a shipping quote from PSLN for a 19000 kg furniture shipment to Dallas.\n        Calculate the total logistics cost, incorporating the shipment value of 250000 and additional handling fees of 15000.\n        Investigate pending furniture orders with this supplier to assess the delivery pipeline.\n        Lastly, devise a capacity plan for WH-14 using the furniture_optimization strategy to address space utilization.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0015"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1015"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1015",
                    "review_cycle_days": 60,
                    "reason": "Scheduling inconsistencies requiring intensive monitoring"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "PSLN",
                    "route": "Thailand-United States"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "instruction_amount": 515
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "FURN-CHAIR-M13",
                    "system_count": 520,
                    "physical_count": 515
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "adjustment_quantity": -5,
                    "reason": "Furniture inventory cycle count adjustment for teak chair stock"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "PSLN",
                    "weight_kg": 19000,
                    "destination": "Dallas"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 250000,
                    "liability_estimate": 15000
                },
            },
            {
                "name": "SearchPurchaseOrders",
                "arguments": {
                    "supplier_id": "SUP-1015",
                    "status": "pending"
                },
            },
            {
                "name": "CreateCapacityPlan",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "optimization_strategy": "furniture_optimization"
                }
            }
        ],
        "outputs": [
                "\"shipment_value\": 250000",
                "\"supplier_rating\": 4.4",
                "\"improvement_plan_created\": true",
                "\"carrier_performance\": 93.5",
                "\"quantity_available\": 520",
                "\"physical_count\": 515",
                "\"variance_percentage\": 0.96",
                "\"adjustment_amount\": -5",
                "\"shipping_quote\": 57000",
                "\"total_cost\": 265000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_66",
        "instruction": "\nAdminister textile shipment SHIP-0020 from Cairo containing cotton bales valued at 210000 with quality issues requiring inspection.\nObtain shipment details first, then evaluate supplier SUP-1020 Cairo Cotton's performance, noting their 4.\n5 rating and 97.\n1% delivery rate.\nDue to quality concerns, quarantine EAC LOT202404D at warehouse WH-04 with the reason \"Quality inspection required for cotton bale shipment pending fiber analysis\".\nCheck the temperature logs to verify cotton storage stayed within the safe range of 20-25C during transport.\nEnsure that carrier NSTS NorthStar Shipping provided proper cargo handling for this textile shipment.\nReview current cotton inventory MATR-COTT-R18 levels at WH-04.\nPerform a physical count, revealing 198 units.\nCalculate the variance between the system inventory count and the physical count of 198.\nMake an inventory adjustment based on the computed variance with the reason \"Cotton inventory audit for textile quality control process\".\nCompute the customs duty for the shipment valued at 210000 from Egypt.\nProcess the calculated duty payment for customs clearance.\nUpdate the customs status to Cleared for the shipment.\nLastly, calculate the total financial impact, considering the product value of 210000 and quality inspection costs of 12000.\n",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0020"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1020"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202404D",
                    "warehouse_id": "WH-04",
                    "reason": "Quality inspection required for cotton bale shipment pending fiber analysis"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0020",
                    "required_temp_range": "20-25C"
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0020",
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "instruction_amount": 198
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "system_count": 200,
                    "physical_count": 198
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "adjustment_quantity": -2,
                    "reason": "Cotton inventory audit for textile quality control process"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0020",
                    "total_value": 210000,
                    "country_of_origin": "Egypt"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0020",
                    "duty_amount": 7350
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0020",
                    "status": "Cleared"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 210000,
                    "liability_estimate": 12000
                }
            }
        ],
        "outputs": [
                "\"shipment_value\": 210000",
                "\"supplier_rating\": 4.5",
                "\"quarantine_status\": \"active\"",
                "\"temperature_compliance\": \"compliant\"",
                "\"quantity_on_hand\": 200",
                "\"physical_count\": 198",
                "\"variance_percentage\": 1.0",
                "\"duty_amount\": 7350",
                "\"customs_status\": \"Cleared\"",
                "\"total_financial_impact\": 222000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_67",
        "instruction": "\n        Manage crucial temperature excursion for pharmaceutical shipment SHIP-0021 carrying life-saving drugs from Stockholm.\n        Examine shipment details indicating 500 units valued at 550000.\n        Assess supplier SUP-1021 Stockholm Pharma's performance, highlighting their 4.\n        9 rating and 99.\n        7% delivery rate.\n        Check temperature logs to confirm compliance with the required range of 2-8C and ensure that NAC carrier maintained cold chain integrity.\n        Current inventory reveals PHRM-DRUG-S19 in WH-06 has 500 units available.\n        Conduct a physical count, which shows 398 units.\n        Calculate the variance between the system count of 500 and the physical count of 398.\n        Implement an inventory adjustment of -102 units with the reason \"Temperature monitoring audit for pharmaceutical compliance\".\n        As a temperature excursion was noted, quarantine EAC LOT202405H at WH-06 with the reason \"Cold chain breach investigation pending regulatory review\".\n        Draft an incident report for product damage with high severity.\n        Inform supplier SUP-1021 about the quality incident.\n        Determine the financial impact, adding the product value of 550000 and regulatory investigation costs of 25000.\n        Finally, escalate incident INC-SHIP-0021-high to the quality team with critical priority.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1021"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "required_temp_range": "2-8C",
                    "excursions_flag": true
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06",
                    "instruction_amount": 398
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "PHRM-DRUG-S19",
                    "system_count": 500,
                    "physical_count": 398
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06",
                    "adjustment_quantity": -102,
                    "reason": "Temperature monitoring audit for pharmaceutical compliance"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405H",
                    "warehouse_id": "WH-06",
                    "reason": "Cold chain breach investigation pending regulatory review"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0021",
                    "incident_type": "product_damage",
                    "severity": "high"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1021",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 550000,
                    "liability_estimate": 25000
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0021-high",
                    "priority": "critical"
                }
            }
        ],
        "outputs": [
                "\"shipment_value\": 550000",
                "\"supplier_rating\": 4.9",
                "\"excursions_detected\": true",
                "\"variance_percentage\": 20.4",
                "\"quarantine_status\": \"active\"",
                "\"total_financial_impact\": 575000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_68",
        "instruction": "\n        Manage inventory distribution for ELEC-SMART-W23 smartphones at West Coast facilities.\n        Assess current inventory at WH-02 Portland, showing 3500 units available.\n        Evaluate WH-02 Portland capacity with 92.\n        1% utilization nearing its limits.\n        Evaluate single primary supplier SUP-1030 Abu Dhabi Electronics performance, rated at 4.\n        7, for potential emergency replenishment.\n        Study inventory by category at WH-09 Phoenix warehouse to locate overflow capacity.\n        Compute current utilization at WH-09,\n        which indicates 85.\n        0% usage.\n        Considering WH-02's capacity is over 90%, pinpoint overflow solutions requiring an additional 2000 units capacity.\n        Develop a capacity optimization plan for WH-09 employing the redistribute_slow_moving strategy.\n        Inspect warehouse capacity at WH-01 which shows 78.\n        5% utilization, with space available.\n        Issue an emergency purchase order for 1500 units from SUP-1030 to WH-01 with High priority, including a note on West Coast inventory\n        rebalancing needs.\n        Obtain status from the primary supplier for ELEC-SMART-W23 to confirm single supplier qualification.\n        Solicit a shipping quote from\n        Desert Falcon Cargo DFC for a 1500kg shipment to San Diego, United States.\n        Review DFC carrier performance including a delivery rate of 98.\n        1%.\n        Choose the most suitable carrier for the destination San Diego, United States with High priority, considering a 1500kg weight and preferring a DFC carrier.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1030"
                },
            },
            {
                "name": "AnalyzeInventoryByCategory",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "IdentifyOverflowOptions",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "required_capacity": 2000
                },
            },
            {
                "name": "CreateCapacityPlan",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "optimization_strategy": "redistribute_slow_moving"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1030",
                    "sku": "ELEC-SMART-W23",
                    "quantity": 1500,
                    "destination_warehouse": "WH-01",
                    "priority": "High",
                    "notes": "West Coast inventory rebalancing requirements"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1030"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "DFC",
                    "weight_kg": 1500,
                    "destination": "San Diego"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_city": "San Diego",
                    "destination_country": "United States",
                    "priority_level": "High",
                    "total_weight_kg": 1500,
                    "preferred_carrier": "DFC"
                }
            }
        ],
        "outputs": [
                "\"quantity_available\": 3500",
                "\"current_utilization_percentage\": 92.1",
                "\"supplier_rating\": 4.7",
                "\"utilization_percentage\": 85.0",
                "\"total_cost\": 1498500",
                "\"primary_supplier_verified\": \"SUP-1030\"",
                "\"estimated_cost\": 4500",
                "\"on_time_delivery_percentage\": 98.1"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_69",
        "instruction": "\n        Coordinate the processing of temperature-sensitive pharmaceutical shipment SHIP-0006 containing vaccines from Mumbai.\n        Obtain shipment details indicating 150 packages valued at 450000.\n        Examine supplier SUP-1006 Mumbai Pharma's performance, rated\n        4.\n        9 with a 99.\n        8% delivery rate.\n        Validate temperature logs within the required range of 2-8C to ensure vaccine integrity.\n        Confirm DFC Desert Falcon Cargo maintained the cold chain during transit.\n        Verify current vaccine inventory PHRM-VACC-D4 at\n        destination WH-06, showing 18000 units available.\n        Conduct a physical count revealing 17950 units.\n        Calculate the variance between\nthe system count of 18000 and physical count of 17950.\n        Adjust inventory by -50 units citing \"Pre-receipt vaccine inventory verification\n        for quality compliance\".\n        Compute customs duty for the shipment value of 450000 from India.\n        Finalize duty payment of 15750 for\n        customs clearance.\n        Update customs status to Cleared.\n        File an incident report for temperature monitoring with medium severity.\n        Assess financial impact, including product value 450000 and compliance verification costs of 8000.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1006"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "required_temp_range": "2-8C"
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "instruction_amount": 17950
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "system_count": 18000,
                    "physical_count": 17950
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "adjustment_quantity": -50,
                    "reason": "Pre-receipt vaccine inventory verification for quality compliance"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "total_value": 450000,
                    "country_of_origin": "India"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "duty_amount": 15750
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "status": "Cleared"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0006",
                    "incident_type": "temperature_monitoring",
                    "severity": "medium"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 450000,
                    "liability_estimate": 8000
                }
            }
        ],
        "outputs": [
                "\"number_of_packages\": 150",
                "\"supplier_rating\": 4.9",
                "\"temperature_compliance\": \"compliant\"",
                "\"quantity_available\": 18000",
                "\"variance_percentage\": 0.28",
                "\"duty_amount\": 15750",
                "\"total_financial_impact\": 458000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_70",
        "instruction": "\n        Oversee hazmat chemical shipment SHIP-0013 consisting of\n        flammable liquids from Helsinki.\n        Retrieve shipment details showing 400 packages valued at 600000.\n        Inspect supplier SUP-1013 Helsinki Chemicals' performance, rated 4.\n        8 with a 99.\n        2% delivery rate.\n        Verify temperature logs for the needed range of 4-20C for chemical stability.\n        Ensure Nordic Marine NRMC carrier upheld proper\n        hazmat handling procedures.\n        Inspect current chemical inventory CHEM-SOLV-K11 at WH-13 showing 380 units available.\n        Determine warehouse utilization at WH-13 to verify hazmat storage capacity.\n        Conduct a physical count revealing 378 units.\n        Determine the variance between system count of 380 and physical count of 378.\n        Adjust inventory by -2 units due to\n        \"Hazmat inventory audit for regulatory compliance verification\".\n        Since this is a hazmat class 3 shipment, sequester EAC LOT202405E at\n        WH-13 citing \"Hazmat class 3 inspection required per OSHA regulations\".\n        Calculate customs duty for the shipment value of 600000 from\n        Finland.\n        Update customs status to Cleared.\n        Compute the total financial impact, including product value 600000 and hazmat\n        compliance costs of 15000.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1013"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "required_temp_range": "4-20C"
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "instruction_amount": 378
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "system_count": 380,
                    "physical_count": 378
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "adjustment_quantity": -2,
                    "reason": "Hazmat inventory audit for regulatory compliance verification"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405E",
                    "warehouse_id": "WH-13",
                    "reason": "Hazmat class 3 inspection required per OSHA regulations"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "total_value": 600000,
                    "country_of_origin": "Finland"
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "status": "Cleared"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 600000,
                    "liability_estimate": 15000
                }
            }
        ],
        "outputs": [
                "\"hazmat_class\": \"3\"",
                "\"supplier_rating\": 4.8",
                "\"quantity_available\": 378",
                "\"utilization_percentage\": 70.0",
                "\"variance_percentage\": 0.53",
                "\"duty_amount\": 21000",
                "\"total_financial_impact\": 615000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_71",
        "instruction": "\n        Evaluate solar panel inventory TECH-SOLR-G7 at WH-09 Phoenix reflecting 1100 units available.\n        As the available stock of 1100 is below the reorder point of 250, create a purchase order for 600 units priced at $299.\n        99 from SUP-1009 Beijing Solar\n        Tech with Medium priority, noting renewable energy project requisites.\n        Examine supplier SUP-1009's performance, including\n        their 4.\n        5 rating and a 96.\n        5% delivery rate.\n        Search for existing inbound shipments of TECH-SOLR-G7 to WH-09 to verify pipeline inventory.\n        Review warehouse capacity at WH-09, indicating 85.\n        0% utilization to confirm space availability.\n        Finally, compute the total cost for the 600-unit purchase order.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1009",
                    "sku": "TECH-SOLR-G7",
                    "quantity": 600,
                    "destination_warehouse": "WH-09",
                    "priority": "Medium",
                    "notes": "Renewable energy project requirements",
                    "unit_price": 299.99
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1009"
                },
            },
            {
                "name": "SearchInboundShipments",
                "arguments": {
                    "sku": "TECH-SOLR-G7",
                    "destination_warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-09"
                }
            }
        ],
        "outputs": [
                "\"quantity_available\": 1100",
                "\"supplier_rating\": 4.5",
                "\"current_inbound\": 600",
                "\"total_cost\": 179994"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_72",
        "instruction": "\n        Evaluate luxury handbag shipment SHIP-0007 from Paris containing designer goods.\n        Retrieve shipment details indicating 12 packages valued at 90000.\n        Assess supplier SUP-1007 Paris Luxury Goods performance, with a 4.\n        7\n        rating and a 98.\n        5% delivery rate.\n        Check current handbag inventory APRL-BAG-E5 at destination WH-07 showing 120 units available.\n        Conduct a physical count revealing 119 units against the system baseline of 120 units with quantity available flag set to true.\n        Calculate the variance between system count of 120 and physical count of 119.\n        Record an inventory adjustment of -1 unit with reason \"Luxury goods quality inspection discrepancy\".\n        Verify SwiftDelivery SWDL carrier performance.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0007"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1007"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                    "instruction_amount": 119,
                    "quantity_available_flag": true
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "APRL-BAG-E5",
                    "system_count": 120,
                    "instruction_count": 119
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                    "adjustment_quantity": -1,
                    "reason": "Luxury goods quality inspection discrepancy"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "SWDL"
                }
            }
        ],
        "outputs": [
                "\"number_of_packages\": 12",
                "\"supplier_rating\": 4.7",
                "\"quantity_available\": 120",
                "\"on_time_delivery_percentage\": 97.5"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_73",
        "instruction": "\n        Handle textile order ORD-0005 for the Canadian fashion retailer.\n        Gather details of the order with shipment directed to Toronto weighing a total of 750kg.\n        Verify the status of inventory allocation for this order.\n        Inspect the current t-shirt inventory APRL-TSHT-O15 at source WH-04 which shows 22000 units available.\n        Choose GPLS as the carrier for the Canadian destination, prioritizing Medium due to the 750kg weight consideration.\n        Produce shipping labels using the Global Parcel Service GPLS carrier for this order.\n        Adjust the order status to Shipped.\n        Request a shipping quote from Global Parcel Service for the 750kg shipment to Toronto to confirm shipping expenses.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "VerifyInventoryAllocation",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_city": "Toronto",
                    "destination_country": "Maple Nation",
                    "priority_level": "Medium",
                    "total_weight_kg": 750,
                    "preferred_carrier": "GPLS"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0005",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0005",
                    "new_status": "Shipped"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "weight_kg": 750,
                    "destination": "Toronto"
                }
            }
        ],
        "outputs": [
                "\"customer_name\": \"Epsilon Fashion Co.\"",
                "\"allocation_status\": \"fully_allocated\"",
                "\"quantity_available\": 22000",
                "\"selected_carrier\": \"GPLS\"",
                "\"estimated_cost\": 2400"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_74",
        "instruction": "\n        Handle the urgent international shipment SHIP-0013 from supplier SUP-1013, which includes hazmat SKU CHEM-SOLV-K11 destined for warehouse WH-13.\n        Confirm that all customs documentation is complete, calculate the customs duty on a total value of 600000 from Finland, and process a duty payment of 15000.\n        Update the customs status to \"Cleared\", then modify the shipment status to \"Ready for Delivery\".\n        Collect performance data for carrier NSTS and request a shipping quote for a weight of 16000 kg to the destination \"Cleveland, United States\" from carrier NSTS.\n        Report the completion of customs clearance and the estimated shipping cost.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "total_value": 600000,
                    "country_of_origin": "Finland"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "duty_amount": 15000
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "status": "Cleared"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "status": "Ready for Delivery"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "weight_kg": 16000,
                    "destination": "Cleveland, United States"
                }
            }
        ],
        "outputs": [
                "\"customs_clearance_status\": \"Cleared\"",
                "\"estimated_cost\": 40000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_75",
        "instruction": "\n        An emergency shortage in mining equipment is observed: SKU HEVY-DRIL-I9 in warehouse WH-11 is critically low.\n        Examine the current inventory details, conduct a physical count with an instruction amount of 32, and compute the inventory variance between the system count of 40 and the physical count of 32.\n        Prepare an inventory adjustment with a quantity of -8 for the reason \"Physical count discrepancy correction\".\n        Identify approved suppliers for SKU HEVY-DRIL-I9, evaluate supplier SUP-1011's performance rating.\n        Since the rating is below the threshold, formulate a 90-day improvement plan citing the reason \"Performance below 4.\n        5 threshold requires improvement\".\n        Create an emergency purchase order for 25 units to supplier SUP-1011 for warehouse WH-11 with a \"Critical\" priority and notes \"Emergency replenishment for mining operations\".\n        Report the total adjustment value and status of the improvement plan.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "instruction_amount": 32
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "HEVY-DRIL-I9",
                    "system_count": 40,
                    "physical_count": 32
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "adjustment_quantity": -8,
                    "reason": "Physical count discrepancy correction"
                },
            },
            {
                "name": "GetApprovedSuppliers",
                "arguments": {
                    "sku": "HEVY-DRIL-I9"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1011"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1011",
                    "sku": "HEVY-DRIL-I9",
                    "quantity": 25,
                    "destination_warehouse": "WH-11",
                    "priority": "Critical",
                    "notes": "Emergency replenishment for mining operations"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1011",
                    "review_cycle_days": 90,
                    "reason": "Performance below 4.5 threshold requires improvement"
                }
            }
        ],
        "outputs": [
                "\"total_adjustment_value\": 17600",
                "\"improvement_plan_status\": \"Created\"",
                "\"po_id\": \"PO-SUP-1011-HEVY-DRIL-I9-001\"",
                "\"total_cost\": 87500"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_76",
        "instruction": "\n        A critical pharmaceutical shipment SHIP-0006 containing vaccines SKU PHRM-VACC-D4 from supplier SUP-1006 demands cold chain verification for warehouse WH-06.\n        Retrieve shipment details, examine temperature logs for the specified \"2-8C\" range, verify cold chain integrity with carrier DFC, and gather supplier SUP-1006's performance rating.\n        Update the shipment status to \"Cleared for Receipt\", adjust customs status to \"Cleared\", and generate an incident report with low severity and the incident type 'for_monitoring'.\n        Calculate the financial impact with a product value of 125000 and a liability estimate of 25000.\n        Report on temperature compliance and the overall financial exposure.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "required_temp_range": "2-8C"
                },
            },
            {
                "name": "VerifyColdChainIntegrity",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1006"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "status": "Cleared for Receipt"
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "status": "Cleared"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0006",
                    "incident_type": "for_monitoring",
                    "severity": "low"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 125000,
                    "liability_estimate": 25000
                }
            }
        ],
        "outputs": [
                "\"temperature_compliance\": \"maintained\"",
                "\"total_financial_exposure\": 150000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_77",
        "instruction": "\n        Handle the processing of a high-value luxury shipment SHIP-0007 containing SKU APRL-BAG-E5 from supplier SUP-1007 directed to secure warehouse WH-07.\n        Assemble shipment details, ensure all customs documentation is complete, and compute the customs duty for a total value of 90000 originating from R\u00e9publique fran\u00e7aise.\n        Process a duty payment of 3150, update the customs status to \"Cleared\", review supplier SUP-1007's performance rating, and quarantine inventory with EAC number LOT202403E in warehouse WH-07 for the reason \"High-value security verification\".\n        Report the status of customs clearance and the supplier rating.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0007"
                },
            },
            {
                "name": "VerifyCustomsDocumentation",
                "arguments": {
                    "shipment_id": "SHIP-0007"
                },
            },
            {
                "name": "CalculateCustomsDuty",
                "arguments": {
                    "shipment_id": "SHIP-0007",
                    "total_value": 90000,
                    "country_of_origin": "République française"
                },
            },
            {
                "name": "ProcessDutyPayment",
                "arguments": {
                    "shipment_id": "SHIP-0007",
                    "duty_amount": 3150
                },
            },
            {
                "name": "UpdateCustomsStatus",
                "arguments": {
                    "shipment_id": "SHIP-0007",
                    "status": "Cleared"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1007"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202403E",
                    "warehouse_id": "WH-07",
                    "reason": "High-value security verification"
                }
            }
        ],
        "outputs": [
                "\"customs_clearance_status\": \"Cleared\"",
                "\"supplier_rating\": 4.7"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_78",
        "instruction": "\n        Handle shipping optimization for the urgent international order ORD-0002 from warehouse WH-02 to Munich, Deutschland.\n        Acquire order specifications, confirm inventory allocation, obtain performance metrics for carriers NSTS and DLOG, and request shipping quotes for a weight of 980 kg to Munich, Deutschland from both NSTS and DLOG.\n        Designate DLOG as the carrier to Deutschland, ensuring priority level is High and weight is 980 kg.\n        Produce shipping labels for chosen carrier DLOG and revise order status to \"Shipped\".\n        Report the chosen carrier, performance comparison between NSTS and DLOG, and projected shipping costs.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0002"
                },
            },
            {
                "name": "VerifyInventoryAllocation",
                "arguments": {
                    "order_id": "ORD-0002"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "weight_kg": 980,
                    "destination": "Munich, Deutschland"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "DLOG",
                    "weight_kg": 980,
                    "destination": "Munich, Deutschland"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "Deutschland",
                    "priority_level": "High",
                    "total_weight_kg": 980,
                    "preferred_carrier": "DLOG"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0002",
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0002",
                    "new_status": "Shipped"
                }
            }
        ],
        "outputs": [
                "\"selected_carrier\": \"DLOG\"",
                "\"estimated_cost\": 1764",
                "\"ontime_delivery_percentage_maeu\": 94.5",
                "\"ontime_delivery_percentage_dbsg\": 95.8"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_79",
        "instruction": "\n        Handle capacity issues, as warehouse WH-09 nears inventory limits with solar panels.\n        Review capacity and utilization rate for WH-09, acquire inventory details for SKU TECH-SOLR-G7 within WH-09, and execute a physical count with a target of 1050 against a system count of 1200.\n        Calculate the inventory variance between the system count of 1200 and the physical count of 1050.\n        Formulate an inventory adjustment of quantity -150 for the reason \"Physical count correction for transfer preparation\" with each panel costing $180.\n        00, and then develop a capacity plan using the \"inventory_redistribution\" strategy for WH-09.\n        Provide a report on the adjustment value.\n    ",
        "actions": [
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "instruction_amount": 1050
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "TECH-SOLR-G7",
                    "system_count": 1200,
                    "physical_count": 1050
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "adjustment_quantity": -150,
                    "reason": "Physical count correction for transfer preparation",
                    "unit_cost": 180.0
                },
            },
            {
                "name": "CreateCapacityPlan",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "optimization_strategy": "inventory_redistribution"
                }
            }
        ],
        "outputs": [
                "\"adjustment_value\": 27000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_80",
        "instruction": "\n        Address the issue of damaged goods identified in warehouse WH-12 for SKU BLDG-TILE-J10 from supplier SUP-1012.\n        Retrieve inventory details for SKU BLDG-TILE-J10, quarantining goods with EAC number LOT202404A in WH-12 citing \"Damaged goods quality control hold\".\n        Evaluate supplier SUP-1012's performance rating, establish a supplier improvement plan with a 90-day review cycle due to \"Quality issues requiring immediate attention\".\n        Inform supplier SUP-1012 via a \"quality_incident\" notification and generate an incident report for shipment SHIP-0012 with type \"product_damage\" and severity \"medium\".\n        Deliver a report on the quarantine status and supplier improvement plan ID.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202404A",
                    "warehouse_id": "WH-12",
                    "reason": "Damaged goods quality control hold"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1012"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1012",
                    "review_cycle_days": 90,
                    "reason": "Quality issues require immediate attention"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1012",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0012",
                    "incident_type": "product_damage",
                    "severity": "medium"
                }
            }
        ],
        "outputs": [
                "\"quarantine_status\": \"Quarantined\"",
                "\"improvement_plan_id\": \"SIP-SUP-1012\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_81",
        "instruction": "\n        Manage the critical shortage of SKU AUTO-GLAS-U21 in warehouse WH-03, which falls below safety stock levels.\n        Retrieve inventory details for SKU AUTO-GLAS-U21 in WH-03 and approved suppliers for this SKU.\n        Assess supplier SUP-1023's performance rating and initiate an emergency purchase order for 100 units to supplier SUP-1023 for WH-03, marked with \"Critical\" priority and comments \"Emergency replenishment - safety stock breach\".\n        Analyze carrier performance for GPLS, select the most suitable carrier for United States, prioritizing Critical level and a weight of 1400 kg.\n        Compile a report on the emergency order status and selected carrier.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetApprovedSuppliers",
                "arguments": {
                    "sku": "AUTO-GLAS-U21"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1023"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "quantity": 100,
                    "supplier_id": "SUP-1023",
                    "sku": "AUTO-GLAS-U21",
                    "destination_warehouse": "WH-03",
                    "priority": "Critical",
                    "notes": "Emergency replenishment - safety stock breach"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "United States",
                    "priority_level": "Critical",
                    "total_weight_kg": 1400
                }
            }
        ],
        "outputs": [
                "\"emergency_order_status\": \"Created\"",
                "\"selected_carrier\": \"GPLS\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_82",
        "instruction": "\nManage a customer return received for order ORD-0003 due to a quality defect.\nObtain order information for ORD-0003 and inventory details for SKU BLDG-TILE-J10 in WH-12, and place inventory with EAC number LOT202404A in quarantine in WH-12 for \"Customer return quality investigation\".\nDraft an incident report for order ORD-0003 with type \"customer_return\" and severity \"medium\", evaluate supplier SUP-1012's performance rating, and issue a \"quality_incident\" notification to supplier SUP-1012.\nProvide a report on the incident ID and quarantine confirmation.\n",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0003"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202404A",
                    "warehouse_id": "WH-12",
                    "reason": "Customer return quality investigation"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "ORD-0003",
                    "incident_type": "customer_return",
                    "severity": "medium"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1012"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1012",
                    "notification_type": "quality_incident"
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"INC-ORD-0003-medium\"",
                "\"quarantine_confirmation\": \"Quarantined\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_83",
        "instruction": "\n        Handle the urgent perishable shipment SHIP-0010 containing SKU FOOD-FISH-H8 from supplier SUP-1010 which requires immediate processing for warehouse WH-10.\n        Retrieve shipment details, verify temperature logs for the specified range \"-5C to 0C\", obtain supplier SUP-1010's performance rating, assess carrier performance for SCF and DFC, and request shipping quotes for a weight of 1200 kg to destination \"San Francisco, United States\" from both SCF and DFC carriers.\n        Choose the optimal carrier for destination country United States, with priority level High, and weight 1200 kg.\n        Update the shipment status to \"Expedited Processing\".\n        Document temperature compliance and the chosen carrier.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0010",
                    "required_temp_range": "-5C to 0C"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1010"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "SCF",
                    "weight_kg": 1200,
                    "destination": "San Francisco, United States"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "DFC",
                    "weight_kg": 1200,
                    "destination": "San Francisco, United States"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "United States",
                    "priority_level": "High",
                    "total_weight_kg": 1200
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0010",
                    "status": "Expedited Processing"
                }
            }
        ],
        "outputs": [
                "\"temperature_compliance\": \"maintained\"",
                "\"selected_carrier\": \"DFC\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_84",
        "instruction": "\n        Coordinate a food safety alert for shipment SHIP-0005 containing SKU FOOD-COFF-C3 from supplier SUP-1005 destined for warehouse WH-05.\n        Acquire shipment details, verify temperature logs for the necessary range \"Cool, Dry\", and assess supplier SUP-1005's performance rating.\n        Place in quarantine the inventory with EAC number LOT202405C at warehouse WH-05 for the reason \"Food safety investigation - temperature deviation\".\n        Draft an incident report for shipment SHIP-0005 detailing the incident type \"food_safety_alert\" and severity \"high\", inform supplier SUP-1005 with a notification type \"quality_incident\", and compute financial impact considering the product value 110000 and liability estimate 15000.\n        Provide the quarantine status and overall financial exposure.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0005"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0005",
                    "required_temp_range": "Cool, Dry"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1005"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405C",
                    "warehouse_id": "WH-05",
                    "reason": "Food safety investigation - temperature deviation"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0005",
                    "incident_type": "food_safety_alert",
                    "severity": "high"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1005",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 110000,
                    "liability_estimate": 15000
                }
            }
        ],
        "outputs": [
                "\"quarantine_status\": \"Quarantined\"",
                "\"total_financial_exposure\": 125000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_85",
        "instruction": "\n        Conduct a security investigation for the delivered order ORD-0001 containing high-value SKU ELEC-CHIP-A1 from warehouse WH-01.\n        Retrieve order details, obtain inventory details for SKU ELEC-CHIP-A1 from warehouse WH-01, and evaluate supplier SUP-1001's performance rating and carrier performance for GPLS and SWDL.\n        Request shipping quotes for a weight of 450 kg to destination \"San Jose, United States\" from both GPLS and SWDL carriers.\n        Determine the optimal carrier for destination country United States, ensuring priority level High, and weight 450 kg.\n        Compile an incident report for order ORD-0001 with the type \"security_investigation\" and severity \"medium\".\n        Provide details of the selected carrier and include the incident ID.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0001"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1001"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "weight_kg": 450,
                    "destination": "San Jose, United States"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "SWDL",
                    "weight_kg": 450,
                    "destination": "San Jose, United States"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_country": "United States",
                    "priority_level": "High",
                    "total_weight_kg": 450,
                    "carriers_list": [
                        "GPLS",
                        "SWDL"
                    ]
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "ORD-0001",
                    "incident_type": "security_investigation",
                    "severity": "medium"
                }
            }
        ],
        "outputs": [
                "\"selected_carrier\": \"GPLS\"",
                "\"incident_id\": \"INC-ORD-0001-medium\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_86",
        "instruction": "\n        Administer a pharmaceutical compliance audit for SKU PHRM-DRUG-S19 in warehouse WH-06 from supplier SUP-1020 Cairo Cotton Co.\n        Retrieve inventory details for SKU PHRM-DRUG-S19 in warehouse WH-06, quarantine inventory with EAC number LOT202405H in warehouse WH-06 for the reason \"GDP compliance audit verification\".\n        Assess supplier SUP-1020's performance rating, devise a supplier improvement plan with a review cycle of 60 days, and state the reason \"Regulatory compliance enhancement required\" which returns improvement plan ID SIP-SUP-1020.\n        Update accuracy metrics for warehouse WH-06, compute financial impact considering the product value 600000 and liability estimate 50000.\n        Compile an incident report with low severity and type 'compliance_monitoring'.\n        Report the supplier improvement plan ID and financial exposure.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405H",
                    "warehouse_id": "WH-06",
                    "reason": "GDP compliance audit verification"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1020"
                },
            },
            {
                "name": "CreateSupplierImprovementPlan",
                "arguments": {
                    "supplier_id": "SUP-1020",
                    "review_cycle_days": 60,
                    "reason": "Regulatory compliance enhancement required"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 600000,
                    "liability_estimate": 50000
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "PHRM-DRUG-S19",
                    "incident_type": "compliance_monitoring",
                    "severity": "low"
                }
            }
        ],
        "outputs": [
                "\"improvement_plan_id\": \"SIP-SUP-1020\"",
                "\"total_financial_exposure\": 650000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_87",
        "instruction": "\n        Manage a hazmat emergency for shipment SHIP-0013 containing SKU CHEM-SOLV-K11 from supplier SUP-1013 destined for warehouse WH-13.\n        Gather shipment details, verify temperature logs for the specified range \"4-20C\", and quarantine inventory with EAC number LOT202405E at warehouse WH-13 for the reason \"Hazmat emergency containment protocol\".\n        Create an incident report for shipment SHIP-0013 featuring the type \"hazmat_emergency\" and severity \"critical\", notify supplier SUP-1013 with a notification type \"quality_incident\", and escalate to the quality team with priority \"critical\".\n        Report the incident status and confirm escalation through the escalation ID.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "required_temp_range": "4-20C"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405E",
                    "warehouse_id": "WH-13",
                    "reason": "Hazmat emergency containment protocol"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0013",
                    "incident_type": "hazmat_emergency",
                    "severity": "critical"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "notification_type": "quality_incident"
                },
            },
            {
                "name": "EscalateToQualityTeam",
                "arguments": {
                    "incident_id": "INC-SHIP-0013-critical",
                    "priority": "critical"
                }
            }
        ],
        "outputs": [
                "\"incident_status\": \"Created\"",
                "\"escalation_id\": \"ESC-INC-SHIP-0013-critical\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_88",
        "instruction": "\n        Manage quality control procedures for SKU AUTO-GLAS-U21 located in warehouse WH-03 provided by supplier SUP-1023.\n        Retrieve inventory data for SKU AUTO-GLAS-U21 in warehouse WH-03, carry out a physical count matching 175 units, determine inventory variance between system count 180 and actual physical count 175.\n        Create an inventory adjustment with a difference of -5 units due to \"Quality control precision adjustment\", acquire supplier SUP-1023's performance rating, coordinate a purchase order of 50 units at a unit price of $250 directed to supplier SUP-1023 for warehouse WH-03, giving it a \"Medium\" priority with the note \"Quality-verified replacement stock\".\n        Summarize adjustment value and purchase order status along with the total expense.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "instruction_amount": 175
                },
            },
            {
                "name": "CalculateInventoryVariance",
                "arguments": {
                    "sku": "AUTO-GLAS-U21",
                    "system_count": 180,
                    "physical_count": 175
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "adjustment_quantity": -5,
                    "reason": "Quality control precision adjustment"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1023"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "quantity": 50,
                    "supplier_id": "SUP-1023",
                    "sku": "AUTO-GLAS-U21",
                    "destination_warehouse": "WH-03",
                    "priority": "Medium",
                    "notes": "Quality-verified replacement stock",
                    "unit_price": 250.0
                }
            }
        ],
        "outputs": [
                "\"adjustment_value\": 750",
                "\"purchase_order_status\": \"Created\"",
                "\"total_cost\": 12500"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_89",
        "instruction": "\n        Handle high-priority processing for order ORD-0005 intended for the Toronto address.\n        Obtain order specifications, confirm inventory allocation for SKU MATR-COTT-R18 situated in warehouse WH-04, conduct a physical inventory count, organize an inventory modification with a deduction of 20 units citing \"picking damage\", assess carrier performance for GPLS, solicit a shipping quote for 750 kg towards \"Toronto, Maple Nation\", create shipping labels via GPLS, change order status to \"Shipped\", compute the financial implications involving shipping value 120000 and processing fee 2500.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "MATR-COTT-R18"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "adjustment_quantity": -20,
                    "reason": "picking damage"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "weight_kg": 750,
                    "destination": "Toronto, Maple Nation"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0005",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0005",
                    "new_status": "Shipped"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 120000,
                    "liability_estimate": 2500
                }
            }
        ],
        "outputs": [
                "\"tracking_number\": \"GPLS-ORD-0005\"",
                "\"total_financial_cost\": 122500"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_90",
        "instruction": "\n        Supervise the temperature-controlled delivery SHIP-0010 carrying SKU FOOD-FISH-H8 from supplier SUP-1010.\n        Acquire shipment specifics, review temperature logs ensuring they are within the \"-5C to 0C\" range, evaluate supplier performance rating, analyze warehouse capacity for destination WH-10, compute the occupancy rate for WH-10, draft an incident report specifying \"temperature_monitoring\" type with \"low\" severity, revise accuracy metrics for WH-10, calculate the financial consequences including a product value of 180000 and liability expenditure of 5000.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0010",
                    "required_range": "-5C to 0C"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1010"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0010",
                    "incident_type": "temperature_monitoring",
                    "severity": "low"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 180000,
                    "liability_estimate": 5000
                }
            }
        ],
        "outputs": [
                "\"temperature_compliance\": \"compliant\"",
                "\"total_monitoring_cost\": 185000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_91",
        "instruction": "\n        Administer an international electronics delivery for order ORD-0006 bound for Nippon.\n        Retrieve order details, evaluate inventory categorized by warehouse WH-05, assess carrier performance for NSTS and NRMC, obtain shipping quotations for 550 kg to the destination \"Yokohama, Nippon\", choose NSTS as the carrier with \"Medium\" priority for the Nippon destination, produce shipping labels, update order status to \"International Processing\", determine the financial impact derived from order value 180000 and shipment expense 2800.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "AnalyzeInventoryByCategory",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "weight_kg": 550,
                    "destination": "Yokohama, Nippon"
                },
            },
            {
                "name": "RequestShippingQuote",
                "arguments": {
                    "carrier_scac": "NRMC",
                    "weight_kg": 550,
                    "destination": "Yokohama, Nippon"
                },
            },
            {
                "name": "SelectOptimalCarrier",
                "arguments": {
                    "destination_city": "Yokohama",
                    "destination_country": "Nippon",
                    "priority_level": "Medium",
                    "preferred_carrier": "NSTS"
                },
            },
            {
                "name": "GenerateShippingLabels",
                "arguments": {
                    "order_id": "ORD-0006",
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "UpdateOrderStatus",
                "arguments": {
                    "order_id": "ORD-0006",
                    "new_status": "International Processing"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 180000,
                    "liability_estimate": 2800
                }
            }
        ],
        "outputs": [
                "\"selected_carrier\": \"NSTS\"",
                "\"total_shipment_value\": 182800"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_93",
        "instruction": "\n        Complete a cycle count audit for premium electronics in warehouse WH-02.\n        Access inventory details for SKU ELEC-SMART-W23 in WH-02, execute a physical tally, arrange an inventory adjustment reflecting a change of 100 units due to \"cycle count correction\", compute the usage percentage for WH-02, evaluate warehouse capacity, refresh accuracy measurements, compile an incident report categorized as \"inventory_variance\" with \"medium\" severity using \"ELEC-SMART-W23\" as identification, determine the financial effect entailing a variance sum of 65000 and audit expense 3500.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "adjustment_quantity": 100,
                    "reason": "cycle count correction"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "ELEC-SMART-W23",
                    "incident_type": "inventory_variance",
                    "severity": "medium"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 65000,
                    "liability_estimate": 3500
                }
            }
        ],
        "outputs": [
                "\"inventory_accuracy\": 100",
                "\"total_audit_cost\": 68500"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_94",
        "instruction": "\n        Handle monitoring of perishable goods nearing their expiration date in the Dallas food warehouse.\n        Obtain inventory specifics for SKU FOOD-COFF-C3 located in warehouse WH-05, initiate a physical count, determine the utilization percentage, create an inventory adjustment with a change of -12 and cite \"damaged_expired\" as the reason, place the inventory EAC LOT202405C in WH-05 under quarantine for \"expiration_review\", assess warehouse capacity, and compile an incident report marking it as \"expiration_alert\" with a \"medium\" severity level.\n        Update accuracy metrics.\n        Communicate the incident and utilization percentage.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-05",
                    "sku": "FOOD-COFF-C3"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "adjustment_quantity": -12,
                    "reason": "damaged_expired"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405C",
                    "warehouse_id": "WH-05",
                    "reason": "expiration_review"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "FOOD-COFF-C3",
                    "incident_type": "expiration_alert",
                    "severity": "medium"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-05"
                }
            }
        ],
        "outputs": [
                "\"incident_id\": INC-FOOD-COFF-C3-medium",
                "\"warehouse_utilization\": 75.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_95",
        "instruction": "\n        Handle processing for the delayed textile shipment SHIP-0004 from Busan supplier SUP-1004 to warehouse WH-04.\n        Acquire shipment details, check supplier performance rating, document an incident report classified as \"weather_delay\" with a \"medium\" severity, assess warehouse capacity for WH-04, compute utilization percentage, organize a purchase order for SKU MATR-COTT-R18 with a quantity of 300 and a priority marked as \"High\" for WH-04, review carrier performance for POCL, and evaluate the financial impact with a delay cost of 25000 and an inventory impact of 75000.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1004"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0004",
                    "incident_type": "weather_delay",
                    "severity": "medium"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1004",
                    "sku": "MATR-COTT-R18",
                    "quantity": 300,
                    "destination_warehouse": "WH-04",
                    "priority": "High"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "POCL"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 75000,
                    "liability_estimate": 25000
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"INC-SHIP-0004-medium\"",
                "\"total_delay_impact\": 100000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_96",
        "instruction": "\n        Coordinate the movement of the auto parts shipment SHIP-0003 from Frankfurt supplier SUP-1003 to Milwaukee depot WH-03.\n        Retrieve shipment details, cross-check supplier performance rating, check warehouse capacity, compute utilization percentage, extract inventory details for SKU AUTO-PAD-B2 in WH-03, perform a physical count, execute an inventory adjustment with an addition of 25 and the reason \"receiving_bonus\", review carrier performance for DLOG, and calculate financial impact with parts value at 200000 and rail transport cost at 12000.\n        Convey shipment arrival date and total shipment value.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0003"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1003"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "adjustment_quantity": 25,
                    "reason": "receiving_bonus"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 200000,
                    "liability_estimate": 12000
                }
            }
        ],
        "outputs": [
                "\"delivery_date\": \"2024-06-15\"",
                "\"total_shipment_value\": 212000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_97",
        "instruction": "\n        Address the processing of high-value watch parts shipment SHIP-0014 from Zurich supplier SUP-1014 to NYC vault WH-07.\n        Access shipment details, confirm compliance with high-security storage requirements, evaluate supplier performance rating, draft an incident report tagged as \"high_value_receipt\" with a \"low\" severity, quarantine inventory EAC LOT202406E in WH-07 for \"security_verification\", check carrier performance for GPLS, update accuracy metrics, and determine financial impact with a parts value of 50000 and a security cost of 5500.\n        Communicate incident ID and total luxury value.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "VerifyStorageCompliance",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "storage_type": "high_security"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1014"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0014",
                    "incident_type": "high_value_receipt",
                    "severity": "low"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202406E",
                    "warehouse_id": "WH-07",
                    "reason": "security_verification"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 50000,
                    "liability_estimate": 5500
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"INC-SHIP-0014-low\"",
                "\"total_luxury_value\": 55500"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_98",
        "instruction": "\n        Manage the logistics of the furniture shipment SHIP-0015 from Bangkok supplier SUP-1015 arriving at Dallas warehouse WH-14.\n        Gather shipment information, assess warehouse capacity, compute utilization percentage, review supplier performance rating, analyze inventory by category, carry out a physical count for furniture items with SKU FURN-CHAIR-M13, execute an inventory adjustment with a reduction of 10 due to \"shipping_damage\", alert the supplier with a \"damage_report\" type, and analyze the financial impact with furniture value at 250000 and damage cost at 15000.\n        Report warehouse utilization and physical count.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0015"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1015"
                },
            },
            {
                "name": "AnalyzeInventoryByCategory",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "adjustment_quantity": -10,
                    "reason": "shipping_damage"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1015",
                    "notification_type": "damage_report"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 250000,
                    "liability_estimate": 15000
                }
            }
        ],
        "outputs": [
                "\"physical_count\": \"596\"",
                "\"utilization_percentage\": 88.9"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_99",
        "instruction": "\n        Handle the in-transit electronics shipment SHIP-0001 originating from Guangzhou supplier SUP-1001 and destined for LA center WH-01.\n        Obtain shipment details indicating the expected arrival on 2024-06-20, assess supplier performance rating, acquire inventory details for SKU ELEC-CHIP-A1 in WH-01,\n        execute a physical count resulting in 16000 units, generate an inventory adjustment with quantity 1000 citing \"bulk_receipt\" as the reason,\n        assess warehouse capacity revealing a 78.\n        5% utilization, examine carrier performance for NSTS NorthStar Shipping, refresh accuracy metrics for WH-01,\n        compute the financial impact with electronics valued at 350000 and an import duty of 28000.\n        Communicate the expected arrival date and total import cost.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1001"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1",
                    "instruction_amount": 16000
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "adjustment_quantity": 1000,
                    "reason": "bulk_receipt"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 350000,
                    "liability_estimate": 28000
                }
            }
        ],
        "outputs": [
                "\"expected_arrival_date\": \"2024-06-20\"",
                "\"total_import_cost\": 378000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_100",
        "instruction": "\n        Supervise critical seafood shipment SHIP-0027 from Akureyri supplier SUP-1027\n        that mandates ultra-cold storage.\n        Retrieve shipment details, inspect temperature logs for adherence to the range\n        \"-18C to -15C\" with an excursion flag marked true, evaluate supplier's performance rating, confirm storage compliance with frozen conditions,\n        quarantine inventory EAC LOT202406F citing \"cold_chain_verification\" as the cause, verify warehouse capacity for the target location,\n        draft an incident report with the type \"cold_chain_receipt\" and a severity of \"low\", compute the financial impact with seafood valued at 180000\n        and cold storage expenditures of 9500.\n        Submit the temperature compliance report, incident id, and total seafood investment.\n    ",
        "actions": [
            {
                "name": "GetShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0027"
                },
            },
            {
                "name": "CheckTemperatureLogs",
                "arguments": {
                    "shipment_id": "SHIP-0027",
                    "required_range": "-18C to -15C",
                    "excursions_flag": true
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1027"
                },
            },
            {
                "name": "VerifyStorageCompliance",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "storage_type": "frozen"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202406F",
                    "warehouse_id": "WH-10",
                    "reason": "cold_chain_verification"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "SHIP-0027",
                    "incident_type": "cold_chain_receipt",
                    "severity": "low"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 180000,
                    "liability_estimate": 9500
                }
            }
        ],
        "outputs": [
                "\"temperature_compliance\": \"non-compliant\"",
                "\"incident_id\": \"INC-SHIP-0027-low\"",
                "\"total_seafood_investment\": 189500"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_101",
        "instruction": "\n        Coordinate customer return processing for order ORD-0015 associated with a Middle East shipment.\n        Fetch order details,\n        compose an incident report with the type \"customer_return\" and a severity level of \"low\",\n        scrutinize category by inventory for items returned to warehouse WH-14, perform a physical count for SKU FURN-CHAIR-M13, and quarantine inventory EAC LOT202402B\n        in WH-14 citing \"return_inspection\" as the reason, compute the utilization percentage, review performance of the associated supplier SUP-1015,\n        calculate the financial impact with a return value of 45000 and processing expenses of 2200.\n        Deliver incident id, status, and total financial cost.\n    ",
        "actions": [
            {
                "name": "GetOrderDetails",
                "arguments": {
                    "order_id": "ORD-0015"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "ORD-0015",
                    "incident_type": "customer_return",
                    "severity": "low"
                },
            },
            {
                "name": "AnalyzeInventoryByCategory",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202402B",
                    "warehouse_id": "WH-14",
                    "reason": "return_inspection"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1015"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 45000,
                    "liability_estimate": 2200
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"INC-ORD-0015-low\"",
                "\"incident_status\": \"Created\"",
                "\"total_financial_impact\": 47200"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_102",
        "instruction": "\n        Facilitate the procurement of premium coffee from S\u00e3o Paulo supplier SUP-1005.\n        Secure the supplier's performance rating, draft a purchase order with SKU FOOD-COFF-C3 for a quantity of 1200 marked \"Medium\" priority for warehouse WH-05,\n        gather inventory details for SKU FOOD-COFF-C3 in WH-05, perform the physical counting,\n        create an inventory adjustment with a quantity of -12 and reason titled \"quality_samples\", ascertain warehouse capacity, compute utilization percentage,\n        enhance accuracy metrics, and assess the financial impact with coffee valued at 264000 and a quality testing cost of 6800.\n        Convey the supplier's performance rating and total cost.\n    ",
        "actions": [
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1005"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1005",
                    "sku": "FOOD-COFF-C3",
                    "quantity": 1200,
                    "destination_warehouse": "WH-05",
                    "priority": "Medium"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-05",
                    "sku": "FOOD-COFF-C3"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "adjustment_quantity": -12,
                    "reason": "quality_samples"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 264000,
                    "liability_estimate": 6800
                }
            }
        ],
        "outputs": [
                "\"supplier_performance\": \"4.8\"",
                "\"total_commodity_investment\": 270800"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_103",
        "instruction": "\n        Evaluate high-value electronics within the Portland facility.\n        Secure inventory details for SKU ELEC-SMART-W23 in warehouse WH-02,\n        compute the utilization percentage, conduct a physical count, issue an inventory adjustment with a quantity of -10 and\n        designation \"shrinkage_investigation\", confirm storage compliance with electronics specifications, ascertain warehouse capacity,\n        draft an incident report of type \"inventory_shrinkage\" with a \"medium\" severity, refine accuracy metrics, and gauge the financial\n        impact with electronics valued at 2600000 and an investigation cost of 12000.\n        Deliver reports concerning utilization, count, and financial impact.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "adjustment_quantity": -10,
                    "reason": "shrinkage_investigation"
                },
            },
            {
                "name": "VerifyStorageCompliance",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "storage_type": "electronics"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "ELEC-SMART-W23",
                    "incident_type": "inventory_shrinkage",
                    "severity": "medium"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 2600000,
                    "liability_estimate": 12000
                }
            }
        ],
        "outputs": [
                "\"count\": \"3970\"",
                "\"utilization_percentage\": 92.1",
                "\"total_investigation_cost\": 2612000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_104",
        "instruction": "\n        Conduct a lithium battery safety compliance inspection at the Milwaukee depot concerning non-compliant hazmat storage.\n        Obtain inventory specifics for SKU TECH-BATT-Q17 in warehouse WH-03; assess hazmat storage compliance, anticipating a non-compliant finding for WH-03.\n        Quarantine inventory EAC LOT202405G in WH-03 citing \"safety_verification\"; arrange a physical count where 1450 units are identified.\n        Acquire the performance rating of supplier SUP-1020, indicating a 4.\n        5 rating; initiate an incident report with the classification \"safety_compliance\" and low severity.\n        Revise accuracy metrics for WH-03 and evaluate the financial repercussions with a battery value of 82500 and compliance cost of 5500.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "VerifyStorageCompliance",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "storage_type": "hazmat",
                    "compliant_flag": false
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202405G",
                    "warehouse_id": "WH-03",
                    "reason": "safety_verification"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17",
                    "instruction_amount": 1450
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1020"
                },
            },
            {
                "name": "CreateIncidentReport",
                "arguments": {
                    "id": "TECH-BATT-Q17",
                    "incident_type": "safety_compliance",
                    "severity": "low"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 82500,
                    "liability_estimate": 5500
                }
            }
        ],
        "outputs": [
                "\"safety_compliance_status\": \"non_compliant\"",
                "\"incident_id\": \"INC-TECH-BATT-Q17-low\"",
                "\"total_battery_compliance_cost\": 88000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_105",
        "instruction": "\n        Coordinate a ceramic tile inventory audit for a construction endeavor.\n        Retrieve inventory specifics for SKU BLDG-TILE-J10 in warehouse WH-12; acquire the performance rating of supplier SUP-1012.\n        Execute a physical inventory count, make an inventory adjustment with a quantity of 75 due to \"construction_delivery\"; quarantine inventory EAC LOT202404A in WH-12 for \"project_allocation\" and calculate the utilization percentage.\n        Determine warehouse capacity; refine accuracy metrics; examine the financial implications with a tile value of 225000 and delivery cost of 7800.\n        Offer feedback on the quarantine ID and overall construction expenditure.\n    ",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1012"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "sku": "BLDG-TILE-J10"
                },
            },
            {
                "name": "CreateInventoryAdjustment",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                    "adjustment_quantity": 75,
                    "reason": "construction_delivery"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202404A",
                    "warehouse_id": "WH-12",
                    "reason": "project_allocation"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseCapacity",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "UpdateAccuracyMetrics",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 225000,
                    "liability_estimate": 7800
                }
            }
        ],
        "outputs": [
                "\"quarantine_id\": \"QTN-LOT202404A-WH-12\"",
                "\"total_construction_cost\": 232800"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "V5TSK_USR_106",
        "instruction": "\n        Handle the immediate procurement of automotive parts from the Frankfurt supplier SUP-1003.\n        Retrieve the supplier's performance rating; access the inventory details for SKU AUTO-PAD-B2 in warehouse WH-03.\n        Calculate the utilization percentage for WH-03 and do a physical count; quarantine inventory EAC LOT202403B in WH-03 for \"batch_testing\" reasons.\n        Create a purchase order for SKU AUTO-PAD-B2, specifying a quantity of 400 with \"High\" priority for WH-03.\n        Assess carrier performance for DLOG; alert the supplier regarding the \"urgent_order\" status.\n        Determine the fiscal impact with a parts value of 180000 and a testing cost of 8500.\n        Report on the purchase order ID and total automotive expense.\n    ",
        "actions": [
            {
                "name": "GetSupplierPerformance",
                "arguments": {
                    "supplier_id": "SUP-1003"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CalculateUtilizationPercentage",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "PerformPhysicalCount",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "QuarantineInventory",
                "arguments": {
                    "lot_number": "LOT202403B",
                    "warehouse_id": "WH-03",
                    "reason": "batch_testing"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1003",
                    "sku": "AUTO-PAD-B2",
                    "quantity": 400,
                    "destination_warehouse": "WH-03",
                    "priority": "High"
                },
            },
            {
                "name": "GetCarrierPerformance",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "NotifySupplier",
                "arguments": {
                    "supplier_id": "SUP-1003",
                    "notification_type": "urgent_order"
                },
            },
            {
                "name": "CalculateFinancialImpact",
                "arguments": {
                    "product_value": 180000,
                    "liability_estimate": 8500
                }
            }
        ],
        "outputs": [
                "\"purchase_order_id\": \"PO-SUP-1003-AUTO-PAD-B2-001\"",
                "\"total_automotive_cost\": 188500"
        ]
    }
]
