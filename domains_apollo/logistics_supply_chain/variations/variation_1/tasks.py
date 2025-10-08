# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "task_01",
        "instruction": "As a pharmaceutical logistics specialist, your client, 'Delta Pharma Inc.' based in Boston, has issued a 'Critical' priority order for 20 boxes of the 'Oncology Drug A'. Your task is to guarantee the full completion and dispatch of this order. Ensure that the originating warehouse is 'FDA Registered' to manage this product, and that the shipment proceeds via Air transport. Once shipped, you must report the final tracking number associated with the order.'Delta Pharma Inc.', located in Boston, has placed a 'Critical' priority order for 20 boxes of the 'Oncology Drug A' medication. Your objective is to ensure this order is fully fulfilled and dispatched. The source warehouse must have an 'FDA Registered' certification to handle this product, and the shipment must be sent via Air transport. After shipping, you must report the final tracking number generated for the order.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Oncology Drug A"
                },
            },
            {
                "name": "ListWarehousesByCapability",
                "arguments": {
                    "certification": "FDA Registered"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Delta Pharma Inc.",
                    "destination_city": "Boston",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "PHRM-DRUG-S19",
                            "quantity": 20
                        }
                    ]
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-06",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_02",
        "instruction": "In your role as an inbound logistics coordinator, a critical delay has affected the sea shipment from 'Helsinki Chemicals Oy' starting from Helsinki. Your responsibility is to oversee this incident thoroughly. Firstly, change the shipment's status to 'Delayed' and insert the note with the precise words 'HAZMAT_DELAY_IMMEDIATE_REVIEW'. Subsequently, record a performance issue against the supplier using the code 'LATE_DELIVERY_CRITICAL'. Then, evaluate the operational implications by verifying the present inventory levels of 'Industrial Solvent' at the 'Cleveland Chemical Storage' warehouse. Lastly, you need to report the contact number for the Cleveland warehouse manager to facilitate an immediate call.'Helsinki Chemicals Oy' originating in Helsinki is critically delayed. Your objective is to manage this incident comprehensively. First, update the shipment's status to 'Delayed' and add a note with the exact text 'HAZMAT_DELAY_IMMEDIATE_REVIEW'. Then, log a performance issue against the supplier using the issue code 'LATE_DELIVERY_CRITICAL'. Afterwards, assess the operational impact by checking the current inventory level of 'Industrial Solvent' at the 'Cleveland Chemical Storage' warehouse. Finally, you must report the phone number of the Cleveland warehouse manager so a call can be placed immediately.",
        "actions": [
            {
                "name": "FindInboundShipment",
                "arguments": {
                    "supplier_name": "Helsinki Chemicals Oy",
                    "origin_city": "Helsinki"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Industrial Solvent"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "new_status": "Delayed",
                    "notes": "HAZMAT_DELAY_IMMEDIATE_REVIEW"
                },
            },
            {
                "name": "LogSupplierPerformanceIssue",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "issue_code": "LATE_DELIVERY_CRITICAL",
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Cleveland Chemical Storage"
                }
            }
        ],
        "outputs": [
                "1-216-555-0113"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_03",
        "instruction": "As an inventory planner, your task is to prepare for a significant sales promotion. The main objective is to elevate the stock level of the '8-bit Microcontroller' at the 'Midwest Parts Warehouse' to reach 10,000 units. Prior to taking action, evaluate the overall system-wide inventory for this product. Following that, carry out the necessary transfer. Your task's success will be evaluated by the correct update of the `quantity_inbound` at the destination warehouse with the transferred amount. Lastly, you must document the new 'quantity_allocated' at the source warehouse to validate the transfer.'8-bit Microcontroller' at the 'Midwest Parts Warehouse' to a target of 10,000 units. Before acting, you must first assess the total system-wide inventory for this product. Then, initiate the required transfer. The success of your task will be measured by the `quantity_inbound` at the destination warehouse being correctly updated with the transferred amount. Finally, report the new 'quantity_allocated' at the source warehouse as confirmation of the transfer.",
        "actions": [
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "InitiateWarehouseTransfer",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "quantity": 2000,
                    "from_warehouse_id": "WH-01",
                    "to_warehouse_id": "WH-03"
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                }
            }
        ],
        "outputs": [
                "4500"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_04",
        "instruction": "As a network performance manager, your duty is to audit and rectify the situation with underperforming partners. Identify and reassign all 'Shipped' orders from any ocean carrier not meeting performance standards to a top-performing alternative. After reallocating all orders for a particular carrier, modify its status to 'Under Review'. Ultimately, verify the updated operational status of the carrier 'NorthStar Shipping'.'Shipped' orders from any ocean carrier that is underperforming according to company policy to the best-performing alternative. After reassigning all orders for a given carrier, update its status to 'Under Review'. Finally, confirm the new operational status of the carrier 'NorthStar Shipping'.",
        "actions": [
            {
                "name": "FindOrdersByCarrier",
                "arguments": {
                    "carrier_name": "NorthStar Shipping",
                    "status": "Shipped"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Sea"
                },
            },
            {
                "name": "ReassignOrderCarrier",
                "arguments": {
                    "order_id": "ORD-0006",
                    "new_carrier_scac": "ALFS"
                },
            },
            {
                "name": "UpdateCarrierStatus",
                "arguments": {
                    "carrier_name": "NorthStar Shipping",
                    "status": "Under Review"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "NorthStar Shipping"
                }
            }
        ],
        "outputs": [
                "Under Review"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_05",
        "instruction": "In your role as a quality control manager at the 'NYC Luxury Vault', you have examined the recently delivered shipment from 'Paris Luxury Goods' originating in Paris. Upon inspection, you found 5 'Leather Handbag' units were damaged and unsellable. Your aim is to meticulously address this incident. Update the inventory to accurately reflect the damaged quantities, submit a formal complaint against the supplier under the code 'DAMAGED_GOODS_RECEIVED', and promptly initiate a new, high-priority purchase order to replace the 5 damaged units. Lastly, you must provide the purchase order number for this replacement order.'NYC Luxury Vault'. You have just inspected the recently received shipment from 'Paris Luxury Goods' that originated in Paris. You discovered that 5 'Leather Handbag' units are damaged and cannot be sold. Your objective is to fully process this incident. You must update the inventory to correctly reflect the damaged quantity, log a formal complaint against the supplier using the code 'DAMAGED_GOODS_RECEIVED', and immediately create a new, high-priority purchase order for the replacement of the 5 damaged units. Finally, you must report the purchase order number for this new replacement order.",
        "actions": [
            {
                "name": "FindInboundShipment",
                "arguments": {
                    "supplier_name": "Paris Luxury Goods",
                    "origin_city": "Paris",
                    "status": "Received"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Leather Handbag"
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0005",
                    "damaged_quantity": 5
                },
            },
            {
                "name": "LogSupplierPerformanceIssue",
                "arguments": {
                    "supplier_id": "SUP-1007",
                    "issue_code": "DAMAGED_GOODS_RECEIVED",
                    "shipment_id": "SHIP-0007"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1007",
                    "line_items": [
                        {
                            "sku": "APRL-BAG-E5",
                            "quantity": 5
                        }
                    ],
                    "priority": "High"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2025-0001"
                }
            }
        ],
        "outputs": [
                "PO-2025-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_06",
        "instruction": "As a customer service lead, you have a directive from your client, 'Alpha Electronics LLC', to return 50 units of the '8-bit Microcontroller' from their original sales order 'SO-2024-0001' because they did not match their new design criteria. Your task is to handle a complete return and credit for these products. You need to generate a return authorization, coordinate the return shipment back to the original warehouse, update the initial sales order to record the return, and issue a credit memo to the client's account. Conclude by communicating both the Return Authorization number and the Credit Memo ID.'Alpha Electronics LLC', has requested to return 50 units of the '8-bit Microcontroller' from their original sales order 'SO-2024-0001' because they were incompatible with their new designs. Your objective is to process a full return and credit for these items. You must create a return authorization, arrange for the return shipment back to the original warehouse, update the original sales order to reflect the return, and issue a credit memo to the customer's account. Finally, you must report both the Return Authorization number and the Credit Memo ID.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0001",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ],
                    "reason": "Incompatible with new designs."
                },
            },
            {
                "name": "CreateInboundReturnShipment",
                "arguments": {
                    "rma_id": "RMA-1001",
                    "from_customer_id": "CUST-2001",
                    "to_warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "Partially Returned"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0001",
                    "customer_id": "CUST-2001",
                    "returned_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ]
                },
            },
            {
                "name": "GetReturnAuthorizationDetails",
                "arguments": {
                    "rma_id": "RMA-1001"
                },
            },
            {
                "name": "GetCreditMemoDetails",
                "arguments": {
                    "credit_memo_id": "CM-0001"
                }
            }
        ],
        "outputs": [
                "RMA-1001",
                "CM-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_07",
        "instruction": "As a fulfillment specialist, your responsibility is to manage a 'High' priority order from 'Gamma Construction Ltd.' for one 'Basic Robotic Starter Kit' destined for their Denver location via 'Truck' transport. This order involves a virtual kit. Coordinate the fulfillment by gathering all necessary components. You must identify each component, confirm their availability in the 'Midwest Parts Warehouse', and subsequently create and dispatch an outbound order including all required components. Conclude your tasks by computing and reporting the shipment's total weight.'Gamma Construction Ltd.' has placed a 'High' priority order for one 'Basic Robotic Starter Kit' to be sent to their site in Denver via 'Truck' transport. This is a virtual kit. Your objective is to fulfill this order by gathering the components. You must identify the components, verify each is available in the 'Midwest Parts Warehouse', and then create and ship a single outbound order containing all required components. Finally, you must calculate and report the total weight of the shipment.",
        "actions": [
            {
                "name": "GetKitComponents",
                "arguments": {
                    "kit_name": "Basic Robotic Starter Kit"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Lithium-Ion Battery Pack"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 1
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Truck"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "251.4"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_08",
        "instruction": "As an order manager dealing with a sizable order, your premier client, 'Alpha Electronics LLC', has requested a 'High' priority order totaling 15,000 units of the '8-bit Microcontroller' for their main office situated in San Jose. Every shipment related to this order must be dispatched using 'Truck' transport. Your task is to ensure the complete fulfillment of this order, potentially involving dispatches from several warehouses. You must organize all necessary outbound orders per stock availability and oversee all dispatches. Conclude your duties by providing the tracking numbers for all shipments executed to address this single requirement.'Alpha Electronics LLC', has placed a 'High' priority order for a total of 15,000 units of the '8-bit Microcontroller' for their main office in San Jose. All shipments for this order must be dispatched via 'Truck' transport. Your objective is to ensure this entire order is fulfilled, even if it requires shipping from multiple warehouses. You must create all necessary outbound orders based on stock availability and dispatch all shipments. Finally, report the tracking numbers for all the shipments created to fulfill this single request.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 12500
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 2500
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Truck"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0018"
                }
            }
        ],
        "outputs": [
                "GPLS-0017",
                "GPLS-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_09",
        "instruction": "As a risk auditor, your assignment is to perform a risk assessment on our two primary luxury product lines: the 'Leather Handbag', supplied by 'Paris Luxury Goods', and the 'Automatic Watch Movement', supplied by 'Zurich Watch Parts AG'. For each item, calculate its total inventory value, determine the insurance coverage limit of the carrier used for its last inbound shipment (from Paris for the Handbag, from Zurich for the Watch Movement), and compute a risk exposure score (Total Value / Insurance Limit). Your final goal is to log an audit event identifying the product with the HIGHER risk exposure score using the outcome code 'HIGHEST_RISK_IDENTIFIED'. Ultimately, you must present only the calculated risk score for the higher-risk product, rounded to five decimal places.'Leather Handbag', supplied by 'Paris Luxury Goods', and the 'Automatic Watch Movement', supplied by 'Zurich Watch Parts AG'. For each product, you must find its total inventory value, the insurance coverage limit of the carrier used for its last inbound shipment (from Paris for the Handbag, and from Zurich for the Watch Movement), and then calculate a risk exposure score (Total Value / Insurance Limit). Your final objective is to log an audit event that identifies the product with the HIGHER risk exposure score using the outcome code 'HIGHEST_RISK_IDENTIFIED'. Finally, you must report only the calculated risk score for the higher-risk product, formatted to five decimal places.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Leather Handbag"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "APRL-BAG-E5"
                },
            },
            {
                "name": "FindInboundShipment",
                "arguments": {
                    "supplier_name": "Paris Luxury Goods",
                    "origin_city": "Paris"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "SwiftDelivery"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Automatic Watch Movement"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "LUX-WATCH-L12"
                },
            },
            {
                "name": "FindInboundShipment",
                "arguments": {
                    "supplier_name": "Zurich Watch Parts AG",
                    "origin_city": "Zurich"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Global Parcel Service"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PRODUCT_RISK_AUDIT",
                    "subject_id": "APRL-BAG-E5",
                    "outcome_code": "HIGHEST_RISK_IDENTIFIED",
                    "outcome_details": {
                        "product_name": "Leather Handbag",
                        "risk_score": 0.00128
                    }
                }
            }
        ],
        "outputs": [
                "0.00128"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_10",
        "instruction": "Operating as a logistics auditor, your role is to execute a thorough post-delivery audit for sales order 'SO-2024-0001' directed to 'Alpha Electronics LLC'. Verify full delivery compliance including inventory accuracy of the '8-bit Microcontroller' at the 'West Coast Distribution Hub', carrier performance validation for 'Global Parcel Service', alongside proper audit documentation with the code 'POST_DELIVERY_AUDIT_OK'. Convey the carrier's on-time delivery percentage.'SO-2024-0001' shipped to 'Alpha Electronics LLC'. Ensure complete delivery compliance including inventory accuracy for the '8-bit Microcontroller' at 'West Coast Distribution Hub', carrier performance validation for 'Global Parcel Service', and proper audit documentation with code 'POST_DELIVERY_AUDIT_OK'. Report the carrier's on-time delivery percentage.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
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
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Global Parcel Service"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "POST_DELIVERY_AUDIT",
                    "subject_id": "ORD-0001",
                    "outcome_code": "POST_DELIVERY_AUDIT_OK"
                }
            }
        ],
        "outputs": [
                "98.2"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_11",
        "instruction": "As a risk analyst, evaluate the adequacy of insurance coverage for high-value international shipments related to Purchase Order 'PO-2024-0011' and outbound order 'ORD-0007'. Compare the shipment values with carrier insurance limits to determine if the coverage is sufficient. Document your findings in the audit event 'INSURANCE_AUDIT' with the outcome 'AUDIT_COMPLETE' and indicate the insurance coverage status for each shipment. Finally, report the insurance coverage limit for the carrier 'Ocean Bridge'.'PO-2024-0011' and outbound order 'ORD-0007'. Determine coverage sufficiency by comparing shipment values against carrier insurance limits, document findings through audit event 'INSURANCE_AUDIT' with outcome 'AUDIT_COMPLETE', and provide coverage status for each shipment. Report the insurance coverage limit for carrier 'Ocean Bridge'.",
        "actions": [
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2024-0011"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Global Ocean Carriers"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0007"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Ocean Bridge"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "INSURANCE_AUDIT",
                    "subject_id": "SHIP-0011;ORD-0007",
                    "outcome_code": "AUDIT_COMPLETE",
                    "outcome_details": {
                        "SHIP-0011": {
                            "value": 1200000,
                            "insurance_limit": 65000000,
                            "status": "COVERED"
                        },
                        "ORD-0007": {
                            "value": 300000,
                            "insurance_limit": 55000000,
                            "status": "COVERED"
                        }
                    }
                }
            }
        ],
        "outputs": [
                "55000000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_12",
        "instruction": "Function as a returns manager. 'Alpha Electronics LLC' needs to return 50 units of the '8-bit Microcontroller' from their sales order 'SO-2024-0001' due to a defect. Apply the reason code 'DEFECT_REPORTED_BY_CUSTOMER' for authorizing the return. Your task is to manage the entire return process for these items and instantly initiate and send out a 'High' priority replacement order for them. Update the order's status to 'RETURN_PROCESSING'. Lastly, provide the tracking number for the NEW replacement shipment.'Alpha Electronics LLC' needs to return 50 units of the '8-bit Microcontroller' from their sales order 'SO-2024-0001' due to a defect. Use the reason code 'DEFECT_REPORTED_BY_CUSTOMER' for the return authorization. Your objective is to process the full return for these items and immediately create and dispatch an identical, 'High' priority replacement order for them. The order's status must be updated to 'RETURN_PROCESSING'. Finally, report the tracking number for the NEW replacement shipment.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0001",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ],
                    "reason": "DEFECT_REPORTED_BY_CUSTOMER"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "RETURN_PROCESSING"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0001",
                    "customer_id": "CUST-2001",
                    "returned_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ]
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0001",
                    "damaged_quantity": 50
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Parcel"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_13",
        "instruction": "Serve as a fulfillment planner for a major retailer. The client 'Beta Retail GmbH' in Munich has requested a 'High' priority order of 700 'Ceramic Brake Pad Sets' and 20 'Teak Wood Dining Chairs'. Each shipment must be transported via 'Air'. Fulfill the entire order, organizing separate shipments for items sourced from various warehouses. Generate all required outbound orders and dispatch all shipments as per policy. Ultimately, furnish the tracking numbers for both new shipments, separated by a semicolon.'Beta Retail GmbH' in Munich, has placed a 'High' priority order for 700 'Ceramic Brake Pad Sets' and 20 'Teak Wood Dining Chairs'. All shipments must use 'Air' transport. Your objective is to fulfill this entire order, creating separate shipments for items sourced from different warehouses. You must create all necessary outbound orders and dispatch all shipments according to policy. Finally, you must report the tracking numbers for both new shipments, joined by a semicolon.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Brake Pad Set"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Teak Wood Dining Chair"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Beta Retail GmbH",
                    "destination_city": "Munich",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 700
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Beta Retail GmbH",
                    "destination_city": "Munich",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "FURN-CHAIR-M13",
                            "quantity": 20
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0018"
                }
            }
        ],
        "outputs": [
                "GPLS-0017;GPLS-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_14",
        "instruction": "Act as a reverse logistics specialist. Oversee the return of 15 'Smartphone Model X' units from 'Beta Retail GmbH' under their order 'SO-2024-0002'. Initially, establish the Return Authorization with the reason code 'CUSTOMER_RETURN'. Once you create the return shipment, and it's flagged for customs inspection, revise the shipment's status to 'CUSTOMS_HOLD' using the specific note code 'RETURN_CUSTOMS_HOLD'. Ensure this event is logged in the audit trail with the audit event 'RETURN_SHIPMENT_EXCEPTION' and the outcome 'STATUS_CUSTOMS_HOLD'. Conclude by obtaining the primary contact email for the carrier ('Express World Delivery') and reporting it.'Smartphone Model X' units from 'Beta Retail GmbH' on their order 'SO-2024-0002'. First, create the Return Authorization using the reason code 'CUSTOMER_RETURN'. After creating the return shipment, you are notified that it is being held by customs for inspection. Your objective is to update the shipment's status to reflect this hold, using the exact status 'CUSTOMS_HOLD' and the exact note code 'RETURN_CUSTOMS_HOLD'. You must then log the event in the audit trail with the audit event 'RETURN_SHIPMENT_EXCEPTION' and outcome code 'STATUS_CUSTOMS_HOLD'. Finally, retrieve the primary contact email for the carrier ('Express World Delivery') and report it.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0002"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Smartphone Model X"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0002",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 15
                        }
                    ],
                    "reason": "CUSTOMER_RETURN"
                },
            },
            {
                "name": "CreateInboundReturnShipment",
                "arguments": {
                    "rma_id": "RMA-1001",
                    "from_customer_id": "CUST-2002",
                    "to_warehouse_id": "WH-02",
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0031",
                    "new_status": "CUSTOMS_HOLD",
                    "notes": "RETURN_CUSTOMS_HOLD"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "RETURN_SHIPMENT_EXCEPTION",
                    "subject_id": "RMA-1001",
                    "outcome_code": "STATUS_CUSTOMS_HOLD"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Express World Delivery"
                }
            }
        ],
        "outputs": [
                "info-us@expressworld.com"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_15",
        "instruction": "Operate as a proactive risk manager. Verify if 'NorthStar Shipping', the ocean carrier for outbound order 'ORD-0006' for 'Zeta Tech Solutions', which is marked as 'Shipped', fulfills performance criteria. Reassign the shipment to a superior performing alternative ocean carrier if standards are not met. After securing compliance with a suitable carrier, document an audit event with the event code 'PROACTIVE_RISK_MANAGEMENT' and the outcome code 'PROACTIVE_CARRIER_CHANGE'. Conclude by reporting the SCAC of the carrier now handling this order.'ORD-0006' for 'Zeta Tech Solutions' is currently marked as 'Shipped' and assigned to the ocean carrier 'NorthStar Shipping'. Your objective is to check if 'NorthStar Shipping' meets performance standards. If they do not, reassign the shipment to the best-performing alternative ocean carrier. After ensuring the order is assigned to a compliant carrier, log an audit event using the event code 'PROACTIVE_RISK_MANAGEMENT' and the outcome code 'PROACTIVE_CARRIER_CHANGE'. Finally, report the SCAC of the carrier now assigned to this order.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "NorthStar Shipping"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Sea"
                },
            },
            {
                "name": "ReassignOrderCarrier",
                "arguments": {
                    "order_id": "ORD-0006",
                    "new_carrier_scac": "ALFS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PROACTIVE_RISK_MANAGEMENT",
                    "subject_id": "ORD-0006",
                    "outcome_code": "PROACTIVE_CARRIER_CHANGE",
                    "outcome_details": {
                        "old_carrier": "NSTS",
                        "new_carrier": "ALFS"
                    }
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0006"
                }
            }
        ],
        "outputs": [
                "ALFS"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_16",
        "instruction": "As a risk manager, handle the comprehensive compliance and risk assessment for the high-value international shipment on Purchase Order 'PO-2024-0011' from South Africa. Ensure complete regulatory compliance for the 'Diamond Core Drill Bit' shipment, verify alignment of warehouse capabilities at 'Denver Heavy Equipment Yard' for heavy equipment handling, confirm sufficient insurance coverage by 'Global Ocean Carriers', and set up an audit trail with the 'INTERNATIONAL_SHIPMENT_AUDIT' event, ensuring an 'AUDIT_PASS' outcome. Report the policy number for the carrier's insurance.'PO-2024-0011' from South Africa. Ensure full regulatory compliance for the 'Diamond Core Drill Bit' shipment, validate warehouse capability alignment at 'Denver Heavy Equipment Yard' for heavy equipment handling, confirm adequate insurance coverage by 'Global Ocean Carriers', and establish audit trail with 'INTERNATIONAL_SHIPMENT_AUDIT' event and 'AUDIT_PASS' outcome. Report the carrier's insurance policy number.",
        "actions": [
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2024-0011"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Diamond Core Drill Bit"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Denver Heavy Equipment Yard"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Global Ocean Carriers"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "INTERNATIONAL_SHIPMENT_AUDIT",
                    "subject_id": "SHIP-0011",
                    "outcome_code": "AUDIT_PASS"
                }
            }
        ],
        "outputs": [
                "POL-GOCN-2024"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_17",
        "instruction": "As an inventory specialist, coordinate the fulfillment of a 'High' priority order from 'Alpha Electronics LLC' for 15,000 '8-bit Microcontrollers' scheduled for shipment to San Jose. Your goal is to ensure the complete fulfillment of this order by distributing shipments from multiple warehouses in accordance with policy. The end result should exhibit: 1. An outbound order for the available stock at the primary warehouse (WH-01) that is created and shipped. 2. A separate order for the remaining amount that is prepared and dispatched from the warehouse with the next-highest stock (WH-03). 3. Both shipments must use the most suitable 'Parcel' carrier. Finally, provide both tracking numbers.'High' priority order from 'Alpha Electronics LLC' for 15,000 '8-bit Microcontrollers' has been received for shipment to San Jose. Your objective is to fulfill this order completely by shipping from multiple warehouses according to policy. The final state must show: 1. An outbound order for the available stock at the primary warehouse (WH-01) is created and shipped. 2. A separate order for the remaining quantity is created and shipped from the warehouse with the next-highest stock (WH-03). 3. Both shipments must use the best 'Parcel' carrier. Finally, report both tracking numbers.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 12500
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 2500
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Parcel"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0018"
                }
            }
        ],
        "outputs": [
                "GPLS-0017",
                "GPLS-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_18",
        "instruction": "As a senior customer service agent, address the critical fulfillment error for 'Alpha Electronics LLC' order 'SO-2024-0001', where 300 'Automotive Windshields' were mistakenly sent instead of 300 '8-bit Microcontrollers'. Complete error resolution should be achieved through appropriate return processing, utilizing the reason code 'INCORRECT_ITEM_SHIPPED', and executing immediate critical priority replacement fulfillment. Update the order's status to 'ITEM_RETURNED_INCORRECTLY'. Provide the tracking number for the replacement shipment.'Alpha Electronics LLC' order 'SO-2024-0001' where 300 'Automotive Windshields' were incorrectly shipped instead of 300 '8-bit Microcontrollers'. Achieve complete error resolution through proper return processing with reason code 'INCORRECT_ITEM_SHIPPED' and immediate critical priority replacement fulfillment. The order's status must be updated to 'ITEM_RETURNED_INCORRECTLY'. Report the tracking number for the replacement shipment.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Automotive Windshield"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0001",
                    "line_items": [
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 300
                        }
                    ],
                    "reason": "INCORRECT_ITEM_SHIPPED"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "ITEM_RETURNED_INCORRECTLY"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0001",
                    "customer_id": "CUST-2001",
                    "returned_items": [
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 300
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 300
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_19",
        "instruction": "In your role as an international customer service lead, manage the return process for your client, 'Beta Retail GmbH' in Munich, Deutschland, returning 20 units of 'Smartphone Model X' from their order 'SO-2024-0002' due to a minor cosmetic defect. Your aim is to facilitate this international return and promptly dispatch an identical replacement order with 'High' priority via Air transport. You must generate the return authorization, organize the return shipment through the designated international returns carrier, issue a credit memo to the customer, and then create and dispatch the new replacement order. Lastly, report the tracking number for the NEW replacement shipment.'Beta Retail GmbH' in Munich, Deutschland, is returning 20 units of 'Smartphone Model X' from their order 'SO-2024-0002' due to a minor cosmetic defect. Your objective is to process this international return and immediately dispatch an identical replacement order with 'High' priority via Air transport. You must create the return authorization, arrange the return shipment via the designated international returns carrier, issue the customer a credit memo, and then create and ship the new replacement order. Finally, report the tracking number for the NEW replacement shipment.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0002"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Smartphone Model X"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0002",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 20
                        }
                    ],
                    "reason": "COSMETIC_DEFECT"
                },
            },
            {
                "name": "CreateInboundReturnShipment",
                "arguments": {
                    "rma_id": "RMA-1001",
                    "from_customer_id": "CUST-2002",
                    "to_warehouse_id": "WH-02",
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0002",
                    "new_status": "Processing Return"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0002",
                    "customer_id": "CUST-2002",
                    "returned_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 20
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Beta Retail GmbH",
                    "destination_city": "Munich",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 20
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-02",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_20",
        "instruction": "As a compliance auditor, your task is to carry out a thorough HAZMAT compliance audit for the inbound shipment under Purchase Order 'PO-2024-0013' arriving from Helsinki with 'Industrial Solvent'. You need to conduct and confirm the following three verifications: 1) The product's HAZMAT class is '3'. 2) The destination warehouse, 'Cleveland Chemical Storage', is qualified for Class 3 materials. 3) The carrier's ('Nordic Marine') insurance limit surpasses the shipment's overall value. After verification, register an audit event with the event type 'HAZMAT_COMPLIANCE_AUDIT' and outcome code 'AUDIT_PASS'. Finally, provide the HAZMAT UN Number for the product.'PO-2024-0013' from Helsinki, which contains 'Industrial Solvent'. You must perform and verify the following three checks: 1) The product's HAZMAT class is '3'. 2) The destination warehouse, 'Cleveland Chemical Storage', is certified for Class 3 materials. 3) The carrier's ('Nordic Marine') insurance limit is greater than the shipment's total value. After verification, log an audit event with event type 'HAZMAT_COMPLIANCE_AUDIT' and outcome code 'AUDIT_PASS'. Finally, report the HAZMAT UN Number for the product.",
        "actions": [
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2024-0013"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Industrial Solvent"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Cleveland Chemical Storage"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Nordic Marine"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "HAZMAT_COMPLIANCE_AUDIT",
                    "subject_id": "SHIP-0013",
                    "outcome_code": "AUDIT_PASS",
                    "outcome_details": {
                        "product_check": "PASS",
                        "warehouse_check": "PASS",
                        "insurance_check": "PASS"
                    }
                }
            }
        ],
        "outputs": [
                "UN1993"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_21",
        "instruction": "As a finance controller finalizing the accounts for sales order 'SO-2024-0003', verify that this order from 'Gamma Construction Ltd.' consisted of two line items: 100 'Ceramic Floor Tile' and 200 'Industrial Paper Roll'. Your aim is to execute a thorough financial reconciliation of this order. Calculate the Total Revenue using product unit prices, the Total Cost using inventory unit costs, and determine the Gross Profit Margin percentage for the entire order. Once calculations are complete, record a 'FINANCIAL_RECONCILIATION' audit event with detailed results. Lastly, report the calculated Gross Profit Margin as a percentage, rounded to two decimal places.'SO-2024-0003'. You have confirmed this order for 'Gamma Construction Ltd.' contained two line items: 100 'Ceramic Floor Tile' and 200 'Industrial Paper Roll'. Your objective is to perform a full financial reconciliation of this order. You must calculate the Total Revenue (based on product unit prices), the Total Cost (based on inventory unit costs), and the final Gross Profit Margin percentage for the entire order. After calculating, log a 'FINANCIAL_RECONCILIATION' audit event with the detailed results. Finally, report the calculated Gross Profit Margin as a percentage, rounded to two decimal places.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Industrial Paper Roll"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "BLDG-TILE-J10"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "MANU-PAPR-F6"
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "FINANCIAL_RECONCILIATION",
                    "subject_id": "ORD-0003",
                    "outcome_code": "RECONCILED_OK",
                    "outcome_details": {
                        "total_revenue": 80600,
                        "total_cost": 50350,
                        "gross_profit_margin_pct": 37.53
                    }
                }
            }
        ],
        "outputs": [
                "37.53"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_22",
        "instruction": "As a decommissioning manager overseeing the closure of the 'NYC Luxury Vault', your task is to relocate all available inventories to the 'West Coast Distribution Hub'. Specifically, coordinate the creation and initiation of warehouse transfers for the full stock of 'Leather Handbag' and 'Automatic Watch Movement'. After handling all transfers, log a single audit event with the event type 'WAREHOUSE_EVACUATION' and outcome code 'EVACUATION_COMPLETE', providing details of the SKUs and quantities moved. Finally, report the total count of individual units transferred.'NYC Luxury Vault' is scheduled to be shut down. Your objective is to evacuate all available inventory from this location to our primary 'West Coast Distribution Hub'. Specifically, you must create and initiate warehouse transfers for the entire available stock of 'Leather Handbag' and 'Automatic Watch Movement'. After initiating all transfers, log a single audit event with the event type 'WAREHOUSE_EVACUATION' and outcome code 'EVACUATION_COMPLETE', detailing the SKUs and quantities transferred. Finally, report the total number of individual units transferred.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Leather Handbag"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Automatic Watch Movement"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "NYC Luxury Vault"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "West Coast Distribution Hub"
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "InitiateWarehouseTransfer",
                "arguments": {
                    "sku": "APRL-BAG-E5",
                    "quantity": 120,
                    "from_warehouse_id": "WH-07",
                    "to_warehouse_id": "WH-01"
                },
            },
            {
                "name": "InitiateWarehouseTransfer",
                "arguments": {
                    "sku": "LUX-WATCH-L12",
                    "quantity": 450,
                    "from_warehouse_id": "WH-07",
                    "to_warehouse_id": "WH-01"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "WAREHOUSE_EVACUATION",
                    "subject_id": "WH-07",
                    "outcome_code": "EVACUATION_COMPLETE",
                    "outcome_details": {
                        "transferred_items": [
                            {
                                "sku": "APRL-BAG-E5",
                                "quantity": 120
                            },
                            {
                                "sku": "LUX-WATCH-L12",
                                "quantity": 450
                            }
                        ]
                    }
                }
            }
        ],
        "outputs": [
                "570"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_23",
        "instruction": "Serving as an exceptions handler, address the 'High' priority order 'ORD-0002' for 'Beta Retail GmbH', which has missed its promised shipping date. To resolve this, your task is to cancel the initial shipment with the status 'Cancelled - Missed Deadline', record a performance issue against the carrier using the event code 'CARRIER_PERFORMANCE_ISSUE' and outcome code 'MISSED_PROMISED_DATE', and promptly create and send a new replacement order for the same items ('Smartphone Model X', quantity 20). The replacement must be dispatched as 'Critical' priority. Finally, provide the tracking number for the expedited new shipment.'High' priority order 'ORD-0002' for 'Beta Retail GmbH' has missed its promised ship date. To fix this, your objective is to cancel the original shipment using the status 'Cancelled - Missed Deadline', log a performance issue against the carrier using the event code 'CARRIER_PERFORMANCE_ISSUE' and outcome code 'MISSED_PROMISED_DATE', and immediately create and dispatch a new replacement order for the same items ('Smartphone Model X', quantity 20). The replacement must be sent as 'Critical' priority. Finally, report the tracking number for the new, expedited shipment.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0002"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0002",
                    "new_status": "Cancelled - Missed Deadline"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "CARRIER_PERFORMANCE_ISSUE",
                    "subject_id": "EWDL",
                    "outcome_code": "MISSED_PROMISED_DATE",
                    "outcome_details": {
                        "order_id": "ORD-0002"
                    }
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Smartphone Model X"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Beta Retail GmbH",
                    "destination_city": "Munich",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 20
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-02",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_24",
        "instruction": "In your role as a senior auditor, perform a compliance examination at the 'Charlotte Cold Chain Center'. Your task is to conduct a full audit of all pharmaceutical products stored: the 'Influenza Vaccine' and the 'Oncology Drug A'. Ensure that for each product: 1) The stock status is 'In Stock'. 2) The expiration date is not past the current date. 3) The temperature and general handling storage requirements are fulfilled by the warehouse's special capabilities. After auditing both products, document a single, consolidated audit event with the event type 'PHARMA_AUDIT' and outcome code 'AUDIT_COMPLETE', noting the pass/fail status of each check for both SKUs. Lastly, report the total number of SKUs that passed all three checks.'Charlotte Cold Chain Center'. Your objective is to perform a full audit on all pharmaceutical products stored there: the 'Influenza Vaccine' and the 'Oncology Drug A'. For each product, you must verify three points: 1) Its stock status is 'In Stock'. 2) Its expiration date has not passed the current date. 3) Its temperature and general handling storage requirements are met by the warehouse's special capabilities. After auditing both products, log a single, consolidated audit event with the event type 'PHARMA_AUDIT' and outcome code 'AUDIT_COMPLETE', detailing the pass/fail status of each check for both SKUs. Finally, report the total number of SKUs that passed all three checks.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Influenza Vaccine"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Oncology Drug A"
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Charlotte Cold Chain Center"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PHARMA_AUDIT",
                    "subject_id": "WH-06",
                    "outcome_code": "AUDIT_COMPLETE",
                    "outcome_details": {
                        "PHRM-VACC-D4": {
                            "stock_status_check": "PASS",
                            "expiration_check": "PASS",
                            "storage_check": "PASS"
                        },
                        "PHRM-DRUG-S19": {
                            "stock_status_check": "PASS",
                            "expiration_check": "PASS",
                            "storage_check": "PASS"
                        }
                    }
                }
            }
        ],
        "outputs": [
                "2"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_25",
        "instruction": "As a HAZMAT logistics specialist, manage the return of 10 'Lithium-Ion Battery Packs' from 'Iota Automotive NAC' in Lyon, due to transit damage from their order 'SO-2024-0009'. Your task is to process this return and immediately send a 'Critical' priority replacement. Verify that the selected international return carrier ('Express World Delivery') is certified for the product's HAZMAT class. Post processing of the total return (including credit memo), generate and dispatch the replacement order, ensuring the new carrier is HAZMAT class compliant. Log the entire transaction. Finally, report the tracking number for the new replacement shipment.'Iota Automotive NAC' in Lyon is returning 10 'Lithium-Ion Battery Packs' from their order 'SO-2024-0009' due to damage in transit. Your objective is to process this return and immediately dispatch a 'Critical' priority replacement. You must verify that the designated international return carrier ('Express World Delivery') is certified for this product's HAZMAT class. After processing the full return (including credit memo), create and ship the replacement order, ensuring the new carrier also supports the HAZMAT class. Log the full transaction. Finally, report the tracking number for the NEW replacement shipment.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0009"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Lithium-Ion Battery Pack"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Express World Delivery"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0009",
                    "line_items": [
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 10
                        }
                    ],
                    "reason": "DAMAGED_IN_TRANSIT"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0009",
                    "customer_id": "CUST-2009",
                    "returned_items": [
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0017",
                    "damaged_quantity": 10
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Iota Automotive NAC",
                    "destination_city": "Lyon",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Global Parcel Service"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "TECH-BATT-Q17"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "HAZMAT_RETURN_REPLACE",
                    "subject_id": "ORD-0009",
                    "outcome_code": "SUCCESS",
                    "outcome_details": {
                        "replacement_order_id": "ORD-0017"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_26",
        "instruction": "As a data integrity auditor, you are required to handle a consistency check on orders 'ORD-0001' and 'ORD-0002'. For each order, retrieve its details along with those of the carrier responsible for it. Ensure that the 'carrier_name' listed in each order's record matches perfectly with the 'carrier_name' in the official carrier master record. Once both orders are checked, record a single audit event with the code 'ORDER_DATA_CONSISTENCY_CHECK', detailing the findings for each order. Lastly, provide the SCAC code for the carrier of order 'ORD-0002'.'ORD-0001' and 'ORD-0002'. For each order, you must retrieve its details and the details of the carrier that handled it. Verify that the 'carrier_name' listed on each order record exactly matches the 'carrier_name' in the official carrier master record. After checking both orders, log a single audit event with the code 'ORDER_DATA_CONSISTENCY_CHECK', detailing your findings for each order. Finally, report the SCAC code for the carrier that handled order 'ORD-0002'.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0001"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Global Parcel Service"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0002"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Express World Delivery"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "ORDER_DATA_CONSISTENCY_CHECK",
                    "subject_id": "ORD-0001;ORD-0002",
                    "outcome_code": "ALL_RECORDS_CONSISTENT",
                    "outcome_details": {
                        "ORD-0001": {
                            "status": "MATCH"
                        },
                        "ORD-0002": {
                            "status": "MATCH"
                        }
                    }
                }
            }
        ],
        "outputs": [
                "EWDL"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_27",
        "instruction": "Your role as a logistics coordinator involves optimizing shipping efficiency by merging two Denver-bound orders: the existing order 'ORD-0003' for 'Gamma Construction Ltd.' and a new high-priority order for 'Denver Heavy Equipment Yard' needing 5 'Diamond Core Drill Bits'. Implement a cost-effective consolidated shipment with a suitable truck carrier, considering insurance coverage for the total value, and create an audit trail with a 'CONSOLIDATED_SHIPMENT_PLANNED' event. Provide the SCAC code of the carrier chosen for the task.'ORD-0003' for 'Gamma Construction Ltd.' and a new high-priority order for 'Denver Heavy Equipment Yard' requesting 5 'Diamond Core Drill Bits'. Achieve cost-effective consolidated shipment with appropriate truck carrier selection based on insurance coverage for total combined value, and establish audit trail with 'CONSOLIDATED_SHIPMENT_PLANNED' event. Report the selected carrier's SCAC code.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Diamond Core Drill Bit"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Denver Heavy Equipment Yard",
                    "destination_city": "Denver",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "HEVY-DRIL-I9",
                            "quantity": 5
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Truck"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "CONSOLIDATED_SHIPMENT_PLANNED",
                    "subject_id": "ORD-0003;ORD-0017",
                    "outcome_code": "CARRIER_SELECTED",
                    "outcome_details": {
                        "chosen_carrier_scac": "GPLS",
                        "total_value": 99500
                    }
                }
            }
        ],
        "outputs": [
                "GPLS"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_28",
        "instruction": "As an auditor examining the returns process, your goal is to initiate a full return for 50 '8-bit Microcontroller' units from sales order 'SO-2024-0001' for 'Alpha Electronics LLC', using the reason code 'AUDIT_TEST_CASE'. Immediately afterward, verify your work by accessing the newly generated RMA and Credit Memo records to confirm their accuracy. Upon confirmation, document a successful audit using the event type 'RETURN_PROCESS_AUDIT' with the outcome code 'VERIFIED_OK'. Finally, disclose the created RMA ID.'8-bit Microcontroller' units from sales order 'SO-2024-0001' for 'Alpha Electronics LLC', using the specific reason code 'AUDIT_TEST_CASE'. Immediately after, you must audit your work by retrieving the newly created RMA and Credit Memo records to verify their details. After confirming, log a successful audit using the event type 'RETURN_PROCESS_AUDIT' and outcome code 'VERIFIED_OK'. Finally, report the created RMA ID.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0001",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ],
                    "reason": "AUDIT_TEST_CASE"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0001",
                    "customer_id": "CUST-2001",
                    "returned_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ]
                },
            },
            {
                "name": "GetReturnAuthorizationDetails",
                "arguments": {
                    "rma_id": "RMA-1001"
                },
            },
            {
                "name": "GetCreditMemoDetails",
                "arguments": {
                    "credit_memo_id": "CM-0001"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "RETURN_PROCESS_AUDIT",
                    "subject_id": "RMA-1001",
                    "outcome_code": "VERIFIED_OK"
                }
            }
        ],
        "outputs": [
                "RMA-1001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_29",
        "instruction": "In your capacity as an outbound planner optimizing shipments for 'Epsilon Fashion Co.', you need to coordinate their pending order 'ORD-0005' shipping from the 'Detroit Apparel Hub'. Additionally, you must prepare and send a new 'High' priority order for the same client to Toronto for 100 'Organic Cotton T-Shirts' via 'Truck' transport. Once both orders have shipped, log an audit event with the precise event type 'CONSOLIDATED_CUSTOMER_FULFILLMENT' and outcome code 'BOTH_ORDERS_SHIPPED', confirming completion. Finally, present the tracking numbers for both shipments, separated by a semicolon.'Epsilon Fashion Co.'. You need to handle their pending order 'ORD-0005' shipping from the 'Detroit Apparel Hub'. In addition, you must create and dispatch a new 'High' priority order for the same customer to Toronto for 100 'Organic Cotton T-Shirts' via 'Truck' transport. After shipping both orders, log an audit event with the exact event type 'CONSOLIDATED_CUSTOMER_FULFILLMENT' and outcome code 'BOTH_ORDERS_SHIPPED' confirming the fulfillment. Finally, report the tracking numbers for both shipments, joined by a semicolon.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Organic Cotton T-Shirt"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 100
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Truck"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0005",
                    "warehouse_id": "WH-04",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-04",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "CONSOLIDATED_CUSTOMER_FULFILLMENT",
                    "subject_id": "ORD-0005;ORD-0017",
                    "outcome_code": "BOTH_ORDERS_SHIPPED"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0005;GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_30",
        "instruction": "As a compliance manager, address the compliance breach where Purchase Order 'PO-2024-0016' containing 'Articulated Robotic Arm' was mistakenly received at 'Midwest Parts Warehouse' instead of the designated high-security location. Achieve regulatory conformity by transferring all 20 units to the correct secure warehouse, updating the shipment status to 'Received' with note code 'REDIRECTED_TO_SECURE_WAREHOUSE', and record the corrective measures taken. Provide the ID for the secure facility's warehouse where the items were redirected.'PO-2024-0016' containing 'Articulated Robotic Arm' was incorrectly received at 'Midwest Parts Warehouse' instead of the required high-security facility. Achieve regulatory compliance by relocating all 20 units to the appropriate secure warehouse, updating shipment status to 'Received' with note code 'REDIRECTED_TO_SECURE_WAREHOUSE', and documenting corrective action. Report the correct secure facility's warehouse ID.",
        "actions": [
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2024-0016"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "ListWarehousesByCapability",
                "arguments": {
                    "certification": "UL Certified Vault"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "InitiateWarehouseTransfer",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "quantity": 20,
                    "from_warehouse_id": "WH-03",
                    "to_warehouse_id": "WH-07"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0016",
                    "new_status": "Received",
                    "notes": "REDIRECTED_TO_SECURE_WAREHOUSE"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "COMPLIANCE_CORRECTION",
                    "subject_id": "SHIP-0016",
                    "outcome_code": "INVENTORY_RELOCATED_TO_SECURE",
                    "outcome_details": {
                        "moved_sku": "TECH-ROBO-N14",
                        "new_warehouse": "WH-07"
                    }
                }
            }
        ],
        "outputs": [
                "WH-07"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_31",
        "instruction": "As a finance manager, evaluate the full financial effect of handling a return for 20 'Smartphone Model X' units from 'Beta Retail GmbH' tied to sales order 'SO-2024-0002'. Compute the Net Financial Impact in USD (total credited value minus original shipping and inventory costs) using an exchange rate of 1 EUR = 1.08 USD, process the return citing reason code 'FINANCIAL_AUDIT_RETURN', and document findings through the 'RETURN_FINANCIAL_RECONCILIATION' audit event. Submit the calculated Net Financial Impact.'Smartphone Model X' units from 'Beta Retail GmbH' on sales order 'SO-2024-0002'. Calculate the Net Financial Impact in USD (total credited value minus original shipping cost and inventory cost) using 1 EUR = 1.08 USD exchange rate, process the return with reason code 'FINANCIAL_AUDIT_RETURN', and document findings through 'RETURN_FINANCIAL_RECONCILIATION' audit event. Report the calculated Net Financial Impact.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0002"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Smartphone Model X"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0002",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 20
                        }
                    ],
                    "reason": "FINANCIAL_AUDIT_RETURN"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0002",
                    "customer_id": "CUST-2002",
                    "returned_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 20
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "RETURN_FINANCIAL_RECONCILIATION",
                    "subject_id": "RMA-1001",
                    "outcome_code": "RECONCILED_OK",
                    "outcome_details": {
                        "credited_value_usd": 19980.0,
                        "shipping_cost_usd": 3456.0,
                        "inventory_cost_usd": 13000.0,
                        "net_financial_impact_usd": 3524.0
                    }
                }
            }
        ],
        "outputs": [
                "3524.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_32",
        "instruction": "As a data integrity analyst, you need to conduct a consistency verification on outbound orders 'ORD-0001' and 'ORD-0002'. For each order, obtain its comprehensive details along with the complete details of the carrier responsible. Ensure the 'carrier_name' mentioned in each order record precisely matches the 'carrier_name' in the official carrier master record. Upon reviewing both orders, record a single audit event with code 'ORDER_DATA_CONSISTENCY_CHECK', outlining the consistency status (pass/fail) for each order. Conclusively, report the SCAC code for the carrier linked to order 'ORD-0002'.'ORD-0001' and 'ORD-0002'. For each order, you must retrieve its full details and the full details of the carrier that handled it. Verify that the 'carrier_name' listed on each order record exactly matches the 'carrier_name' in the official carrier master record. After checking both orders, log a single audit event with the code 'ORDER_DATA_CONSISTENCY_CHECK', detailing the pass/fail consistency status for each order. Finally, report the SCAC code for the carrier that handled order 'ORD-0002'.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0001"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Global Parcel Service"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0002"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Express World Delivery"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "ORDER_DATA_CONSISTENCY_CHECK",
                    "subject_id": "ORD-0001;ORD-0002",
                    "outcome_code": "ALL_RECORDS_CONSISTENT",
                    "outcome_details": {
                        "ORD-0001": {
                            "status": "MATCH"
                        },
                        "ORD-0002": {
                            "status": "MATCH"
                        }
                    }
                }
            }
        ],
        "outputs": [
                "EWDL"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_33",
        "instruction": "As a senior auditor testing the fulfillment system, you need to first carry out the fulfillment for an order of 15,000 '8-bit Microcontrollers' for 'Alpha Electronics LLC' in San Jose, necessitating shipment from multiple warehouses under 'High' priority using 'Truck' transport. Subsequently, promptly audit the transactions. Confirm that the right warehouses and carrier adhered to company policy. Once verification is complete, register a consolidated audit event with the event code 'MULTI_WAREHOUSE_AUDIT' and an outcome code 'AUDIT_PASS'. Ultimately, provide the carrier's name used.'8-bit Microcontrollers' for 'Alpha Electronics LLC' to San Jose, which will require shipping from multiple warehouses under 'High' priority using 'Truck' transport. Your second objective is to immediately audit the transactions. You must verify that the correct warehouses and carrier were used according to policy. After verifying, log a consolidated audit event with the event code 'MULTI_WAREHOUSE_AUDIT' and the outcome code 'AUDIT_PASS'. Finally, report the name of the carrier used.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 12500
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 2500
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Truck"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0018"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Global Parcel Service"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "MULTI_WAREHOUSE_AUDIT",
                    "subject_id": "ORD-0017;ORD-0018",
                    "outcome_code": "AUDIT_PASS"
                }
            }
        ],
        "outputs": [
                "Global Parcel Service"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_34",
        "instruction": "As a compliance specialist, you have discovered a compliance issue where our entire stock of 'Lithium-Ion Battery Packs' is incorrectly housed at the 'Midwest Parts Warehouse' which lacks certification for HAZMAT goods. Immediately address this breach by initiating a transfer of all available stock of this item from Milwaukee to our certified facility, 'Cleveland Chemical Storage'. Post-initiation of the transfer, verify by accessing the updated inventory logs for both locations. Record the corrective action using event code 'HAZMAT_COMPLIANCE_TRANSFER' and outcome code 'INVENTORY_RELOCATED', and finally report the new 'quantity_inbound' at the Cleveland site.'Lithium-Ion Battery Packs' is incorrectly stored at the 'Midwest Parts Warehouse', which is not certified for HAZMAT goods. Your objective is to correct this compliance breach immediately. You must initiate a transfer of the entire available stock of this product from Milwaukee to our certified facility, the 'Cleveland Chemical Storage'. After initiating the transfer, you must perform a verification by retrieving the updated inventory records for both warehouses. Finally, log the corrective action with the event code 'HAZMAT_COMPLIANCE_TRANSFER' and outcome code 'INVENTORY_RELOCATED' and report the new 'quantity_inbound' at the Cleveland facility.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Lithium-Ion Battery Pack"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Midwest Parts Warehouse"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Cleveland Chemical Storage"
                },
            },
            {
                "name": "InitiateWarehouseTransfer",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "quantity": 1400,
                    "from_warehouse_id": "WH-03",
                    "to_warehouse_id": "WH-13"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "HAZMAT_COMPLIANCE_TRANSFER",
                    "subject_id": "TECH-BATT-Q17",
                    "outcome_code": "INVENTORY_RELOCATED"
                }
            }
        ],
        "outputs": [
                "1400"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_35",
        "instruction": "As an inventory accountant, ensure complete financial accountability for '8-bit Microcontroller' stock across the entire warehouse network. Attain a full system-wide inventory evaluation, encompassing total quantities, financial values, and distribution by location, with detailed audit documentation using the event code 'MULTI_WAREHOUSE_INVENTORY_AUDIT' marked with outcome 'AUDIT_COMPLETE'. Finally, report the calculated system-wide total value.'8-bit Microcontroller' inventory across the entire warehouse network. Achieve complete system-wide inventory valuation including total quantities, financial values, and location distribution, with consolidated audit documentation using event code 'MULTI_WAREHOUSE_INVENTORY_AUDIT' and outcome 'AUDIT_COMPLETE'. Report the calculated system-wide total value.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "MULTI_WAREHOUSE_INVENTORY_AUDIT",
                    "subject_id": "ELEC-CHIP-A1",
                    "outcome_code": "AUDIT_COMPLETE",
                    "outcome_details": {
                        "total_quantity_on_hand": 23000,
                        "total_value": 57500.0,
                        "location_count": 2
                    }
                }
            }
        ],
        "outputs": [
                "57500.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_36",
        "instruction": "As a quality auditor, while readying order 'ORD-0001' for 'Alpha Electronics LLC', examine the batch of 300 '8-bit Microcontroller' units designated for dispatch. Upon inspection, you discover that 10 units are defective. Your goal is to address this quality issue prior to delivery. You need to: 1) Amend the inventory records to account for the 10 newly identified defective units. 2) Void the initial order with the status 'Cancelled - Damaged Stock' to allow for proper re-processing. 3) Determine the inventory loss caused by the damaged items. 4) Record a comprehensive audit with event code 'PRE_SHIPMENT_QUALITY_FAIL' and outcome code 'ORDER_CANCELLED'. Lastly, disclose the calculated inventory loss.'ORD-0001' for 'Alpha Electronics LLC', you inspect the 300 '8-bit Microcontroller' units allocated for shipment. Your inspection reveals that 10 units are damaged. Your objective is to handle this quality failure before shipment. You must: 1) Update the inventory record to reflect the 10 newly discovered damaged units. 2) Cancel the original order with status 'Cancelled - Damaged Stock' so it can be re-processed correctly. 3) Calculate the inventory loss from the damaged goods. 4) Log a detailed audit with event code 'PRE_SHIPMENT_QUALITY_FAIL' and outcome code 'ORDER_CANCELLED'. Finally, report the calculated inventory loss.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0001",
                    "damaged_quantity": 10
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "Cancelled - Damaged Stock"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PRE_SHIPMENT_QUALITY_FAIL",
                    "subject_id": "ORD-0001",
                    "outcome_code": "ORDER_CANCELLED",
                    "outcome_details": {
                        "scrapped_qty": 10,
                        "inventory_loss_usd": 25.0
                    }
                }
            }
        ],
        "outputs": [
                "25.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_37",
        "instruction": "As a fulfillment specialist, manage a 'Critical' priority order for 'Alpha Electronics LLC' comprising 13,000 '8-bit Microcontrollers' destined for San Jose. Only 12,500 units are in stock at the 'West Coast Distribution Hub'. Your task is to fulfill the order through split shipments from various warehouses. The final results should indicate that: 1. An outbound order of 12,500 units is established and sent from San Diego (WH-01). 2. A supplementary order covering the remaining 500 units is set up and dispatched from the 'Midwest Parts Warehouse' (WH-03). 3. Both consignments are to use the optimal 'Air' carrier according to policy. Conclude by documenting the tracking numbers for both shipments.'Critical' priority order for 'Alpha Electronics LLC' for 13,000 '8-bit Microcontrollers' to be shipped to San Jose. The 'West Coast Distribution Hub' only has 12,500 units available. Your objective is to fulfill the order by creating split shipments from multiple warehouses. The final state must show: 1. An outbound order for 12,500 units is created and shipped from San Diego (WH-01). 2. A second order for the remaining 500 units is created and shipped from the 'Midwest Parts Warehouse' (WH-03). 3. Both shipments use the best 'Air' carrier per policy. Finally, report the tracking numbers for both shipments.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 12500
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 500
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "ORDER_FULFILLMENT_SPLIT",
                    "subject_id": "ORD-0017;ORD-0018",
                    "outcome_code": "FULFILLED_FROM_MULTIPLE_WAREHOUSES",
                    "outcome_details": {
                        "original_request_qty": 13000,
                        "wh1_qty": 12500,
                        "wh2_qty": 500
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017",
                "GPLS-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_38",
        "instruction": "As a transport analyst evaluating a 'High' priority shipment of 1,000 'Organic Cotton T-Shirts' to Toronto for 'Epsilon Fashion Co.', discern the best carrier option between Global Parcel Service and SwiftDelivery. Your mission involves a detailed comparative analysis aligned with policy. You should: 1) Establish and dispatch two identical test orders (one via Global Parcel Service, the other through SwiftDelivery). 2) Since the shipping fees are equivalent, implement the policy's tie-breaker rule by assessing the carriers' 'on_time_delivery_percentage'. 3) Record an audit event with the code 'CARRIER_PROFITABILITY_ANALYSIS' and outcome code 'TIEBREAKER_APPLIED'. The 'Organic Cotton T-Shirts' are primarily stocked at the East Coast Fashion Center (WH-04). Finally, announce the name of the superior carrier.'High' priority shipment of 1,000 'Organic Cotton T-Shirts' to Toronto for 'Epsilon Fashion Co.', determine the optimal carrier between Global Parcel Service and SwiftDelivery. Your objective is a comparative analysis based on policy. You must: 1) Create and ship two identical test orders (one Global Parcel Service, one SwiftDelivery). 2) As the shipping costs are identical, apply the policy's tie-breaker rule by comparing the carriers' 'on_time_delivery_percentage'. 3) Log an audit event with event code 'CARRIER_PROFITABILITY_ANALYSIS' and outcome code 'TIEBREAKER_APPLIED'. The 'Organic Cotton T-Shirts' are primarily stocked at the East Coast Fashion Center (WH-04). Finally, report the name of the superior carrier.",
        "actions": [
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 1000
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 1000
                        }
                    ]
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Organic Cotton T-Shirt"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "East Coast Fashion Center"
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
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-04",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-04",
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Global Parcel Service"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "SwiftDelivery"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "CARRIER_PROFITABILITY_ANALYSIS",
                    "subject_id": "APRL-TSHT-O15",
                    "outcome_code": "TIEBREAKER_APPLIED",
                    "outcome_details": {
                        "most_profitable_carrier": "Global Parcel Service",
                        "tiebreaker_metric": "ON_TIME_DELIVERY_PERCENTAGE"
                    }
                }
            }
        ],
        "outputs": [
                "Global Parcel Service"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_39",
        "instruction": "As an international auditor tasked with reviewing our returns procedure, first perform a complete return for 'Beta Retail GmbH' in Munich, Deutschland, involving 15 'Smartphone Model X' units from their order 'SO-2024-0002', utilizing the reason code 'AUDIT_SCENARIO'. Your ensuing task is to promptly audit this transaction. Confirm that: 1) The credit memo value aligns correctly with the product's unit price. 2) The appropriate international return carrier ('Express World Delivery') was employed. Upon verification, record a successful audit employing the event code 'INTERNATIONAL_RETURN_AUDIT' and outcome code 'RETURN_AUDIT_PASS', detailing the outcome {\"financial_check\": \"PASS\", \"logistics_check\": \"PASS\"}. Finally, furnish the ID of the incoming return shipment.'Beta Retail GmbH' in Munich, Deutschland, for 15 'Smartphone Model X' units from their sales order 'SO-2024-0002', using the reason code 'AUDIT_SCENARIO'. Your second objective is to immediately audit this transaction. You must verify that: 1) The credit memo value correctly matches the product's unit price. 2) The correct international return carrier ('Express World Delivery') was used. After verifying, log a successful audit using the event code 'INTERNATIONAL_RETURN_AUDIT' and outcome code 'RETURN_AUDIT_PASS', with the outcome details {\"financial_check\": \"PASS\", \"logistics_check\": \"PASS\"}. Finally, report the ID of the inbound return shipment created.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0002"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Smartphone Model X"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0002",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 15
                        }
                    ],
                    "reason": "AUDIT_SCENARIO"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0002",
                    "customer_id": "CUST-2002",
                    "returned_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 15
                        }
                    ]
                },
            },
            {
                "name": "CreateInboundReturnShipment",
                "arguments": {
                    "rma_id": "RMA-1001",
                    "from_customer_id": "CUST-2002",
                    "to_warehouse_id": "WH-02",
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "GetCreditMemoDetails",
                "arguments": {
                    "credit_memo_id": "CM-0002"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Express World Delivery"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "INTERNATIONAL_RETURN_AUDIT",
                    "subject_id": "RMA-1001",
                    "outcome_code": "RETURN_AUDIT_PASS",
                    "outcome_details": {
                        "financial_check": "PASS",
                        "logistics_check": "PASS"
                    }
                }
            }
        ],
        "outputs": [
                "SHIP-0031"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_40",
        "instruction": "As a priority fulfillment manager, you oversee a new 'Critical' order for 10,000 '8-bit Microcontrollers' for 'Zeta Tech Solutions', located in Yokohama, which necessitates shipping from the 'West Coast Distribution Hub'. Upon evaluation, you note that although the warehouse possesses stock, it's fully assigned to a 'Low' priority order, 'ORD-0001'. You must resolve this impasse by cancelling the low-priority order ('ORD-0001') to release the inventory. Subsequently, initiate and dispatch the new 'Critical' order for Zeta Tech Solutions, assigning it the ID 'ORD-0017'. Record the resolution event. Finally, provide the tracking number for the new critical shipment.'Critical' priority order for 10,000 '8-bit Microcontrollers' for 'Zeta Tech Solutions', located in Yokohama, that must ship from the 'West Coast Distribution Hub'. Upon checking, you see the warehouse has stock on hand, but none is available. The entire stock is allocated to a 'Low' priority order, 'ORD-0001'. Your objective is to resolve this deadlock. You must cancel the low-priority order ('ORD-0001') to free up the inventory. Then, create and ship the new 'Critical' order for Zeta Tech Solutions. This new order will be assigned the ID 'ORD-0017'. Log the resolution event. Finally, report the tracking number for the new critical shipment.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
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
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "Cancelled"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Zeta Tech Solutions",
                    "destination_city": "Yokohama",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 10000
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "DEADLOCK_RESOLUTION",
                    "subject_id": "ORD-0017",
                    "outcome_code": "FULFILLED_BY_CANCELLING_ORD-0001"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_41",
        "instruction": "As a finance auditor, your task is to verify the integrity of inventory data. Focus on the 'Teak Wood Dining Chair' located at the 'Dallas Home Goods DC' by conducting a full reconciliation of its financial inventory record. Begin by retrieving the inventory record to obtain the 'quantity_on_hand' and 'unit_cost', and manually recalculate the accurate 'total_value'. Afterward, compare your calculated value with the 'total_value' recorded in the system. Document an audit event with the code 'INVENTORY_FINANCIAL_AUDIT', specifying both the system value and the one you calculated. Lastly, provide a report of your computed total value.'Teak Wood Dining Chair' at the 'Dallas Home Goods DC', your objective is to perform a full financial reconciliation of its inventory record. You must retrieve the inventory record to get the system's 'quantity_on_hand' and 'unit_cost', then manually recalculate the correct 'total_value'. You must then compare your calculated value with the 'total_value' currently stored in the system. Log an audit event with the code 'INVENTORY_FINANCIAL_AUDIT' detailing both the system value and your calculated value. Finally, report your calculated total value.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Teak Wood Dining Chair"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Dallas Home Goods DC"
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
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "INVENTORY_FINANCIAL_AUDIT",
                    "subject_id": "INV-0013",
                    "outcome_code": "VALUES_RECONCILED",
                    "outcome_details": {
                        "system_total_value": 72000.0,
                        "calculated_total_value": 72000.0,
                        "discrepancy": 0.0
                    }
                }
            }
        ],
        "outputs": [
                "72000.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_42",
        "instruction": "Taking the role of a logistics planner, manage the consolidated order for 'Epsilon Fashion Co.' earmarked for Toronto with a 'High' priority label. The order comprises 20 'Teak Wood Dining Chairs' and 10 'Raw Cotton Bales'. Ship each item from its respective source warehouse using 'Truck' transportation. Your task is to coordinate the completion of this fulfillment. Ensure the resulting state is as follows: 1) A shipment of chairs is organized from their source warehouse (WH-14). 2) A separate shipment for the cotton bales is arranged from their respective source warehouse (WH-04). 3) Both shipments utilize the most efficient 'Truck' carrier. Conclude by reporting the tracking numbers for both shipments, separated by a semicolon.'Epsilon Fashion Co.' to be sent to Toronto with 'High' priority. The order consists of 20 'Teak Wood Dining Chairs' and 10 'Raw Cotton Bales'. The items must be shipped from their respective source warehouses via 'Truck' transport. Your objective is to execute this fulfillment. The final state must show: 1) A shipment for the chairs is created from their source warehouse (WH-14). 2) A separate shipment for the cotton bales is created from their source warehouse (WH-04). 3) Both shipments use the best-performing 'Truck' carrier. Finally, report the tracking numbers for both shipments, joined by a semicolon.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Teak Wood Dining Chair"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Raw Cotton Bale"
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "FURN-CHAIR-M13",
                            "quantity": 20
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "MATR-COTT-R18",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Truck"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-04",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0018"
                }
            }
        ],
        "outputs": [
                "GPLS-0017;GPLS-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_43",
        "instruction": "You are acting as a priority fulfillment manager addressing a new 'Critical' priority order for 10,000 '8-bit Microcontrollers' for 'Zeta Tech Solutions', which must be dispatched from the 'West Coast Distribution Hub' to Yokohama. Upon review, you find stock is available in the warehouse, yet it is not accessible as it is fully assigned to a 'Low' priority order, 'ORD-0001'. Your goal is to address this deadlock. Cancel the low-priority order ('ORD-0001') to release the inventory, then create and dispatch the new 'Critical' order. Record the resolution event. Lastly, report the tracking number for the new critical shipment.'Critical' priority order for 10,000 '8-bit Microcontrollers' for 'Zeta Tech Solutions' that must ship from the 'West Coast Distribution Hub' to Yokohama. Upon checking, you see the warehouse has stock on hand, but none is available. The entire stock is allocated to a 'Low' priority order, 'ORD-0001'. Your objective is to resolve this deadlock. You must cancel the low-priority order ('ORD-0001') to free up the inventory, then create and ship the new 'Critical' order. Log the resolution event. Finally, report the tracking number for the new critical shipment.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "West Coast Distribution Hub"
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
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "Cancelled"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Zeta Tech Solutions",
                    "destination_city": "Yokohama",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 10000
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "DEADLOCK_RESOLUTION",
                    "subject_id": "ORD-0017",
                    "outcome_code": "FULFILLED_BY_CANCELLING_ORD-0001"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_44",
        "instruction": "As a kitting specialist, make sure to effectively fulfill a high-priority order for a 'Basic Robotic Starter Kit' for 'Gamma Construction Ltd.' headed for Denver from the 'Midwest Parts Warehouse'. Ensure compliance for pre-fulfillment verification of every kit component, successful order creation and shipment, and audit confirmation of fulfillment success. The audit must indicate that the 'Articulated Robotic Arm' compliance check results in 'FAIL' and that the 'Lithium-Ion Battery Pack' compliance check is 'FAIL' as well. Provide the tracking number.'Basic Robotic Starter Kit' order for 'Gamma Construction Ltd.' destined for Denver from 'Midwest Parts Warehouse'. Achieve complete pre-fulfillment compliance verification for all kit components, successful order creation and shipment execution, and audit confirmation of fulfillment success. The audit must show that the 'Articulated Robotic Arm' compliance check is 'FAIL' and the 'Lithium-Ion Battery Pack' compliance check is 'FAIL'. Report the tracking number.",
        "actions": [
            {
                "name": "GetKitComponents",
                "arguments": {
                    "kit_sku": "KIT-ROBO-S1"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Lithium-Ion Battery Pack"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Midwest Parts Warehouse"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 1
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "KIT_FULFILLMENT_AUDIT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "STOCK_VERIFIED_AND_SHIPPED",
                    "outcome_details": {
                        "robotic_arm_compliance_check": "FAIL",
                        "battery_compliance_check": "FAIL"
                    }
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_45",
        "instruction": "As a returns inspector, manage a return involving partial damage for 100 'Ceramic Floor Tile' from order 'SO-2024-0003' by 'Gamma Construction Ltd.' at the 'Fort Lauderdale Building Materials' warehouse. Out of these, 85 tiles are intact while 15 are damaged. Complete the return process ensuring full customer credit, appropriately separate sellable inventory from the damaged stock, and meticulously document the outcomes of the split-disposition process. Log an event in the audit trail tagged 'RETURN_INSPECTION_AUDIT' with the outcome code 'DISPOSITION_COMPLETED_SUCCESSFULLY'. State the updated quantity_damaged for this product at the Fort Lauderdale warehouse.'Ceramic Floor Tile' from 'Gamma Construction Ltd.' order 'SO-2024-0003' at 'Fort Lauderdale Building Materials' warehouse, where 85 tiles are perfect and 15 are broken. Achieve complete return processing with full customer credit, proper inventory disposition separating sellable from damaged stock, and documentation of split-disposition outcomes. Log an audit trail with the exact audit event 'RETURN_INSPECTION_AUDIT' and outcome code 'DISPOSITION_COMPLETED_SUCCESSFULLY'. Report the new quantity_damaged for this product at Fort Lauderdale warehouse.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0003",
                    "line_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ],
                    "reason": "PARTIAL_DAMAGE_RETURN"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0003",
                    "customer_id": "CUST-2003",
                    "returned_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ]
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": -85
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": 15
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "RETURN_INSPECTION_AUDIT",
                    "subject_id": "RMA-1001",
                    "outcome_code": "DISPOSITION_COMPLETED_SUCCESSFULLY",
                    "outcome_details": {
                        "restocked_qty": 85,
                        "damaged_qty": 15
                    }
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                }
            }
        ],
        "outputs": [
                "180"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_46",
        "instruction": "As a carrier relations manager, handle the performance shortfall of ocean carrier 'NorthStar Shipping', which is below the company's acceptable standards. Ensure full risk mitigation by reallocating all active 'Shipped' orders to the top-performing alternate ocean carriers and imposing suspension on the carrier to prevent future allocations. Report the total count of orders that have been reassigned.'NorthStar Shipping' which has fallen below acceptable company standards. Achieve complete risk mitigation by reassigning all active 'Shipped' orders to best-performing alternative ocean carriers and implementing carrier suspension to prevent future assignments. Report the total number of orders reassigned.",
        "actions": [
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "NorthStar Shipping"
                },
            },
            {
                "name": "FindOrdersByCarrier",
                "arguments": {
                    "carrier_name": "NorthStar Shipping",
                    "status": "Shipped"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Sea"
                },
            },
            {
                "name": "ReassignOrderCarrier",
                "arguments": {
                    "order_id": "ORD-0006",
                    "new_carrier_scac": "ALFS"
                },
            },
            {
                "name": "UpdateCarrierStatus",
                "arguments": {
                    "carrier_name": "NorthStar Shipping",
                    "status": "Suspended"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "CARRIER_SUSPENSION",
                    "subject_id": "NSTS",
                    "outcome_code": "ORDERS_REASSIGNED",
                    "outcome_details": {
                        "reassigned_order_count": 1,
                        "new_carrier": "ALFS"
                    }
                }
            }
        ],
        "outputs": [
                "1"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_47",
        "instruction": "As a logistics planner, coordinate a complex multi-modal international shipment of 700 'Ceramic Brake Pad Sets' for 'Iota Automotive NAC' from 'Midwest Parts Warehouse' to Lyon, R\u00e9publique fran\u00e7aise. This shipment holds a 'High' priority status and needs domestic rail and international ocean transit segments. Select the most suitable carriers for both rail and ocean parts as per company policies, set up comprehensive planning documentation with a 'MULTI_LEG_PLAN_CREATED' audit event, and start the initial transportation leg. Report the tracking number assigned to the rail segment.'Ceramic Brake Pad Sets' for 'Iota Automotive NAC' from 'Midwest Parts Warehouse' to Lyon, R\u00e9publique fran\u00e7aise. This shipment has 'High' priority and requires domestic rail and international ocean transport legs. Achieve optimal carrier selection for both rail and ocean segments based on company policy, establish comprehensive planning documentation with 'MULTI_LEG_PLAN_CREATED' audit event, and initiate first-leg transportation. Report the tracking number for the rail segment.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Brake Pad Set"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Iota Automotive NAC",
                    "destination_city": "Lyon",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 700
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Rail"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Sea"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Midwest Parts Warehouse"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "MULTI_LEG_PLAN_CREATED",
                    "subject_id": "ORD-0017",
                    "outcome_code": "CARRIERS_SELECTED",
                    "outcome_details": {
                        "rail_carrier": "ALFS",
                        "sea_carrier": "ALFS"
                    }
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "ALFS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_48",
        "instruction": "Working as a returns specialist, oversee the safe return process of 20 'Smartphone Model X' units from 'Beta Retail GmbH' order 'SO-2024-0002' that were damaged during transit, ensuring compliance with hazardous materials regulations. Fully resolve the return with reason code 'DAMAGED_IN_TRANSIT', issue customer credit, manage a compliant international return shipment through 'Express World Delivery', and document hazmat compliance via 'HAZMAT_RETURN_AUDIT' with an outcome of 'CARRIER_COMPLIANT'. Provide the RMA ID once completed.'Smartphone Model X' units from 'Beta Retail GmbH' order 'SO-2024-0002' damaged in transit, ensuring hazardous materials compliance. Achieve complete return resolution with reason code 'DAMAGED_IN_TRANSIT', customer credit, compliant international return shipment via 'Express World Delivery', and hazmat compliance documentation through 'HAZMAT_RETURN_AUDIT' with 'CARRIER_COMPLIANT' outcome. Report the RMA ID.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0002"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Smartphone Model X"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Express World Delivery"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0002",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 20
                        }
                    ],
                    "reason": "DAMAGED_IN_TRANSIT"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0002",
                    "customer_id": "CUST-2002",
                    "returned_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 20
                        }
                    ]
                },
            },
            {
                "name": "CreateInboundReturnShipment",
                "arguments": {
                    "rma_id": "RMA-1001",
                    "from_customer_id": "CUST-2002",
                    "to_warehouse_id": "WH-02",
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "HAZMAT_RETURN_AUDIT",
                    "subject_id": "RMA-1001",
                    "outcome_code": "CARRIER_COMPLIANT"
                }
            }
        ],
        "outputs": [
                "RMA-1001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_49",
        "instruction": "As a returns inspector, finalize the processing of 100 'Ceramic Floor Tile' units returned from order 'SO-2024-0003' at the 'Fort Lauderdale Building Materials' warehouse, identifying 85 tiles in perfect condition and 15 as damaged. Ensure complete resolution of the return, including the authorization of full customer credit, correct inventory actions for both intact and damaged goods, and full event documentation. Report the updated quantity_damaged for this product at the Fort Lauderdale warehouse.'Ceramic Floor Tile' returned from order 'SO-2024-0003' at 'Fort Lauderdale Building Materials' warehouse, with 85 tiles in perfect condition and 15 broken. Achieve comprehensive return resolution including full customer credit authorization, appropriate inventory disposition for both good and damaged stock, and complete event documentation. Report the new quantity_damaged for this product at Fort Lauderdale warehouse.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0003",
                    "line_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ],
                    "reason": "PARTIAL_DAMAGE_RETURN"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0003",
                    "customer_id": "CUST-2003",
                    "returned_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ]
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": -85
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": 15
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PARTIAL_DAMAGE_RETURN",
                    "subject_id": "RMA-1001",
                    "outcome_code": "SPLIT_DISPOSITION_COMPLETE"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12"
                }
            }
        ],
        "outputs": [
                "180"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_50",
        "instruction": "In the role of a Logistics Manager, manage a 'Critical' priority order for 2 'Basic Robotic Starter Kits' requested by 'Alpha Electronics LLC' for delivery to San Jose, United States. This kit includes HAZMAT components like Lithium-Ion Battery Packs. 'Midwest Parts Warehouse' (WH-03) is the fulfillment warehouse. Your aim is to ensure the order's compliant fulfillment. The final state must confirm: 1. Identification of individual kit components. 2. Creation of the order. 3. Shipment of the order using the optimal 'Air' carrier, maintaining HAZMAT compliance. 4. Record a 'HAZMAT_KIT_FULFILLMENT_AUDIT' event with an outcome code of 'HAZMAT_ORDER_SHIPPED_COMPLIANT', detailing total value, total weight, and carrier SCAC. Lastly, provide the final tracking number.'Critical' priority order for 2 'Basic Robotic Starter Kits' has been placed by 'Alpha Electronics LLC' for delivery to San Jose, United States. This kit contains HAZMAT components (Lithium-Ion Battery Packs). The fulfillment warehouse is 'Midwest Parts Warehouse' (WH-03). Your objective is to ensure this order is fulfilled compliantly. The final state must show: 1. The individual components of the kit are identified. 2. The order is created. 3. The order is shipped using the best available 'Air' carrier, ensuring HAZMAT compliance. 4. A 'HAZMAT_KIT_FULFILLMENT_AUDIT' event is logged with outcome code 'HAZMAT_ORDER_SHIPPED_COMPLIANT', including the total value, total weight, and carrier SCAC in the outcome details. Finally, report the final tracking number.",
        "actions": [
            {
                "name": "GetKitComponents",
                "arguments": {
                    "kit_name": "Basic Robotic Starter Kit"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Lithium-Ion Battery Pack"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 2
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 4
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "HAZMAT_KIT_FULFILLMENT_AUDIT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "HAZMAT_ORDER_SHIPPED_COMPLIANT",
                    "outcome_details": {
                        "total_value_usd": 50359.96,
                        "total_weight_kg": 502.8,
                        "carrier_scac": "GPLS"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_51",
        "instruction": "As a risk manager, handle the assessment and resolution of potential performance risks for order 'ORD-0006', which was shipped to 'Zeta Tech Solutions' via 'NorthStar Shipping'. Determine whether the carrier's performance aligns with company standards (OTD \u2265 95%) and coordinate risk mitigation by potentially reassigning to the best-performing 'Sea' carrier if necessary, ensuring thorough audit documentation and confirmation of successful changes. The audit log must contain the exact reason code 'CARRIER_OTD_BELOW_THRESHOLD' for any reassignment. Report the final performance rating of the assigned carrier.'ORD-0006' shipped to 'Zeta Tech Solutions' via 'NorthStar Shipping'. Determine if carrier performance meets company standards (OTD \u2265 95%) and achieve risk mitigation through carrier reassignment to best-performing 'Sea' carrier if needed, with comprehensive audit documentation and verification of successful changes. The audit log must include the exact reason code 'CARRIER_OTD_BELOW_THRESHOLD' for reassignment. Report the performance rating of the final assigned carrier.",
        "actions": [
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "NorthStar Shipping"
                },
            },
            {
                "name": "FindOrdersByCarrier",
                "arguments": {
                    "carrier_name": "NorthStar Shipping",
                    "status": "Shipped"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Sea"
                },
            },
            {
                "name": "ReassignOrderCarrier",
                "arguments": {
                    "order_id": "ORD-0006",
                    "new_carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Alpine Freight Solutions"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PROACTIVE_CARRIER_REASSIGNMENT",
                    "subject_id": "ORD-0006",
                    "outcome_code": "SUCCESS_AND_VERIFIED",
                    "outcome_details": {
                        "original_carrier": "NSTS",
                        "new_carrier": "ALFS",
                        "reason": "CARRIER_OTD_BELOW_THRESHOLD"
                    }
                }
            }
        ],
        "outputs": [
                "4.8"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_52",
        "instruction": "In your role as a returns auditor, determine the overall financial impact of processing 100 'Ceramic Floor Tile' returns from order 'SO-2024-0003', where 85 tiles can be resold and 15 are damaged. Ensure comprehensive financial accounting that includes full customer credit processing, correct inventory disposition, precise calculation of inventory loss due to damaged goods, and detailed audit documentation. Provide a report on the computed inventory loss.'Ceramic Floor Tile' returned from order 'SO-2024-0003', where 85 tiles are sellable and 15 are damaged. Achieve comprehensive financial accounting including full customer credit processing, proper inventory disposition, accurate inventory loss calculation for damaged goods, and detailed audit documentation. Report the calculated inventory loss.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0003",
                    "customer_id": "CUST-2003",
                    "returned_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ]
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": -85
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": 15
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PARTIAL_DAMAGE_RETURN",
                    "subject_id": "ORD-0003",
                    "outcome_code": "SPLIT_DISPOSITION_COMPLETE",
                    "outcome_details": {
                        "restocked_qty": 85,
                        "scrapped_qty": 15,
                        "inventory_loss": 52.5
                    }
                }
            }
        ],
        "outputs": [
                "52.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_53",
        "instruction": "Being a quality manager, tackle the critical stock issues related to expired 'Organic Arabica Coffee Beans' (EAC 'LOT202405C') stored at 'Gulf Coast Food Storage' influencing the pending order 'ORD-0012'. Implement complete incident resolution, including order cancellation tagged with 'Cancelled - Expired Stock' status, ensuring the safe disposal of expired inventory through damage marking, quantifying financial losses, and documenting the incident using the 'EXPIRING_STOCK_INCIDENT' event code. Provide a report on the entire financial loss calculated.'Organic Arabica Coffee Beans' (EAC 'LOT202405C') at 'Gulf Coast Food Storage' that affects pending order 'ORD-0012'. Achieve complete incident resolution including order cancellation with 'Cancelled - Expired Stock' status, safe disposal of expired inventory through damage marking, financial loss quantification, and incident documentation with 'EXPIRING_STOCK_INCIDENT' event code. Report the total calculated financial loss.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0012"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Organic Arabica Coffee Beans"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Gulf Coast Food Storage"
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
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0012",
                    "new_status": "Cancelled - Expired Stock"
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0003",
                    "damaged_quantity": 5000
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "EXPIRING_STOCK_INCIDENT",
                    "subject_id": "FOOD-COFF-C3",
                    "outcome_code": "INVENTORY_SCRAPPED_ORDERS_CANCELLED",
                    "outcome_details": {
                        "cancelled_order_count": 1,
                        "total_financial_loss": 110000.0
                    }
                }
            }
        ],
        "outputs": [
                "110000.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_54",
        "instruction": "Functioning as a quality manager, avert the shipment of potentially expired 'Organic Arabica Coffee Beans' for a new urgent order from 'Theta Foods SA', requiring a 100kg delivery to S\u00e3o Paulo from 'Gulf Coast Food Storage'. If the stock is found expired, enforce full safety compliance by canceling the order with the specified status 'CANCELLED_EXPIRED_STOCK', marking the expired stock for disposal, and recording the crucial incident with the 'CRITICAL_STOCK_ISSUE' event type and 'ORDER_CANCELLED_DUE_TO_EXPIRED_STOCK' result. Report the Order ID that was canceled.'Organic Arabica Coffee Beans' for a new high-priority order from 'Theta Foods SA' requesting 100kg delivery to S\u00e3o Paulo from 'Gulf Coast Food Storage'. If stock is expired, achieve complete safety compliance by canceling the customer order with the exact status 'CANCELLED_EXPIRED_STOCK', marking expired inventory for disposal, and documenting the critical incident with 'CRITICAL_STOCK_ISSUE' event type and 'ORDER_CANCELLED_DUE_TO_EXPIRED_STOCK' outcome. Report the Order ID that was cancelled.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Organic Arabica Coffee Beans"
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
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Theta Foods SA",
                    "destination_city": "São Paulo",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "FOOD-COFF-C3",
                            "quantity": 100
                        }
                    ]
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "CANCELLED_EXPIRED_STOCK"
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0003",
                    "damaged_quantity": 5000
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "CRITICAL_STOCK_ISSUE",
                    "subject_id": "FOOD-COFF-C3",
                    "outcome_code": "ORDER_CANCELLED_DUE_TO_EXPIRED_STOCK"
                }
            }
        ],
        "outputs": [
                "ORD-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_55",
        "instruction": "As a kitting specialist, manage the compliance failure for a critical 'Basic Robotic Starter Kit' order from 'Gamma Construction Ltd.' shipping to Denver from 'Midwest Parts Warehouse'. Discover that the kit includes HAZMAT components that require certified warehouse capabilities currently unavailable at the location. Resolve compliance by placing the order on hold with 'On Hold - Compliance Failure' status and noting the violation with 'KIT_FULFILLMENT_COMPLIANCE_FAIL' event and 'INVALID_HAZMAT_WAREHOUSE' outcome. Report the SKU of the non-compliant component.'Basic Robotic Starter Kit' order from 'Gamma Construction Ltd.' shipping to Denver from 'Midwest Parts Warehouse'. Upon identifying that the kit contains HAZMAT components requiring certified warehouse capabilities not available at the current location, achieve compliance resolution by placing the order on hold with 'On Hold - Compliance Failure' status and documenting the violation with 'KIT_FULFILLMENT_COMPLIANCE_FAIL' event and 'INVALID_HAZMAT_WAREHOUSE' outcome. Report the SKU of the non-compliant component.",
        "actions": [
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "KIT-ROBO-S1",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "GetKitComponents",
                "arguments": {
                    "kit_sku": "KIT-ROBO-S1"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Lithium-Ion Battery Pack"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Midwest Parts Warehouse"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "On Hold - Compliance Failure"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "KIT_FULFILLMENT_COMPLIANCE_FAIL",
                    "subject_id": "ORD-0017",
                    "outcome_code": "INVALID_HAZMAT_WAREHOUSE",
                    "outcome_details": {
                        "non_compliant_sku": "TECH-BATT-Q17",
                        "warehouse_id": "WH-03"
                    }
                }
            }
        ],
        "outputs": [
                "TECH-BATT-Q17"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_56",
        "instruction": "You are an auditor. Handle the comprehensive audit validation concerning multi-warehouse order 'ORD-0003' executed for 'Gamma Construction Ltd.' including 100 'Ceramic Floor Tiles' from 'Fort Lauderdale Building Materials' and 10 'Industrial Paper Rolls' from 'Detroit Packaging Supplies'. Ensure complete verification of logistics that covers full inventory cost calculation, cross-docking operations capability validation in warehouses, performance assessment of 'SwiftDelivery', and consolidated audit documentation using 'MULTI_WAREHOUSE_SHIPMENT_AUDIT' and 'AUDIT_COMPLETE' codes. Provide the average rating of the carrier.'ORD-0003' fulfilled for 'Gamma Construction Ltd.' with 100 'Ceramic Floor Tiles' from 'Fort Lauderdale Building Materials' and 10 'Industrial Paper Rolls' from 'Detroit Packaging Supplies'. Achieve complete logistics verification including total inventory cost calculation, warehouse capability validation for cross-docking operations, carrier performance assessment for 'SwiftDelivery', and consolidated audit documentation with 'MULTI_WAREHOUSE_SHIPMENT_AUDIT' and 'AUDIT_COMPLETE' codes. Report the carrier's average rating.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Industrial Paper Roll"
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
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Detroit Packaging Supplies"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "SwiftDelivery"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Fort Lauderdale Building Materials"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "MULTI_WAREHOUSE_SHIPMENT_AUDIT",
                    "subject_id": "ORD-0003",
                    "outcome_code": "AUDIT_COMPLETE",
                    "outcome_details": {
                        "total_inventory_cost": 2850.0,
                        "wh_capability_check": {
                            "WH-12": "PASS",
                            "WH-08": "FAIL"
                        }
                    }
                }
            }
        ],
        "outputs": [
                "4.8"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_57",
        "instruction": "You are a specialist. Facilitate a quality-related financial return for 'Alpha Electronics LLC' involving 50 faulty '8-bit Microcontroller' units from order 'SO-2024-0001'. Ensure complete resolution of the return process including creation of RMA with 'DEFECTIVE_RETURN' reason code, issuance of customer credit, adjustment of inventory marking returned units as damaged at 'West Coast Distribution Hub', and comprehensive documentation of the transaction. State the credit memo ID.'Alpha Electronics LLC' returning 50 defective '8-bit Microcontroller' units from order 'SO-2024-0001'. Achieve complete return resolution including RMA creation with 'DEFECTIVE_RETURN' reason code, customer credit issuance, inventory adjustment marking returned units as damaged at 'West Coast Distribution Hub', and comprehensive transaction documentation. Report the credit memo ID.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0001",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ],
                    "reason": "DEFECTIVE_RETURN"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0001",
                    "customer_id": "CUST-2001",
                    "returned_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ]
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0001",
                    "damaged_quantity": 50
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "DEFECTIVE_RETURN_PROCESSED",
                    "subject_id": "RMA-1001",
                    "outcome_code": "INVENTORY_SCRAPPED_AND_CREDITED"
                }
            }
        ],
        "outputs": [
                "CM-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_58",
        "instruction": "You are an auditor. Conduct a data integrity audit on the sales order 'SO-2024-0003'. Your aim is to confirm that the warehouse and carrier specified in the order record align with their master data files. Undertake the following: 1) Access the order details. 2) Obtain the master data for the origin warehouse ('Fort Lauderdale Building Materials') and the carrier ('SwiftDelivery'). 3) Record a consolidated audit of your findings using the event code 'DATA_INTEGRITY_AUDIT' and outcome code 'VALIDATION_PASS'. Lastly, provide the carrier's average rating.'SO-2024-0003'. Your objective is to verify that the warehouse and carrier listed on the order record are consistent with their master data files. You must: 1) Retrieve the order details. 2) Retrieve the master data for the origin warehouse ('Fort Lauderdale Building Materials') and the carrier ('SwiftDelivery'). 3) Log a consolidated audit of your findings using the event code 'DATA_INTEGRITY_AUDIT' and outcome code 'VALIDATION_PASS'. Finally, report the average rating of the carrier.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Fort Lauderdale Building Materials"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "SwiftDelivery"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "DATA_INTEGRITY_AUDIT",
                    "subject_id": "ORD-0003",
                    "outcome_code": "VALIDATION_PASS",
                    "outcome_details": {
                        "customer": "CUST-2003",
                        "carrier": "SWDL",
                        "warehouse": "WH-12"
                    }
                }
            }
        ],
        "outputs": [
                "4.8"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_59",
        "instruction": "You are a returns specialist. Navigate carrier unavailability to manage the return of 50 '8-bit Microcontrollers' for 'Alpha Electronics LLC' from order 'SO-2024-0001' when standard return carrier 'Pacific Ocean Lines' is not available. Resolve the return process effectively despite carrier restrictions by opting for the best substitute 'Parcel' carrier based on the highest average rating policy, establishing return authorization with the precise reason code 'UNAVAILABLE_CARRIER_ISSUE', and arranging inbound shipment with the new carrier, alongside issuing customer credit. Maintain an audit trail with the specific event 'RETURN_CARRIER_EXCEPTION_AUDIT' and outcome code 'ALTERNATIVE_CARRIER_ASSIGNED'. List the SCAC code of the chosen carrier.'8-bit Microcontrollers' for 'Alpha Electronics LLC' from order 'SO-2024-0001' when standard return carrier 'Pacific Ocean Lines' is inactive. Achieve complete return resolution despite carrier constraints by selecting best alternative 'Parcel' carrier based on highest average rating policy, creating return authorization with the exact reason code 'UNAVAILABLE_CARRIER_ISSUE', and inbound shipment with new carrier, and issuing customer credit. Log an audit trail with the exact event 'RETURN_CARRIER_EXCEPTION_AUDIT' and outcome code 'ALTERNATIVE_CARRIER_ASSIGNED'. Report the selected carrier's SCAC code.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0001",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ],
                    "reason": "UNAVAILABLE_CARRIER_ISSUE"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Pacific Ocean Lines"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Parcel"
                },
            },
            {
                "name": "CreateInboundReturnShipment",
                "arguments": {
                    "rma_id": "RMA-1001",
                    "from_customer_id": "CUST-2001",
                    "to_warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0001",
                    "customer_id": "CUST-2001",
                    "returned_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ]
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "RETURN_CARRIER_EXCEPTION_AUDIT",
                    "subject_id": "RMA-1001",
                    "outcome_code": "ALTERNATIVE_CARRIER_ASSIGNED"
                }
            }
        ],
        "outputs": [
                "GPLS"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_60",
        "instruction": "You are a carrier auditor. 'NorthStar Shipping' performance has dropped below an acceptable level. Initially, commence a complete suspension: locate all their 'Shipped' orders, reassign each to the best alternative 'Sea' carrier, and subsequently update NorthStar Shipping's status to 'Suspended'. Following this, immediately perform an audit on this action. You need to acquire the updated order ('ORD-0006') and the modified master record for 'NorthStar Shipping' to verify correct implementation of changes. After confirmation, document the successful audit and indicate the new status of NorthStar Shipping.'NorthStar Shipping' has fallen below the acceptable threshold. Your first objective is to execute a full suspension: find all their 'Shipped' orders, reassign each to the best alternative 'Sea' carrier, and then update NorthStar Shipping's status to 'Suspended'. Your second objective is to immediately audit this action. You must retrieve the updated order ('ORD-0006') and the updated master record for 'NorthStar Shipping' to confirm the changes were applied correctly. After verifying, log the successful audit and report the new status of NorthStar Shipping.",
        "actions": [
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "NorthStar Shipping"
                },
            },
            {
                "name": "FindOrdersByCarrier",
                "arguments": {
                    "carrier_name": "NorthStar Shipping",
                    "status": "Shipped"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Sea"
                },
            },
            {
                "name": "ReassignOrderCarrier",
                "arguments": {
                    "order_id": "ORD-0006",
                    "new_carrier_scac": "ALFS"
                },
            },
            {
                "name": "UpdateCarrierStatus",
                "arguments": {
                    "carrier_name": "NorthStar Shipping",
                    "status": "Suspended"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "NorthStar Shipping"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "CARRIER_SUSPENSION_AUDIT",
                    "subject_id": "NSTS",
                    "outcome_code": "SUSPENSION_AND_REASSIGNMENT_VERIFIED"
                }
            }
        ],
        "outputs": [
                "Suspended"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_61",
        "instruction": "As a kitting specialist, your task is to manage a 'High' priority order for a 'Super Starter Kit' (comprising one 'Teak Wood Dining Chair' and ten 'Organic Cotton T-Shirts') for 'Epsilon Fashion Co.' in Toronto. The components reside in different warehouses. Your aim is to complete the order by shipping from each location. The final requirements are: 1. An outbound order for the chair is generated and dispatched from its warehouse (WH-14). 2. A separate outbound order for the t-shirts is created and dispatched from its warehouse (WH-04). 3. Ensure that both shipments utilize the most efficient 'Truck' carrier. Lastly, provide both tracking numbers.'High' priority order for a 'Super Starter Kit' (one 'Teak Wood Dining Chair' and ten 'Organic Cotton T-Shirts') is placed for 'Epsilon Fashion Co.' in Toronto. The components are in separate warehouses. Your objective is to fulfill the order by shipping from each location. The final state must show: 1. An outbound order for the chair is created and shipped from its warehouse (WH-14). 2. A separate outbound order for the t-shirts is created and shipped from its warehouse (WH-04). 3. Both shipments must use the best-performing 'Truck' carrier. Finally, report both tracking numbers.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Teak Wood Dining Chair"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Organic Cotton T-Shirt"
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "FURN-CHAIR-M13",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Truck"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-04",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0018"
                }
            }
        ],
        "outputs": [
                "GPLS-0017",
                "GPLS-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_62",
        "instruction": "As a logistics corrections specialist, address the fulfillment error for 'Gamma Construction Ltd.' concerning order 'SO-2024-0003', where 10 'Industrial Paper Roll' were mistakenly sent instead of 100 'Ceramic Floor Tile'. Implement a full correction of the mistake, including processing returns with the 'INCORRECT_ITEM_SHIPPED' reason code, dispatching a high-priority replacement order, quantifying the inventory cost of the error, and completing an audit with the 'SHIPMENT_ERROR_CORRECTION' event and 'RETURN_AND_REPLACE_COMPLETE' outcome. Present the calculated inventory cost of the error.'Gamma Construction Ltd.' order 'SO-2024-0003' where 10 'Industrial Paper Roll' were shipped instead of 100 'Ceramic Floor Tile'. Achieve complete error correction including return processing with 'INCORRECT_ITEM_SHIPPED' reason code, critical priority replacement order dispatch, inventory cost quantification of the error, and comprehensive audit documentation with 'SHIPMENT_ERROR_CORRECTION' event and 'RETURN_AND_REPLACE_COMPLETE' outcome. Report the calculated inventory cost of the error.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Industrial Paper Roll"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0003",
                    "line_items": [
                        {
                            "sku": "MANU-PAPR-F6",
                            "quantity": 10
                        }
                    ],
                    "reason": "INCORRECT_ITEM_SHIPPED"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0003",
                    "customer_id": "CUST-2003",
                    "returned_items": [
                        {
                            "sku": "MANU-PAPR-F6",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "MANU-PAPR-F6"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0006",
                    "damaged_quantity": -10
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "BLDG-TILE-J10"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-12",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "SHIPMENT_ERROR_CORRECTION",
                    "subject_id": "ORD-0003",
                    "outcome_code": "RETURN_AND_REPLACE_COMPLETE",
                    "outcome_details": {
                        "replacement_order_id": "ORD-0017",
                        "error_inventory_cost": 2500.0
                    }
                }
            }
        ],
        "outputs": [
                "2500.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_63",
        "instruction": "As a priority fulfillment manager, you need to solve an inventory allocation issue where a critical order for 10,000 '8-bit Microcontrollers' destined for 'Zeta Tech Solutions', from 'West Coast Distribution Hub' to Yokohama, can't proceed due to stock being reserved for low-priority order 'ORD-0001'. Implement a resolution prioritizing high-priority needs by reallocating stock to the critical order, guaranteeing successful shipment, and documenting the solution including details of the orders affected. Deliver the tracking number for the critical shipment upon completion.'8-bit Microcontrollers' for 'Zeta Tech Solutions' shipping from 'West Coast Distribution Hub' to Yokohama cannot be fulfilled due to stock being allocated to low-priority order 'ORD-0001'. Achieve priority-based resolution by reallocating inventory to the critical order, ensuring successful shipment execution, and documenting the resolution including affected order details. Report the tracking number for the critical shipment.",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "Cancelled"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Zeta Tech Solutions",
                    "destination_city": "Yokohama",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 10000
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "DEADLOCK_RESOLUTION",
                    "subject_id": "ORD-0017",
                    "outcome_code": "FULFILLED_BY_CANCELLING_ORD-0001",
                    "outcome_details": {
                        "cancelled_order_id": "ORD-0001",
                        "new_order_id": "ORD-0017"
                    }
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_64",
        "instruction": "As a fulfillment auditor, assess the 'Midwest Parts Warehouse' procedure by executing and auditing a new 'High' priority order for 'Gamma Construction Ltd.' in Denver using 'Truck' transport. The order should include 5 'Articulated Robotic Arms' and 20 'Lithium-Ion Battery Packs'. After order creation and dispatch, carry out a comprehensive audit: 1) Procure final order details. 2) Access inventory records to confirm appropriate stock reduction. 3) Record your observations using the event code 'FULFILLMENT_PROCESS_AUDIT' and outcome code 'FULFILLMENT_AUDIT_PASS'. Conclude by sharing the shipment's tracking number.'Midwest Parts Warehouse' process. Your objective is to execute and audit a new 'High' priority order for 'Gamma Construction Ltd.' in Denver via 'Truck' transport. The order must contain 5 'Articulated Robotic Arms' and 20 'Lithium-Ion Battery Packs'. After creating and shipping the order, you must perform a full audit: 1) Retrieve the final order details. 2) Retrieve inventory records to verify stock was correctly decremented. 3) Log your findings with the event code 'FULFILLMENT_PROCESS_AUDIT' and outcome code 'FULFILLMENT_AUDIT_PASS'. Finally, report the tracking number for the shipment.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Lithium-Ion Battery Pack"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Midwest Parts Warehouse"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 5
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 20
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Truck"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "FULFILLMENT_PROCESS_AUDIT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "FULFILLMENT_AUDIT_PASS",
                    "outcome_details": {
                        "carrier_policy_check": "PASS",
                        "inventory_deduction_check": "PASS"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_65",
        "instruction": "As a quality auditor at the 'Midwest Parts Warehouse', while preparing order 'ORD-0014' for 10 'Articulated Robotic Arms', you identify 2 units as irreparably damaged. Your task is to address this quality issue before shipping. Follow these steps: 1) Amend the inventory record to account for the 2 damaged items. 2) Cancel the initial order with the status 'Cancelled - Damaged Stock'. 3) Determine the inventory loss due to the damaged goods. 4) Record a thorough audit using the event code 'PRE_SHIPMENT_QUALITY_FAIL' and outcome code 'ORDER_CANCELLED'. Conclude by reporting the calculated inventory loss.'Midwest Parts Warehouse'. While preparing order 'ORD-0014' for 10 'Articulated Robotic Arms', your inspection reveals that 2 units are damaged beyond repair. Your objective is to handle this quality failure before shipment. You must: 1) Update the inventory record to reflect the 2 newly discovered damaged units. 2) Cancel the original order using the status 'Cancelled - Damaged Stock'. 3) Calculate the inventory loss from the damaged goods. 4) Log a detailed audit with the event code 'PRE_SHIPMENT_QUALITY_FAIL' and outcome code 'ORDER_CANCELLED'. Finally, report the calculated inventory loss.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0014"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Midwest Parts Warehouse"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0014",
                    "damaged_quantity": 2
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0014",
                    "new_status": "Cancelled - Damaged Stock"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PRE_SHIPMENT_QUALITY_FAIL",
                    "subject_id": "ORD-0014",
                    "outcome_code": "ORDER_CANCELLED",
                    "outcome_details": {
                        "scrapped_qty": 2,
                        "inventory_loss": 24000.0
                    }
                }
            }
        ],
        "outputs": [
                "24000.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_66",
        "instruction": "As a kitting auditor, handle and confirm a complex multi-component kit fulfillment for 'Epsilon Fashion Co.' requesting a 'Super Starter Kit' (one 'Teak Wood Dining Chair', ten 'Organic Cotton T-Shirts') destined for Toronto via truck transport from varied source warehouses. This is designated as a 'High' priority fulfillment. Accomplish thorough fulfillment execution with separate component shipments, complete a financial audit including revenue calculation ($25.00/unit for t-shirts per policy), cost analysis, gross profit determination, and audit documentation with 'MULTI_SHIP_KIT_AUDIT' event. Report the computed gross profit.'Epsilon Fashion Co.' requesting a 'Super Starter Kit' (one 'Teak Wood Dining Chair', ten 'Organic Cotton T-Shirts') shipping to Toronto via truck transport from separate source warehouses. This is a 'High' priority fulfillment. Achieve comprehensive fulfillment execution with separate component shipments, complete financial audit including revenue calculation ($25.00/unit for t-shirts per policy), cost analysis, gross profit determination, and audit documentation with 'MULTI_SHIP_KIT_AUDIT' event. Report the calculated gross profit.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Teak Wood Dining Chair"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Organic Cotton T-Shirt"
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "FURN-CHAIR-M13",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Truck"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-04",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "MULTI_SHIP_KIT_AUDIT",
                    "subject_id": "ORD-0017;ORD-0018",
                    "outcome_code": "PROFIT_CALCULATED",
                    "outcome_details": {
                        "profit": 44.99
                    }
                }
            }
        ],
        "outputs": [
                "44.99"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_67",
        "instruction": "As a returns auditor, assess the total financial impact of processing 100 'Ceramic Floor Tile' returned from order 'SO-2024-0003', noting that 85 tiles are sellable and 15 are damaged. Achieve comprehensive financial reconciliation including the issuance of full customer credit, proper inventory disposition distinguishing good from damaged stock, accurate calculation of inventory loss for damaged goods, and detailed audit documentation with the precise audit event 'RETURN_AUDIT_SPLIT_DISPOSITION' and outcome code 'DISPOSITION_COMPLETE'. Report the calculated inventory loss.'Ceramic Floor Tile' returned from order 'SO-2024-0003', where 85 tiles are sellable and 15 are damaged. Achieve comprehensive financial reconciliation including full customer credit processing, proper inventory disposition separating good from damaged stock, accurate inventory loss calculation for damaged goods, and detailed audit documentation with the exact audit event 'RETURN_AUDIT_SPLIT_DISPOSITION' and outcome code 'DISPOSITION_COMPLETE'. Report the calculated inventory loss.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0003",
                    "customer_id": "CUST-2003",
                    "returned_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ]
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": -85
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": 15
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "RETURN_AUDIT_SPLIT_DISPOSITION",
                    "subject_id": "ORD-0003",
                    "outcome_code": "DISPOSITION_COMPLETE",
                    "outcome_details": {
                        "restocked_qty": 85,
                        "scrapped_qty": 15,
                        "inventory_loss": 52.5
                    }
                }
            }
        ],
        "outputs": [
                "52.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_68",
        "instruction": "As a specialist in financial returns, audit a return from 'Gamma Construction Ltd.' on order 'SO-2024-0003'. The return contains 100 'Ceramic Floor Tile', with 15 reported as broken. Your task is to achieve a fully reconciled state for this incident. The final state must confirm that: 1) A full credit for all 100 tiles has been issued. 2) The 85 undamaged tiles have been reintroduced to available stock. 3) The 15 broken tiles have been identified as damaged. 4) A detailed audit log with the exact audit event 'FINANCIAL_RETURN_RECONCILIATION' and the outcome code 'PARTIAL_DAMAGE_RECONCILED' has been generated, including the calculated inventory loss (cost of damaged goods). Utilize the specific reason code 'PARTIAL_DAMAGE_REPORTED'. Finally, report the computed inventory loss.'Gamma Construction Ltd.' on order 'SO-2024-0003'. The return consists of 100 'Ceramic Floor Tile', of which 15 are reported as broken. Your objective is to achieve a fully reconciled state for this incident. The final state must show that: 1) A full credit for all 100 tiles has been issued. 2) The 85 undamaged tiles have been returned to available stock. 3) The 15 broken tiles have been marked as damaged. 4) A detailed audit log with the exact audit event 'FINANCIAL_RETURN_RECONCILIATION' and the outcome code 'PARTIAL_DAMAGE_RECONCILED' has been created, including the calculated inventory loss (cost of damaged goods). The return authorization must use the exact reason code 'PARTIAL_DAMAGE_REPORTED'. Finally, you must report the calculated inventory loss.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0003",
                    "line_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ],
                    "reason": "PARTIAL_DAMAGE_REPORTED"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0003",
                    "customer_id": "CUST-2003",
                    "returned_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ]
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": -85
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": 15
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "FINANCIAL_RETURN_RECONCILIATION",
                    "subject_id": "RMA-1001",
                    "outcome_code": "PARTIAL_DAMAGE_RECONCILED",
                    "outcome_details": {
                        "credited_value": 600.0,
                        "inventory_loss": 52.5
                    }
                }
            }
        ],
        "outputs": [
                "52.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_69",
        "instruction": "As an inventory planner, coordinate a 'Critical' priority order placement for 14,500 '8-bit Microcontrollers' for 'Alpha Electronics LLC' in San Jose. A primary requirement is that the entire order is shipped from the 'West Coast Distribution Hub'. Currently, this warehouse has 12,500 units available. Your objective is to ensure that fulfillment from San Diego is accomplished as specified. The final state should demonstrate that 2,000 required units have been transferred from our 'Midwest Parts Warehouse', the customer order has been created, and the complete shipment dispatched from San Diego. Finally, provide the tracking number for the customer's shipment.'Critical' priority order has been placed for 14,500 '8-bit Microcontrollers' for 'Alpha Electronics LLC' in San Jose. A key requirement is that the entire order must be shipped from the 'West Coast Distribution Hub'. Currently, that warehouse has 12,500 units available. Your objective is to ensure the order can be fulfilled from San Diego as requested. The final state must show that the necessary 2,000 units have been transferred from our 'Midwest Parts Warehouse', the customer order has been created, and the full shipment has been dispatched from San Diego. Finally, report the tracking number for the customer's shipment.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "InitiateWarehouseTransfer",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "quantity": 2000,
                    "from_warehouse_id": "WH-03",
                    "to_warehouse_id": "WH-01"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 14500
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "CONSOLIDATION_FULFILLMENT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "TRANSFER_PREREQUISITE_MET"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_70",
        "instruction": "As a returns auditor, process a return from 'Gamma Construction Ltd.' on order 'SO-2024-0003' for 100 'Ceramic Floor Tile', noting upon inspection that 85 tiles are in perfect condition while 15 are broken. Your objective is to achieve a fully reconciled state for this case. The final state must verify that: 1) A full credit memo for all 100 tiles has been issued. 2) The 85 undamaged tiles are accounted for in the available inventory. 3) The 15 broken tiles are recorded in the damaged inventory. 4) A detailed audit log with the event code 'PARTIAL_DAMAGE_RECONCILED' and outcome code 'SPLIT_DISPOSITION_COMPLETE' has been established, including the calculated inventory loss. Lastly, you must report the calculated inventory loss.'Gamma Construction Ltd.' on order 'SO-2024-0003' for 100 'Ceramic Floor Tile' has been inspected, revealing that 85 tiles are in perfect condition while 15 are broken. Your objective is to achieve a fully reconciled state for this incident. The final state must show that: 1) A full credit memo for all 100 tiles has been issued. 2) The 85 undamaged tiles are reflected in the available inventory. 3) The 15 broken tiles are reflected in the damaged inventory. 4) A detailed audit log with the event code 'PARTIAL_DAMAGE_RECONCILED' and outcome code 'SPLIT_DISPOSITION_COMPLETE' has been created, including the calculated inventory loss. Finally, you must report the calculated inventory loss.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0003",
                    "customer_id": "CUST-2003",
                    "returned_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ]
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": -85
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": 15
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PARTIAL_DAMAGE_RECONCILED",
                    "subject_id": "ORD-0003",
                    "outcome_code": "SPLIT_DISPOSITION_COMPLETE",
                    "outcome_details": {
                        "restocked_qty": 85,
                        "scrapped_qty": 15,
                        "inventory_loss": 52.5
                    }
                }
            }
        ],
        "outputs": [
                "52.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_71",
        "instruction": "As a kitting planner, manage a 'Critical' priority order for a 'Super Kit' (consisting of one 'Teak Wood Dining Chair' and one 'Articulated Robotic Arm') placed by 'Gamma Construction Ltd.' in Denver. The components should be dispatched from their respective warehouses using 'Air' transport, as required for Critical orders. The task is to ensure this order is completed. The final outcome must confirm: 1) Each component is individually ordered and shipped from its origin warehouse. 2) An audit log with the event code 'MULTI_SHIP_KIT_FULFILLMENT' and the outcome code 'FULFILLMENT_COMPLETE' is recorded. Lastly, provide both tracking numbers.'Critical' priority order for a 'Super Kit' (one 'Teak Wood Dining Chair', one 'Articulated Robotic Arm') is placed for 'Gamma Construction Ltd.' in Denver. The components must ship from their respective warehouses via 'Air' transport, as required for Critical orders. Your objective is to fulfill this order. The final state must show: 1) A separate order is created and shipped for each component from its source warehouse. 2) An audit log with the event code 'MULTI_SHIP_KIT_FULFILLMENT' and outcome code 'FULFILLMENT_COMPLETE' is created. Finally, report both tracking numbers.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Teak Wood Dining Chair"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "FURN-CHAIR-M13",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "MULTI_SHIP_KIT_FULFILLMENT",
                    "subject_id": "ORD-0017;ORD-0018",
                    "outcome_code": "FULFILLMENT_COMPLETE"
                }
            }
        ],
        "outputs": [
                "GPLS-0017",
                "GPLS-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_72",
        "instruction": "Act as a specialist in financial returns to audit the return from 'Gamma Construction Ltd.' for order 'SO-2024-0003'. The return involves 100 'Ceramic Floor Tile' to be restocked at WH-12, and 10 'Industrial Paper Roll' to be returned to WH-08. Apply the reason code 'UNUSED_MATERIAL_RETURN'. The aim is to reach a fully reconciled status. Ensure the final state indicates that: 1) A complete credit is granted. 2) Out of the tiles, 85 units are restocked while 15 are designated as damaged. 3) All 10 paper rolls are successfully restocked. 4) An extensive audit log with the code 'MULTI_ITEM_RETURN_RECONCILED' is created, capturing the calculated inventory loss. Lastly, document the computed inventory loss.'Gamma Construction Ltd.' on order 'SO-2024-0003'. The return contains 100 'Ceramic Floor Tile' to be restocked at WH-12, and 10 'Industrial Paper Roll' to be restocked at WH-08. Use the reason code 'UNUSED_MATERIAL_RETURN'. Your objective is to achieve a fully reconciled state. The final state must show that: 1) A full credit has been issued. 2) For the tiles, 85 are restocked and 15 are marked as damaged. 3) The 10 paper rolls are restocked. 4) A detailed audit log with code 'MULTI_ITEM_RETURN_RECONCILED' is created, including the calculated inventory loss. Finally, report the calculated inventory loss.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Industrial Paper Roll"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0003",
                    "line_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        },
                        {
                            "sku": "MANU-PAPR-F6",
                            "quantity": 10
                        }
                    ],
                    "reason": "UNUSED_MATERIAL_RETURN"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0003",
                    "customer_id": "CUST-2003",
                    "returned_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        },
                        {
                            "sku": "MANU-PAPR-F6",
                            "quantity": 10
                        }
                    ]
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": -85
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": 15
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0006",
                    "damaged_quantity": -10
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "FINANCIAL_RECONCILIATION",
                    "subject_id": "RMA-1001",
                    "outcome_code": "MULTI_ITEM_RETURN_RECONCILED",
                    "outcome_details": {
                        "inventory_loss": 52.5
                    }
                }
            }
        ],
        "outputs": [
                "52.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_73",
        "instruction": "Take on the role of an inventory rebalancing specialist. A new 'Critical' priority order has been received for 'Zeta Tech Solutions' requiring 10,000 '8-bit Microcontrollers' to be sent to Yokohama from the 'West Coast Distribution Hub' (WH-01). To ensure proper fulfillment, arrange the transfer of 2,000 units of '8-bit Microcontroller' from the 'Midwest Parts Warehouse' (WH-03) to the 'West Coast Distribution Hub' (WH-01). Post-transfer, generate and dispatch the 'Critical' priority order using the most suitable 'Air' carrier. The final state must confirm: 1) Completion of the transfer. 2) Full creation and dispatch of the new 'Critical' order. 3) Logging of a 'STOCK_REBALANCE_AUDIT' event with the outcome code 'FULFILLMENT_TRANSFER_COMPLETE', outlining the quantities that were transferred and shipped. Record the tracking number for the fresh critical shipment.'Critical' priority order has arrived for 'Zeta Tech Solutions' for 10,000 '8-bit Microcontrollers' to be shipped to Yokohama from the 'West Coast Distribution Hub' (WH-01). To ensure fulfillment, you must transfer 2,000 units of '8-bit Microcontroller' from 'Midwest Parts Warehouse' (WH-03) to 'West Coast Distribution Hub' (WH-01). After the transfer, create and ship the 'Critical' priority order using the best 'Air' carrier. The final state must show: 1) The transfer is completed. 2) The new 'Critical' order is created and fully dispatched. 3) A 'STOCK_REBALANCE_AUDIT' event is logged with outcome code 'FULFILLMENT_TRANSFER_COMPLETE', detailing the quantities transferred and shipped. Report the tracking number for the new critical shipment.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03"
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
                "name": "InitiateWarehouseTransfer",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "quantity": 2000,
                    "from_warehouse_id": "WH-03",
                    "to_warehouse_id": "WH-01"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Zeta Tech Solutions",
                    "destination_city": "Yokohama",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 10000
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Global Parcel Service"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "STOCK_REBALANCE_AUDIT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "FULFILLMENT_TRANSFER_COMPLETE",
                    "outcome_details": {
                        "transferred_quantity": 2000,
                        "shipped_quantity": 10000,
                        "fulfillment_warehouse": "WH-01",
                        "carrier_scac": "GPLS"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_74",
        "instruction": "As a kitting specialist, address a 'Critical' order for a 'Super Kit' (including one 'Teak Wood Dining Chair' and one 'Articulated Robotic Arm') placed by 'Gamma Construction Ltd.' located in Denver. The components need to be sent from their distinct warehouses via 'Air' transport due to Critical priority orders. Your duty is to complete this order. The final state should illustrate: 1) The chair shipment's creation from its source warehouse in Dallas (WH-14). 2) A distinct shipment creation for the robotic arm from its source warehouse in Milwaukee (WH-03). 3) Recording of an audit log with event code 'MULTI_SHIP_KIT_FULFILLMENT'. In conclusion, provide both tracking numbers, connected by a semicolon.'Critical' order for a 'Super Kit' (one 'Teak Wood Dining Chair', one 'Articulated Robotic Arm') is placed for 'Gamma Construction Ltd.' in Denver. The components must ship from their respective warehouses via 'Air' transport, as required for Critical priority orders. Your objective is to fulfill this order. The final state must show: 1) A shipment for the chair is created from its source warehouse in Dallas (WH-14). 2) A separate shipment for the robotic arm is created from its source warehouse in Milwaukee (WH-03). 3) An audit log with the event code 'MULTI_SHIP_KIT_FULFILLMENT' is created. Finally, report both tracking numbers, joined by a semicolon.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Teak Wood Dining Chair"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
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
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "FURN-CHAIR-M13",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "MULTI_SHIP_KIT_FULFILLMENT",
                    "subject_id": "ORD-0017;ORD-0018",
                    "outcome_code": "FULFILLMENT_COMPLETE"
                }
            }
        ],
        "outputs": [
                "GPLS-0017;GPLS-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_75",
        "instruction": "Function as a corrections auditor. Order 'SO-2024-0003' for 'Gamma Construction Ltd.' was mistakenly fulfilled with the wrong item: 10 'Industrial Paper Roll' instead of the intended 100 'Ceramic Floor Tile'. Your assignment is to reach a fully rectified and reconciled condition. This entails the following: 1) A complete return of the incorrect items is processed involving a credit memo utilizing the reason code 'INCORRECT_ITEM_SHIPPED'. 2) The returned, undamaged paper rolls are restocked at their designated warehouse ('Detroit Packaging Supplies'). 3) Dispatch a new 'Critical' replacement order for the correct items. Finally, you must give the tracking number for the correct, new shipment.'SO-2024-0003' for 'Gamma Construction Ltd.' was fulfilled with the wrong item: 10 'Industrial Paper Roll' instead of 100 'Ceramic Floor Tile'. Your objective is to achieve a fully corrected and reconciled state. This requires that: 1) A full return for the incorrect items is processed with a credit memo using reason code 'INCORRECT_ITEM_SHIPPED'. 2) The returned, undamaged paper rolls are restocked at their proper warehouse ('Detroit Packaging Supplies'). 3) A new 'Critical' replacement order for the correct items is dispatched. Finally, you must report the tracking number of the correct, new shipment.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Industrial Paper Roll"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0003",
                    "line_items": [
                        {
                            "sku": "MANU-PAPR-F6",
                            "quantity": 10
                        }
                    ],
                    "reason": "INCORRECT_ITEM_SHIPPED"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0003",
                    "customer_id": "CUST-2003",
                    "returned_items": [
                        {
                            "sku": "MANU-PAPR-F6",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Detroit Packaging Supplies"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0006",
                    "damaged_quantity": -10
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "BLDG-TILE-J10"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-12",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_103",
        "instruction": "Act as a Supply Chain Compliance Auditor. Handle an immediate audit for 'Influenza Vaccine' (SKU PHRM-VACC-D4) at the 'Charlotte Cold Chain Center' (WH-06). Your tasks are: 1) Confirm its stock status, expiration date (consider today's date as 2025-07-23), and temperature storage requirements. Currently, the inventory holds a batch of 'Influenza Vaccine' expiring on '2025-01-01'. 2) Should the product be non-compliant (like expired), promptly mark all 18,000 available units of this batch as damaged in inventory. 3) File a performance issue against 'Mumbai Pharma Supplies' (SUP-1006) for 'EXPIRED_GOODS_RECEIVED' linked to purchase order 'PO-2024-0006' and the specific shipment 'SHIP-0006'. 4) Generate a new 'Critical' priority purchase order for 18,000 units of 'Influenza Vaccine' from 'Mumbai Pharma Supplies' (SUP-1006). 5) Adjust the new inbound shipment (which will be 'SHIP-0031') to 'Expedited' status with the annotation 'URGENT_REPLENISHMENT_AFTER_DISPOSAL'. 6) Record an audit event with the title 'COMPLIANCE_AUDIT_AND_REPLENISHMENT', result 'NON_COMPLIANT_STOCK_HANDLED', and specifics including 'disposed_quantity' (18000), 'new_po_number' ('PO-2025-0001'), and 'replenishment_shipment_id' ('SHIP-0031'). Provide the new Purchase Order number.'Influenza Vaccine' (SKU PHRM-VACC-D4) at the 'Charlotte Cold Chain Center' (WH-06). Your objective is to: 1) Verify its stock status, expiration date (assume current date is 2025-07-23), and temperature storage requirements. The inventory currently has a batch of 'Influenza Vaccine' with an expiration date of '2025-01-01'. 2) If the product is non-compliant (e.g., expired), immediately mark all 18,000 available units of this batch as damaged in inventory. 3) Log a performance issue against 'Mumbai Pharma Supplies' (SUP-1006) for 'EXPIRED_GOODS_RECEIVED' related to purchase order 'PO-2024-0006' and specific shipment 'SHIP-0006'. 4) Create a new 'Critical' priority purchase order for 18,000 units of 'Influenza Vaccine' from 'Mumbai Pharma Supplies' (SUP-1006). 5) Update the new inbound shipment (which will be 'SHIP-0031') to 'Expedited' status with the note 'URGENT_REPLENISHMENT_AFTER_DISPOSAL'. 6) Log an audit event with event 'COMPLIANCE_AUDIT_AND_REPLENISHMENT', outcome 'NON_COMPLIANT_STOCK_HANDLED', and details including 'disposed_quantity' (18000), 'new_po_number' ('PO-2025-0001'), and 'replenishment_shipment_id' ('SHIP-0031'). Report the new Purchase Order number.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Influenza Vaccine"
                },
            },
            {
                "name": "GetWarehouseDetails",
                "arguments": {
                    "warehouse_name": "Charlotte Cold Chain Center"
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0004",
                    "damaged_quantity": 18000
                },
            },
            {
                "name": "LogSupplierPerformanceIssue",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "issue_code": "EXPIRED_GOODS_RECEIVED",
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "line_items": [
                        {
                            "sku": "PHRM-VACC-D4",
                            "quantity": 18000
                        }
                    ],
                    "priority": "Critical"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2025-0001"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0031",
                    "new_status": "Expedited",
                    "notes": "URGENT_REPLENISHMENT_AFTER_DISPOSAL"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Influenza Vaccine"
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
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "COMPLIANCE_AUDIT_AND_REPLENISHMENT",
                    "subject_id": "PHRM-VACC-D4;WH-06",
                    "outcome_code": "NON_COMPLIANT_STOCK_HANDLED",
                    "outcome_details": {
                        "disposed_quantity": 18000,
                        "new_po_number": "PO-2025-0001",
                        "replenishment_shipment_id": "SHIP-0031"
                    }
                }
            }
        ],
        "outputs": [
                "PO-2025-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_77",
        "instruction": "As a kitting specialist, address a 'Critical' priority order for a 'Home & Auto Combo' consisting of one 'Ceramic Brake Pad Set' and four 'Teak Wood Dining Chairs' placed for 'Iota Automotive NAC' located in Lyon. The components reside in different warehouses. Your goal is to complete this order by organizing the shipment of the components from their respective warehouses via 'Air' transport. The final arrangement must show: 1) Separate orders are established and dispatched for each component from its source warehouse. 2) Both shipments are to utilize the most effective 'Air' carrier according to policy. Conclude by reporting both tracking numbers.'Critical' priority order for a 'Home & Auto Combo' (one 'Ceramic Brake Pad Set' and four 'Teak Wood Dining Chairs') is placed for 'Iota Automotive NAC' in Lyon. The components are in different warehouses. Your objective is to fulfill this order by shipping the components from their respective locations via 'Air' transport. The final state must show: 1) A separate order is created and shipped for each component from its source warehouse. 2) Both shipments use the best-performing 'Air' carrier per policy. Finally, report both tracking numbers.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Brake Pad Set"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Teak Wood Dining Chair"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Iota Automotive NAC",
                    "destination_city": "Lyon",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Iota Automotive NAC",
                    "destination_city": "Lyon",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "FURN-CHAIR-M13",
                            "quantity": 4
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0018"
                }
            }
        ],
        "outputs": [
                "GPLS-0017",
                "GPLS-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_78",
        "instruction": "Function as a Quality Assurance Lead. Address a significant fulfillment error with order SO-2024-0002 for 'Beta Retail GmbH'. The warehouse incorrectly sent 1,200 units of '8-bit Microcontroller' instead of 'Smartphone Model X'. Your goal is a complete recovery. The final documentation must display: 1. A thorough return authorization using the reason code 'INCORRECT_ITEM_SHIPPED' and a comprehensive credit memo are generated. 2. A new, 'Critical' priority replacement order for the correct quantity of 'Smartphone Model X' is arranged and shipped from the original warehouse ('WH-02'). 3. A comprehensive audit log with the event code 'FULFILLMENT_CORRECTION' and outcome code 'RECOVERY_COMPLETE' is recorded. Finally, provide the new tracking number and the ID of the distributed credit memo.'Beta Retail GmbH'. The warehouse shipped 1,200 units of '8-bit Microcontroller' instead of 'Smartphone Model X'. Your objective is a full recovery. The final state must show: 1. A complete return authorization using the reason code 'INCORRECT_ITEM_SHIPPED' and a full credit memo are issued. 2. A new, 'Critical' priority replacement order for the correct quantity of 'Smartphone Model X' is created and shipped from the original warehouse ('WH-02'). 3. A detailed audit log with the event code 'FULFILLMENT_CORRECTION' and outcome code 'RECOVERY_COMPLETE' is created. Finally, report the new tracking number and the ID of the issued credit memo.",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0002"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Smartphone Model X"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0002",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 1200
                        }
                    ],
                    "reason": "INCORRECT_ITEM_SHIPPED"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0002",
                    "customer_id": "CUST-2002",
                    "returned_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 1200
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Beta Retail GmbH",
                    "destination_city": "Munich",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 1200
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-02",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "FULFILLMENT_CORRECTION",
                    "subject_id": "ORD-0002",
                    "outcome_code": "RECOVERY_COMPLETE",
                    "outcome_details": {
                        "replacement_order_id": "ORD-0017",
                        "rma_id": "RMA-1001",
                        "credit_memo_id": "CM-0002"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017",
                "CM-0002"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_79",
        "instruction": "Operate as a Returns Manager. Handle a partial return process for Customer 'Alpha Electronics LLC' against order 'ORD-0001'. They are returning 25 units of '8-bit Microcontroller'. Your evaluation shows that 10 of these units are damaged and need to be written off, while 15 remain in excellent condition. Your task is to execute this intricate return. The final documentation must show: 1. An RMA is structured for all 25 units with the reason code 'SPLIT_RETURN_DAMAGED_OVERSTOCK'. 2. Inventory at WH-01 is modified to move 10 units to 'damaged' and return 15 to 'available' stock. 3. A credit memo is furnished solely for the 15 undamaged items. 4. A 'PARTIAL_RETURN_AUDIT' log is entered with an outcome code 'PROCESSED_WITH_SPLIT'. Lastly, deliver the RMA ID and the Credit Memo ID.'Alpha Electronics LLC' is processing a partial return against order 'ORD-0001'. They are returning 25 units of '8-bit Microcontroller'. Your inspection reveals that 10 of these units are damaged and must be written off, while 15 are in perfect condition. Your objective is to process this complex return. The final state must show: 1. An RMA is created for all 25 units using the reason code 'SPLIT_RETURN_DAMAGED_OVERSTOCK'. 2. Inventory at WH-01 is updated to move 10 units to 'damaged' and return 15 to 'available' stock. 3. A credit memo is issued for only the 15 undamaged items. 4. A 'PARTIAL_RETURN_AUDIT' log is created with outcome code 'PROCESSED_WITH_SPLIT'. Finally, report the RMA ID and the Credit Memo ID.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0001",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 25
                        }
                    ],
                    "reason": "SPLIT_RETURN_DAMAGED_OVERSTOCK"
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0001",
                    "damaged_quantity": 10
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0001",
                    "damaged_quantity": -15
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0001",
                    "customer_id": "CUST-2001",
                    "returned_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 15
                        }
                    ]
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PARTIAL_RETURN_AUDIT",
                    "subject_id": "RMA-1001",
                    "outcome_code": "PROCESSED_WITH_SPLIT",
                    "outcome_details": {
                        "original_order_id": "ORD-0001",
                        "damaged_quantity": 10,
                        "restocked_quantity": 15,
                        "credited_quantity": 15,
                        "credit_memo_id": "CM-0001"
                    }
                }
            }
        ],
        "outputs": [
                "RMA-1001",
                "CM-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_80",
        "instruction": "Perform as a Risk & Compliance Officer. An urgent alert has emerged for inbound shipment 'SHIP-0013', denoting a 'High' priority shipment of 'Industrial Solvent' from 'Helsinki Chemicals Oy'. The designated carrier, 'Nordic Marine', lacks certification for this HAZMAT class, constituting a serious compliance breach. Your task is to manage this risk. The final report must illustrate: 1. The inbound shipment 'SHIP-0013' is changed to a status of 'On Hold - Compliance Review' accompanied by the note code 'NOTE:NON_COMPLIANT_CARRIER_HLCU'. 2. Assign 'Nordic Marine' to 'Under Review'. 3. Initiate a new, 'Critical' priority purchase order for the same products. 4. Document an audit trail with the event code 'HAZMAT_COMPLIANCE_BREACH' and outcome code 'MITIGATION_INITIATED'. 5. Record a supplier performance issue with the issue code 'NON_COMPLIANT_CARRIER'. Lastly, submit the new Purchase Order ID and the audited shipment ID.'SHIP-0013', a 'High' priority shipment of 'Industrial Solvent' from 'Helsinki Chemicals Oy'. The assigned carrier, 'Nordic Marine', is not certified for this HAZMAT class. This is a major compliance breach. Your objective is to mitigate this risk. The final state must show: 1. The inbound shipment 'SHIP-0013' is updated to a status of 'On Hold - Compliance Review' with the note code 'NOTE:NON_COMPLIANT_CARRIER_HLCU'. 2. The carrier 'Nordic Marine' is set to 'Under Review'. 3. A new, 'Critical' priority purchase order is created for the same items. 4. An audit trail is logged with the event code 'HAZMAT_COMPLIANCE_BREACH' and outcome code 'MITIGATION_INITIATED'. 5. A supplier performance issue is logged using the issue code 'NON_COMPLIANT_CARRIER'. Finally, report the new Purchase Order ID and the audited shipment ID.",
        "actions": [
            {
                "name": "FindInboundShipment",
                "arguments": {
                    "supplier_name": "Helsinki Chemicals Oy",
                    "origin_city": "Helsinki"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Nordic Marine"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Industrial Solvent"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "new_status": "On Hold - Compliance Review",
                    "notes": "NOTE:NON_COMPLIANT_CARRIER_HLCU"
                },
            },
            {
                "name": "UpdateCarrierStatus",
                "arguments": {
                    "carrier_name": "Nordic Marine",
                    "status": "Under Review"
                },
            },
            {
                "name": "LogSupplierPerformanceIssue",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "issue_code": "NON_COMPLIANT_CARRIER",
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "line_items": [
                        {
                            "sku": "CHEM-SOLV-K11",
                            "quantity": 400
                        }
                    ],
                    "priority": "Critical"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2025-0001"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "HAZMAT_COMPLIANCE_BREACH",
                    "subject_id": "SHIP-0013",
                    "outcome_code": "MITIGATION_INITIATED",
                    "outcome_details": {
                        "non_compliant_carrier": "NRMC",
                        "new_po_number": "PO-2025-0001"
                    }
                }
            }
        ],
        "outputs": [
                "PO-2025-0001",
                "SHIP-0013"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_81",
        "instruction": "As a Supply Chain Analyst, you have identified 'Johannesburg Mining Equipment' (SUP-1011) as an underperforming supplier. Your task is to minimize future risk. Locate their major 'In Transit' shipment ('SHIP-0011') and change its status using the note code 'FLAG_INSPECT_PERFORMANCE'. Then, draft a new, 'High' priority Purchase Order for 20 'Diamond Core Drill Bits' with 'Bavaria Parts GmbH' (SUP-1003), our approved alternate in this category. Finally, log a performance issue against the original supplier using the issue code 'BELOW_OTD_THRESHOLD' and document the mitigation action with the audit event 'SUPPLIER_RISK_MITIGATION_AUDIT' and result code 'ORDER_DIVERSIFICATION_SUCCESS'. Report back with the new Purchase Order number.'ve determined that 'Johannesburg Mining Equipment' (SUP-1011) is an underperforming supplier. Your objective is to mitigate future risk. Find their large 'In Transit' shipment ('SHIP-0011'). Update its status with the note code 'FLAG_INSPECT_PERFORMANCE'. Then, create a new, 'High' priority Purchase Order for 20 'Diamond Core Drill Bits' with 'Bavaria Parts GmbH' (SUP-1003), our designated alternate for this category. Finally, log the performance issue against the original supplier using the issue code 'BELOW_OTD_THRESHOLD' and audit the mitigation action with the exact audit event 'SUPPLIER_RISK_MITIGATION_AUDIT' and outcome code 'ORDER_DIVERSIFICATION_SUCCESS'. Report the new Purchase Order number.",
        "actions": [
            {
                "name": "FindInboundShipment",
                "arguments": {
                    "supplier_name": "Johannesburg Mining Equipment",
                    "origin_city": "Johannesburg",
                    "status": "In Transit"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Diamond Core Drill Bit"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0011",
                    "new_status": "In Transit",
                    "notes": "FLAG_INSPECT_PERFORMANCE"
                },
            },
            {
                "name": "LogSupplierPerformanceIssue",
                "arguments": {
                    "supplier_id": "SUP-1011",
                    "issue_code": "BELOW_OTD_THRESHOLD",
                    "shipment_id": "SHIP-0011"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1003",
                    "line_items": [
                        {
                            "sku": "HEVY-DRIL-I9",
                            "quantity": 20
                        }
                    ],
                    "priority": "High"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2025-0001"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "SUPPLIER_RISK_MITIGATION_AUDIT",
                    "subject_id": "SUP-1011",
                    "outcome_code": "ORDER_DIVERSIFICATION_SUCCESS",
                    "outcome_details": {
                        "underperforming_supplier": "SUP-1011",
                        "flagged_shipment": "SHIP-0011",
                        "new_supplier": "SUP-1003",
                        "new_po": "PO-2025-0001"
                    }
                }
            }
        ],
        "outputs": [
                "PO-2025-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_82",
        "instruction": "As a Logistics Coordinator, you need to address a critical service failure. The shipment 'ORD-0007', containing 50 units of 'Diamond Core Drill Bit' for 'Eta Mining Pty Ltd.', was returned because of incorrect customs documentation by the carrier, 'Ocean Bridge'. The customer requires a prompt reshipment. Your role is to manage this incident fully. Ensure the final state shows: 1. The original order 'ORD-0007' is marked 'Returned'. 2. The carrier 'Ocean Bridge' is put 'Under Review'. 3. The returned 50 items are restocked at the origin warehouse 'WH-11'. 4. A new 'Critical' priority order for the 50 units is initiated. 5. The new order is dispatched using the best available 'Air' carrier. 6. An audit entry with the event 'RESHIPMENT_HAZMAT_FAILURE', outcome code 'RESHIPMENT_COMPLETED', and outcome details mentioning the new order ID 'ORD-0017', original carrier SCAC 'OCBR', and new carrier SCAC 'GPLS' is recorded. Provide the new tracking number afterwards.'ORD-0007', a shipment containing 50 units of 'Diamond Core Drill Bit' for 'Eta Mining Pty Ltd.', was returned due to incorrect customs documentation filed by the carrier, 'Ocean Bridge'. The customer requires an immediate reshipment. Your objective is to manage this incident completely. The final state must show: 1. The original order 'ORD-0007' is updated to 'Returned'. 2. The carrier 'Ocean Bridge' is placed 'Under Review'. 3. The 50 returned items are restocked into inventory at the origin warehouse 'WH-11'. 4. A new 'Critical' priority order is created for the 50 units. 5. The new order is shipped using the best available 'Air' carrier. 6. An audit log with the event 'RESHIPMENT_HAZMAT_FAILURE', outcome code 'RESHIPMENT_COMPLETED', and outcome details specifying the new order ID 'ORD-0017', original carrier SCAC 'OCBR', and new carrier SCAC 'GPLS' is created. Finally, report the new tracking number.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Diamond Core Drill Bit"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0007"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0007",
                    "new_status": "Returned"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Ocean Bridge"
                },
            },
            {
                "name": "UpdateCarrierStatus",
                "arguments": {
                    "carrier_name": "Ocean Bridge",
                    "status": "Under Review"
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0009",
                    "damaged_quantity": -50
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Eta Mining Pty Ltd.",
                    "destination_city": "Perth",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "HEVY-DRIL-I9",
                            "quantity": 50
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-11",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "RESHIPMENT_HAZMAT_FAILURE",
                    "subject_id": "ORD-0007",
                    "outcome_code": "RESHIPMENT_COMPLETED",
                    "outcome_details": {
                        "new_order_id": "ORD-0017",
                        "original_carrier_scac": "OCBR",
                        "new_carrier_scac": "GPLS"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_83",
        "instruction": "As an Inventory Manager, you're responsible for stock rotation. Conduct an audit on our stock of 'Influenza Vaccine' (SKU PHRM-VACC-D4). According to policy, any batch expiring within the next 12 months must be earmarked for disposal. Your task is to carry out this policy. The final state should reflect: 1. You have located the batch of vaccines at the 'Charlotte Cold Chain Center' (WH-06) meeting the expiration requirement. 2. The entire supply of this expiring batch is moved to the 'damaged' category. 3. A new 'High' priority Purchase Order is issued for the exact number of disposed units from our essential pharma supplier, 'Mumbai Pharma Supplies' (SUP-1006). 4. The new inbound shipment from this PO is set to 'Expedited' status with the comment 'REPLENISHMENT_FOR_DISPOSED_STOCK'. 5. An audit log with the event 'EXPIRING_STOCK_DISPOSAL' is logged. Finally, please provide the new Purchase Order number.'Influenza Vaccine' (SKU PHRM-VACC-D4). Per policy, any batch expiring within the next 12 months must be written off for disposal. Your objective is to execute this policy. The final state must show: 1. You have identified the batch of vaccines at the 'Charlotte Cold Chain Center' (WH-06) that meets the expiration criteria. 2. The entire available quantity of this expiring batch has been moved to the 'damaged' category. 3. A new 'High' priority purchase order has been created for the exact quantity of disposed units from our critical pharma supplier, 'Mumbai Pharma Supplies' (SUP-1006). 4. The new inbound shipment created from this PO has been updated to 'Expedited' status with the note 'REPLENISHMENT_FOR_DISPOSED_STOCK'. 5. An audit log with the event 'EXPIRING_STOCK_DISPOSAL' is created. Finally, report the new Purchase Order number.",
        "actions": [
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0004",
                    "damaged_quantity": 18000
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "line_items": [
                        {
                            "sku": "PHRM-VACC-D4",
                            "quantity": 18000
                        }
                    ],
                    "priority": "High"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2025-0001"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0031",
                    "new_status": "Expedited",
                    "notes": "REPLENISHMENT_FOR_DISPOSED_STOCK"
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
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "EXPIRING_STOCK_DISPOSAL",
                    "subject_id": "PHRM-VACC-D4",
                    "outcome_code": "DISPOSED_AND_REORDERED",
                    "outcome_details": {
                        "inventory_id": "INV-0004",
                        "disposed_quantity": 18000,
                        "new_po_number": "PO-2025-0001",
                        "replenishment_shipment_id": "SHIP-0031"
                    }
                }
            }
        ],
        "outputs": [
                "PO-2025-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_84",
        "instruction": "As a Customs Broker, you are preparing an international shipment. A 'Critical' priority order for 5 units of the 'Basic Robotic Starter Kit' has been placed by 'Beta Retail GmbH' for delivery to Munich, Deutschland, originating from warehouse WH-03. This kit includes batteries (Hazmat Class 9). Your duty is to ensure the correct preparation and dispatch of this order. The final status should display: 1. The components of the kit have been itemized. 2. The overall weight and value of the order are calculated for the customs form. 3. The order has been initiated. 4. The shipment is dispatched using the top available 'Air' carrier. 5. An audit log 'CUSTOMS_PREP' capturing the final weight, value, and new order ID is generated for records. Lastly, provide the final tracking number.'Critical' priority order for 5 units of the 'Basic Robotic Starter Kit' has been placed by 'Beta Retail GmbH' for delivery to Munich, Deutschland, shipping from warehouse WH-03. This is a multi-component kit containing batteries (Hazmat Class 9). Your objective is to prepare and ship this order correctly. The final state must show: 1. The individual components of the kit have been identified. 2. The total weight and total value of the entire order have been calculated for the customs declaration. 3. The order has been created. 4. The order has been shipped using the best available 'Air' carrier. 5. A 'CUSTOMS_PREP' audit log has been created containing the final calculated weight, value, and the new order ID for documentation purposes. Finally, report the final tracking number.",
        "actions": [
            {
                "name": "GetKitComponents",
                "arguments": {
                    "kit_name": "Basic Robotic Starter Kit"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Lithium-Ion Battery Pack"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Beta Retail GmbH",
                    "destination_city": "Munich",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 5
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "CUSTOMS_PREP",
                    "subject_id": "ORD-0017",
                    "outcome_code": "DATA_AGGREGATED",
                    "outcome_details": {
                        "total_weight_kg": 1257.0,
                        "total_value_usd": 125899.9,
                        "carrier_scac": "GPLS"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_85",
        "instruction": "As the Receiving Manager at WH-03, you have received inbound shipment 'SHIP-0003' from 'Bavaria Parts GmbH', tied to PO 'PO-2024-0003'. The PO should contain 'Ceramic Brake Pad Set', but the shipment has 300 units of 'Automotive Windshield' instead. This is a critical discrepancy. You need to document and rectify this issue. The final state should reflect: 1. The shipment 'SHIP-0003' is noted as 'Received Incorrectly' with the comment 'INCORRECT_SKU_RECEIVED'. 2. Record a performance issue against the supplier with the code 'WRONG_ITEM_RECEIVED'. 3. A new 'Critical' priority Purchase Order is created with the same supplier for the correct item (800 units of 'Ceramic Brake Pad Set'). 4. The total value of the 300 incorrect goods is calculated and included in an audit log with the event 'RECEIVING_ERROR_CORRECTION' and outcome code 'REPLACEMENT_ORDERED_AND_LOGGED'. Finally, provide the new PO number.'ve just received inbound shipment 'SHIP-0003' from 'Bavaria Parts GmbH', which corresponds to PO 'PO-2024-0003'. The PO was for 'Ceramic Brake Pad Set', but the shipment contained 300 units of 'Automotive Windshield' instead. This is a critical error. Your objective is to document and rectify this situation. The final state must show: 1. The inbound shipment 'SHIP-0003' is updated to a status of 'Received Incorrectly' with the exact note 'INCORRECT_SKU_RECEIVED'. 2. A performance issue is logged against the supplier using the code 'WRONG_ITEM_RECEIVED'. 3. A new 'Critical' priority purchase order is created with the same supplier for the correct item (800 units of 'Ceramic Brake Pad Set'). 4. The total value of the 300 incorrectly received goods is calculated and included in a final audit log with the exact audit event 'RECEIVING_ERROR_CORRECTION' and outcome code 'REPLACEMENT_ORDERED_AND_LOGGED'. Finally, report the new PO number.",
        "actions": [
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2024-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Brake Pad Set"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Automotive Windshield"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0003",
                    "new_status": "Received Incorrectly",
                    "notes": "INCORRECT_SKU_RECEIVED"
                },
            },
            {
                "name": "LogSupplierPerformanceIssue",
                "arguments": {
                    "supplier_id": "SUP-1003",
                    "issue_code": "WRONG_ITEM_RECEIVED",
                    "shipment_id": "SHIP-0003"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1003",
                    "line_items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 800
                        }
                    ],
                    "priority": "Critical"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2025-0001"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "RECEIVING_ERROR_CORRECTION",
                    "subject_id": "SHIP-0003",
                    "outcome_code": "REPLACEMENT_ORDERED_AND_LOGGED",
                    "outcome_details": {
                        "supplier_id": "SUP-1003",
                        "incorrect_shipment_value_usd": 75000,
                        "new_po_number": "PO-2025-0001"
                    }
                }
            }
        ],
        "outputs": [
                "PO-2025-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_86",
        "instruction": "Handle the fulfillment optimization for order 'ORD-0002' from 'Beta Retail GmbH', which includes 1200 units of 'Smartphone Model X' (SKU ELEC-SMART-W23) and is currently 'In Transit' via 'Express World Delivery'. The customer requires a shipment division: 400 units to Munich and the remaining 800 to a new hub in Frankfurt. Your task is to achieve this. The final state must display: 1. Cancellation of the original order 'ORD-0002'. 2. Explicit release of the 1200 units back to available stock at WH-02. 3. Creation of two new 'High' priority orders. 4. Both new orders must be shipped using the most efficient 'Air' carrier. 5. An audit log entry with the event 'ORDER_SPLIT_AND_REDIRECT' must be made. Provide the tracking numbers for both new shipments.'ORD-0002' for 'Beta Retail GmbH', containing 1200 units of 'Smartphone Model X' (SKU ELEC-SMART-W23), is 'In Transit' via 'Express World Delivery'. The customer wants to split the shipment: 400 units to Munich and the remaining 800 to a new hub in Frankfurt. Your objective is to resolve this. The final state must show: 1. The original order 'ORD-0002' is cancelled. 2. The 1200 units are explicitly released back to available stock at WH-02. 3. Two new 'High' priority orders are created. 4. Both new orders are shipped using the best 'Air' carrier. 5. An audit log with event 'ORDER_SPLIT_AND_REDIRECT' is created. Report both new tracking numbers.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0002"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0002",
                    "new_status": "Cancelled"
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0023",
                    "damaged_quantity": -1200
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Beta Retail GmbH",
                    "destination_city": "Munich",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 400
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Beta Retail GmbH",
                    "destination_city": "Frankfurt",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 800
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-02",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-02",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "ORDER_SPLIT_AND_REDIRECT",
                    "subject_id": "ORD-0002",
                    "outcome_code": "SPLIT_COMPLETE",
                    "outcome_details": {
                        "new_order_hamburg": "ORD-0017",
                        "new_order_berlin": "ORD-0018"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017",
                "GPLS-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_87",
        "instruction": "Coordinate the resolution of a major shipping mistake as an International Logistics Specialist. Our high-value order of 5 'Articulated Robotic Arms' intended for 'Iota Automotive NAC' was incorrectly sent to 'Alpha Electronics LLC', tagged under order ID 'ORD-0001'. You are tasked with recalling the erroneous shipment and ensuring the correct order is fulfilled. The final state must show: 1. The incorrect order 'ORD-0001' as 'Returned'. 2. Processing of a full return and credit memo with reason code 'INCORRECT_RECIPIENT'. 3. Reintroduction of the recalled robotic arms to available inventory at WH-03. 4. Creation of a new 'Critical' priority order for the correct items to be shipped to 'Iota Automotive NAC' in Lyon. 5. The new order must utilize the best available 'Air' carrier. 6. Log a detailed audit trail with event code 'MISSHIPMENT_RECOVERY' and outcome code 'RECOVERY_COMPLETE'. Report the new tracking number and the credit memo ID.'Articulated Robotic Arms' for 'Iota Automotive NAC' was mistakenly shipped to 'Alpha Electronics LLC' under order ID 'ORD-0001'. You must recall the incorrect shipment and fulfill the correct order. The final state must show: 1. The incorrect order 'ORD-0001' is updated to 'Returned'. 2. A full return and credit memo have been processed using the reason code 'INCORRECT_RECIPIENT'. 3. The recalled robotic arms are returned to available inventory at WH-03. 4. A new 'Critical' priority order for the correct items is created for 'Iota Automotive NAC' in Lyon. 5. This new order is shipped using the best available 'Air' carrier. 6. A detailed audit trail with event code 'MISSHIPMENT_RECOVERY' and outcome code 'RECOVERY_COMPLETE' is logged. Report the new tracking number and the credit memo ID.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "Returned"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0001",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 5
                        }
                    ],
                    "reason": "INCORRECT_RECIPIENT"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0001",
                    "customer_id": "CUST-2001",
                    "returned_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 5
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0014",
                    "damaged_quantity": -5
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Iota Automotive NAC",
                    "destination_city": "Lyon",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 5
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "MISSHIPMENT_RECOVERY",
                    "subject_id": "ORD-0001",
                    "outcome_code": "RECOVERY_COMPLETE",
                    "outcome_details": {
                        "incorrect_customer_id": "CUST-2001",
                        "correct_customer_name": "Iota Automotive NAC",
                        "new_order_id": "ORD-0017",
                        "credit_memo_id": "CM-0001"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017",
                "CM-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_88",
        "instruction": "Manage a supply chain risk by addressing the flagged underperformance of two suppliers: 'Global Components Inc.' (SUP-1001) and 'Shanghai Electronics Co.' (SUP-1025). Cancel their significant in-transit shipments ('SHIP-0001' and 'SHIP-0025', respectively) and procure the products from our top-rated supplier, 'Osaka Electronics Ltd.' (SUP-1002). The final state should be: 1. Both shipments marked 'Cancelled' with the note 'SUPPLIER_UNDERPERFORMANCE_CANCEL'. 2. Logging of a performance issue against each supplier for the cancelled shipments using code 'SUPPLIER_PERFORMANCE_FAIL'. 3. Creation of two new 'High' priority purchase orders with 'Osaka Electronics Ltd.' for '8-bit Microcontroller' (15000 units) and 'Smartphone Model X' (4000 units). 4. Ensure an audit trail is logged. Provide both new purchase order numbers.'Global Components Inc.' (SUP-1001) and 'Shanghai Electronics Co.' (SUP-1025). You must cancel their key in-transit shipments ('SHIP-0001' and 'SHIP-0025' respectively) and re-source the products from our top-rated supplier, 'Osaka Electronics Ltd.' (SUP-1002). The final state must show: 1. Both shipments are marked 'Cancelled' with the exact note 'SUPPLIER_UNDERPERFORMANCE_CANCEL'. 2. A performance issue is logged against each respective supplier for each cancelled shipment using the code 'SUPPLIER_PERFORMANCE_FAIL'. 3. Two new, 'High' priority purchase orders are created with 'Osaka Electronics Ltd.' for the products '8-bit Microcontroller' (15000 units) and 'Smartphone Model X' (4000 units). 4. An audit trail is logged. Report both new purchase order numbers.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Smartphone Model X"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2024-0001"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2024-0025"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "new_status": "Cancelled",
                    "notes": "SUPPLIER_UNDERPERFORMANCE_CANCEL"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0025",
                    "new_status": "Cancelled",
                    "notes": "SUPPLIER_UNDERPERFORMANCE_CANCEL"
                },
            },
            {
                "name": "LogSupplierPerformanceIssue",
                "arguments": {
                    "supplier_id": "SUP-1001",
                    "issue_code": "SUPPLIER_PERFORMANCE_FAIL",
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "LogSupplierPerformanceIssue",
                "arguments": {
                    "supplier_id": "SUP-1025",
                    "issue_code": "SUPPLIER_PERFORMANCE_FAIL",
                    "shipment_id": "SHIP-0025"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1002",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 15000
                        }
                    ],
                    "priority": "High"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1002",
                    "line_items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 4000
                        }
                    ],
                    "priority": "High"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "SUPPLIER_RESOURCING",
                    "subject_id": "SUP-1001;SUP-1025",
                    "outcome_code": "ORDERS_REPLACED",
                    "outcome_details": {
                        "cancelled_shipments": "SHIP-0001;SHIP-0025",
                        "new_supplier_id": "SUP-1002",
                        "new_po_numbers": "PO-2025-0001;PO-2025-0002"
                    }
                }
            }
        ],
        "outputs": [
                "PO-2025-0001",
                "PO-2025-0002"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_89",
        "instruction": "Handle a spoilage incident as a Cold Chain Auditor for PO 'PO-2024-0010', a shipment of 'Frozen Tuna Loin', which shows a critical temperature failure. The final state should include: 1. Update of the shipment status to 'Received - Damaged' with note code 'LOSS_TEMP_BREACH'. 2. Marking of the entire available stock (2400 units) at WH-10 as damaged. 3. Logging of a performance issue against the supplier with code 'COLD_CHAIN_BREACH'. 4. Creation of a new 'Critical' priority PO for replenishing the disposed quantity. 5. Mark the new inbound shipment as 'Expedited' with the note 'URGENT_REPLACEMENT'. 6. Log an audit with the event 'COLD_CHAIN_SPOILAGE_AUDIT' and outcome 'STOCK_REPLENISHED', detailing 'disposed_inventory_id' as 'INV-0008' and 'new_po_number' as 'PO-2025-0001'. Report the number of the new PO.'PO-2024-0010', a shipment of 'Frozen Tuna Loin'. Temperature logs show a critical failure. The final state must show: 1. The shipment status is updated to 'Received - Damaged' with note code 'LOSS_TEMP_BREACH'. 2. The entire available quantity (2400 units) of the stock at WH-10 is marked as damaged. 3. A performance issue is logged against the supplier with code 'COLD_CHAIN_BREACH'. 4. A new 'Critical' priority PO is created to replenish the disposed quantity. 5. The new inbound shipment is marked 'Expedited' with note code 'URGENT_REPLACEMENT'. 6. An audit is logged with the exact audit event 'COLD_CHAIN_SPOILAGE_AUDIT', and the exact outcome code 'STOCK_REPLENISHED'. The outcome details must specify 'disposed_inventory_id' as 'INV-0008' and 'new_po_number' as 'PO-2025-0001'. Report the new PO number.",
        "actions": [
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2024-0010"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Frozen Tuna Loin"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0010",
                    "new_status": "Received - Damaged",
                    "notes": "LOSS_TEMP_BREACH"
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0008",
                    "damaged_quantity": 2400
                },
            },
            {
                "name": "LogSupplierPerformanceIssue",
                "arguments": {
                    "supplier_id": "SUP-1010",
                    "issue_code": "COLD_CHAIN_BREACH",
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1010",
                    "line_items": [
                        {
                            "sku": "FOOD-FISH-H8",
                            "quantity": 2400
                        }
                    ],
                    "priority": "Critical"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2025-0001"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0031",
                    "new_status": "Expedited",
                    "notes": "URGENT_REPLACEMENT"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "COLD_CHAIN_SPOILAGE_AUDIT",
                    "subject_id": "SHIP-0010",
                    "outcome_code": "STOCK_REPLENISHED",
                    "outcome_details": {
                        "disposed_inventory_id": "INV-0008",
                        "new_po_number": "PO-2025-0001"
                    }
                }
            }
        ],
        "outputs": [
                "PO-2025-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_90",
        "instruction": "Address a fraud alert as a Fraud Analyst for customer 'Alpha Electronics LLC' (CUST-2001) who has reported order 'ORD-0001', involving 300 units of '8-bit Microcontroller', as fraudulent. This must be processed as a high-priority security incident. The final state must include: 1. Updating the order status to 'On Hold - Fraud Investigation'. 2. Issuance of a provisional credit memo for the fraudulent items. 3. Addition of a security note to the originating warehouse (WH-01) stating 'SECURITY_ALERT:ORD-0001_FRAUD_INVESTIGATION'. 4. Logging a security audit with the event 'FRAUDULENT_ORDER_REPORTED' and the outcome 'INVESTIGATION_OPENED'. Provide the issued credit memo ID.'Alpha Electronics LLC' (CUST-2001) has reported that order 'ORD-0001', which contained 300 units of '8-bit Microcontroller', is fraudulent. You must process this as a high-priority security incident. The final state must show: 1. The order status is updated to 'On Hold - Fraud Investigation'. 2. A provisional credit memo is issued for the fraudulent items. 3. A security note is added to the origin warehouse (WH-01) with the exact text: 'SECURITY_ALERT:ORD-0001_FRAUD_INVESTIGATION'. 4. A security audit is logged using the audit event 'FRAUDULENT_ORDER_REPORTED' and outcome code 'INVESTIGATION_OPENED'. Report the ID of the credit memo issued.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0001"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "On Hold - Fraud Investigation"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0001",
                    "customer_id": "CUST-2001",
                    "returned_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 300
                        }
                    ]
                },
            },
            {
                "name": "UpdateWarehouseNotes",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "notes": "SECURITY_ALERT:ORD-0001_FRAUD_INVESTIGATION"
                },
            },
            {
                "name": "GetCreditMemoDetails",
                "arguments": {
                    "credit_memo_id": "CM-0001"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "FRAUDULENT_ORDER_REPORTED",
                    "subject_id": "ORD-0001",
                    "outcome_code": "INVESTIGATION_OPENED",
                    "outcome_details": {
                        "customer_id": "CUST-2001",
                        "credit_memo_id": "CM-0001"
                    }
                }
            }
        ],
        "outputs": [
                "CM-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_91",
        "instruction": "As a Product Manager, you're responsible for introducing a new 'Robotics Pro Kit', which includes one 'Articulated Robotic Arm' and four 'Lithium-Ion Battery Packs'. 'Osaka Robotics Corp.' is placing a 'High' priority order for 3 kits, to be dispatched from 'Midwest Parts Warehouse' (WH-03) to Osaka via 'Air'. Your task is to handle this initial order. The final state should reflect: 1) Validation of component SKUs and stock availability confirmation. 2) Creation of a new outbound order. 3) Shipment of the order through the most suitable 'Air' carrier. 4) Logging of an audit trail with event 'NEW_KIT_FULFILLMENT' and outcome code 'PRO_KIT_LAUNCH_ORDER_SHIPPED'. Provide the final tracking number.'Robotics Pro Kit'. The kit consists of one 'Articulated Robotic Arm' and four 'Lithium-Ion Battery Packs'. Customer 'Osaka Robotics Corp.' wants to place a 'High' priority order for 3 of these new kits, to be shipped from 'Midwest Parts Warehouse' (WH-03) to Osaka via 'Air' transport. Your objective is to process this first-ever order. The final state must show: 1) You have verified the component SKUs and checked available stock. 2) A new outbound order is created. 3) The order is shipped using the best available 'Air' carrier. 4) An audit trail with event 'NEW_KIT_FULFILLMENT' and outcome code 'PRO_KIT_LAUNCH_ORDER_SHIPPED' is logged. Report the final tracking number.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Lithium-Ion Battery Pack"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Osaka Robotics Corp.",
                    "destination_city": "Osaka",
                    "priority_level": "High",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 3
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 12
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "NEW_KIT_FULFILLMENT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "PRO_KIT_LAUNCH_ORDER_SHIPPED",
                    "outcome_details": {
                        "customer_name": "Osaka Robotics Corp.",
                        "carrier_scac": "GPLS"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_92",
        "instruction": "As a Returns Manager, 'Theta Foods SA' has reported a spoilage incident involving their 'Frozen Tuna Loin' shipment from sales order 'SO-2024-0008', attributed to a temperature breach during inbound shipment 'SHIP-0010' by 'Melbourne Seafood Exporters'. The initial shipment left 'Buenos Aires Cold Chain', with returns routed to 'San Francisco Fresh Foods DC' (WH-10). Your role is to manage this international return and restock. The final steps must include: 1. Creation of return authorization for the 2400 spoiled units, utilizing reason code 'SPOILAGE_TEMP_BREACH'. 2. Issuance of a credit memo for 2400 units. 3. Explicit marking of all 2400 'Frozen Tuna Loin' units as damaged in WH-10 inventory. 4. Logging a performance issue against 'Melbourne Seafood Exporters' (SUP-1010) using issue code 'COLD_CHAIN_FAILURE_RETURN' for 'SHIP-0010'. 5. Generation of a 'Critical' priority purchase order for 2400 units of 'Frozen Tuna Loin' with 'Melbourne Seafood Exporters' (SUP-1010). 6. Updating new inbound shipment 'SHIP-0031' to 'Expedited' with note 'URGENT_SPOILAGE_REPLENISHMENT'. 7. Documenting the event in the audit trail as 'SPOILAGE_RETURN_RECOVERY' with outcome code 'REPLENISHMENT_INITIATED'. Please submit the credit memo ID and new Purchase Order number 'PO-2025-0001'.'Theta Foods SA' has reported a complete spoilage of their 'Frozen Tuna Loin' shipment from sales order 'SO-2024-0008' due to a critical temperature breach in transit, linked to inbound shipment 'SHIP-0010' from 'Melbourne Seafood Exporters'. The original outbound shipment departed from the 'Buenos Aires Cold Chain' warehouse, but the return destination is the 'San Francisco Fresh Foods DC' (WH-10). Your objective is to process this international return and replenish the stock. The final state must show: 1. A return authorization is created for the 2400 spoiled units using the reason code 'SPOILAGE_TEMP_BREACH'. 2. A credit memo is issued for these 2400 units. 3. All 2400 currently available units of 'Frozen Tuna Loin' are explicitly marked as damaged in inventory at WH-10. 4. A performance issue is logged against the supplier ('Melbourne Seafood Exporters', SUP-1010) using the issue code 'COLD_CHAIN_FAILURE_RETURN' for shipment 'SHIP-0010'. 5. A new 'Critical' priority purchase order for the exact quantity (2400 units) of 'Frozen Tuna Loin' is created with 'Melbourne Seafood Exporters' (SUP-1010). 6. The new inbound shipment created from this PO (which will be 'SHIP-0031') is updated to 'Expedited' status with the note 'URGENT_SPOILAGE_REPLENISHMENT'. 7. The entire incident is logged in the audit trail with the event 'SPOILAGE_RETURN_RECOVERY' and outcome code 'REPLENISHMENT_INITIATED'. Report the ID of the credit memo and the new Purchase Order number (which will be 'PO-2025-0001').",
        "actions": [
            {
                "name": "GetOutboundOrderDetailsBySo",
                "arguments": {
                    "sales_order_number": "SO-2024-0008"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Frozen Tuna Loin"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0008",
                    "line_items": [
                        {
                            "sku": "FOOD-FISH-H8",
                            "quantity": 2400
                        }
                    ],
                    "reason": "SPOILAGE_TEMP_BREACH"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0008",
                    "customer_id": "CUST-2008",
                    "returned_items": [
                        {
                            "sku": "FOOD-FISH-H8",
                            "quantity": 2400
                        }
                    ]
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0008",
                    "damaged_quantity": 2400
                },
            },
            {
                "name": "LogSupplierPerformanceIssue",
                "arguments": {
                    "supplier_id": "SUP-1010",
                    "issue_code": "COLD_CHAIN_FAILURE_RETURN",
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1010",
                    "line_items": [
                        {
                            "sku": "FOOD-FISH-H8",
                            "quantity": 2400
                        }
                    ],
                    "priority": "Critical"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2025-0001"
                },
            },
            {
                "name": "UpdateShipmentStatus",
                "arguments": {
                    "shipment_id": "SHIP-0031",
                    "new_status": "Expedited",
                    "notes": "URGENT_SPOILAGE_REPLENISHMENT"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "SPOILAGE_RETURN_RECOVERY",
                    "subject_id": "ORD-0008;RMA-1001",
                    "outcome_code": "REPLENISHMENT_INITIATED",
                    "outcome_details": {
                        "credit_memo_id": "CM-0008",
                        "new_po_number": "PO-2025-0001",
                        "damaged_qty": 2400
                    }
                }
            }
        ],
        "outputs": [
                "CM-0008",
                "PO-2025-0001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_93",
        "instruction": "As a Returns Supervisor, manage the return of order 'ORD-0005' to 'Epsilon Fashion Co.' due to 'Incorrect Size'. The order included 1500 units of 'Organic Cotton T-Shirt', and per policy, must be sent back to 'East Coast Fashion Center' (WH-04) using 'Global Parcel Service'. The return is domestic. Ensure the final state includes: 1. RMA creation. 2. Credit memo issuance. 3. Creation of an inbound return shipment to the correct warehouse using 'Global Parcel Service'. 4. Return of the 1500 units to available stock at WH-04. 5. Update of the original order status to 'Returned'. Submit the RMA and inbound shipment IDs.'ORD-0005' to 'Epsilon Fashion Co.' is being returned due to 'Incorrect Size'. The order contained 1500 units of 'Organic Cotton T-Shirt'. Per policy, the return must go back to the origin warehouse, 'East Coast Fashion Center' (WH-04). This is a domestic return. You must use 'Global Parcel Service' carrier. The final state must show: 1. An RMA is created. 2. A credit memo is issued. 3. An inbound return shipment is created for the correct warehouse and carrier. 4. The 1500 units are explicitly returned to available stock at WH-04. 5. The original order is updated to 'Returned'. Report the RMA and inbound shipment IDs.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Organic Cotton T-Shirt"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0005",
                    "line_items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 1500
                        }
                    ],
                    "reason": "Incorrect Size"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0005",
                    "customer_id": "CUST-2005",
                    "returned_items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 1500
                        }
                    ]
                },
            },
            {
                "name": "CreateInboundReturnShipment",
                "arguments": {
                    "rma_id": "RMA-1001",
                    "from_customer_id": "CUST-2005",
                    "to_warehouse_id": "WH-04",
                    "carrier_scac": "GPLS"
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0015",
                    "damaged_quantity": -1500
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0005",
                    "new_status": "Returned"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "DOMESTIC_RETURN_PROCESSING",
                    "subject_id": "ORD-0005",
                    "outcome_code": "RETURN_COMPLETE",
                    "outcome_details": {
                        "rma_id": "RMA-1001",
                        "inbound_shipment_id": "SHIP-0031",
                        "credit_memo_id": "CM-0005"
                    }
                }
            }
        ],
        "outputs": [
                "RMA-1001",
                "SHIP-0031"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_94",
        "instruction": "Serving as an Inventory Auditor, you are to conduct a significant inventory write-off. All 'Organic Arabica Coffee Beans' (SKU FOOD-COFF-C3) at WH-05 and 'Frozen Tuna Loin' (SKU FOOD-FISH-H8) at WH-10 have expired. Undertake this disposal and initiate replacement orders. Your final report must display: 1. Transfer of all expired product quantities to 'damaged' in the respective warehouses. 2. Creation of a 'High' priority purchase order for replacements from 'Rio Grande Coffee Traders' (SUP-1005), for 1500 units of 'Extra Virgin Olive Oil' and 800 units of 'Argentinian Malbec Wine'. 3. Logging of 'FINANCIAL_WRITE_OFF' audit event with total inventory loss valuation and the new PO number. Provide the new PO number and total loss figure.'Organic Arabica Coffee Beans' (SKU FOOD-COFF-C3) at WH-05 and all available 'Frozen Tuna Loin' (SKU FOOD-FISH-H8) at WH-10. Your objective is to process this disposal and reorder replacements. The final state must show: 1. The entire available quantity of both expired products has been moved to the 'damaged' category in their respective warehouses. 2. A single new 'High' priority purchase order has been created for replacement products from our top-rated grocery supplier, 'Rio Grande Coffee Traders' (SUP-1005). The replacements are 1500 units of 'Extra Virgin Olive Oil' and 800 units of 'Argentinian Malbec Wine'. 3. A 'FINANCIAL_WRITE_OFF' audit event is logged, containing the total calculated value of the inventory loss and the new PO number. Report the new PO number and the total loss value.",
        "actions": [
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05"
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0003",
                    "damaged_quantity": 5000
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0008",
                    "damaged_quantity": 2400
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Extra Virgin Olive Oil"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Argentinian Malbec Wine"
                },
            },
            {
                "name": "CreatePurchaseOrder",
                "arguments": {
                    "supplier_id": "SUP-1005",
                    "line_items": [
                        {
                            "sku": "FOOD-OLIV-V22",
                            "quantity": 1500
                        },
                        {
                            "sku": "BEVG-WINE-P16",
                            "quantity": 800
                        }
                    ],
                    "priority": "High"
                },
            },
            {
                "name": "GetPurchaseOrderDetails",
                "arguments": {
                    "po_number": "PO-2025-0001"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "FINANCIAL_WRITE_OFF",
                    "subject_id": "FOOD-COFF-C3;FOOD-FISH-H8",
                    "outcome_code": "DISPOSED_AND_REPLACED",
                    "outcome_details": {
                        "total_loss_value_usd": 194000.0,
                        "new_po_number": "PO-2025-0001",
                        "replenishment_shipment_id": "SHIP-0031"
                    }
                }
            }
        ],
        "outputs": [
                "PO-2025-0001",
                "194000.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_95",
        "instruction": "As a Risk Manager, you must address a critical alert regarding 'Express World Delivery' and its temporary gap in international insurance coverage. Order 'ORD-0002', a high-value shipment to 'Beta Retail GmbH', is currently 'In Transit' with them and vulnerable. Take immediate action to correct this. The final outcome needs to indicate: 1. Change of 'Express World Delivery' status to 'On Hold - Insurance Lapse'. 2. Mid-transit reassignment of the at-risk order 'ORD-0002' to the leading alternative 'Air' carrier. 3. Update of the order status to 'In Transit - Carrier Reassigned'. 4. Addition of a note with the code 'ALERT:ORD-0002_CARRIER_REASSIGNED_TO_UPSN' at 'Northwest Fulfillment Center'. 5. Comprehensive logging of the incident in audit trail with event code 'CARRIER_RISK_MITIGATION', outcome code 'CARRIER_REASSIGNED_SUCCESS', and reason code 'INSURANCE_LAPSE'. Provide the new shipment tracking number.'ve received a critical alert that 'Express World Delivery' has a temporary lapse in their international insurance coverage. Order 'ORD-0002', a high-value shipment to 'Beta Retail GmbH' currently 'In Transit' with this carrier, is at risk. Your objective is to mitigate this immediately. The final state must show: 1. The carrier 'Express World Delivery' has its status updated to 'On Hold - Insurance Lapse'. 2. The at-risk order 'ORD-0002' is reassigned mid-transit to the best-performing alternative 'Air' carrier. 3. The order's status is updated to 'In Transit - Carrier Reassigned'. 4. A note with the code 'ALERT:ORD-0002_CARRIER_REASSIGNED_TO_UPSN' is added to the origin warehouse ('Northwest Fulfillment Center'). 5. The entire incident is logged in the audit trail with the event code 'CARRIER_RISK_MITIGATION', outcome code 'CARRIER_REASSIGNED_SUCCESS', and reason code 'INSURANCE_LAPSE'. Report the new tracking number for the shipment.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0002"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "Express World Delivery"
                },
            },
            {
                "name": "UpdateCarrierStatus",
                "arguments": {
                    "carrier_name": "Express World Delivery",
                    "status": "On Hold - Insurance Lapse"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ReassignOrderCarrier",
                "arguments": {
                    "order_id": "ORD-0002",
                    "new_carrier_scac": "GPLS"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0002",
                    "new_status": "In Transit - Carrier Reassigned"
                },
            },
            {
                "name": "UpdateWarehouseNotes",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "notes": "ALERT:ORD-0002_CARRIER_REASSIGNED_TO_UPSN"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "CARRIER_RISK_MITIGATION",
                    "subject_id": "ORD-0002",
                    "outcome_code": "CARRIER_REASSIGNED_SUCCESS",
                    "outcome_details": {
                        "original_carrier_scac": "EWDL",
                        "new_carrier_scac": "GPLS",
                        "reason_code": "INSURANCE_LAPSE"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0002"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_96",
        "instruction": "As a Fulfillment Manager handling a stock deadlock, a 'Critical' priority order has been placed by 'Zeta Tech Solutions' in Yokohama for 10,000 '8-bit Microcontrollers' that need to be shipped from WH-01. Currently, there's a 'Low' priority order, 'ORD-0001', for 'Alpha Electronics LLC', already allocated 12,500 units at WH-01. Policy requires you to cancel the low-priority order to allocate stock accordingly. You must then re-allocate the original 12,500 units from 'ORD-0001': fulfill 10,000 units for 'Zeta Tech Solutions' as the new 'Critical' order, and create a new 'Low' priority order for 'Alpha Electronics LLC' with the remaining 2,500 units to be shipped from WH-03 using the most efficient 'Truck' carrier. The 'Critical' order for 'Zeta Tech Solutions' must be dispatched from WH-01 using the best 'Air' carrier. Ensure the final status reflects: 1. 'ORD-0001' is marked as 'Cancelled'. 2. A new 'Low' priority order for 2,500 units to 'Alpha Electronics' is created and routed from WH-03. 3. The new 'Critical' order for 10,000 units is established for 'Zeta Tech Solutions' with shipping from WH-01. 4. Log an audit entry with event 'DEADLOCK_RESOLUTION_REASSIGN'. Submit the tracking numbers for both the new Critical and new Low-priority orders.'Critical' priority order has arrived from 'Zeta Tech Solutions' located in Yokohama for 10,000 '8-bit Microcontrollers' to ship from WH-01. However, 12,500 units at WH-01 are currently allocated to a 'Low' priority order, 'ORD-0001', for 'Alpha Electronics LLC'. Policy dictates you must cancel the low-priority order to free up stock. You must then ensure the original quantity of 12,500 units from 'ORD-0001' is re-fulfilled: 10,000 units for 'Zeta Tech Solutions' as the new 'Critical' order, and the remaining 2,500 units as a new 'Low' priority order for 'Alpha Electronics LLC' shipped from the next best warehouse (WH-03) using the best 'Truck' carrier. The new 'Critical' order for 'Zeta Tech Solutions' must be shipped from WH-01 using the best 'Air' carrier. The final state must show: 1. Order 'ORD-0001' is 'Cancelled'. 2. A new 'Low' priority order for 'Alpha Electronics' of 2,500 units is created and shipped from WH-03. 3. The new 'Critical' order for 'Zeta Tech Solutions' of 10,000 units is created and shipped from WH-01. 4. An audit trail with event 'DEADLOCK_RESOLUTION_REASSIGN' is logged. Report the tracking numbers for the new Critical order and the new Low-priority order.",
        "actions": [
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
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
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0001"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001",
                    "new_status": "Cancelled"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Low",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 2500
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Truck"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Zeta Tech Solutions",
                    "destination_city": "Yokohama",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 10000
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0018",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "DEADLOCK_RESOLUTION_REASSIGN",
                    "subject_id": "ORD-0018",
                    "outcome_code": "SUCCESS",
                    "outcome_details": {
                        "cancelled_order_id": "ORD-0001",
                        "reassigned_order_id": "ORD-0017"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0018",
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_97",
        "instruction": "Your role as a Carrier Relations Manager involves addressing a critical service alert for 'DeutschLogistik': their 'EuroCargo' rail service has been halted. 'ORD-0009' for 'Iota Automotive NAC' is currently 'In Transit' to Lyon utilizing this service. Your task is to minimize this disturbance. The desired final condition should ensure: 1. 'DeutschLogistik' carrier status is updated to 'Partial Service Suspension'. 2. The order is reassigned to the best alternative 'Rail' carrier available. 3. The order's status becomes 'In Transit - Reassigned'. 4. An audit log is created featuring the event code 'SERVICE_DISRUPTION_MITIGATION' and outcome code 'CARRIER_REASSIGNED'. Provide the new tracking number.'DeutschLogistik': their 'EuroCargo' rail service has been suspended. Order 'ORD-0009' for 'Iota Automotive NAC' is currently 'In Transit' to Lyon using this exact service. Your objective is to mitigate this disruption. The final state must show: 1. The 'DeutschLogistik' carrier status is updated to 'Partial Service Suspension'. 2. The order is reassigned to the best-performing alternative 'Rail' carrier. 3. The order's status is updated to 'In Transit - Reassigned'. 4. A detailed audit is logged with the event code 'SERVICE_DISRUPTION_MITIGATION' and outcome code 'CARRIER_REASSIGNED'. Report the new tracking number.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0009"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_name": "DeutschLogistik"
                },
            },
            {
                "name": "UpdateCarrierStatus",
                "arguments": {
                    "carrier_name": "DeutschLogistik",
                    "status": "Partial Service Suspension"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Rail"
                },
            },
            {
                "name": "ReassignOrderCarrier",
                "arguments": {
                    "order_id": "ORD-0009",
                    "new_carrier_scac": "ALFS"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0009",
                    "new_status": "In Transit - Reassigned"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "SERVICE_DISRUPTION_MITIGATION",
                    "subject_id": "ORD-0009",
                    "outcome_code": "CARRIER_REASSIGNED",
                    "outcome_details": {
                        "original_carrier_scac": "DBSK",
                        "new_carrier_scac": "ALFS",
                        "reason": "SERVICE_SUSPENSION"
                    }
                }
            }
        ],
        "outputs": [
                "ALFS-0009"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_98",
        "instruction": "As the Kitting Fulfillment Lead, you need to address a 'Critical' priority order requesting 20 'Basic Robotic Starter Kits' for 'Alpha Electronics LLC' to be delivered to San Jose. The 'Midwest Parts Warehouse' (WH-03) holds all 20 necessary 'Articulated Robotic Arms' but only 30 of the 40 needed 'Lithium-Ion Battery Packs'. For critical orders, you are to immediately dispatch available items and put the rest on backorder. This shipment will go via 'Air' transport. Manage this split fulfillment to ensure the final status includes: 1. An outbound order for the partial kit (20 arms, 30 batteries) is issued and shipped. 2. A separate backorder for the remaining 10 batteries is initiated with status 'Pending - Awaiting Stock'. 3. Log an audit entry with event code 'KIT_FULFILLMENT_SPLIT' and the precise outcome code 'PARTIAL_KIT_SHIPPED'. Report the tracking number for the partial shipment and the backorder ID.'Critical' priority order for 20 'Basic Robotic Starter Kits' is placed for 'Alpha Electronics LLC' to be shipped to San Jose. The fulfillment warehouse, 'Midwest Parts Warehouse' (WH-03), has all 20 required 'Articulated Robotic Arms' but only 30 of the 40 required 'Lithium-Ion Battery Packs'. Per policy for critical orders, you must ship what is available immediately and backorder the rest. The shipment must use 'Air' transport. Your objective is to manage this split fulfillment. The final state must show: 1. An outbound order for the partial kit (20 arms, 30 batteries) is created and shipped. 2. A separate backorder for the remaining 10 batteries is created with status 'Pending - Awaiting Stock'. 3. An audit log is created with event code 'KIT_FULFILLMENT_SPLIT' and the exact outcome code 'PARTIAL_KIT_SHIPPED'. Report the tracking number for the partial shipment and the ID for the backorder.",
        "actions": [
            {
                "name": "GetKitComponents",
                "arguments": {
                    "kit_name": "Basic Robotic Starter Kit"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Articulated Robotic Arm"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Lithium-Ion Battery Pack"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryDetails",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 20
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 30
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Pending - Awaiting Stock"
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-03",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "KIT_FULFILLMENT_SPLIT",
                    "subject_id": "ORD-0017",
                    "outcome_code": "PARTIAL_KIT_SHIPPED",
                    "outcome_details": {
                        "backorder_id": "ORD-0018"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017",
                "ORD-0018"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_99",
        "instruction": "In your role as a Proactive Risk Manager, a significant port strike targeting all of California will impede all 'Sea' freight. Order 'ORD-0006' for 'Zeta Tech Solutions' containing 900 '8-bit Microcontroller' units is marked as 'Shipped' from San Francisco (WH-05) via 'NorthStar Shipping' but has not yet departed. Your aim is to avert a delay. The intended final update must reflect: 1. Cancellation of 'ORD-0006' under the status 'Cancelled - Force Majeure'. 2. Returning 900 units as available stock to the West Coast Distribution Hub (WH-01). 3. Creating a new 'Critical' priority order for the same merchandise. 4. Ensuring the new order is shipped via the optimal 'Air' carrier. 5. Recording an audit event 'PROACTIVE_REROUTE' with an outcome of 'SUCCESS'. Supply the new tracking number.'Sea' freight. Order 'ORD-0006' for 'Zeta Tech Solutions' (containing 900 units of '8-bit Microcontroller') is 'Shipped' from San Francisco (WH-05) via 'NorthStar Shipping' but has not yet departed. Your objective is to proactively prevent a delay. The final state must show: 1. The original order 'ORD-0006' is cancelled using the status 'Cancelled - Force Majeure'. 2. The 900 units are returned to available stock at the West Coast Distribution Hub (WH-01). 3. A new 'Critical' priority order is created for the same items. 4. The new order is shipped via the best available 'Air' carrier. 5. An audit is logged with event 'PROACTIVE_REROUTE' and outcome 'SUCCESS'. Report the new tracking number.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0006",
                    "new_status": "Cancelled - Force Majeure"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "8-bit Microcontroller"
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0001",
                    "damaged_quantity": -900
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Zeta Tech Solutions",
                    "destination_city": "Yokohama",
                    "priority_level": "Critical",
                    "line_items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 900
                        }
                    ]
                },
            },
            {
                "name": "ListCarriersByMode",
                "arguments": {
                    "mode": "Air"
                },
            },
            {
                "name": "ShipOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0017",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "PROACTIVE_REROUTE",
                    "subject_id": "ORD-0006",
                    "outcome_code": "SUCCESS",
                    "outcome_details": {
                        "new_order_id": "ORD-0017"
                    }
                }
            }
        ],
        "outputs": [
                "GPLS-0017"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_100",
        "instruction": "As a Finance Returns Auditor, your task involves managing an incident involving 'Gamma Construction Ltd.' and order 'ORD-0003'. They returned 100 'Ceramic Floor Tiles'. Upon inspection, 85 were found undamaged and 15 broken. Following policy, credit is issued solely for undamaged goods. Aim to process this split return along with its complete financial repercussions. The intended final state should document: 1. An RMA initiated citing 'SPLIT_RETURN_DAMAGED'. 2. Issue a credit memo for the 85 undamaged tiles only. 3. Update inventory at WH-12 (85 restocked, 15 recorded as damaged). 4. Log a 'FINANCIAL_RECONCILIATION' audit specifying the credit amount and the loss value (cost of damaged goods). Document the total credited amount and the inventory loss value.'Gamma Construction Ltd.' and order 'ORD-0003'. They returned 100 'Ceramic Floor Tiles'. Inspection revealed 85 are undamaged and 15 are broken. Per policy, credit is issued only for undamaged items. Your objective is to process this split return and its full financial impact. The final state must show: 1. An RMA is created with reason 'SPLIT_RETURN_DAMAGED'. 2. A credit memo is issued for only the 85 undamaged tiles. 3. Inventory is updated at WH-12 (85 restocked, 15 damaged). 4. A 'FINANCIAL_RECONCILIATION' audit is logged with outcome 'RETURN_PROCESSED', detailing the credited value and the inventory loss value (cost of damaged goods). Report the total credited value and the inventory loss value.",
        "actions": [
            {
                "name": "GetOutboundOrderDetails",
                "arguments": {
                    "order_id": "ORD-0003"
                },
            },
            {
                "name": "GetProductDetails",
                "arguments": {
                    "product_name": "Ceramic Floor Tile"
                },
            },
            {
                "name": "CreateReturnAuthorization",
                "arguments": {
                    "order_id": "ORD-0003",
                    "line_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 100
                        }
                    ],
                    "reason": "SPLIT_RETURN_DAMAGED"
                },
            },
            {
                "name": "IssueCustomerCreditMemo",
                "arguments": {
                    "order_id": "ORD-0003",
                    "customer_id": "CUST-2003",
                    "returned_items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 85
                        }
                    ]
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
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": -85
                },
            },
            {
                "name": "UpdateInventoryDamageStatus",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "damaged_quantity": 15
                },
            },
            {
                "name": "GetCreditMemoDetails",
                "arguments": {
                    "credit_memo_id": "CM-0003"
                },
            },
            {
                "name": "LogAuditTrail",
                "arguments": {
                    "audit_event": "FINANCIAL_RECONCILIATION",
                    "subject_id": "CM-0003",
                    "outcome_code": "RETURN_PROCESSED",
                    "outcome_details": {
                        "credited_value_usd": 510.0,
                        "inventory_loss_usd": 52.5
                    }
                }
            }
        ],
        "outputs": [
                "510.00",
                "52.50"
        ]
    }
]
