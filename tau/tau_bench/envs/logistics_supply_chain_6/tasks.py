
tasks = [
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_001",
        "instruction": "Handle the requirement from Mercy General Hospital for 100 Influenza Vaccine (PHRM-VACC-D4) and 50 Oncology Drug A (PHRM-DRUG-S19). Begin by identifying warehouses with Cold Chain capabilities, then confirm inventory availability for both items at the first appropriate warehouse, create the order (ORD-0017) for Mercy General to 789 Health Blvd, Charlotte, SC, and finally, assign the Air carrier 'CARR-006' with tracking MED-PRIORITY-001. Lastly, report the order ID for the new order.'CARR-006' with tracking MED-PRIORITY-001. Finally, report the order ID for the new order",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Cold Chain (2-8°C)"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Mercy General",
                    "warehouse_id": "WH-06",
                    "items": [
                        {
                            "sku": "PHRM-VACC-D4",
                            "quantity": 100
                        },
                        {
                            "sku": "PHRM-DRUG-S19",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "789 Health Blvd, Charlotte, SC"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "MED-PRIORITY-001"
                }
            }
        ],
        "outputs": [
                "ORD-0017"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_002",
        "instruction": "Coordinate the arrival of 650 Solar Panels (TECH-SOLR-G7) in shipment SHIP-0009 at Phoenix Renewable Warehouse (WH-09), then promptly fulfill an order for 100 panels to Solaris Inc at 1 Sun Way, Phoenix, AZ. Begin by receiving the shipment, verify updated inventory levels, create the outbound order, locate the best Truck carrier, and dispatch with tracking SOLAR-RUSH-100. Report the new order ID.",
        "actions": [
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0009"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0009",
                    "items_received": [
                        {
                            "sku": "TECH-SOLR-G7",
                            "quantity": 650
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "sku": "TECH-SOLR-G7"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "TECH-SOLR-G7"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Solaris Inc",
                    "warehouse_id": "WH-09",
                    "items": [
                        {
                            "sku": "TECH-SOLR-G7",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "1 Sun Way, Phoenix, AZ"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "SOLAR-RUSH-100"
                }
            }
        ],
        "outputs": [
                "ORD-0017"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_003",
        "instruction": "Facilitate a cycle count for 'Teak Wood Dining Chair' (FURN-CHAIR-M13) at 'WH-14'. The system indicates 600 units, but a physical count shows 595. Adjust the inventory with the reason 'Cycle Count Adjustment'. Then, check if the new quantity falls below the reorder point and report the final count.'Teak Wood Dining Chair' (FURN-CHAIR-M13) at 'WH-14'. The system shows 600 units, but a physical count reveals 595. Adjust the inventory with reason 'Cycle Count Adjustment'. Then, check if the new quantity is below the reorder point and report the final count.",
        "actions": [
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13",
                    "quantity_change": -5,
                    "reason": "Cycle Count Adjustment"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0013\", \"quantity_on_hand\": 595, \"reorder_point\": 150}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_004",
        "instruction": "Manage the situation regarding the delayed Smartphone X shipment. Start by identifying inbound shipments from SUP-1002 to Portland warehouse (WH-02), change the status of the found shipment to 'Delayed', check current inventory of ELEC-SMART-W23 at that warehouse, and if stock is under 5000 units, deploy the Truck carrier 'CARR-014' and set up an emergency inbound shipment for 300 units arriving on 2024-08-01. Retrieve details of the final inbound shipment.'Delayed', check current inventory of ELEC-SMART-W23 at that warehouse, and if stock is below 5000 units, use the Truck carrier 'CARR-014' and create emergency inbound shipment for 300 units arriving 2024-08-01. Retrieve final inbound shipment details.",
        "actions": [
            {
                "name": "FindInboundShipments",
                "arguments": {
                    "supplier_id": "SUP-1002",
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0002",
                    "status": "Delayed"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1002",
                    "destination_warehouse_id": "WH-02",
                    "carrier_id": "CARR-014",
                    "items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 300
                        }
                    ],
                    "estimated_arrival_date": "2024-08-01"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\", \"supplier_id\": \"SUP-1002\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_005",
        "instruction": "TechStall requires 20 units of 8-bit Microcontroller (SKU: ELEC-CHIP-A1). Start by checking inventory at San Diego warehouse (WH-01), create the order for TechStall to 789 Tech Way, Silicon Valley, OR, confirm the order was created successfully, check the updated available quantity after order creation, and assign Air carrier CARR-006 with tracking TECH-FAST-020.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "TechStall",
                    "warehouse_id": "WH-01",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 20
                        }
                    ],
                    "shipping_address": "789 Tech Way, Silicon Valley, OR"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "TECH-FAST-020"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_006",
        "instruction": "Coordinate the processing of the Industrial Solvent (CHEM-SOLV-K11) return from order ORD-0014. Customer returns 2 units. Begin by retrieving order details to confirm the warehouse involved, examine the current inventory at that location, reintegrate the returned items into the stock with the description 'Customer Return', then simultaneously deduct the same 2 units as damaged due to 'Damaged Goods', and confirm the final inventory count.'Customer Return', then write off same 2 units as damaged with reason 'Damaged Goods', and verify final inventory level.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0014"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-13",
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-13",
                    "sku": "CHEM-SOLV-K11",
                    "quantity_change": 2,
                    "reason": "Customer Return"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-13",
                    "sku": "CHEM-SOLV-K11",
                    "quantity_change": -2,
                    "reason": "Damaged Goods"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-13",
                    "sku": "CHEM-SOLV-K11"
                }
            }
        ],
        "outputs": [
                "\"inventory_id\": \"INV-0011\", \"sku\": \"CHEM-SOLV-K11\", \"warehouse_id\": \"WH-13\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_007",
        "instruction": "Home Essentials requires 10 Ceramic Break Pad Set (AUTO-PAD-B2). Initially, identify United States warehouses equipped with Heavy Equipment Handling. Assess the inventory for this SKU at the first located warehouse, if inadequate, proceed to inspect the next warehouse, organize an order for Home Essentials to be sent to 123 Smart Home, Austin, OK, and dispatch using the most efficient Truck carrier with tracking AUTO-PAD-010.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "country": "United States",
                    "special_capability": "Heavy Equipment Handling"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Home Essentials",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "123 Smart Home, Austin, OK"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "AUTO-PAD-010"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_008",
        "instruction": "Book Nook requests 200 units of 8-bit Microcontroller (ELEC-CHIP-A1) divided between warehouses WH-01 and WH-03. Start by checking the inventory at both locations, form an initial order for 100 units from WH-01 with tracking number CHIP-EAST-100 to 456 Reading Lane, Boston, MA, create a second order for 100 units from WH-03 with tracking number CHIP-WEST-100 to the same destination, and designate different carriers (CARR-014 and CARR-007) for each order to ensure load distribution.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Book Nook",
                    "warehouse_id": "WH-01",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "456 Reading Lane, Boston, MA"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Book Nook",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "456 Reading Lane, Boston, MA"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "CHIP-EAST-100"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-007",
                    "tracking_number": "CHIP-WEST-100"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\"",
                "\"order_id\": \"ORD-0018\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_009",
        "instruction": "Innovate Inc. is in need of specialized equipment: 15 units of Articulated Robotic Arm (TECH-ROBO-N14) and 5 Lithium-Ion Battery Packs (TECH-BATT-Q17). Start by locating warehouses with the capacity to handle heavy equipment, verify the inventory for both products at a suitable warehouse, assemble an order for Innovate Inc to be delivered to 789 Innovation Drive, Cambridge, MA, with tracking number 'INNOV-RAIL-001' and send using Rail carrier 'CARR-008' for the heavy equipment.'INNOV-RAIL-001' and ship with Rail carrier 'CARR-008' for heavy equipment.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Heavy Equipment Handling"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Innovate Inc.",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 15
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 5
                        }
                    ],
                    "shipping_address": "789 Innovation Drive, Cambridge, MA"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Rail"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-008",
                    "tracking_number": "INNOV-RAIL-001"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_010",
        "instruction": "Global Beverages requires 1000 units of Sparkling Mineral Water (BEVG-WATR-S1). Start by identifying suppliers in the Beverages category, then obtain comprehensive performance data for supplier 'SUPP-1018', locate all Sea carriers and pick the one with the highest on-time-delivery percentage, organize an inbound shipment to WH-15 using the chosen carrier scheduled for arrival on 2024-09-01, and confirm that the shipment has been created.'SUPP-1018', find all Sea carriers and select the one with the highest on-time-delivery percentage, create inbound shipment to WH-15 using the chosen carrier for arrival on 2024-09-01, and verify shipment creation.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Beverages"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1018"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Sea"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-012"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1018",
                    "destination_warehouse_id": "WH-15",
                    "carrier_id": "CARR-012",
                    "items": [
                        {
                            "sku": "BEVG-WATR-S1",
                            "quantity": 1000
                        }
                    ],
                    "estimated_arrival_date": "2024-09-01"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\", \"supplier_id\": \"SUP-1018\", \"destination_warehouse_id\": \"WH-15\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_011",
        "instruction": "Coordinate the transfer of 50 Industrial Solvent (CHEM-SOLV-K11) from WH-13 to WH-03. Start by assessing the current inventory at the source warehouse, decrease inventory at WH-13 with the reason 'Internal Transfer to WH-03', generate an inbound shipment record for the internal transfer to WH-03 scheduled to arrive on 2024-07-28, and confirm both inventory adjustment and shipment creation.'Internal Transfer to WH-03', create inbound shipment record for internal transfer to WH-03 arriving 2024-07-28, and verify both inventory adjustment and shipment creation.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-13",
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-13",
                    "sku": "CHEM-SOLV-K11",
                    "quantity_change": -50,
                    "reason": "Internal Transfer to WH-03"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "Internal",
                    "destination_warehouse_id": "WH-03",
                    "carrier_id": "Internal Transfer",
                    "items": [
                        {
                            "sku": "CHEM-SOLV-K11",
                            "quantity": 50
                        }
                    ],
                    "estimated_arrival_date": "2024-07-28"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-13",
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_012",
        "instruction": "Fashion Forward requires 10 Leather Handbags (APRL-BAG-E5) from WH-07 and 20 Cotton Tshirts (APRL-TSHT-O15) from WH-04, United States warehouses. Begin by identifying United States warehouses, inspect inventory for both products at each location until locating warehouses with available stock, generate an order for Fashion Forward to 123 Style Street, Fort Lauderdale, SC, with tracking numbers 'FASHION-AIR-001' and 'FASHION-AIR-002'. Deliver via Air carrier for expedited service. Select the carrier offering the Pharma service level and who has the highest average rating.'FASHION-AIR-002'. Ship via Air carrier for fast delivery. Choose the carrier that supports the Pharma service level and has the highest average rating.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "country": "United States"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "APRL-TSHT-O15"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Fashion Forward",
                    "warehouse_id": "WH-07",
                    "items": [
                        {
                            "sku": "APRL-BAG-E5",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "123 Style Street, Fort Lauderdale, SC"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Fashion Forward",
                    "warehouse_id": "WH-04",
                    "items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 20
                        }
                    ],
                    "shipping_address": "123 Style Street, Fort Lauderdale, SC"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "FASHION-AIR-001"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "FASHION-AIR-002"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\"",
                "\"order_id\": \"ORD-0018\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_013",
        "instruction": "Handle the return of Dining Chair (FURN-CHAIR-M13) from order ORD-0015. The customer returns 1 damaged unit. Begin by retrieving order details, inspect the current inventory at the order's warehouse, add the returned unit citing 'Customer Return' as the reason, promptly adjust the same unit out as damaged goods, and validate the final inventory.'s warehouse, add returned unit with reason 'Customer Return', immediately adjust same unit out as damaged goods, and verify final inventory.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0015"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13",
                    "quantity_change": 1,
                    "reason": "Customer Return"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13",
                    "quantity_change": -1,
                    "reason": "Damaged Goods"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0013\", \"sku\": \"FURN-CHAIR-M13\"}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_014",
        "instruction": "Gamerz Inc. requires 5 Solar Panel 450W (ELEC-SMART-W23). Initiate the process by locating United States warehouses, checking inventory at each warehouse in order until a stock-ready location is found, generate an order for Gamerz Inc to 1337 Gamer Way, Austin, OK, with the tracking number 'GAMER-FAST-005' and dispatch using carrier 'CARR-006'.'GAMER-FAST-005' and ship with carrier 'CARR-006'.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "country": "United States"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gamerz Inc.",
                    "warehouse_id": "WH-02",
                    "items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 5
                        }
                    ],
                    "shipping_address": "1337 Gamer Way, Austin, OK"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "GAMER-FAST-005"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_015",
        "instruction": "The Daily Grind requires 500 8-Bit Microcontrollers (ELEC-CHIP-A1) divided between WH-01 and WH-03. Start by reviewing inventory at both warehouses, formulate the first order for 250 units from WH-01 to 789 Cafe Ave, Portland, OR (tracking number: DAILY-1-250), initiate the second order for 250 units from WH-03 to the same address (tracking number: DAILY-2-250), and synchronize delivery scheduling. Use the carrier that supports Next Day Air delivery service.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "The Daily Grind",
                    "warehouse_id": "WH-01",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 250
                        }
                    ],
                    "shipping_address": "789 Cafe Ave, Portland, OR"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "The Daily Grind",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 250
                        }
                    ],
                    "shipping_address": "789 Cafe Ave, Portland, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "DAILY-1-250"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "DAILY-2-250"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\"",
                "\"order_id\": \"ORD-0018\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_016",
        "instruction": "BuildIt Better requires 10 Power Drills (TECH-ROBO-N14) and 2 Circular Saws (MATR-COTT-R18). Start by locating United States warehouses and examining the inventory for both items at each site until one is found with both items available. Prepare orders for BuildIt Better to 456 Construction Way, Denver, CO, (tracking numbers BUILD-TOOLS-012 and BUILD-TOOLS-013) and dispatch via Truck carrier (CARR-014) for delivery to the construction site.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "country": "United States"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "MATR-COTT-R18"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "sku": "MATR-COTT-R18"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "MATR-COTT-R18"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "MATR-COTT-R18"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "BuildIt Better",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "456 Construction Way, Denver, CO"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "BuildIt Better",
                    "warehouse_id": "WH-04",
                    "items": [
                        {
                            "sku": "MATR-COTT-R18",
                            "quantity": 2
                        }
                    ],
                    "shipping_address": "456 Construction Way, Denver, CO"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "BUILD-TOOLS-012"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "BUILD-TOOLS-013"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\"",
                "\"order_id\": \"ORD-0018\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_017",
        "instruction": "The new hospital, 'Mercy West', needs an urgent setup order: 150 units of Influenza Vaccine (PHRM-VACC-D4) and 75 units of Oncology Drug A (PHRM-DRUG-S19). Begin by identifying a warehouse with both 'Cold Chain (2-8\u00b0C)' and 'Pharmaceutical Handling' capabilities. Review inventory for both items at the chosen warehouse (WH-06). Formulate the outbound order for 'Mercy West' to '987 Health Parkway, Phoenix, AZ'. Select the top 'Air' carrier that accommodates the Pharma service level. Dispatch the order with this carrier and assign the tracking number 'CRITICAL-CARE-987'. Lastly, confirm the updated available inventory for both SKUs in the warehouse.'Mercy West', requires a critical setup order: 150 units of Influenza Vaccine (PHRM-VACC-D4) and 75 units of Oncology Drug A (PHRM-DRUG-S19). First, find a warehouse with both 'Cold Chain (2-8\u00b0C)' and 'Pharmaceutical Handling' capabilities. Check inventory for both items at the identified warehouse (WH-06). Create the outbound order for 'Mercy West' to '987 Health Parkway, Phoenix, AZ'. Find the highest-rated 'Air' carrier that supports the Pharma service level. Ship the order with this carrier and assign the tracking number 'CRITICAL-CARE-987'. Finally, verify the new available inventory for both SKUs in the warehouse.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capabilities": [
                        "Cold Chain (2-8°C)",
                        "Pharmaceutical Handling"
                    ]
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Mercy West",
                    "warehouse_id": "WH-06",
                    "items": [
                        {
                            "sku": "PHRM-VACC-D4",
                            "quantity": 150
                        },
                        {
                            "sku": "PHRM-DRUG-S19",
                            "quantity": 75
                        }
                    ],
                    "shipping_address": "987 Health Parkway, Phoenix, AZ"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "CRITICAL-CARE-987"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-DRUG-S19"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0004\"}",
                "{\"inventory_id\": \"INV-0019\"}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_018",
        "instruction": "Relocate 50 Cotton Tshirts (APRL-TSHT-O15) from WH-04 to WH-07 to achieve regional inventory balance. Begin by checking inventory at the source warehouse, adjust the inventory at WH-04 with the reason for transfer, record the internal shipment for the transfer arriving on 2024-07-31, verify the inventory change, and confirm the shipment creation.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "APRL-TSHT-O15"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "APRL-TSHT-O15",
                    "quantity_change": -50,
                    "reason": "Internal Transfer to WH-07"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "Internal",
                    "destination_warehouse_id": "WH-07",
                    "carrier_id": "Internal Transfer",
                    "items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 50
                        }
                    ],
                    "estimated_arrival_date": "2024-07-31"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "APRL-TSHT-O15"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0015\", \"sku\": \"APRL-TSHT-O15\", \"warehouse_id\": \"WH-04\"}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_019",
        "instruction": "Process the return of Fresh Cut Roses (FOOD-FLWR-X24) from order ORD-0011. The customer is returning 1 damaged unit. Begin by obtaining order details to pinpoint the warehouse, check the current inventory, add the returned unit with the reason 'Customer Return', write off the same unit as damaged, and verify the final inventory level.'Customer Return', write off same unit as damaged, and verify final inventory level.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0011"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "sku": "FOOD-FLWR-X24"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "sku": "FOOD-FLWR-X24",
                    "quantity_change": 1,
                    "reason": "Customer Return"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "sku": "FOOD-FLWR-X24",
                    "quantity_change": -1,
                    "reason": "Damaged Goods"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "sku": "FOOD-FLWR-X24"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0024\", \"sku\": \"FOOD-FLWR-X24\", \"warehouse_id\": \"WH-10\"}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_020",
        "instruction": "Art Supplies Co. requests 100 Frozen Tuna Loin (FOOD-FISH-H8) from a United States warehouse. Start by identifying all United States warehouses with Perishables Handling capability, sequentially verify inventory at each location, issue an order (tracking number: 'ART-AIR-100') from the warehouse with sufficient stock to 123 Art Street, Portland, OR, and coordinate Air shipping with CARR-006 for art supplies.'ART-AIR-100') from warehouse with adequate stock to 123 Art Street, Portland, OR, and arrange Air shipping with CARR-006 for art supplies.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "country": "United States",
                    "special_capability": "Perishables Handling"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "sku": "FOOD-FISH-H8"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Art Supplies Co.",
                    "warehouse_id": "WH-10",
                    "items": [
                        {
                            "sku": "FOOD-FISH-H8",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "123 Art Street, Portland, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "ART-AIR-100"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_021",
        "instruction": "Healthy Living needs fresh produce: 50 Frozen Tuna (FOOD-FISH-H8) and 100 Fresh Cut Roses (FOOD-FLWR-X24) with cold chain requirements. Begin by locating Cold Chain (0-4\u00b0C) equipped warehouses, check inventory for both items at a suitable warehouse, generate an order (tracking number: FRESH-COLD-150) for Healthy Living to 789 Wellness Way, San Diego, OR, and arrange refrigerated transport via carrier CARR-014.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Cold Chain (0-4°C)"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "sku": "FOOD-FISH-H8"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "sku": "FOOD-FLWR-X24"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Healthy Living",
                    "warehouse_id": "WH-10",
                    "items": [
                        {
                            "sku": "FOOD-FISH-H8",
                            "quantity": 50
                        },
                        {
                            "sku": "FOOD-FLWR-X24",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "789 Wellness Way, San Diego, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "FRESH-COLD-150"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_022",
        "instruction": "Relocate 20 Diamond Core Drill Bits (HEVY-DRIL-I9) from WH-11 to WH-03 for demand balancing. First, obtain warehouse information, then verify the current stock at the source, decrease inventory at WH-11 with the correct transfer reason, create an internal shipment for transfer arriving 2024-07-30, and confirm both inventory adjustment and shipment record.",
        "actions": [
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-11",
                    "sku": "HEVY-DRIL-I9"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-11",
                    "sku": "HEVY-DRIL-I9",
                    "quantity_change": -20,
                    "reason": "Internal Transfer to WH-03"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "Internal",
                    "destination_warehouse_id": "WH-03",
                    "carrier_id": "Internal Transfer",
                    "items": [
                        {
                            "sku": "HEVY-DRIL-I9",
                            "quantity": 20
                        }
                    ],
                    "estimated_arrival_date": "2024-07-30"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\", \"supplier_id\": \"Internal\", \"destination_warehouse_id\": \"WH-03\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_023",
        "instruction": "Bookworm wants 50 units of Ceramic Floor Tile (BLDG-TILE-J10) from the highest stock location. Begin by checking inventory across all warehouses, identify the location with the most stock, ensure adequate inventory at that warehouse, create an order to 123 Reading Rainbow, San Francisco, OR, and ship via standard carrier with tracking number BOOK-WORM-050.",
        "actions": [
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "BLDG-TILE-J10"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "sku": "BLDG-TILE-J10"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Bookworm",
                    "warehouse_id": "WH-12",
                    "items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "123 Reading Rainbow, San Francisco, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Parcel"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-014"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "BOOK-WORM-050"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_024",
        "instruction": "Handle Luxury Watch (LUX-WATCH-L12) arrival in high-security shipment SHIP-0014 at WH-07 with 10 units, then fulfill premium order ORD-0010. Start by obtaining shipment details, receive the high-value shipment, verify secure inventory update, check priority order status, and ship with premium Air carrier tracking EK-CARGO-457.",
        "actions": [
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0014",
                    "items_received": [
                        {
                            "sku": "LUX-WATCH-L12",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "LUX-WATCH-L12"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0010",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "EK-CARGO-457"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0010\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_025",
        "instruction": "Manage Ceramic Floor Tile (BLDG-TILE-J10) return from order ORD-0013. Customer returns 1 defective unit. Start by obtaining order information to identify the warehouse, check current inventory levels, add the returned unit with reason 'Customer Return', immediately write off as defective, and verify inventory adjustment.'Customer Return', immediately write off as defective, and verify inventory adjustment.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0013"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "sku": "BLDG-TILE-J10"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "sku": "BLDG-TILE-J10",
                    "quantity_change": 1,
                    "reason": "Customer Return"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "sku": "BLDG-TILE-J10",
                    "quantity_change": -1,
                    "reason": "Damaged Goods"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "sku": "BLDG-TILE-J10"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0010\", \"sku\": \"BLDG-TILE-J10\", \"warehouse_id\": \"WH-12\"}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_026",
        "instruction": "Handle the request for 200 units of Oncology Drug A (PHRM-DRUG-S19) needed by The Green Thumb from a United States warehouse. Begin by identifying all United States warehouses with Pharmaceutical Handling capabilities, systematically assess inventory at each site, generate an order from the warehouse with enough quantity for delivery to 456 Garden Lane, Austin, OK, and coordinate Truck delivery with carrier 'CARR-014' and tracking number ONCO-DRUG-200.'CARR-014' and tracking number ONCO-DRUG-200.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "country": "United States",
                    "special_capability": "Pharmaceutical Handling"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-16",
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "The Green Thumb",
                    "warehouse_id": "WH-06",
                    "items": [
                        {
                            "sku": "PHRM-DRUG-S19",
                            "quantity": 200
                        }
                    ],
                    "shipping_address": "456 Garden Lane, Austin, OK"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "ONCO-DRUG-200"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_027",
        "instruction": "A customer 'Future Auto' needs 10 'Articulated Robotic Arm' (TECH-ROBO-N14) and 50 'Lithium-Ion Battery Pack' (TECH-BATT-Q17). Identify a warehouse with 'Heavy Equipment Handling' and 'VMI (Vendor Managed Inventory)' capabilities. Verify inventory for both SKUs at 'Midwest Parts Warehouse' (WH-03). Set up the order for 'Future Auto' to be shipped to '1 Robot Way, Detroit, MI'. Ship using 'DeutschLogistik' (CARR-003) via 'Rail' transport with tracking 'AUTO-ROBOT-RAIL-1'.'Future Auto' needs 10 'Articulated Robotic Arm' (TECH-ROBO-N14) and 50 'Lithium-Ion Battery Pack' (TECH-BATT-Q17). Find a warehouse that has 'Heavy Equipment Handling' and 'VMI (Vendor Managed Inventory)' capabilities. Check inventory for both SKUs at 'Midwest Parts Warehouse' (WH-03). Create the order for 'Future Auto' to '1 Robot Way, Detroit, MI'. Ship via 'DeutschLogistik' (CARR-003) using 'Rail' transport with tracking 'AUTO-ROBOT-RAIL-1'.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capabilities": [
                        "Heavy Equipment Handling",
                        "VMI (Vendor Managed Inventory)"
                    ]
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Future Auto",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 10
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "1 Robot Way, Detroit, MI"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-003"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-003",
                    "tracking_number": "AUTO-ROBOT-RAIL-1"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_028",
        "instruction": "The Toy Box is requesting 1000 units of Malbec Wine (BEVG-WINE-P16). Identify a warehouse that provides 'Beverage Distribution', check stock levels, and initiate an order for 1000 units from that location to 789 Playtime Ave, Orlando, SC (tracking number: TOY-EAST-1000) using 'Air' carrier 'CARR-014' and manage deliveries for the toy store.'Beverage Distribution', check inventory, and create order for 1000 units from that warehouse to 789 Playtime Ave, Orlando, SC (tracking number: TOY-EAST-1000) with 'Air' carrier 'CARR-014' and coordinate deliveries for toy store.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "sku": "BEVG-WINE-P16"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "The Toy Box",
                    "warehouse_id": "WH-15",
                    "items": [
                        {
                            "sku": "BEVG-WINE-P16",
                            "quantity": 1000
                        }
                    ],
                    "shipping_address": "789 Playtime Ave, Orlando, SC"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "TOY-EAST-1000"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_029",
        "instruction": "The Cellar wine shop requires climate-controlled delivery for 100 Red Wine (BEVG-WINE-P16). Start by finding Temperature Controlled (10-15\u00b0C) warehouses, confirm wine stock at an appropriate location, initiate an order for The Cellar to 123 Vino Way, Napa, OR, (tracking number: WINE-TEMP-100) and organize temperature-controlled, Next Day Air shipping.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Temperature Control (10-15°C)"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "sku": "BEVG-WINE-P16"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "The Cellar",
                    "warehouse_id": "WH-15",
                    "items": [
                        {
                            "sku": "BEVG-WINE-P16",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "123 Vino Way, Napa, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "WINE-TEMP-100"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_030",
        "instruction": "Coordinate a critical hazmat shipment for ChemCorp that requires 100 Industrial Solvent (CHEM-SOLV-K11). First, locate Chemical suppliers and assess their performance data, identify hazmat certified warehouses in the United States, arrange an inbound shipment from the best supplier to the hazmat warehouse using the leading (highest on-time-delivery percentage) Sea carrier for arrival on 2024-08-15, confirm hazmat compliance, verify warehouse capabilities in detail, and ensure that all safety protocols are adhered to.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Chemicals"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1013"
                },
            },
            {
                "name": "FindWarehouses",
                "arguments": {
                    "country": "United States",
                    "special_capability": "Hazmat Certified (Classes 3, 6.1, 9)"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Sea"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-012"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "destination_warehouse_id": "WH-13",
                    "carrier_id": "CARR-012",
                    "items": [
                        {
                            "sku": "CHEM-SOLV-K11",
                            "quantity": 100
                        }
                    ],
                    "estimated_arrival_date": "2024-08-15"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\", \"supplier_id\": \"SUP-1013\", \"destination_warehouse_id\": \"WH-13\", \"carrier_id\": \"CARR-012\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_031",
        "instruction": "Luxury Retail Group is placing a high-profile order for 50 Leather Handbags (APRL-BAG-E5) and 100 Automatic Watch Movements (LUX-WATCH-L12). Begin by locating High-Value Cage warehouses, and select the one with the lower usage percentage. Next, verify the stock for both luxury products at the secure facility, prepare the order for Luxury Retail Group to 1 Rodeo Drive, Beverly Hills, OR, find Air carriers, dispatch using carrier 'CARR-006' with tracking EK-CARGO-456, and supply a comprehensive order summary.'CARR-006' using tracking EK-CARGO-456, and provide complete order details.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "High-Value Cage"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "LUX-WATCH-L12"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Luxury Retail Group",
                    "warehouse_id": "WH-07",
                    "items": [
                        {
                            "sku": "APRL-BAG-E5",
                            "quantity": 50
                        },
                        {
                            "sku": "LUX-WATCH-L12",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "1 Rodeo Drive, Beverly Hills, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-006"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "EK-CARGO-456"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"status\": \"Shipped\", \"warehouse_id\": \"WH-07\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_032",
        "instruction": "Assess earthquake damage and recovery at the Midwest Parts Warehouse (WH-03). Inventory impact shows 10% of AUTO-PAD-B2 and 5% of AUTO-GLAS-U21 damaged. Begin by confirming current stock levels for both products at WH-03, calculate the affected quantities (80 B2, 10 U21), update inventory for both with reason 'Damaged in Natural Disaster', check aggregate inventory across all warehouses for both SKUs, and if any SKU falls below 1000 total, locate an Automotive supplier with the shortest standard lead time, arrange an emergency consignment of 500 each low SKU to San Diego (WH-01) via SwiftDelivery to arrive on 2024-08-10, and verify that the emergency shipment has been arranged.'Damaged in Natural Disaster', check total inventory across all warehouses for both SKUs, if any SKU below 1000 total, find Automotive supplier with the lowest standard lead time, create emergency shipment of 500 each low SKU to San Diego (WH-01) via SwiftDelivery arriving 2024-08-10, and verify emergency shipment creation.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2",
                    "quantity_change": -80,
                    "reason": "Damaged in Natural Disaster"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-GLAS-U21"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-GLAS-U21",
                    "quantity_change": -10,
                    "reason": "Damaged in Natural Disaster"
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
                    "sku": "AUTO-GLAS-U21"
                },
            },
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Automotive"
                    ]
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1023",
                    "destination_warehouse_id": "WH-01",
                    "carrier_id": "CARR-007",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 500
                        },
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 500
                        }
                    ],
                    "estimated_arrival_date": "2024-08-10"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\", \"supplier_id\": \"SUP-1023\", \"destination_warehouse_id\": \"WH-01\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_033",
        "instruction": "Prepare 8-Bit Microcontroller (ELEC-CHIP-A1) stock for a flash sale by consolidating inventory. Start by checking total inventory across all locations, identify every warehouse holding this SKU, transfer all units from other warehouses to San Diego (WH-01) with the reason 'Internal Transfer to WH-01', document internal shipments for the transfers arriving on 2024-07-26 accordingly. Process the incoming shipment. Confirm inventory adjustments and shipment records, and verify consolidated stock at WH-01.'Internal Transfer to WH-01', create internal shipment records for transfers arriving on 2024-07-26 respectively. Receive the shipment. Verify inventory adjustments and shipment creations, and confirm consolidated inventory at WH-01.",
        "actions": [
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "ELEC-CHIP-A1",
                    "quantity_change": -8000,
                    "reason": "Internal Transfer to WH-01"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "Internal",
                    "destination_warehouse_id": "WH-01",
                    "carrier_id": "Internal Transfer",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 8000
                        }
                    ],
                    "estimated_arrival_date": "2024-07-26"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0031",
                    "items_received": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 8000
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                }
            }
        ],
        "outputs": [
                "\"inventory_id\": \"INV-0001\", \"sku\": \"ELEC-CHIP-A1\", \"warehouse_id\": \"WH-01\", \"quantity_on_hand\": 16200}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_034",
        "instruction": "The customer 'AutoRestore' has returned 15 'Automatic Watch Movement' (LUX-WATCH-L12) from order ORD-0008 due to incorrect parts. The items remain intact. First, retrieve the order details to verify the originating warehouse (WH-07). Update the inventory at WH-07, reintegrating the 15 sets with reason 'Customer Return - Resalable'. Afterwards, create a new shipment for the correct item, 'Leather Handbag' (APRL-BAG-E5), for 15 units to the same customer at '555 Repair Lane, Milwaukee, WI'. Dispatch it via 'Global Parcel Service' (CARR-014) with tracking 'CORRECT-PART-555'.'AutoRestore', has returned 15 'Automatic Watch Movement' (LUX-WATCH-L12) from order ORD-0008 due to a mismatch. The items are undamaged. First, get the order details to confirm the origin warehouse (WH-07). Adjust the inventory at WH-07, adding the 15 sets back with reason 'Customer Return - Resalable'. Then, create a new outbound order for the correct part, 'Leather Handbag' (APRL-BAG-E5), for 15 units to the same customer at '555 Repair Lane, Milwaukee, WI'. Ship it via 'Global Parcel Service' (CARR-014) with tracking 'CORRECT-PART-555'.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0008"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "LUX-WATCH-L12"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "LUX-WATCH-L12",
                    "quantity_change": 15,
                    "reason": "Customer Return - Resalable"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "AutoRestore",
                    "warehouse_id": "WH-07",
                    "items": [
                        {
                            "sku": "APRL-BAG-E5",
                            "quantity": 15
                        }
                    ],
                    "shipping_address": "555 Repair Lane, Milwaukee, WI"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-014"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "CORRECT-PART-555"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_035",
        "instruction": "VIP Global Tech urgently requires 2 Automatic Watches (LUX-WATCH-L12) with premium servicing. Start by locating High-Value Cage and 24/7 Security Detail warehouses for secure storage, assess availability at the secure location, organize a VIP order for Global Tech to 1 Quantum Way, Palo Alto, OR, find the top-rated Air carrier service with a High-Value level, dispatch using the premium carrier with tracking EK-VIP-789, and issue a complete confirmation of the order.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capabilities": [
                        "High-Value Cage",
                        "24/7 Security Detail"
                    ]
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "LUX-WATCH-L12"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Global Tech",
                    "warehouse_id": "WH-07",
                    "items": [
                        {
                            "sku": "LUX-WATCH-L12",
                            "quantity": 2
                        }
                    ],
                    "shipping_address": "1 Quantum Way, Palo Alto, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-006"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "EK-VIP-789"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"status\": \"Shipped\", \"warehouse_id\": \"WH-07\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_036",
        "instruction": "Handle Global Construction emergency order for heavy equipment: 35 Diamond Core Drill Bits (HEVY-DRIL-I9) and 180 Automotive Windshields (AUTO-GLAS-U21). Begin by locating Heavy Equipment and Automotive suppliers and assessing their performance ratings, confirm inventory for drill bits at WH-11 and windshields at WH-03, formulate separate orders for each item to 123 Construction Site, Denver, CO, identify Rail carrier (CARR-008) for drill bits and Truck carrier (CARR-014) for windshields, dispatch drill bits via Rail with tracking CN-RAIL-789 and windshields via Truck with tracking Global Parcel Service-TRUCK-101, ensure both shipments are created successfully.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Heavy Equipment"
                    ]
                },
            },
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Automotive"
                    ]
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-11",
                    "sku": "HEVY-DRIL-I9"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-GLAS-U21"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Global Construction",
                    "warehouse_id": "WH-11",
                    "items": [
                        {
                            "sku": "HEVY-DRIL-I9",
                            "quantity": 35
                        }
                    ],
                    "shipping_address": "123 Construction Site, Denver, CO"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Global Construction",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 180
                        }
                    ],
                    "shipping_address": "123 Construction Site, Denver, CO"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Rail"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-008",
                    "tracking_number": "CN-RAIL-789"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "Global Parcel Service-TRUCK-101"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"new_status\": \"Shipped\"",
                "\"order_id\": \"ORD-0018\", \"new_status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_037",
        "instruction": "Coordinate the establishment of a new supply chain for Global Construction's 10 Heavy-Duty Excavators (HEVY-EXCV-T5). Start by finding Heavy Equipment suppliers and evaluating their performance metrics, select the top supplier and gather detailed information, locate all Rail carriers and choose CARR-008, organize a comprehensive inbound shipment to WH-11 using the most suitable Rail carrier for arrival 2024-09-15, verify shipment setup, obtain full carrier service details, and confirm the establishment of the supply chain.'s 10 Heavy-Duty Excavators (HEVY-EXCV-T5). First find Heavy Equipment suppliers and evaluate their performance metrics, select top supplier and get detailed information, find all Rail carriers and select CARR-008, create comprehensive inbound shipment to WH-11 using optimal Rail carrier for arrival 2024-09-15, verify shipment setup, get complete carrier service details, and confirm supply chain establishment.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Heavy Equipment"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1011"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Rail"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-008"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1011",
                    "destination_warehouse_id": "WH-11",
                    "carrier_id": "CARR-008",
                    "items": [
                        {
                            "sku": "HEVY-EXCV-T5",
                            "quantity": 10
                        }
                    ],
                    "estimated_arrival_date": "2024-09-15"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\", \"supplier_id\": \"SUP-1011\", \"destination_warehouse_id\": \"WH-11\", \"carrier_id\": \"CARR-008\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_038",
        "instruction": "Perform a comprehensive inventory audit and discrepancy correction for SHIP-0018 containing Argentinian Malbec Wine (BEVG-WINE-P16). The shipment expected 900 cases but only 850 were received at WH-15. Begin by obtaining complete shipment details, record the actual quantity (850 cases), inspect updated inventory levels, write off 50 missing cases citing 'Shipping Discrepancy' as the reason, confirm that adjustment is applied, acquire final inventory confirmation, and document the entire audit trail.'Shipping Discrepancy', verify adjustment applied, get final inventory confirmation, and document complete audit trail.",
        "actions": [
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0018"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0018",
                    "items_received": [
                        {
                            "sku": "BEVG-WINE-P16",
                            "quantity": 850
                        }
                    ]
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "sku": "BEVG-WINE-P16"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "sku": "BEVG-WINE-P16",
                    "quantity_change": -50,
                    "reason": "Shipping Discrepancy"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "sku": "BEVG-WINE-P16"
                }
            }
        ],
        "outputs": [
                "\"warehouse_id\": \"WH-15\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_039",
        "instruction": "Manage a multi-phase pharmaceutical distribution setup for critical medicines. The hospital client requires temperature-controlled distribution of 500 units of Influenza Vaccine (PHRM-VACC-D4) and 200 Oncology Drug A (PHRM-DRUG-S19). Initially, identify the pharmaceutical supplier with the shortest standard lead time in days, gather detailed supplier performance data, locate the Cold Chain (2-8\u00b0C) warehouse with the fewest number of docks, confirm inventory availability for both medications at an appropriate facility, arrange a priority medical order for Metro General Hospital to 456 Medical Center Dr, Milwaukee, WI, select the specialized medical carrier (CARR-006), and coordinate expedited cold chain delivery with tracking MED-CRITICAL-001.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Pharmaceuticals"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1006"
                },
            },
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Cold Chain (2-8°C)"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Metro General Hospital",
                    "warehouse_id": "WH-06",
                    "items": [
                        {
                            "sku": "PHRM-VACC-D4",
                            "quantity": 500
                        },
                        {
                            "sku": "PHRM-DRUG-S19",
                            "quantity": 200
                        }
                    ],
                    "shipping_address": "456 Medical Center Dr, Milwaukee, WI"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-006"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "MED-CRITICAL-001"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_040",
        "instruction": "Orchestrate complete supply chain optimization for Tech Innovation Hub requiring specialized components: 25 Lithium-Ion Batteries (TECH-BATT-Q17), 15 Robotic Arms (TECH-ROBO-N14), and 50 8-Bit Microcontrollers (ELEC-CHIP-A1). Begin by locating Electronics suppliers and evaluating their high-tech capabilities, acquire detailed supplier performance and specialization data. Select the supplier with the highest performance rating. Identify Heavy Equipment Handling warehouses for secure component storage, confirm availability for all three components at the secure facility, prepare a comprehensive order for Tech Innovation Hub to 789 Silicon Valley Blvd, San Jose, OR, evaluate Air carriers for expedited tech shipping, dispatch with carrier 'CARR-006' using tracking TECH-INNOVATION-001, and provide full delivery confirmation along with security protocols.'CARR-006' using tracking TECH-INNOVATION-001, and provide complete delivery confirmation with security protocols.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Electronics"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1002"
                },
            },
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Heavy Equipment Handling"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Tech Innovation Hub",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 25
                        },
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 15
                        },
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "789 Silicon Valley Blvd, San Jose, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-006"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "TECH-INNOVATION-001"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_041",
        "instruction": "Handle the establishment of a luxury goods distribution network for Premium Fashion Boutique, requiring high-security processing of 30 Leather Handbags (APRL-BAG-E5), and 20 Luxury Watches (LUX-WATCH-L12). Initially, secure luxury goods suppliers and examine their security protocols, obtaining comprehensive supplier information, including certifications. Utilize supplier 'SUP-1007'. Locate warehouses with High-Value Cage and 24/7 Security Detail capabilities that can manage jewelry, check the secure inventory for all luxury items, and institute a high-priority order for Premium Fashion Boutique to 1 Luxury Lane, Beverly Hills, OR. Assess specialized Air carriers for valuable cargo transport, opt for carrier 'CARR-006', and coordinate the secure shipping with tracking LUXURY-SECURE-001. Present order details.'SUP-1007'. Find High-Value Cage and 24/7 Security Detail warehouses with jewelry handling capabilities, verify secure inventory for all luxury items, create high-priority order for Premium Fashion Boutique to 1 Luxury Lane, Beverly Hills, OR, evaluate specialized Air carriers for valuable cargo transport, select carrier 'CARR-006', arrange secure shipping with tracking LUXURY-SECURE-001. Display order information",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Luxury Goods"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1007"
                },
            },
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capabilities": [
                        "High-Value Cage",
                        "24/7 Security Detail"
                    ]
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "LUX-WATCH-L12"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Premium Fashion Boutique",
                    "warehouse_id": "WH-07",
                    "items": [
                        {
                            "sku": "APRL-BAG-E5",
                            "quantity": 30
                        },
                        {
                            "sku": "LUX-WATCH-L12",
                            "quantity": 20
                        }
                    ],
                    "shipping_address": "1 Luxury Lane, Beverly Hills, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-006"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "LUXURY-SECURE-001"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_042",
        "instruction": "Coordinate the complex international food distribution for Gourmet Restaurant Chain, necessitating temperature-controlled logistics for 200 units of Coffee Beans (FOOD-COFF-C3), and 150 Olive Oil bottles (FOOD-OLIV-V22). Begin by identifying Groceries and Beverage suppliers specializing in gourmet items, evaluating their cold chain capabilities, and obtaining detailed supplier certifications and performance data. Locate warehouses equipped with Temperature Controlled and Pest Control capabilities, confirm fresh inventory availability for all gourmet items, and organize a priority order for Gourmet Restaurant Chain to 456 Culinary Ave, New York, NY. Investigate specialized Truck food carriers with temperature monitoring, finalize carrier 'CARR-014', and arrange refrigerated transport with tracking GOURMET-FRESH-001, ensuring complete cold chain integrity documentation.'CARR-014', arrange refrigerated transport with tracking GOURMET-FRESH-001, and confirm complete cold chain integrity documentation.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Groceries",
                        "Beverages"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1005"
                },
            },
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capabilities": [
                        "Temperature Control (Ambient)",
                        "Pest Control Program"
                    ]
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-05",
                    "sku": "FOOD-COFF-C3"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-05",
                    "sku": "FOOD-OLIV-V22"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Gourmet Restaurant Chain",
                    "warehouse_id": "WH-05",
                    "items": [
                        {
                            "sku": "FOOD-COFF-C3",
                            "quantity": 200
                        },
                        {
                            "sku": "FOOD-OLIV-V22",
                            "quantity": 150
                        }
                    ],
                    "shipping_address": "456 Culinary Ave, New York, NY"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-014"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "GOURMET-FRESH-001"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_043",
        "instruction": "Manoeuvre a comprehensive Beverage supply chain for Industrial Safety Corp, necessitating specialized handling of 75 Cork Stoppers (MATR-CORK-T20), and 50 Wine Bottles (BEVG-WINE-P16). Start by identifying Groceries and Beverage suppliers specializing in alcohol supply, obtaining detailed supplier credentials and performance ratings. Identify warehouses with Temperature Controlled capabilities and validate inventory availability for all items. Establish an order for Industrial Safety Corp to 789 Safety Blvd, Dallas, OK, assess specialized Truck food carriers with temperature monitoring, finalize carrier 'CARR-014', and coordinate shipping with tracking SAFETY-WINE-001.'CARR-014', arrange shipping with tracking SAFETY-WINE-001.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Groceries",
                        "Beverages"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1005"
                },
            },
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capabilities": [
                        "Temperature Control (10-15°C)"
                    ]
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "sku": "MATR-CORK-T20"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "sku": "BEVG-WINE-P16"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Industrial Safety Corp",
                    "warehouse_id": "WH-15",
                    "items": [
                        {
                            "sku": "MATR-CORK-T20",
                            "quantity": 75
                        },
                        {
                            "sku": "BEVG-WINE-P16",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "789 Safety Blvd, Dallas, OK"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-014"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "SAFETY-WINE-001"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_044",
        "instruction": "Manage a multi-tier automotive parts distribution for Premium Auto Dealership, necessitating 40 Ceramic Brake Pad Sets (AUTO-PAD-B2), and 25 Automotive Windshields (AUTO-GLAS-U21). Initiate by locating Automotive suppliers and assessing their specialization in performance parts, acquiring comprehensive supplier capabilities and quality certifications. Opt for the supplier with the highest performance rating. Identify suitable warehouses for Heavy Equipment Handling with adequate space, validate inventory for all performance parts at a suitable facility, and establish a high-priority automotive order for Premium Auto Dealership to 123 Auto Mile, Detroit, MI. Explore Truck carriers specializing in automotive transport, examine carrier automotive handling experience, finalize carrier 'CARR-014', coordinate specialized automotive shipping with tracking AUTO-PREMIUM-001, and furnish complete automotive parts delivery confirmation with handling specifications.'CARR-014', arrange specialized automotive shipping with tracking AUTO-PREMIUM-001, and provide complete automotive parts delivery confirmation with handling specifications.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Automotive"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1003"
                },
            },
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Heavy Equipment Handling"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-GLAS-U21"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Premium Auto Dealership",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 40
                        },
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 25
                        }
                    ],
                    "shipping_address": "123 Auto Mile, Detroit, MI"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-014"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "AUTO-PREMIUM-001"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_045",
        "instruction": "Direct advanced electronics distribution for Research Laboratory, necessitating the handling of 20 8-Bit Microcontrollers (ELEC-CHIP-A1), 15 Lithium-Ion Batteries (TECH-BATT-Q17), and 10 Robotic Arms (TECH-ROBO-N14). Commence by locating Electronics and Components suppliers and acquiring detailed supplier certifications, identify warehouses capable of handling heavy equipment, confirm inventory availability for all laboratory equipment at a suitable facility, and organize a critical research order for Research Laboratory to 456 Science Park, Boston, MA. Employ carrier 'CARR-006' and coordinate specialized scientific shipping with tracking RESEARCH-LAB-001.'CARR-006', arrange specialized scientific shipping with tracking RESEARCH-LAB-001.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Electronics",
                        "Components"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1001"
                },
            },
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Heavy Equipment Handling"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Research Laboratory",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 20
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 15
                        },
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "456 Science Park, Boston, MA"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-006"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "RESEARCH-LAB-001"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_046",
        "instruction": "Handle a critical 'Hazmat' shipment of 100 units of 'Industrial Solvent' (CHEM-SOLV-K11) required for a client, 'ChemCorp'. Locate a supplier dealing with this product category. Next, identify a warehouse that possesses 'Hazmat Certified' facilities within the United States. Lastly, arrange an inbound shipment record for the items from the supplier to the hazmat warehouse, set to arrive on '2025-08-15'. Employ the top-rated 'Sea' carrier (highest performance rating, then alphabetical name for ties). Confirm the shipment particulars.'Hazmat' shipment of 100 units of 'Industrial Solvent' (CHEM-SOLV-K11) is needed for a client, 'ChemCorp'. Find a supplier for this product category. Then, find a warehouse with 'Hazmat Certified' capabilities in the United States. Finally, create an inbound shipment record for the items from the supplier to the hazmat warehouse, expected to arrive on '2025-08-15'. Use the best-rated 'Sea' carrier (highest performance rating, then alphabetical name for ties). Confirm the shipment details.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Chemicals"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1013"
                },
            },
            {
                "name": "FindWarehouses",
                "arguments": {
                    "country": "United States",
                    "special_capability": "Hazmat Certified (Classes 3, 6.1, 9)"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Sea"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-012"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "destination_warehouse_id": "WH-13",
                    "carrier_id": "CARR-012",
                    "items": [
                        {
                            "sku": "CHEM-SOLV-K11",
                            "quantity": 100
                        }
                    ],
                    "estimated_arrival_date": "2025-08-15"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_047",
        "instruction": "Coordinate a major order for a significant customer, 'Luxury Retail Group', requiring 50 'Leather Handbag' (APRL-BAG-E5) and 100 'Automatic Watch Movement' (LUX-WATCH-L12). Both items are high-value. Locate a warehouse with a 'High-Value Cage' capability. Verify stock levels for both products. Should inventory suffice, generate an order for 'Luxury Retail Group', shipping to '1 Rodeo Drive, Beverly Hills, OR', using the leading 'Air' carrier (highest on-time-delivery percentage, then alphabetical name for ties). Apply tracking number EK-CARGO-456 and record the final order ID.'Luxury Retail Group', wants to place a large order for 50 'Leather Handbag' (APRL-BAG-E5) and 100 'Automatic Watch Movement' (LUX-WATCH-L12). Both are high-value. Find a warehouse with 'High-Value Cage' capability. Check if it has enough stock for both items. If stock is sufficient, create the order for 'Luxury Retail Group' shipping to '1 Rodeo Drive, Beverly Hills, OR', ship it with the best 'Air' carrier (highest on-time-delivery percentage, then alphabetical name for ties). Use tracking number EK-CARGO-456 and report the final order ID.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "High-Value Cage"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "APRL-BAG-E5"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "LUX-WATCH-L12"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "LUX-WATCH-L12"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Luxury Retail Group",
                    "warehouse_id": "WH-07",
                    "items": [
                        {
                            "sku": "APRL-BAG-E5",
                            "quantity": 50
                        },
                        {
                            "sku": "LUX-WATCH-L12",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "1 Rodeo Drive, Beverly Hills, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "EK-CARGO-456"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_048",
        "instruction": "The 'West Coast Distribution Hub' (WH-01) experienced damage in a minor earthquake. 10% of the '8-bit Microcontroller' (SKU: ELEC-CHIP-A1) is damaged. Initially, retrieve the current inventory for the SKU in WH-01 to assess the loss. Modify the inventory for the SKU with the reason 'Damaged in Natural Disaster'. Subsequently, examine the updated total stock for the SKU across all warehouses. If the SKU\u2019s total is under 20,000, identify the primary supplier for 'Electronics' (ID 'SUP-1001'), and arrange a new inbound shipment of 5,000 units for the SKU that is low, aimed to be delivered to the 'Midwest Parts Warehouse' (WH-03) by 'SwiftDelivery' (CARR-007) on '2025-08-10'. Verify the new shipment ID.'West Coast Distribution Hub' (WH-01) was damaged in a minor earthquake. 10% of the '8-bit Microcontroller' (SKU: ELEC-CHIP-A1) isdamaged. First, get current inventory for the SKU in WH-01 to calculate the loss. Adjust the inventory for the SKU with the reason 'Damaged in Natural Disaster'. Then, check the new total stock for the SKU across all warehouses. If the total for the SKU is below 20,000, find the primary supplier for 'Electronics' (ID 'SUP-1001') and create a new inbound shipment of 5,000 units for the SKU that is low, to be delivered to the 'Midwest Parts Warehouse' (WH-03) by 'SwiftDelivery' (CARR-007) on '2025-08-10'. Confirm the new shipment ID.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1",
                    "quantity_change": -1500,
                    "reason": "Damaged in Natural Disaster"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Electronics"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1001"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1001",
                    "destination_warehouse_id": "WH-03",
                    "carrier_id": "CARR-007",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 5000
                        }
                    ],
                    "estimated_arrival_date": "2025-08-10"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_049",
        "instruction": "An ongoing inventory audit indicates a quantity discrepancy for 'PHRM-DRUG-S19' in 'WH-06'. The physical count stands at 50 units, but the system lists 500. Start by obtaining the current system quantity, followed by executing an inventory adjustment to align with the physical count with the reason being 'Audit Adjustment'. Next, assess the reorder point for 'PHRM-DRUG-S19' in 'WH-06'. Should the revised quantity fall below the reorder point, commence a new inbound shipment of 100 units from 'SUP-1006' using 'Express World Delivery' (CARR-009) with an ETA of '2025-08-15'. Confirm the updated quantity and new shipment ID if created.'PHRM-DRUG-S19' has an incorrect quantity in 'WH-06'. The physical count is 50 units, but the system shows 500. First, get the current system quantity, then apply an inventory adjustment to match the physical count with reason 'Audit Adjustment'. Then, check the reorder point for 'PHRM-DRUG-S19' in 'WH-06'. If the new quantity is below the reorder point, initiate a new inbound shipment of 100 units from 'SUP-1006' via 'Express World Delivery' (CARR-009) with ETA '2025-08-15'. Confirm final quantity and new shipment ID if created.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-DRUG-S19",
                    "quantity_change": -450,
                    "reason": "Audit Adjustment"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1006"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1006",
                    "destination_warehouse_id": "WH-06",
                    "carrier_id": "CARR-009",
                    "items": [
                        {
                            "sku": "PHRM-DRUG-S19",
                            "quantity": 100
                        }
                    ],
                    "estimated_arrival_date": "2025-08-15"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_050",
        "instruction": "An urgent order from 'BuildFast Corp' requires 35 'Diamond Core Drill Bit' (HEVY-DRIL-I9) and 180 'Automotive Windshield' (AUTO-GLAS-U21). Identify a supplier specializing in 'Heavy Equipment' parts. Review their ratings. Locate warehouses capable of accommodating these products (WH-11 for heavy equipment, WH-03 for glass). Validate stock levels for both items in their respective warehouses. If adequate, create two distinct orders. Ship the drill bits from WH-11 using the premier 'Rail' carrier (highest performance rating, then alphabetical name for ties) and the windshields from WH-03 using the leading 'Truck' carrier (highest performance rating, then alphabetical name for ties). Utilize tracking numbers 'CN-RAIL-789' and 'Global Parcel Service-TRUCK-101'. Report both order IDs.'BuildFast Corp' requires 35 'Diamond Core Drill Bit' (HEVY-DRIL-I9) and 180 'Automotive Windshield' (AUTO-GLAS-U21). Find supplier for 'Heavy Equipment' parts. Check their ratings. Find warehouses that can handle these items (WH-11 for heavy equipment, WH-03 for glass). Check stock for both items in their respective warehouses. If stock is sufficient, create two separate orders. Ship the drill bits from WH-11 using the best 'Rail' carrier (highest performance rating, then alphabetical name for ties) and the windshields from WH-03 using the best 'Truck' carrier (highest performance rating, then alphabetical name for ties). Use tracking numbers 'CN-RAIL-789' and 'Global Parcel Service-TRUCK-101'. Report both order IDs.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Heavy Equipment"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1011"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-11",
                    "sku": "HEVY-DRIL-I9"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-GLAS-U21"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "BuildFast Corp",
                    "warehouse_id": "WH-11",
                    "items": [
                        {
                            "sku": "HEVY-DRIL-I9",
                            "quantity": 35
                        }
                    ],
                    "shipping_address": "123 Construction Site, Denver, CO"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "BuildFast Corp",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 180
                        }
                    ],
                    "shipping_address": "123 Construction Site, Denver, CO"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Rail"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-012",
                    "tracking_number": "CN-RAIL-789"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "Global Parcel Service-TRUCK-101"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\"",
                "\"order_id\": \"ORD-0018\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_051",
        "instruction": "A recall alert has been announced for '8-Bit Microcontroller' (SKU: ELEC-CHIP-A1). Identify all warehouses storing this product. Set the inventory for this SKU to zero in every implicated warehouse, citing 'Product Recall' as the reason. Verify the updated quantities for each warehouse.'8-Bit Microcontroller' (SKU: ELEC-CHIP-A1). Find all warehouses with this product. Adjust the inventory to zero for this SKU in all affected warehouses, with the reason 'Product Recall'. Confirm the adjusted quantities for each warehouse.",
        "actions": [
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1",
                    "quantity_change": -15000,
                    "reason": "Product Recall"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "ELEC-CHIP-A1",
                    "quantity_change": -8000,
                    "reason": "Product Recall"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "ELEC-CHIP-A1"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0001\", \"sku\": \"ELEC-CHIP-A1\", \"warehouse_id\": \"WH-01\"}",
                "{\"inventory_id\": \"INV-0025\", \"sku\": \"ELEC-CHIP-A1\", \"warehouse_id\": \"WH-03\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_052",
        "instruction": "A VIP customer 'Global Tech' requires an urgent delivery of 2 '8-Bit Microcontrollers' (SKU: ELEC-CHIP-A1). Search for warehouses featuring a 'High-Value Cage' and choose the one with the highest number of docks. Check stock availability. If in stock, proceed to create the order. Next, opt for the 'Air' carrier 'CARR-006' and dispatch the order to '1 Quantum Way, Palo Alto, OR' with tracking number 'EK-VIP-789'. Lastly, confirm the status of the order.'Global Tech' has an urgent order for 2 '8-Bit Microcontrollers' (SKU: ELEC-CHIP-A1). Find warehouses with 'High-Value Cage' and select the one with the most number of docks, and check for stock. If available, create the order. Then, select the 'Air' carrier 'CARR-006' and ship the order to '1 Quantum Way, Palo Alto, OR' with tracking number 'EK-VIP-789' . Finally, confirm the order status.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "High-Value Cage"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Global Tech",
                    "warehouse_id": "WH-01",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 2
                        }
                    ],
                    "shipping_address": "1 Quantum Way, Palo Alto, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "EK-VIP-789"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"status\": \"Shipped\", \"warehouse_id\": \"WH-01\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_053",
        "instruction": "Due to a fire at 'Detroit Packaging Supplies' (WH-08), 25% of the 'Industrial Paper Roll' (MANU-PAPR-F6) stock is damaged. Assess the loss and adjust the inventory citing 'Damaged by Fire'. Review the total stock across all sites. If it falls below 500 rolls, contact the supplier 'Toronto Paper Mills' (SUP-1008) to place an urgent order for 200 rolls to the 'Midwest Parts Warehouse' (WH-03) through the top-rated 'Rail' carrier 'CARR-012', expected by '2025-08-12'.'Detroit Packaging Supplies' (WH-08) damaged 25% of the 'Industrial Paper Roll' (MANU-PAPR-F6) inventory. Calculate the loss, adjust the inventory with reason 'Damaged by Fire'. Check the total stock across all locations. If the total quantity is now below 500 rolls, find the supplier 'Toronto Paper Mills' (SUP-1008), and place an emergency inbound order of 200 rolls to the 'Midwest Parts Warehouse' (WH-03) via the best-rated 'Rail' carrier 'CARR-012', to arrive by '2025-08-12'.",
        "actions": [
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-08",
                    "sku": "MANU-PAPR-F6"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-08",
                    "sku": "MANU-PAPR-F6",
                    "quantity_change": -75,
                    "reason": "Damaged by Fire"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "MANU-PAPR-F6"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1008"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Rail"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-012"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1008",
                    "destination_warehouse_id": "WH-03",
                    "carrier_id": "CARR-012",
                    "items": [
                        {
                            "sku": "MANU-PAPR-F6",
                            "quantity": 200
                        }
                    ],
                    "estimated_arrival_date": "2025-08-12"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_054",
        "instruction": "A customer 'Fashion Forward' is returning a defective 'Organic Cotton Tshirt' (SKU: APRL-TSHT-O15). The order ID is 'ORD-0005'. The item cannot be repaired. Update the inventory in warehouse WH-04 by adding 1 unit (returned item), then adjust it by -1 unit citing 'Unrepairable Damage'. Locate the main supplier for 'Apparel' (SUP-1002) and arrange an inbound shipment with supplier ID 'WH-04' (acting as supplier) directed to warehouse ID 'SUP-1002-returns' to return the damaged item for disposal. Use 'Air' carrier 'CARR-007' (SwiftDelivery) with ETA '2025-08-10'. Confirm both the inventory adjustment and the return shipment ID.'Fashion Forward' returns a faulty 'Organic Cotton Tshirt' (SKU: APRL-TSHT-O15). The order ID is 'ORD-0005'. The dress is unrepairable. Update the inventory in warehouse WH-04 by adding 1 unit (customer return), then immediately adjusting it by -1 unit with reason 'Unrepairable Damage'. Then, find the primary supplier for 'Apparel' (SUP-1002) and create an inbound shipment with supplier ID 'WH-04' (the warehouse acts as a supplier) and destination warehouse ID 'SUP-1002-returns' to send the damaged dress back to them for disposal. Ship with 'Air' carrier 'CARR-007' (SwiftDelivery) and ETA '2025-08-10'. Confirm the final inventory adjustment and the return shipment ID.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "APRL-TSHT-O15",
                    "quantity_change": 1,
                    "reason": "Customer Return"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "APRL-TSHT-O15",
                    "quantity_change": -1,
                    "reason": "Unrepairable Damage"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1002"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "WH-04",
                    "destination_warehouse_id": "SUP-1002-returns",
                    "carrier_id": "CARR-007",
                    "items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 1
                        }
                    ],
                    "estimated_arrival_date": "2025-08-10"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\", \"supplier_id\": \"WH-04\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_055",
        "instruction": "A customer 'Home Appliances Inc.' desires to purchase 15 'Luxury Watch' (SKU: LUX-WATCH-L12) and 10 'Leather Handbag' (SKU: APRL-BAG-E5). Locate the US warehouse equipped with both High-Value Cage and 24/7 Security Detail capabilities, ensuring it has adequate stock. Initiate the order and arrange shipment to '456 Appliance Way, Portland, OR' using carrier 'CARR-006' with tracking 'GLOBAL-APRL-001'. Validate the order specifics and the updated stock levels in the warehouse.'Home Appliances Inc.' wants to order 15 'Luxury Watch' (SKU: LUX-WATCH-L12) and 10 'Leather Handbag' (SKU: APRL-BAG-E5). Find the US warehouse that has both High-Value Cage and 24/7 Security Detail capabilities and has sufficient stock. Create the order and ship to '456 Appliance Way, Portland, OR' using carrier 'CARR-006' and tracking 'GLOBAL-APRL-001'. Confirm the order details and the new available quantities in the warehouse.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "country": "United States",
                    "special_capabilities": [
                        "High-Value Cage",
                        "24/7 Security Detail"
                    ]
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "LUX-WATCH-L12"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Home Appliances Inc.",
                    "warehouse_id": "WH-07",
                    "items": [
                        {
                            "sku": "LUX-WATCH-L12",
                            "quantity": 15
                        },
                        {
                            "sku": "APRL-BAG-E5",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "456 Appliance Way, Portland, OR"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "GLOBAL-APRL-001"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "LUX-WATCH-L12"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0012\", \"sku\": \"LUX-WATCH-L12\", \"warehouse_id\": \"WH-07\"}",
                "{\"inventory_id\": \"INV-0005\", \"sku\": \"APRL-BAG-E5\", \"warehouse_id\": \"WH-07\"}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_056",
        "instruction": "The customer 'PharmaPlus' needs to purchase 50 'Insulin Pens' (SKU: PHRM-DRUG-S19) and 20 'Syringes' (SKU: PHRM-VACC-D4). Locate a warehouse offering 'Cold Chain' and 'Pharmaceutical Handling' services with the highest current utilization rate. Proceed to create an order for delivery to '1 Medical Way, Philadelphia, PA'. Subsequently, verify the updated quantities for both SKUs in that warehouse.'PharmaPlus' wants to order 50 'Insulin Pens' (SKU: PHRM-DRUG-S19) and 20 'Syringes' (SKU: PHRM-VACC-D4). Find a warehouse with 'Cold Chain' and 'Pharmaceutical Handling' capabilities and the highest current utilization percentage. Create the order to be shipped to '1 Medical Way, Philadelphia, PA'. Immediately after, check the new available quantities of both SKUs in that warehouse.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capabilities": [
                        "Cold Chain (2-8°C)",
                        "Pharmaceutical Handling"
                    ]
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "PharmaPlus",
                    "warehouse_id": "WH-06",
                    "items": [
                        {
                            "sku": "PHRM-DRUG-S19",
                            "quantity": 50
                        },
                        {
                            "sku": "PHRM-VACC-D4",
                            "quantity": 20
                        }
                    ],
                    "shipping_address": "1 Medical Way, Philadelphia, PA"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-VACC-D4"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0019\", \"sku\": \"PHRM-DRUG-S19\", \"warehouse_id\": \"WH-06\"}",
                "{\"inventory_id\": \"INV-0004\", \"sku\": \"PHRM-VACC-D4\", \"warehouse_id\": \"WH-06\"}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_057",
        "instruction": "The important client 'Global Retail Inc.' is planning to order 200 'Cotton Tshirts' (SKU: APRL-TSHT-O15) and 150 'Raw Cotton Bale' (SKU: MATR-COTT-R18). Identify a warehouse with Garment on Hanger (GOH) capabilities. Ensure it has sufficient stock of both items. If available, generate the order for shipment to '777 Retail Way, Dallas, OK'. Next, adjust the order to utilize 'Air' carrier (CARR-006) with tracking number 'GLOBAL-APRL-001'. Confirm both the updated order status and warehouse utilization.'Global Retail Inc.' wants to order 200 'Cotton Tshirts' (SKU: APRL-TSHT-O15) and 150 'Raw Cotton Bale' (SKU: MATR-COTT-R18). Find a warehouse with Garment on Hanger (GOH) capability. Check if it has both items in stock. If stock is sufficient, create the order to be shipped to '777 Retail Way, Dallas, OK'. Then update the order to use 'Air' carrier (CARR-006) and tracking number 'GLOBAL-APRL-001'. Confirm the updated order status and the chosen warehouse's utilization.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Garment on Hanger (GOH)"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "APRL-TSHT-O15"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "MATR-COTT-R18"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Global Retail Inc.",
                    "warehouse_id": "WH-04",
                    "items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 200
                        },
                        {
                            "sku": "MATR-COTT-R18",
                            "quantity": 150
                        }
                    ],
                    "shipping_address": "777 Retail Way, Dallas, OK"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "GLOBAL-APRL-001"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-04"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"status\": \"Shipped\", \"warehouse_id\": \"WH-04\"",
                "\"warehouse_id\": \"WH-04\", \"warehouse_name\": \"East Coast Fashion Center\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_058",
        "instruction": "A customer, 'ChemSolutions', urgently needs a shipment of 150 units of 'Industrial Solvent' (CHEM-SOLV-K11). Search for a warehouse in the United States with 'Hazmat Certified (Classes 3, 6.1, 9)' features. Verify stock levels and, if adequate, issue an order for delivery to '123 Chemical Lane, Dallas, OK'. Employ the 'Air' carrier 'CARR-022' and tracking number 'CHEM-URGENT-001'. Validate the order ID.'ChemSolutions', requires an urgent shipment of 150 units of 'Industrial Solvent' (CHEM-SOLV-K11). Find a warehouse in the United States with 'Hazmat Certified (Classes 3, 6.1, 9)' capabilities. Check for stock and if sufficient, create an order to be shipped to '123 Chemical Lane, Dallas, OK'. Use the 'Air' carrier 'CARR-022' and tracking number 'CHEM-URGENT-001'. Confirm the order ID.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "country": "United States",
                    "special_capability": "Hazmat Certified (Classes 3, 6.1, 9)"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-13",
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "ChemSolutions",
                    "warehouse_id": "WH-13",
                    "items": [
                        {
                            "sku": "CHEM-SOLV-K11",
                            "quantity": 150
                        }
                    ],
                    "shipping_address": "123 Chemical Lane, Dallas, OK"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-022"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-022",
                    "tracking_number": "CHEM-URGENT-001"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_059",
        "instruction": "The dining establishment 'The Gilded Spoon' requires 50 'Frozen Tuna Loins' (FOOD-FISH-H8). Discover a warehouse capable of 'Perishables Handling' and check stock levels. Create an order for delivery to '789 Gourmet Ave, San Francisco, OR'. Arrange for shipment using a 'Reefer' truck from the highest-rated carrier allowing it. Apply tracking number 'GILDED-FISH-001'.'The Gilded Spoon' needs 50 'Frozen Tuna Loins' (FOOD-FISH-H8). Find a warehouse with 'Perishables Handling' and check for stock. Create an order to '789 Gourmet Ave, San Francisco, OR'. Ship it using a 'Reefer' truck from the best-rated carrier that supports it. Use tracking 'GILDED-FISH-001'.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Perishables Handling"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "sku": "FOOD-FISH-H8"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "The Gilded Spoon",
                    "warehouse_id": "WH-10",
                    "items": [
                        {
                            "sku": "FOOD-FISH-H8",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "789 Gourmet Ave, San Francisco, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-001",
                    "tracking_number": "GILDED-FISH-001"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_060",
        "instruction": "'DigDeep Corp', a mining firm, requests 10 'Diamond Core Drill Bits' (HEVY-DRIL-I9). Identify supplier 'SUP-1011' specializing in 'Heavy Equipment' and evaluate their performance metrics. Then, inspect inventory at 'WH-11'. If the stock meets requirements, finalize an order for 'DigDeep Corp' to '999 Mine Road, Denver, CO' using 'Rail' carrier 'CARR-008' with tracking 'DIG-RAIL-002'.'DigDeep Corp' needs 10 'Diamond Core Drill Bits' (HEVY-DRIL-I9). Find supplier 'SUP-1011' for 'Heavy Equipment' and check their performance. Then, check inventory at 'WH-11'. If stock is sufficient, create an order for 'DigDeep Corp' to '999 Mine Road, Denver, CO' and ship via 'Rail' carrier 'CARR-008' with tracking 'DIG-RAIL-002'.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Heavy Equipment"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1011"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-11",
                    "sku": "HEVY-DRIL-I9"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "DigDeep Corp",
                    "warehouse_id": "WH-11",
                    "items": [
                        {
                            "sku": "HEVY-DRIL-I9",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "999 Mine Road, Denver, CO"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Rail"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-008",
                    "tracking_number": "DIG-RAIL-002"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_061",
        "instruction": "Handle a return of a 'Leather Handbag' (APRL-BAG-E5) from order 'ORD-0001' to 'WH-07'. Since the item is in perfect condition, reintegrate it into the inventory stating 'Customer Return - Resalable' as the reason. Verify the final inventory count.'Leather Handbag' (APRL-BAG-E5) from order 'ORD-0001' to 'WH-07'. The item is in perfect condition. Add it back to the inventory with reason 'Customer Return - Resalable'. Verify the final inventory count.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0001"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5",
                    "quantity_change": 1,
                    "reason": "Customer Return - Resalable"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0005\", \"sku\": \"APRL-BAG-E5\", \"quantity_available\": 121}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_062",
        "instruction": "A construction company 'BuildRight' requires 5000 'Ceramic Floor Tiles' (BLDG-TILE-J10). Identify warehouses with 'Bulk Storage' capability and select the one with the highest current utilization percentage. Check inventory levels. Formulate an order to '456 Construction Ave, Fort Lauderdale, SC' and dispatch using 'Truck' carrier 'CARR-007' with tracking 'BUILD-TILE-5000'.'BuildRight' needs 5000 'Ceramic Floor Tiles' (BLDG-TILE-J10). Find warehouses with 'Bulk Storage' capability and choose the one with the highest current utilization percentage. Check inventory. Create an order to '456 Construction Ave, Fort Lauderdale, SC' and ship via 'Truck' carrier 'CARR-007' with tracking 'BUILD-TILE-5000'.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Bulk Storage"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "sku": "BLDG-TILE-J10"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "BuildRight",
                    "warehouse_id": "WH-12",
                    "items": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 5000
                        }
                    ],
                    "shipping_address": "456 Construction Ave, Fort Lauderdale, SC"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-007"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-007",
                    "tracking_number": "BUILD-TILE-5000"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_063",
        "instruction": "Coordinate the transfer of 50 'Automotive Windshields' (AUTO-GLAS-U21) from 'WH-03' to 'WH-01'. Due to their fragile nature, decrease inventory at the source, prepare an inbound shipment for the destination with an ETA of '2025-08-01', and select a carrier that offers 'Truck' transport (CARR-014). Verify the final inventory at WH-03.'Automotive Windshields' (AUTO-GLAS-U21) from 'WH-03' to 'WH-01'. These are fragile. Reduce inventory at the source, create an inbound shipment for the destination with ETA '2025-08-01', and use a carrier that supports 'Truck' transport (CARR-014). Confirm the final inventory at WH-03.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-GLAS-U21"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-GLAS-U21",
                    "quantity_change": -50,
                    "reason": "Internal Transfer to WH-01"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "Internal",
                    "destination_warehouse_id": "WH-01",
                    "carrier_id": "CARR-014",
                    "items": [
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 50
                        }
                    ],
                    "estimated_arrival_date": "2025-08-01"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-GLAS-U21"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0021\", \"quantity_on_hand\": 150}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_064",
        "instruction": "Assist an e-commerce client 'GadgetGo' with an order of 200 'Smartphone Model X' (ELEC-SMART-W23). Locate a warehouse with 'E-commerce Fulfillment' capability. Confirm stock availability. Arrange an order to '123 E-com St, Portland, OR' and ship via 'Parcel' using carrier 'CARR-014' with tracking 'GADGET-ECOM-200'.'GadgetGo' needs 200 'Smartphone Model X' (ELEC-SMART-W23). Find a warehouse with 'E-commerce Fulfillment' capability. Check stock. Create an order to '123 E-com St, Portland, OR' and ship via 'Parcel' using carrier 'CARR-014' with tracking 'GADGET-ECOM-200'.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "E-commerce Fulfillment"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "GadgetGo",
                    "warehouse_id": "WH-02",
                    "items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 200
                        }
                    ],
                    "shipping_address": "123 E-com St, Portland, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Parcel"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-014"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "GADGET-ECOM-200"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_065",
        "instruction": "A client 'BioChem Corp' requires 10 'Industrial Solvent' (CHEM-SOLV-K11) and 50 'Ceramic Brake Pad Set' (AUTO-PAD-B2). Locate a warehouse carrying both items. If unavailable, identify two warehouses (WH-13 and WH-03) and create two distinct orders to '789 Lab Ave, Cleveland, OH'. Dispatch both via 'Truck' using carrier ID 'CARR-007'. Apply tracking 'BIO-HAZ-001' for the solvent and 'BIO-AUTO-001' for the pads.'BioChem Corp' needs 10 'Industrial Solvent' (CHEM-SOLV-K11) and 50 'Ceramic Brake Pad Set' (AUTO-PAD-B2). Find a warehouse that has both. If none, find two warehouses (WH-13 and WH-03) and create two separate orders to '789 Lab Ave, Cleveland, OH'. Ship both via 'Truck' carrier ID 'CARR-007'. Use tracking 'BIO-HAZ-001' for the solvent and 'BIO-AUTO-001' for the pads.",
        "actions": [
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "BioChem Corp",
                    "warehouse_id": "WH-13",
                    "items": [
                        {
                            "sku": "CHEM-SOLV-K11",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "789 Lab Ave, Cleveland, OH"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "BioChem Corp",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "789 Lab Ave, Cleveland, OH"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-007",
                    "tracking_number": "BIO-HAZ-001"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-007",
                    "tracking_number": "BIO-AUTO-001"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\"",
                "\"order_id\": \"ORD-0018\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_066",
        "instruction": "Handle an inbound shipment 'SHIP-0020' of 'Raw Cotton Bale' (MATR-COTT-R18) at 'WH-04'. The shipment comprises 1100 units. After handling, coordinate a quality check by adjusting out 10 units as 'Damaged on Arrival'. Verify the final available quantity.'SHIP-0020' of 'Raw Cotton Bale' (MATR-COTT-R18) at 'WH-04'. The shipment contains 1100 units. After receiving, perform a quality check by adjusting out 10 units as 'Damaged on Arrival'. Confirm the final available quantity.",
        "actions": [
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0020"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0020",
                    "items_received": [
                        {
                            "sku": "MATR-COTT-R18",
                            "quantity": 1100
                        }
                    ]
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "MATR-COTT-R18",
                    "quantity_change": -10,
                    "reason": "Damaged on Arrival"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "MATR-COTT-R18"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0018\", \"quantity_on_hand\": 1290}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_067",
        "instruction": "A customer 'Style Maven' requires 50 'Organic Cotton T-Shirt' (APRL-TSHT-O15) and 10 'Leather Handbag' (APRL-BAG-E5). The T-shirts are located in 'WH-04' and handbags in 'WH-07'. Generate two separate orders shipping to '1 Fashionista Way, New York, NY'. Employ Air carrier 'Global Parcel Service' for both with tracking numbers 'STYLE-TSHIRT-001' and 'STYLE-BAG-001'.'Style Maven' needs 50 'Organic Cotton T-Shirt' (APRL-TSHT-O15) and 10 'Leather Handbag' (APRL-BAG-E5). The T-shirts are in 'WH-04' and handbags in 'WH-07'. Create two separate orders shipping to '1 Fashionista Way, New York, NY'. Use Air carrier 'Global Parcel Service' for both with tracking numbers 'STYLE-TSHIRT-001' and 'STYLE-BAG-001'.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "APRL-TSHT-O15"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "sku": "APRL-BAG-E5"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Style Maven",
                    "warehouse_id": "WH-04",
                    "items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "1 Fashionista Way, New York, NY"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Style Maven",
                    "warehouse_id": "WH-07",
                    "items": [
                        {
                            "sku": "APRL-BAG-E5",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "1 Fashionista Way, New York, NY"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "STYLE-TSHIRT-001"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "STYLE-BAG-001"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\"",
                "\"order_id\": \"ORD-0018\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_068",
        "instruction": "A shipment of 1200 units of 'Solar Panel 450W' (TECH-SOLR-G7) has been received at 'WH-09' via shipment 'SHIP-0009'. Immediately cross-dock 100 panels to complete order 'ORD-0010' for 'Kappa Books Pvt Ltd.'. Update the order status to 'Shipped' using carrier 'CARR-007' and tracking 'CROSSDOCK-SOLAR-01'.'Solar Panel 450W' (TECH-SOLR-G7) has arrived at 'WH-09' via shipment 'SHIP-0009'. Immediately cross-dock 100 panels to fulfill order 'ORD-0010' for 'Kappa Books Pvt Ltd.'. Update the order status to 'Shipped' with carrier 'CARR-007' and tracking 'CROSSDOCK-SOLAR-01'.",
        "actions": [
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0009"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "sku": "TECH-SOLR-G7"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0009",
                    "items_received": [
                        {
                            "sku": "TECH-SOLR-G7",
                            "quantity": 1200
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "sku": "TECH-SOLR-G7"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "sku": "TECH-SOLR-G7",
                    "quantity_change": -100,
                    "reason": "Cross-dock for ORD-0010"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-007"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0010",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-007",
                    "tracking_number": "CROSSDOCK-SOLAR-01"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0010"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0010\", \"status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_069",
        "instruction": "A customer 'DIY Garage' requires 20 'Ceramic Brake Pad Set' (AUTO-PAD-B2) and 10 'Automotive Windshield' (AUTO-GLAS-U21). Locate a warehouse that stocks both items (WH-03). Create two separate orders for 'DIY Garage' to '789 DIY Ave, Denver, CO'. Ship both orders utilizing the 'Truck' carrier with the best on-time delivery percentage ('Global Parcel Service' - CARR-014). Use tracking numbers 'DIY-BRAKES-01' and 'DIY-GLASS-02'.'DIY Garage' needs 20 'Ceramic Brake Pad Set' (AUTO-PAD-B2) and 10 'Automotive Windshield' (AUTO-GLAS-U21). Find a warehouse that has both items (WH-03).  Create two separate orders for 'DIY Garage' to '789 DIY Ave, Denver, CO'. Ship both orders using the 'Truck' carrier with the best on-time delivery percentage ('Global Parcel Service' - CARR-014). Use tracking numbers 'DIY-BRAKES-01' and 'DIY-GLASS-02'.",
        "actions": [
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "AUTO-GLAS-U21"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-GLAS-U21"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "DIY Garage",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 20
                        }
                    ],
                    "shipping_address": "789 DIY Ave, Denver, CO"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "DIY Garage",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "789 DIY Ave, Denver, CO"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "DIY-BRAKES-01"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "DIY-GLASS-02"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\"",
                "\"order_id\": \"ORD-0018\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_070",
        "instruction": "A shipment (SHIP-0029) of 'Fresh Cut Roses' (FOOD-FLWR-X24) has reached 'San Francisco Fresh Foods DC' (WH-10). The shipment contains 65 units. Acknowledge the shipment. Immediately, a customer 'Petal Pushers' places an order (ORD-0017) for 50 bouquets to '45 Rose St, Portland, OR'. Check the inventory to confirm stock, create the order, and dispatch it using the 'Air' carrier with the highest on-time delivery, 'Desert Falcon Cargo' (CARR-006), with tracking 'PETAL-AIR-50'.'Fresh Cut Roses' (FOOD-FLWR-X24) has arrived at 'San Francisco Fresh Foods DC' (WH-10). The shipment contains 65 units. Receive the shipment. Immediately, a customer 'Petal Pushers' places an order (ORD-0017) for 50 bouquets to '45 Rose St, Portland, OR'. Check the inventory to ensure stock, create the order, and ship it using the 'Air' carrier with the highest on-time delivery, 'Desert Falcon Cargo' (CARR-006), with tracking 'PETAL-AIR-50'.",
        "actions": [
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0029"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0029",
                    "items_received": [
                        {
                            "sku": "FOOD-FLWR-X24",
                            "quantity": 65
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "sku": "FOOD-FLWR-X24"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Petal Pushers",
                    "warehouse_id": "WH-10",
                    "items": [
                        {
                            "sku": "FOOD-FLWR-X24",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "45 Rose St, Portland, OR"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "PETAL-AIR-50"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\", \"status\": \"Shipped\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_071",
        "instruction": "Handle an order for 'RoboBuilders' requiring 5 'Robotic Kits'. Each kit includes 1 'Articulated Robotic Arm' (TECH-ROBO-N14) and 2 'Lithium-Ion Battery Pack' (TECH-BATT-Q17). Verify the stock of both items at 'WH-03'. If the stock is sufficient, organize an order for the 5 kits (5 arms, 10 batteries) to be delivered to '789 Robot Way, Pittsburgh, PA' using the 'Rail' carrier 'CARR-008' with tracking number 'ROBO-KIT-005'.'RoboBuilders' needs 5 'Robotic Kits'. Each kit consists of 1 'Articulated Robotic Arm' (TECH-ROBO-N14) and 2 'Lithium-Ion Battery Pack' (TECH-BATT-Q17). Check inventory for both components at 'WH-03'. If available, create an order for the 5 kits (5 arms, 10 batteries) to '789 Robot Way, Pittsburgh, PA' and ship via 'Rail' carrier 'CARR-008' with tracking 'ROBO-KIT-005'.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "RoboBuilders",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 5
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "789 Robot Way, Pittsburgh, PA"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Rail"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-008",
                    "tracking_number": "ROBO-KIT-005"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_072",
        "instruction": "Coordinate the update of the status of international shipment 'SHIP-0004' of textiles, marking it as 'Delayed - Customs Hold'. Inspect the status of order 'ORD-0005', which relies on this stock. Then, arrange for a replacement shipment of 100 'Organic Cotton T-Shirt' (APRL-TSHT-O15) from 'SUP-1004' to 'WH-04' using an alternative 'Air' carrier 'CARR-016', aiming for an ETA of '2025-07-30'.'SHIP-0004' of textiles is delayed. Update its status to 'Delayed - Customs Hold'. Check the status of order 'ORD-0005' which depends on this stock. Then, find an alternative 'Air' carrier 'CARR-016' to expedite a replacement shipment of 100 'Organic Cotton T-Shirt' (APRL-TSHT-O15) from 'SUP-1004' to 'WH-04' with ETA '2025-07-30'.",
        "actions": [
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0004",
                    "status": "Delayed - Customs Hold"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1004",
                    "destination_warehouse_id": "WH-04",
                    "carrier_id": "CARR-016",
                    "items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 100
                        }
                    ],
                    "estimated_arrival_date": "2025-07-30"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_073",
        "instruction": "Manage an order for 'EcoBuild' requiring 1000 'Solar Panel 450W' (TECH-SOLR-G7). Confirm stock availability at 'Phoenix Renewable Warehouse' (WH-09). Prepare the order for 'EcoBuild', shipping to '321 Green Energy Way, Austin, OK'. As this is an oversized shipment, select a 'Truck' carrier with 'Freight LTL' that offers the highest average rating. Dispatch the order with this carrier (CARR-014) and tracking 'ECO-SOLAR-LTL-321'. After dispatching, verify the details of the warehouse.'EcoBuild' needs 1000 'Solar Panel 450W' (TECH-SOLR-G7). The 'Phoenix Renewable Warehouse' (WH-09) has stock. Create the order for 'EcoBuild' to '321 Green Energy Way, Austin, OK'. This is an oversized shipment. Find a 'Truck' carrier that supports 'Freight LTL' and has the highest average rating. Ship the order with this carrier (CARR-014) and tracking 'ECO-SOLAR-LTL-321'. After shipping, verify the warehouse's details.",
        "actions": [
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "sku": "TECH-SOLR-G7"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "EcoBuild",
                    "warehouse_id": "WH-09",
                    "items": [
                        {
                            "sku": "TECH-SOLR-G7",
                            "quantity": 1000
                        }
                    ],
                    "shipping_address": "321 Green Energy Way, Austin, OK"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-014"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "ECO-SOLAR-LTL-321"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-09"
                }
            }
        ],
        "outputs": [
                "\"warehouse_id\": \"WH-09\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_074",
        "instruction": "Arrange a rush order for 'Flash Electronics' needing 500 '8-bit Microcontroller' (ELEC-CHIP-A1). Locate the warehouse with the maximum stock. Next, identify the 'Air' carrier boasting the highest on-time delivery percentage. Establish the order to '1 Speed St, Austin, OK', and dispatch using the chosen carrier, utilizing tracking 'FLASH-RUSH-01'.'Flash Electronics' needs a rush order of 500 '8-bit Microcontroller' (ELEC-CHIP-A1). Find the warehouse with the most stock. Then find the 'Air' carrier with the highest on-time delivery percentage. Create the order to '1 Speed St, Austin, OK' and ship with the selected carrier. Use tracking 'FLASH-RUSH-01'.",
        "actions": [
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Flash Electronics",
                    "warehouse_id": "WH-01",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 500
                        }
                    ],
                    "shipping_address": "1 Speed St, Austin, OK"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-014"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "FLASH-RUSH-01"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_075",
        "instruction": "Facilitate an order for 'Arctic Research Station' in Greenland requesting 5 'Solar Panel 450W' (TECH-SOLR-G7). Identify a warehouse with available stock. Research to find an 'Air' carrier (CARR-022) that offers global coverage. Formulate the order shipping to '1 Research Base, Nuuk, Greenland' and dispatch with the selected carrier. Use tracking 'ARCTIC-SOLAR-01'.'Arctic Research Station' in Greenland needs 5 'Solar Panel 450W' (TECH-SOLR-G7). Find a warehouse with stock. Research and find an 'Air' carrier (CARR-022) with global coverage. Create the order to '1 Research Base, Nuuk, Greenland' and ship with the selected carrier. Tracking 'ARCTIC-SOLAR-01'.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "sku": "TECH-SOLR-G7"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Arctic Research Station",
                    "warehouse_id": "WH-09",
                    "items": [
                        {
                            "sku": "TECH-SOLR-G7",
                            "quantity": 5
                        }
                    ],
                    "shipping_address": "1 Research Base, Nuuk, Greenland"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-022",
                    "tracking_number": "ARCTIC-SOLAR-01"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_076",
        "instruction": "Handle an order for a new art gallery, 'Canvas Dreams', needing 10 'Teak Wood Dining Chairs' (FURN-CHAIR-M13) and 50 'Organic Cotton T-Shirts' (APRL-TSHT-O15) for its opening event. Items are located in different warehouses (WH-14 and WH-04). Coordinate the creation of two distinct orders for 'Canvas Dreams', shipping them to '1 Art Plaza, New York, NY'. Identify a 'Parcel' carrier and a 'Truck' carrier. Assign the chairs to be shipped through the truck carrier (CARR-007) with tracking 'ART-CHAIR-NYC', and the t-shirts via the parcel carrier (CARR-014) with tracking 'ART-TSHIRT-NYC'.'Canvas Dreams', needs 10 'Teak Wood Dining Chairs' (FURN-CHAIR-M13) and 50 'Organic Cotton T-Shirts' (APRL-TSHT-O15) for their opening event. The items are in different warehouses (WH-14 and WH-04). Create two separate orders for 'Canvas Dreams' shipping to '1 Art Plaza, New York, NY'. Find a 'Parcel' carrier and a 'Truck' carrier. Ship the chairs via the truck carrier (CARR-007) with tracking 'ART-CHAIR-NYC' and the t-shirts via the parcel carrier (CARR-014) with tracking 'ART-TSHIRT-NYC'.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "APRL-TSHT-O15"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Canvas Dreams",
                    "warehouse_id": "WH-14",
                    "items": [
                        {
                            "sku": "FURN-CHAIR-M13",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "1 Art Plaza, New York, NY"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Canvas Dreams",
                    "warehouse_id": "WH-04",
                    "items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "1 Art Plaza, New York, NY"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Parcel"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-007",
                    "tracking_number": "ART-CHAIR-NYC"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "ART-TSHIRT-NYC"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\"",
                "\"order_id\": \"ORD-0018\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_077",
        "instruction": "Manage two existing LTL orders for 'AutoStop' parts (SKU AUTO-PAD-B2) from 'WH-03' destined for Milwaukee. Merge these into one single FTL shipment. Proceed with canceling orders 'ORD-0003' and 'ORD-0009'. Formulate a new order for 'Consolidated Auto' to include 25 units of 'AUTO-PAD-B2' directed to '1 Central Depot, Milwaukee, WI'. Transport via 'Truck' carrier 'CARR-007' with tracking 'FTL-AUTO-Milwaukee-01'.'AutoStop' parts (SKU AUTO-PAD-B2) from 'WH-03' to Milwaukee. Consolidate them into a single FTL shipment. Cancel orders 'ORD-0003' and 'ORD-0009'. Create a new order for 'Consolidated Auto' for 25 units of 'AUTO-PAD-B2' to '1 Central Depot, Milwaukee, WI'. Ship via 'Truck' carrier 'CARR-007' with tracking 'FTL-AUTO-Milwaukee-01'.",
        "actions": [
            {
                "name": "CancelOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0003"
                },
            },
            {
                "name": "CancelOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0009"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Consolidated Auto",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 25
                        }
                    ],
                    "shipping_address": "1 Central Depot, Milwaukee, WI"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-007",
                    "tracking_number": "FTL-AUTO-Milwaukee-01"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_078",
        "instruction": "Receive 'SHIP-0012' of tiles at 'WH-12', taking note that 100 units of 'BLDG-TILE-J10' were damaged. Accept the shipment with the precise count (1100 units), adjusting the inventory by writing off the 100 damaged units with the reason 'Damaged in Transit'. Validate the final inventory.'SHIP-0012' of tiles arrived at 'WH-12', but 100 units of 'BLDG-TILE-J10' were damaged. Receive the shipment with the correct quantity (1100 units), and adjust the inventory to write off the 100 damaged units with reason 'Damaged in Transit'. Confirm the final inventory.",
        "actions": [
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0012"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0012",
                    "items_received": [
                        {
                            "sku": "BLDG-TILE-J10",
                            "quantity": 1100
                        }
                    ]
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "sku": "BLDG-TILE-J10",
                    "quantity_change": -100,
                    "reason": "Damaged in Transit"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "sku": "BLDG-TILE-J10"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0010\", \"quantity_on_hand\": 19000}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_079",
        "instruction": "Correct the mistake in order 'ORD-0010' that was raised with the wrong SKU. It ought to be for 'Industrial Paper Roll' (MANU-PAPR-F6), not books. Nullify the incorrect order. Initiate a new order for 'Kappa Books Pvt Ltd.' for 50 units of 'MANU-PAPR-F6' from 'WH-08' to the same delivery address. Dispatch via 'Truck' carrier 'CARR-003' with tracking 'PAPER-REORDER-01'.'ORD-0010' was created with the wrong SKU. It should be for 'Industrial Paper Roll' (MANU-PAPR-F6), not books. Cancel the incorrect order. Create a new order for 'Kappa Books Pvt Ltd.' for 50 units of 'MANU-PAPR-F6' from 'WH-08' to the same address. Ship via 'Truck' carrier 'CARR-003' with tracking 'PAPER-REORDER-01'.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "CancelOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-08",
                    "sku": "MANU-PAPR-F6"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Kappa Books Pvt Ltd.",
                    "warehouse_id": "WH-08",
                    "items": [
                        {
                            "sku": "MANU-PAPR-F6",
                            "quantity": 50
                        }
                    ],
                    "shipping_address": "12 Writer's Block, Mumbai, India"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-003"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-003",
                    "tracking_number": "PAPER-REORDER-01"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_080",
        "instruction": "The carrier allocated for shipment 'SHIP-0004' identified by carrier ID 'CARR-004' is no longer active. Locate an alternative 'Sea' carrier with the highest rating, 'CARR-002'. Amend the shipment to reflect the new carrier. Subsequently, revise the shipment status to 'In Transit'.'SHIP-0004' with carrier ID 'CARR-004', is inactive. Find an alternative 'Sea' carrier with the highest rating (CARR-002). Update the shipment to use the new carrier. Then, update the shipment status to 'In Transit'.",
        "actions": [
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-004"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-002"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Sea"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0004",
                    "carrier_id": "CARR-002",
                    "carrier_name": "Sakura Express",
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0004",
                    "status": "In Transit"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                }
            }
        ],
        "outputs": [
                "{\"shipment_id\": \"SHIP-0004\", \"carrier_id\": \"CARR-002\", \"status\": \"In Transit\"}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_081",
        "instruction": "An order 'ORD-0015' features an incorrect shipping address. Cancel the order. Following that, set up a new order for 'Omicron Trading Ltd.' for the identical items (100 units of 'FURN-CHAIR-M13') from 'WH-14' with the revised address '123 Commerce St, Riyadh, Saudi Arabia'. Dispatch via 'Truck' carrier 'CARR-003' with tracking 'ADDRESS-FIX-01'.'ORD-0015' has an invalid shipping address. Cancel the order. Then, create a new order for 'Omicron Trading Ltd.' for the same items (100 units of 'FURN-CHAIR-M13') from 'WH-14' with the corrected address '123 Commerce St, Riyadh, Saudi Arabia'. Ship via 'Truck' carrier 'CARR-003' with tracking 'ADDRESS-FIX-01'.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0015"
                },
            },
            {
                "name": "CancelOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0015"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Omicron Trading Ltd.",
                    "warehouse_id": "WH-14",
                    "items": [
                        {
                            "sku": "FURN-CHAIR-M13",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "123 Commerce St, Riyadh, Saudi Arabia"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-003"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-003",
                    "tracking_number": "ADDRESS-FIX-01"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_082",
        "instruction": "Stock of 'Organic Arabica Coffee Beans' (FOOD-COFF-C3) at 'WH-05' is nearing its expiration date ('2025-05-20'). Arrange a promotional outbound shipment for 'Theta Foods SA' for 100 units to '200 Avenida Paulista, S\u00e3o Paulo, Brazil'. Send through 'Air' carrier 'CARR-020' with tracking 'COFFEE-PROMO-01'.'Organic Arabica Coffee Beans' (FOOD-COFF-C3) at 'WH-05' is approaching its expiration date ('2025-05-20'). Create a promotional outbound order for 'Theta Foods SA' for 100 units to '200 Avenida Paulista, S\u00e3o Paulo, Brazil'. Ship via 'Air' carrier 'CARR-020' with tracking 'COFFEE-PROMO-01'.",
        "actions": [
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-05",
                    "sku": "FOOD-COFF-C3"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Theta Foods SA",
                    "warehouse_id": "WH-05",
                    "items": [
                        {
                            "sku": "FOOD-COFF-C3",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "200 Avenida Paulista, São Paulo, Brazil"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-020"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-020",
                    "tracking_number": "COFFEE-PROMO-01"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_083",
        "instruction": "A significant order for 20,000 '8-bit Microcontroller' (ELEC-CHIP-A1) is placed by 'MegaCorp'. 'WH-01' holds only 12,500 units. Fill the order with what is available from 'WH-01', and obtain the remaining 7,500 from 'WH-03'. Formulate two orders for 'MegaCorp' to '1 Mega Plaza, New York, NY'. Dispatch both using 'CARR-014' with tracking numbers 'MEGA-NY-1' and 'MEGA-NY-2'.'8-bit Microcontroller' (ELEC-CHIP-A1) comes from 'MegaCorp'. 'WH-01' only has 12,500 units. Fulfill what you can from 'WH-01', and fulfill the remaining 7,500 from 'WH-03'. Create two orders for 'MegaCorp' to '1 Mega Plaza, New York, NY'. Ship both via 'CARR-014' with tracking numbers 'MEGA-NY-1' and 'MEGA-NY-2'.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "MegaCorp",
                    "warehouse_id": "WH-01",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 12500
                        }
                    ],
                    "shipping_address": "1 Mega Plaza, New York, NY"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "MegaCorp",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 7500
                        }
                    ],
                    "shipping_address": "1 Mega Plaza, New York, NY"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "MEGA-NY-1"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "MEGA-NY-2"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\"",
                "\"order_id\": \"ORD-0018\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_084",
        "instruction": "A customer sends back a 'Lithium-Ion Battery Pack' (TECH-BATT-Q17) from order 'ORD-0016'. This item was subject to a recall. Update the stock at 'WH-03' to reintegrate the unit citing 'Recalled Product Return' as the reason, then instantly adjust it out with the reason 'Disposal of Recalled Item'. Verify final stock.'Lithium-Ion Battery Pack' (TECH-BATT-Q17) from order 'ORD-0016'. This product was recalled. Adjust the inventory at 'WH-03' to add the unit back with reason 'Recalled Product Return', then immediately adjust it out with reason 'Disposal of Recalled Item'. Confirm final inventory.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0016"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17",
                    "quantity_change": 1,
                    "reason": "Recalled Product Return"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17",
                    "quantity_change": -1,
                    "reason": "Disposal of Recalled Item"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17"
                }
            }
        ],
        "outputs": [
                "{\"inventory_id\": \"INV-0017\", \"quantity_on_hand\": 1500}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_085",
        "instruction": "A production run at 'RoboMation' demands 20 'Articulated Robotic Arm' (TECH-ROBO-N14) to be delivered precisely on '2025-09-01'. Identify the supplier 'SUP-1016' and organize a just-in-time incoming shipment to 'WH-03'. Opt for an 'Air' carrier with the highest on-time delivery percentage to secure punctuality.'RoboMation' requires 20 'Articulated Robotic Arm' (TECH-ROBO-N14) to arrive exactly on '2025-09-01'. Find the supplier 'SUP-1016' and create a just-in-time inbound shipment to 'WH-03'. Select an 'Air' carrier that has the best on-time delivery percentage to ensure timeliness.",
        "actions": [
            {
                "name": "FindSuppliers",
                "arguments": {
                    "product_categories": [
                        "Automation"
                    ]
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1016"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1016",
                    "destination_warehouse_id": "WH-03",
                    "carrier_id": "CARR-014",
                    "items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 20
                        }
                    ],
                    "estimated_arrival_date": "2025-09-01"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_086",
        "instruction": "An incoming shipment of 5000 'Solar Panel 450W' (TECH-SOLR-G7) is arranged for 'WH-09', currently at 85% capacity. Identify another warehouse with 'Outdoor Storage' and the least utilization. Redirect the shipment 'SHIP-0009' to this alternate warehouse.'Solar Panel 450W' (TECH-SOLR-G7) is planned for 'WH-09', but it is over capacity (currently 85% utilization). Find an alternative warehouse with 'Outdoor Storage' and the lowest utilization. Re-route the shipment 'SHIP-0009' to the new warehouse.",
        "actions": [
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "TECH-SOLR-G7"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capability": "Outdoor Storage"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0009",
                    "destination_warehouse_id": "WH-11",
                    "destination_warehouse_name": "Denver Heavy Equipment Yard",
                    "destination_address": "950 Quarry Rd",
                    "destination_city": "Denver"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0009"
                }
            }
        ],
        "outputs": [
                "{\"shipment_id\": \"SHIP-0009\", \"destination_warehouse_id\": \"WH-11\"}"
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_087",
        "instruction": "A defect has been detected with 'Ceramic Brake Pad Set' (AUTO-PAD-B2) from supplier 'SUP-1003'. Void the outbound order (ORD-0010). Subsequently, return the total of 750 units to the supplier (tagged as 'SUP-1003-RETURNS') from warehouse 'WH-03'. Organize an outbound delivery back to the supplier at 'Maximilianstra\u00dfe 200, Frankfurt, Deutschland'. Opt for 'Air' carrier 'CARR-003' and apply tracking number 'RETURN-SUP1003-01'. Obtain the detailed final order information.'Ceramic Brake Pad Set' (AUTO-PAD-B2) from supplier 'SUP-1003'. Cancel the outbound order (ORD-0010). Then, make a return of all 750 units to the supplier (use customer name 'SUP-1003-RETURNS') from warehouse 'WH-03'. Create an outbound shipment to the supplier to the address 'Maximilianstra\u00dfe 200, Frankfurt, Deutschland'. Use 'Air' carrier 'CARR-003' and tracking number 'RETURN-SUP1003-01'. Retrieve the final order details",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "CancelOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1003"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "SUP-1003-RETURNS",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 750
                        }
                    ],
                    "shipping_address": "Maximilianstraße 200, Frankfurt, Deutschland"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-003"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-003",
                    "tracking_number": "RETURN-SUP1003-01"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_088",
        "instruction": "A remote clinic, 'Mountain View Clinic', requires 20 'Influenza Vaccine' (PHRM-VACC-D4). Locate a warehouse with 'Cold Chain (2-8\u00b0C)' and 'Pharmaceutical Handling' facilities. Select the one with the highest usage rate. Formulate an order to '15 Mountain Pass, Aspen, CO'. 'Air' transportation is needed. Utilize carrier 'CARR-016'. Dispatch to address 15 Mountain Pass, Aspen, CO with tracking 'REMOTE-VAX-01'.'Mountain View Clinic', needs 20 'Influenza Vaccine' (PHRM-VACC-D4). Find a warehouse with 'Cold Chain (2-8\u00b0C)' and 'Pharmaceutical Handling' capability. Choose the warehouse with the highest utilization percentage. Create an order to '15 Mountain Pass, Aspen, CO'. The delivery requires 'Air' transport. Use carrier 'CARR-016'. Ship to address 15 Mountain Pass, Aspen, CO with tracking 'REMOTE-VAX-01'.",
        "actions": [
            {
                "name": "FindWarehouses",
                "arguments": {
                    "special_capabilities": [
                        "Cold Chain (2-8°C)",
                        "Pharmaceutical Handling"
                    ]
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Mountain View Clinic",
                    "warehouse_id": "WH-06",
                    "items": [
                        {
                            "sku": "PHRM-VACC-D4",
                            "quantity": 20
                        }
                    ],
                    "shipping_address": "15 Mountain Pass, Aspen, CO"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-016"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-016",
                    "tracking_number": "REMOTE-VAX-01"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_089",
        "instruction": "Manage a multi-modal delivery of 10,000 'Raw Cotton Bale' (MATR-COTT-R18) from 'SUP-1020' in Egypt to 'WH-08' in Detroit. It will first be routed to 'SUP-1013' (use destination warehouse ID as 'SUP-1013') via 'Rail' 'CARR-001' with an estimated arrival date of '2025-09-20'. Next, transport it to Detroit (supplier ID: SUP-1013, destination warehouse: WH-08) using 'Rail' 'CARR-008' with an ETA of '2025-09-25'. Initiate the primary inbound shipment to 'SUP-1013', then arrange a transfer shipment from there to WH-08.'Raw Cotton Bale' (MATR-COTT-R18) from 'SUP-1020' in Egypt to 'WH-08' in Detroit. The shipment will travel to 'SUP-1013' (use destination warehouse ID as 'SUP-1013') via 'Rail' 'CARR-001' with ETA '2025-09-20'. Then to Detroit (supplier ID: SUP-1013, destination warehouse: WH-08) via 'Rail' 'CARR-008' with ETA '2025-09-25'. Create the initial inbound shipment to 'SUP-1013', then create a transfer shipment from there to WH-08.",
        "actions": [
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "MATR-COTT-R18"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Rail"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1020"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1020",
                    "destination_warehouse_id": "SUP-1013",
                    "carrier_id": "CARR-001",
                    "items": [
                        {
                            "sku": "MATR-COTT-R18",
                            "quantity": 10000
                        }
                    ],
                    "estimated_arrival_date": "2025-09-20"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Rail"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1013"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "destination_warehouse_id": "WH-08",
                    "carrier_id": "CARR-008",
                    "items": [
                        {
                            "sku": "MATR-COTT-R18",
                            "quantity": 10000
                        }
                    ],
                    "estimated_arrival_date": "2025-09-25"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0032"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\"",
                "\"shipment_id\": \"SHIP-0032\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_090",
        "instruction": "Establish a new distribution channel to Alaska for 'The North Store'. They require 100 'Teak Wood Dining Chair' (FURN-CHAIR-M13). Utilize warehouse WH-14. Set up the order to '1 NSC Road, Anchorage, AK' and send via 'Air' carrier 'CARR-007'. Tracking 'ALASKA-FURN-01'.'The North Store'. They need 100 'Teak Wood Dining Chair' (FURN-CHAIR-M13). Use warehouse WH-14. Create the order to '1 NSC Road, Anchorage, AK' and ship with 'Air' carrier 'CARR-007'. Tracking 'ALASKA-FURN-01'.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "The North Store",
                    "warehouse_id": "WH-14",
                    "items": [
                        {
                            "sku": "FURN-CHAIR-M13",
                            "quantity": 100
                        }
                    ],
                    "shipping_address": "1 NSC Road, Anchorage, AK"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-007",
                    "tracking_number": "ALASKA-FURN-01"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_091",
        "instruction": "Handle a drop-shipping order for 'OnlineMart' requiring 10 'Smartphone Model X' (ELEC-SMART-W23) to be dispatched directly from the supplier 'SUP-1030' to the final customer at '123 Main St, Anytown, United States'. Initially, verify inventory and supplier details, then issue an outbound order with the supplier as the 'warehouse' and utilize 'Truck' for shipping via 'Express World Delivery' (CARR-022) with the tracking number 'DROPSHIP-SMART-01'.'OnlineMart' needs 10 'Smartphone Model X' (ELEC-SMART-W23) to be sent directly from the supplier 'SUP-1030' to the end customer at '123 Main St, Anytown, United States'. First check inventory and supplier details, then create an outbound order with the supplier as the 'warehouse' and ship via 'Truck' using 'Express World Delivery' (CARR-022) and tracking number 'DROPSHIP-SMART-01'.",
        "actions": [
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1030"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "OnlineMart",
                    "warehouse_id": "SUP-1030",
                    "items": [
                        {
                            "sku": "ELEC-SMART-W23",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "123 Main St, Anytown, United States"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-022"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-022",
                    "tracking_number": "DROPSHIP-SMART-01"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_092",
        "instruction": "Coordinate the supply of 10 'Brake Kits' for the customer 'DIY Auto'. Each kit comprises 1 'Ceramic Brake Pad Set' (AUTO-PAD-B2) from supplier 'SUP-1003' and 1 'Automotive Windshield' (AUTO-GLAS-U21) from supplier 'SUP-1023'. Arrange two inbound shipments to 'WH-03' using 'CARR-003' and 'CARR-007' respectively, both expected by 2025-08-01. Once both shipments are received, assemble an outbound order for the 10 kits to be delivered to '789 DIY Garage, Detroit, MI' with the ETA of 2025-08-01.'DIY Auto' needs 10 'Brake Kits'. Each kit needs 1 'Ceramic Brake Pad Set' (AUTO-PAD-B2) from supplier 'SUP-1003' and 1 'Automotive Windshield' (AUTO-GLAS-U21) from supplier 'SUP-1023'. Create two inbound shipments to 'WH-03' using 'CARR-003' and 'CARR-007' respectively, both with ETA 2025-08-01. Once both have arrived, create an outbound order for the 10 kits to '789 DIY Garage, Detroit, MI' with ETA 2025-08-01.",
        "actions": [
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1003"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1003",
                    "destination_warehouse_id": "WH-03",
                    "carrier_id": "CARR-003",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 10
                        }
                    ],
                    "estimated_arrival_date": "2025-08-01"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1023"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1023",
                    "destination_warehouse_id": "WH-03",
                    "carrier_id": "CARR-007",
                    "items": [
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 10
                        }
                    ],
                    "estimated_arrival_date": "2025-08-01"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0031",
                    "items_received": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0032",
                    "items_received": [
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 10
                        }
                    ]
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-GLAS-U21"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "DIY Auto",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 10
                        },
                        {
                            "sku": "AUTO-GLAS-U21",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "789 DIY Garage, Detroit, MI"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_093",
        "instruction": "Perform tests with two carriers on the LA to NYC route. Dispatch 10 '8-bit Microcontroller' (ELEC-CHIP-A1) from 'WH-01' to 'Test Customer A' at '1 Test St, New York, NY' using 'Global Parcel Service' (CARR-014), with tracking number 'AB-TEST-Global Parcel Service-01'. Similarly, dispatch another 10 units to 'Test Customer B' at '2 Test St, New York, NY' using 'SwiftDelivery' (CARR-007), with tracking number 'AB-TEST-SwiftDelivery-01'. Obtain details for both of these orders.'8-bit Microcontroller' (ELEC-CHIP-A1) from 'WH-01' to 'Test Customer A' at '1 Test St, New York, NY' via 'Global Parcel Service' (CARR-014), tracking number 'AB-TEST-Global Parcel Service-01'. Send another 10 units to 'Test Customer B' at '2 Test St, New York, NY' via 'SwiftDelivery' (CARR-007), tracking number 'AB-TEST-SwiftDelivery-01'. Retrieve details for both orders.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Test Customer A",
                    "warehouse_id": "WH-01",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "1 Test St, New York, NY"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Test Customer B",
                    "warehouse_id": "WH-01",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 10
                        }
                    ],
                    "shipping_address": "2 Test St, New York, NY"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-014",
                    "tracking_number": "AB-TEST-Global Parcel Service-01"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-007",
                    "tracking_number": "AB-TEST-SwiftDelivery-01"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0018"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\"",
                "\"order_id\": \"ORD-0018\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_094",
        "instruction": "Manage inventory augmentation for 'Solar Panel 450W' (TECH-SOLR-G7) at 'WH-09' in light of a sales forecast. The forecast indicates a requirement for 2000 units for the following month. With current stock at 1200, check warehouse and supplier details, and order the shortfall from the main supplier 'SUP-1009' to be delivered by '2025-08-20' using the 'Sea' carrier 'CARR-009'.'Solar Panel 450W' (TECH-SOLR-G7) at 'WH-09'. The forecast predicts a need for 2000 units next month. Current stock is 1200. Verify warehouse and supplier details and order the difference from the primary supplier 'SUP-1009' to arrive by '2025-08-20' via 'Sea' carrier 'CARR-009'.",
        "actions": [
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "sku": "TECH-SOLR-G7"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1009"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1009",
                    "destination_warehouse_id": "WH-09",
                    "carrier_id": "CARR-009",
                    "items": [
                        {
                            "sku": "TECH-SOLR-G7",
                            "quantity": 800
                        }
                    ],
                    "estimated_arrival_date": "2025-08-20"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_095",
        "instruction": "A trade show in Las Vegas requires 5 'Articulated Robotic Arm' (TECH-ROBO-N14) and 20 'Lithium-Ion Battery Pack' (TECH-BATT-Q17) from 'WH-03'. Arrange an order for 'Trade Show Logistics' to be dispatched to the 'Las Vegas Convention Center, Las Vegas, NV'. Given this is a time-sensitive shipment, employ the 'Air' carrier 'CARR-006' with the tracking number 'TRADESHOW-LV-01'.'Articulated Robotic Arm' (TECH-ROBO-N14) and 20 'Lithium-Ion Battery Pack' (TECH-BATT-Q17) from 'WH-03'. Create an order for 'Trade Show Logistics' to 'Las Vegas Convention Center, Las Vegas, NV'. This is a time-critical shipment, so use the 'Air' carrier 'CARR-006' with tracking number 'TRADESHOW-LV-01'.",
        "actions": [
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "TECH-BATT-Q17"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Trade Show Logistics",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "TECH-ROBO-N14",
                            "quantity": 5
                        },
                        {
                            "sku": "TECH-BATT-Q17",
                            "quantity": 20
                        }
                    ],
                    "shipping_address": "Las Vegas Convention Center, Las Vegas, NV"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Air"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-006",
                    "tracking_number": "TRADESHOW-LV-01"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_096",
        "instruction": "Handle the slow-moving '8-Bit Microcontroller' (ELEC-CHIP-A1) at 'WH-03'. For optimal space utilization, transfer 200 units to the 'West Coast Distribution Hub' (WH-01) with an ETA of '2025-08-10'. Ensure inventory levels are updated at both sites through an internal transfer.'8-Bit Microcontroller' (ELEC-CHIP-A1) is slow-moving at 'WH-03'. To optimize space, move 200 units to the 'West Coast Distribution Hub' (WH-01) with ETA '2025-08-10'. Adjust inventory at both locations via an internal transfer.",
        "actions": [
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "AdjustInventory",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "ELEC-CHIP-A1",
                    "quantity_change": -200,
                    "reason": "Internal Transfer to WH-01 for space optimization"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "Internal",
                    "destination_warehouse_id": "WH-01",
                    "carrier_id": "Internal Transfer",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 200
                        }
                    ],
                    "estimated_arrival_date": "2025-08-10"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0031",
                    "items_received": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 200
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0031\", \"status\": \"Received\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_097",
        "instruction": "The customer 'Book Depository' has an order 'ORD-0010' that remains pending. They wish to include 10 units of 'Industrial Paper Roll' (MANU-PAPR-F6) in this order. Cancel the current order and initiate a new one with the modified quantity (210 units) to the same address. Arrange shipping via 'Truck' using carrier 'CARR-003' with tracking number 'BOOK-DEPOT-UPDATE-01'.'Book Depository' has order 'ORD-0010' which is still pending. They want to add 10 units of 'Industrial Paper Roll' (MANU-PAPR-F6) to this order. Cancel the existing order and create a new one with the updated quantity (210 units) to the same address. Ship via 'Truck' carrier 'CARR-003' with tracking number 'BOOK-DEPOT-UPDATE-01'.",
        "actions": [
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "CancelOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "GetInventoryBySku",
                "arguments": {
                    "sku": "MANU-PAPR-F6"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-08",
                    "sku": "MANU-PAPR-F6"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Book Depository",
                    "warehouse_id": "WH-08",
                    "items": [
                        {
                            "sku": "MANU-PAPR-F6",
                            "quantity": 210
                        }
                    ],
                    "shipping_address": "12 Writer's Block, Mumbai, India"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-003",
                    "tracking_number": "BOOK-DEPOT-UPDATE-01"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_098",
        "instruction": "Due to a port strike, the port of San Diego is closed. Route inbound shipment 'SHIP-0001' through an alternative 'Sea' carrier. Update the shipment to use the new carrier 'CARR-011' and redirect to 'WH-02'. Then, arrange an inbound shipment with an 'Internal' supplied ID, which includes 1200 units of the item (SKU: ELEC-CHIP-A1) with an ETA of '2025-07-05'. Following that, employ 'Truck' transport carrier 'CARR-014' from Portland to deliver to the initial destination 'WH-01'.'SHIP-0001' must be re-routed. Use an alternative 'Sea' carrier. Update the shipment to use the new carrier 'CARR-011' and destination 'WH-02'. Then, create an inbound shipment with an 'Internal' supplied ID, which includes 1200 units of the item (SKU: ELEC-CHIP-A1) and has an ETA of '2025-07-05'. Then, use 'Truck' transport carrier 'CARR-014' from Portland to the original destination 'WH-01'.",
        "actions": [
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Sea"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-011"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "carrier_id": "CARR-011",
                    "carrier_name": "Global Ocean Carriers",
                    "carrier_scac": "GOCN",
                    "destination_warehouse_id": "WH-02",
                    "destination_warehouse_name": "Northwest Fulfillment Center",
                    "destination_address": "321 Port Boulevard N",
                    "destination_city": "Portland"
                },
            },
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-014"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "Internal",
                    "destination_warehouse_id": "WH-01",
                    "carrier_id": "CARR-014",
                    "items": [
                        {
                            "sku": "ELEC-CHIP-A1",
                            "quantity": 1200
                        }
                    ],
                    "estimated_arrival_date": "2025-07-05"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "GetInboundShipmentDetails",
                "arguments": {
                    "shipment_id": "SHIP-0031"
                }
            }
        ],
        "outputs": [
                "\"shipment_id\": \"SHIP-0001\"",
                "\"shipment_id\": \"SHIP-0031\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_099",
        "instruction": "Manage a request from the customer 'Vintage Cars Club' for 5 'Ceramic Brake Pad Set' (AUTO-PAD-B2). The units in storage are obsolete. Identify supplier 'SUP-1003' and review their details. Set up an inbound shipment to 'WH-03' for new units using carrier 'CARR-003' with an ETA of '2025-08-20', then complete the order delivery to '1 Classic Car Lane, Monterey, OR' via carrier 'CARR-008' and tracking number 'VINTAGE-PADS-09'.'Vintage Cars Club' needs 5 'Ceramic Brake Pad Set' (AUTO-PAD-B2). The stored units of this product are obsolete. Find the supplier 'SUP-1003' and check their details. Create an inbound shipment to 'WH-03' for new units of the product using carrier 'CARR-003' with ETA '2025-08-20' and then fulfill the order to '1 Classic Car Lane, Monterey, OR' using carrier 'CARR-008' and tracking number 'VINTAGE-PADS-09'.",
        "actions": [
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "GetSupplierInfo",
                "arguments": {
                    "supplier_id": "SUP-1003"
                },
            },
            {
                "name": "CreateInboundShipment",
                "arguments": {
                    "supplier_id": "SUP-1003",
                    "destination_warehouse_id": "WH-03",
                    "carrier_id": "CARR-003",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 5
                        }
                    ],
                    "estimated_arrival_date": "2025-08-20"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "ReceiveInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0031",
                    "items_received": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 5
                        }
                    ]
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Vintage Cars Club",
                    "warehouse_id": "WH-03",
                    "items": [
                        {
                            "sku": "AUTO-PAD-B2",
                            "quantity": 5
                        }
                    ],
                    "shipping_address": "1 Classic Car Lane, Monterey, OR"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-008",
                    "tracking_number": "VINTAGE-PADS-09"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
    ,
    {
        "annotator": samarthkulshrestha,
        "user_id": "USR_100",
        "instruction": "Coordinate a donation of 1000 'Organic Cotton T-Shirt' (APRL-TSHT-O15) to the charity 'Goodwill Givers'. Generate an order from 'WH-04' to '1 Charity Plaza, Washington D.C.' with a total order value of 0. Organize shipping using 'Truck' carrier 'CARR-008' and tracking number 'DONATION-DC-01'.'Goodwill Givers' is receiving a donation of 1000 'Organic Cotton T-Shirt' (APRL-TSHT-O15). Create an order from 'WH-04' to '1 Charity Plaza, Washington D.C.' with the order's total value being 0. Ship via 'Truck' carrier 'CARR-008' and tracking number 'DONATION-DC-01'.",
        "actions": [
            {
                "name": "GetWarehouseInfo",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetInventoryInWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "sku": "APRL-TSHT-O15"
                },
            },
            {
                "name": "CreateOutboundOrder",
                "arguments": {
                    "customer_name": "Goodwill Givers",
                    "warehouse_id": "WH-04",
                    "items": [
                        {
                            "sku": "APRL-TSHT-O15",
                            "quantity": 1000
                        }
                    ],
                    "total_value": 0,
                    "shipping_address": "1 Charity Plaza, Washington D.C."
                },
            },
            {
                "name": "FindCarriers",
                "arguments": {
                    "transport_mode": "Truck"
                },
            },
            {
                "name": "GetCarrierDetails",
                "arguments": {
                    "carrier_id": "CARR-008"
                },
            },
            {
                "name": "UpdateOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017",
                    "new_status": "Shipped",
                    "carrier_id": "CARR-008",
                    "tracking_number": "DONATION-DC-01"
                },
            },
            {
                "name": "GetOutboundOrderStatus",
                "arguments": {
                    "order_id": "ORD-0017"
                }
            }
        ],
        "outputs": [
                "\"order_id\": \"ORD-0017\""
        ]
    }
]
