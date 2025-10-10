from typing import Any, Dict, List, Optional
from domains.dto import Action, Task


TASKS = [
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_001",
        instruction="Mercy General Hospital needs 100 Influenza Vaccine (PHRM-VACC-D4) and 50 Oncology Drug A (PHRM-DRUG-S19). First find warehouses with Cold Chain capabilities, then check inventory availability for both items at the first suitable warehouse, create the order (ORD-0017) for Mercy General to 789 Health Blvd, Atlanta, GA, and finally assign the Air carrier 'CARR-006' with tracking MED-PRIORITY-001. Finally, report the order ID for the new order",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "Cold Chain (2-8°C)"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-06",
                "sku": "PHRM-VACC-D4"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-06",
                "sku": "PHRM-DRUG-S19"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Mercy General",
                "warehouse_id": "WH-06",
                "items": [
                    {"sku": "PHRM-VACC-D4", "quantity": 100},
                    {"sku": "PHRM-DRUG-S19", "quantity": 50}
                ],
                "shipping_address": "789 Health Blvd, Atlanta, GA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "MED-PRIORITY-001"
            })
        ],
        outputs=["ORD-0017"]
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_002",
        instruction="Process arrival of 650 Solar Panels (TECH-SOLR-G7) in shipment SHIP-0009 at Phoenix Renewable Warehouse (WH-09), then immediately fulfill an order for 100 panels to Solaris Inc at 1 Sun Way, Phoenix, AZ. First receive the shipment, verify new inventory levels, create the outbound order, find the best Truck carrier, and ship with tracking SOLAR-RUSH-100. Report the new order ID",
        actions=[
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0009",
                "items_received": [{"sku": "TECH-SOLR-G7", "quantity": 650}]
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-09",
                "sku": "TECH-SOLR-G7"
            }),
            Action(name="get_inventory_by_sku", kwargs={
                "sku": "TECH-SOLR-G7"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Solaris Inc",
                "warehouse_id": "WH-09",
                "items": [{"sku": "TECH-SOLR-G7", "quantity": 100}],
                "shipping_address": "1 Sun Way, Phoenix, AZ"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "SOLAR-RUSH-100"
            })
        ],
        outputs=["ORD-0017"]
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_003",
        instruction="Perform a cycle count for 'Teak Wood Dining Chair' (FURN-CHAIR-M13) at 'WH-14'. The system shows 600 units, but a physical count reveals 595. Adjust the inventory with reason 'Cycle Count Adjustment'. Then, check if the new quantity is below the reorder point and report the final count.",
        actions=[
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-14"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-14", "sku": "FURN-CHAIR-M13"}),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-14",
                "sku": "FURN-CHAIR-M13",
                "quantity_change": -5,
                "reason": "Cycle Count Adjustment"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-14", "sku": "FURN-CHAIR-M13"}),
        ],
        outputs=['{"inventory_id": "INV-0013", "quantity_on_hand": 595, "reorder_point": 150}']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_004",
        instruction="Handle delayed Smartphone X shipment crisis. First find inbound shipments from SUP-1002 to Seattle warehouse (WH-02), update the found shipment status to 'Delayed', check current inventory of ELEC-SMART-W23 at that warehouse, and if stock is below 5000 units, use the Truck carrier 'CARR-014' and create emergency inbound shipment for 300 units arriving 2024-08-01. Retrieve final inbound shipment details.",
        actions=[
            Action(name="find_inbound_shipments", kwargs={
                "supplier_id": "SUP-1002",
                "warehouse_id": "WH-02"
            }),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0002",
                "status": "Delayed"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-02",
                "sku": "ELEC-SMART-W23"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1002",
                "destination_warehouse_id": "WH-02",
                "carrier_id": "CARR-014",
                "items": [{"sku": "ELEC-SMART-W23", "quantity": 300}],
                "estimated_arrival_date": "2024-08-01"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"})
        ],
        outputs=['"shipment_id": "SHIP-0031", "supplier_id": "SUP-1002"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_005",
        instruction="TechStall wants 20 units of 8-bit Microcontroller (SKU: ELEC-CHIP-A1). First check inventory at Los Angeles warehouse (WH-01), create the order for TechStall to 789 Tech Way, Silicon Valley, CA, verify the order was created successfully, check updated available quantity after order creation, and assign Air carrier CARR-006 with tracking TECH-FAST-020.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "TechStall",
                "warehouse_id": "WH-01",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 20}],
                "shipping_address": "789 Tech Way, Silicon Valley, CA"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "TECH-FAST-020"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_006",
        instruction="Handle Industrial Solvent (CHEM-SOLV-K11) return from order ORD-0014. Customer returns 2 units. First get order details to verify warehouse, check current inventory at that warehouse, add returned items back to inventory with reason 'Customer Return', then write off same 2 units as damaged with reason 'Damaged Goods', and verify final inventory level.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0014"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-13",
                "sku": "CHEM-SOLV-K11"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-13",
                "sku": "CHEM-SOLV-K11",
                "quantity_change": 2,
                "reason": "Customer Return"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-13",
                "sku": "CHEM-SOLV-K11",
                "quantity_change": -2,
                "reason": "Damaged Goods"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-13",
                "sku": "CHEM-SOLV-K11"
            })
        ],
        outputs=['"inventory_id": "INV-0011", "sku": "CHEM-SOLV-K11", "warehouse_id": "WH-13"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_007",
        instruction="Home Essentials wants 10 Ceramic Break Pad Set (AUTO-PAD-B2). First find USA warehouses with Heavy Equipment Handling capabilities. Check inventory for this SKU at the first warehouse found, if insufficient check next warehouse, create order for Home Essentials to 123 Smart Home, Austin, TX, and ship with best Truck carrier using tracking AUTO-PAD-010.",
        actions=[
            Action(name="find_warehouses", kwargs={
                "country": "USA",
                "special_capability": "Heavy Equipment Handling"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-PAD-B2"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Home Essentials",
                "warehouse_id": "WH-03",
                "items": [{"sku": "AUTO-PAD-B2", "quantity": 10}],
                "shipping_address": "123 Smart Home, Austin, TX"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "AUTO-PAD-010"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_008",
        instruction="Book Nook needs 200 8-bit Microcontroller (ELEC-CHIP-A1) split between warehouses WH-01 and WH-03. First check inventory at both warehouses, create first order for 100 units from WH-01 with tracking number CHIP-EAST-100 to 456 Reading Lane, Boston, MA, create second order for 100 units from WH-03 with tracking number CHIP-WEST-100 to same address, and assign different carriers (CARR-014 and CARR-007) to each order for load balancing.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Book Nook",
                "warehouse_id": "WH-01",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 100}],
                "shipping_address": "456 Reading Lane, Boston, MA"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Book Nook",
                "warehouse_id": "WH-03",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 100}],
                "shipping_address": "456 Reading Lane, Boston, MA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "CHIP-EAST-100"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0018",
                "new_status": "Shipped",
                "carrier_id": "CARR-007",
                "tracking_number": "CHIP-WEST-100"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"',
                 '"order_id": "ORD-0018", "new_status": "Shipped"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_009",
        instruction="Innovate Inc. needs specialized equipment: 15 units of Articulated Robotic Arm (TECH-ROBO-N14) and 5 Lithium-Ion Battery Packs (TECH-BATT-Q17). First find warehouses with Heavy Equipment Handling capability, check inventory for both items at suitable warehouse, create order for Innovate Inc to 789 Innovation Drive, Cambridge, MA, with tracking number 'INNOV-RAIL-001' and ship with Rail carrier 'CARR-008' for heavy equipment.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "Heavy Equipment Handling"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "TECH-ROBO-N14"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "TECH-BATT-Q17"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Innovate Inc.",
                "warehouse_id": "WH-03",
                "items": [
                    {"sku": "TECH-ROBO-N14", "quantity": 15},
                    {"sku": "TECH-BATT-Q17", "quantity": 5}
                ],
                "shipping_address": "789 Innovation Drive, Cambridge, MA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Rail"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-008",
                "tracking_number": "INNOV-RAIL-001"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_010",
        instruction="Global Beverages wants 1000 units of Sparkling Mineral Water (BEVG-WATR-S1). First find suppliers in Beverages category, and get detailed performance information for supplier 'SUPP-1018', find all Sea carriers and select the one with the highest on-time-delivery percentage, create inbound shipment to WH-15 using the chosen carrier for arrival on 2024-09-01, and verify shipment creation.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Beverages"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1018"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Sea"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-012"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1018",
                "destination_warehouse_id": "WH-15",
                "carrier_id": "CARR-012",
                "items": [{"sku": "BEVG-WATR-S1", "quantity": 1000}],
                "estimated_arrival_date": "2024-09-01"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"})
        ],
        outputs=['"shipment_id": "SHIP-0031", "supplier_id": "SUP-1018", "destination_warehouse_id": "WH-15"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_011",
        instruction="Transfer 50 Industrial Solvent (CHEM-SOLV-K11) from WH-13 to WH-03. First check current inventory at source warehouse, reduce inventory at WH-13 with reason 'Internal Transfer to WH-03', create inbound shipment record for internal transfer to WH-03 arriving 2024-07-28, and verify both inventory adjustment and shipment creation.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-13",
                "sku": "CHEM-SOLV-K11"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-13",
                "sku": "CHEM-SOLV-K11",
                "quantity_change": -50,
                "reason": "Internal Transfer to WH-03"
            }),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "Internal",
                "destination_warehouse_id": "WH-03",
                "carrier_id": "Internal Transfer",
                "items": [{"sku": "CHEM-SOLV-K11", "quantity": 50}],
                "estimated_arrival_date": "2024-07-28"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-13",
                "sku": "CHEM-SOLV-K11"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"})
        ],
        outputs=['"shipment_id": "SHIP-0031"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_012",
        instruction="Fashion Forward needs 10 Leather Handbags (APRL-BAG-E5) from WH-07 and 20 Cotton Tshirts (APRL-TSHT-O15) from WH-04, USA warehouses. First find USA warehouses, check inventory for both items at each warehouse until finding the warehouses where the respective items are in stock, create order for Fashion Forward to 123 Style Street, Miami, FL, with tracking numbers ‘FASHION-AIR-001’ and 'FASHION-AIR-002'. Ship via Air carrier for fast delivery. Choose the carrier that supports the Pharma service level and has the highest average rating.",
        actions=[
            Action(name="find_warehouses", kwargs={"country": "USA"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-07",
                "sku": "APRL-BAG-E5"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-04",
                "sku": "APRL-TSHT-O15"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Fashion Forward",
                "warehouse_id": "WH-07",
                "items": [
                    {"sku": "APRL-BAG-E5", "quantity": 10},
                ],
                "shipping_address": "123 Style Street, Miami, FL"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Fashion Forward",
                "warehouse_id": "WH-04",
                "items": [
                    {"sku": "APRL-TSHT-O15", "quantity": 20}
                ],
                "shipping_address": "123 Style Street, Miami, FL"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "FASHION-AIR-001"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0018",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "FASHION-AIR-002"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"',
                 '"order_id": "ORD-0018", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_013",
        instruction="Handle Dining Chair (FURN-CHAIR-M13) return from order ORD-0015. Customer returns 1 damaged unit. First get order details, check current inventory at order's warehouse, add returned unit with reason 'Customer Return', immediately adjust same unit out as damaged goods, and verify final inventory.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0015"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-14",
                "sku": "FURN-CHAIR-M13"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-14",
                "sku": "FURN-CHAIR-M13",
                "quantity_change": 1,
                "reason": "Customer Return"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-14",
                "sku": "FURN-CHAIR-M13",
                "quantity_change": -1,
                "reason": "Damaged Goods"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-14",
                "sku": "FURN-CHAIR-M13"
            })
        ],
        outputs=['{"inventory_id": "INV-0013", "sku": "FURN-CHAIR-M13"}']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_014",
        instruction="Gamerz Inc. needs 5 Solar Panel 450W (ELEC-SMART-W23). First find USA warehouses, check inventory at each warehouse sequentially until finding one with adequate stock, create order for Gamerz Inc to 1337 Gamer Way, Austin, TX, with tracking number 'GAMER-FAST-005' and ship with carrier 'CARR-006'.",
        actions=[
            Action(name="find_warehouses", kwargs={"country": "USA"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "ELEC-SMART-W23"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-02",
                "sku": "ELEC-SMART-W23"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Gamerz Inc.",
                "warehouse_id": "WH-02",
                "items": [{"sku": "ELEC-SMART-W23", "quantity": 5}],
                "shipping_address": "1337 Gamer Way, Austin, TX"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "GAMER-FAST-005"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_015",
        instruction="The Daily Grind needs 500 8-Bit Microcontrollers (ELEC-CHIP-A1) split between WH-01 and WH-03. First check inventory at both warehouses, create first order for 250 units from WH-01 to 789 Cafe Ave, Seattle, WA (tracking number: DAILY-1-250), create second order for 250 units from WH-03 to same address (tracking number: DAILY-2-250), and coordinate delivery timing. Ship using the carrier that supports Next Day Air delivery service",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "The Daily Grind",
                "warehouse_id": "WH-01",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 250}],
                "shipping_address": "789 Cafe Ave, Seattle, WA"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "The Daily Grind",
                "warehouse_id": "WH-03",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 250}],
                "shipping_address": "789 Cafe Ave, Seattle, WA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "DAILY-1-250"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0018",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "DAILY-2-250"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"',
                 '"order_id": "ORD-0018", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_016",
        instruction="BuildIt Better needs 10 Power Drills (TECH-ROBO-N14) and 2 Circular Saws (MATR-COTT-R18). First find USA warehouses, check inventory for both items at each warehouse until finding one with both in stock, create orders for BuildIt Better to 456 Construction Way, Denver, CO, (tracking numbers BUILD-TOOLS-012 and BUILD-TOOLS-013) and ship via Truck carrier (CARR-014) for construction site delivery.",
        actions=[
            Action(name="find_warehouses", kwargs={"country": "USA"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "TECH-ROBO-N14"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "MATR-COTT-R18"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-02",
                "sku": "TECH-ROBO-N14"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-02",
                "sku": "MATR-COTT-R18"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "TECH-ROBO-N14"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "MATR-COTT-R18"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-04",
                "sku": "MATR-COTT-R18"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "BuildIt Better",
                "warehouse_id": "WH-03",
                "items": [
                    {"sku": "TECH-ROBO-N14", "quantity": 10},
                ],
                "shipping_address": "456 Construction Way, Denver, CO"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "BuildIt Better",
                "warehouse_id": "WH-04",
                "items": [
                    {"sku": "MATR-COTT-R18", "quantity": 2}
                ],
                "shipping_address": "456 Construction Way, Denver, CO"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "BUILD-TOOLS-012"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0018",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "BUILD-TOOLS-013"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"',
                 '"order_id": "ORD-0018", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_017",
        instruction="A new hospital, 'Mercy West', requires a critical setup order: 150 units of Influenza Vaccine (PHRM-VACC-D4) and 75 units of Oncology Drug A (PHRM-DRUG-S19). First, find a warehouse with both 'Cold Chain (2-8°C)' and 'Pharmaceutical Handling' capabilities. Check inventory for both items at the identified warehouse (WH-06). Create the outbound order for 'Mercy West' to '987 Health Parkway, Phoenix, AZ'. Find the highest-rated 'Air' carrier that supports the Pharma service level. Ship the order with this carrier and assign the tracking number 'CRITICAL-CARE-987'. Finally, verify the new available inventory for both SKUs in the warehouse.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capabilities": ["Cold Chain (2-8°C)", "Pharmaceutical Handling"]}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-VACC-D4"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-DRUG-S19"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Mercy West",
                "warehouse_id": "WH-06",
                "items": [
                    {"sku": "PHRM-VACC-D4", "quantity": 150},
                    {"sku": "PHRM-DRUG-S19", "quantity": 75}
                ],
                "shipping_address": "987 Health Parkway, Phoenix, AZ"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "CRITICAL-CARE-987"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-VACC-D4"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-DRUG-S19"}),
        ],
        outputs=['{"inventory_id": "INV-0004"}', '{"inventory_id": "INV-0019"}']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_018",
        instruction="Transfer 50 Cotton Tshirts (APRL-TSHT-O15) from WH-04 to WH-07 for regional balancing. First check inventory at source warehouse, adjust inventory at WH-04 with transfer reason, create internal shipment record for transfer arriving 2024-07-31, verify inventory change, and confirm shipment creation.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-04",
                "sku": "APRL-TSHT-O15"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-04",
                "sku": "APRL-TSHT-O15",
                "quantity_change": -50,
                "reason": "Internal Transfer to WH-07"
            }),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "Internal",
                "destination_warehouse_id": "WH-07",
                "carrier_id": "Internal Transfer",
                "items": [{"sku": "APRL-TSHT-O15", "quantity": 50}],
                "estimated_arrival_date": "2024-07-31"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-04",
                "sku": "APRL-TSHT-O15"
            })
        ],
        outputs=['{"inventory_id": "INV-0015", "sku": "APRL-TSHT-O15", "warehouse_id": "WH-04"}']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_019",
        instruction="Handle Fresh Cut Roses (FOOD-FLWR-X24) return from order ORD-0011. Customer returns 1 damaged unit. First get order details to identify warehouse, check current inventory, add returned unit with reason 'Customer Return', write off same unit as damaged, and verify final inventory level.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0011"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-10",
                "sku": "FOOD-FLWR-X24"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-10",
                "sku": "FOOD-FLWR-X24",
                "quantity_change": 1,
                "reason": "Customer Return"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-10",
                "sku": "FOOD-FLWR-X24",
                "quantity_change": -1,
                "reason": "Damaged Goods"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-10",
                "sku": "FOOD-FLWR-X24"
            })
        ],
        outputs=['{"inventory_id": "INV-0024", "sku": "FOOD-FLWR-X24", "warehouse_id": "WH-10"}']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_020",
        instruction="Art Supplies Co. needs 100 Frozen Tuna Loin (FOOD-FISH-H8) from a USA warehouse. First find all USA warehouses which have Perishables Handling capability, check inventory at each location sequentially, create order (tracking number: 'ART-AIR-100') from warehouse with adequate stock to 123 Art Street, Portland, OR, and arrange Air shipping with CARR-006 for art supplies.",
        actions=[
            Action(name="find_warehouses", kwargs={"country": "USA", "special_capability": "Perishables Handling"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-10",
                "sku": "FOOD-FISH-H8"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Art Supplies Co.",
                "warehouse_id": "WH-10",
                "items": [{"sku": "FOOD-FISH-H8", "quantity": 100}],
                "shipping_address": "123 Art Street, Portland, OR"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "ART-AIR-100"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_021",
        instruction="Healthy Living needs fresh produce: 50 Frozen Tuna (FOOD-FISH-H8) and 100 Fresh Cut Roses (FOOD-FLWR-X24) with cold chain requirements. First find Cold Chain (0-4°C) capable warehouses, check inventory for both items at suitable warehouse, create order (tracking number: FRESH-COLD-150) for Healthy Living to 789 Wellness Way, Los Angeles, CA, and arrange refrigerated transport via carrier CARR-014.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "Cold Chain (0-4°C)"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-10",
                "sku": "FOOD-FISH-H8"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-10",
                "sku": "FOOD-FLWR-X24"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Healthy Living",
                "warehouse_id": "WH-10",
                "items": [
                    {"sku": "FOOD-FISH-H8", "quantity": 50},
                    {"sku": "FOOD-FLWR-X24", "quantity": 100}
                ],
                "shipping_address": "789 Wellness Way, Los Angeles, CA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "FRESH-COLD-150"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_022",
        instruction="Transfer 20 Diamond Core Drill Bits (HEVY-DRIL-I9) from WH-11 to WH-03 for demand balancing. First get warehouse information, then verify current stock at source, reduce inventory at WH-11 with appropriate transfer reason, create internal shipment for transfer arriving 2024-07-30, and confirm both inventory adjustment and shipment record.",
        actions=[
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-11"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-11",
                "sku": "HEVY-DRIL-I9"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-11",
                "sku": "HEVY-DRIL-I9",
                "quantity_change": -20,
                "reason": "Internal Transfer to WH-03"
            }),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-03"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "Internal",
                "destination_warehouse_id": "WH-03",
                "carrier_id": "Internal Transfer",
                "items": [{"sku": "HEVY-DRIL-I9", "quantity": 20}],
                "estimated_arrival_date": "2024-07-30"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"})
        ],
        outputs=['"shipment_id": "SHIP-0031", "supplier_id": "Internal", "destination_warehouse_id": "WH-03"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_023",
        instruction="Bookworm wants 50 units of Ceramic Floor Tile (BLDG-TILE-J10) from highest stock location. First check inventory across all warehouses, identify location with most stock, verify adequate inventory at that warehouse, create order to 123 Reading Rainbow, San Francisco, CA, and ship via standard carrier with tracking number BOOK-WORM-050.",
        actions=[
            Action(name="get_inventory_by_sku", kwargs={"sku": "BLDG-TILE-J10"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-12",
                "sku": "BLDG-TILE-J10"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Bookworm",
                "warehouse_id": "WH-12",
                "items": [{"sku": "BLDG-TILE-J10", "quantity": 50}],
                "shipping_address": "123 Reading Rainbow, San Francisco, CA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Parcel"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-014"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "BOOK-WORM-050"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_024",
        instruction="Process Luxury Watch (LUX-WATCH-L12) arrival in high-security shipment SHIP-0014 at WH-07 with 10 units, then fulfill premium order ORD-0010. First get shipment details, receive high-value shipment, verify secure inventory update, check priority order status, and ship with premium Air carrier tracking EK-CARGO-457.",
        actions=[
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0014"}),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0014",
                "items_received": [{"sku": "LUX-WATCH-L12", "quantity": 10}]
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-07",
                "sku": "LUX-WATCH-L12"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0010"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0010",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "EK-CARGO-457"
            })
        ],
        outputs=['"order_id": "ORD-0010", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_025",
        instruction="Handle Ceramic Floor Time (BLDG-TILE-J10) return from order ORD-0013. Customer returns 1 defective unit. First get order information to identify warehouse, check current inventory levels, add returned unit with reason 'Customer Return', immediately write off as defective, and verify inventory adjustment.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0013"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-12",
                "sku": "BLDG-TILE-J10"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-12",
                "sku": "BLDG-TILE-J10",
                "quantity_change": 1,
                "reason": "Customer Return"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-12",
                "sku": "BLDG-TILE-J10",
                "quantity_change": -1,
                "reason": "Damaged Goods"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-12",
                "sku": "BLDG-TILE-J10"
            })
        ],
        outputs=['{"inventory_id": "INV-0010", "sku": "BLDG-TILE-J10", "warehouse_id": "WH-12"}']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_026",
        instruction="The Green Thumb needs 200 units of Oncology Drug A (PHRM-DRUG-S19) from a USA warehouse. First find all USA warehouses with Pharmaceutical Handling capabilities, check inventory at each location systematically, create order from warehouse with sufficient stock to 456 Garden Lane, Austin, TX, and arrange Truck delivery with carrier 'CARR-014' and tracking number ONCO-DRUG-200.",
        actions=[
            Action(name="find_warehouses", kwargs={"country": "USA", "special_capability": "Pharmaceutical Handling"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-06",
                "sku": "PHRM-DRUG-S19"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={  # will return error with no inventory in WH-16
                "warehouse_id": "WH-16",
                "sku": "PHRM-DRUG-S19"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "The Green Thumb",
                "warehouse_id": "WH-06",
                "items": [{"sku": "PHRM-DRUG-S19", "quantity": 200}],
                "shipping_address": "456 Garden Lane, Austin, TX"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "ONCO-DRUG-200"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_027",
        instruction="A customer 'Future Auto' needs 10 'Articulated Robotic Arm' (TECH-ROBO-N14) and 50 'Lithium-Ion Battery Pack' (TECH-BATT-Q17). Find a warehouse that has 'Heavy Equipment Handling' and 'VMI (Vendor Managed Inventory)' capabilities. Check inventory for both SKUs at 'Chicago Parts Depot' (WH-03). Create the order for 'Future Auto' to '1 Robot Way, Detroit, MI'. Ship via 'DB Schenker' (CARR-003) using 'Rail' transport with tracking 'AUTO-ROBOT-RAIL-1'.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capabilities": ["Heavy Equipment Handling", "VMI (Vendor Managed Inventory)"]}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "TECH-ROBO-N14"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "TECH-BATT-Q17"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Future Auto",
                "warehouse_id": "WH-03",
                "items": [
                    {"sku": "TECH-ROBO-N14", "quantity": 10},
                    {"sku": "TECH-BATT-Q17", "quantity": 50}
                ],
                "shipping_address": "1 Robot Way, Detroit, MI"
            }),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-003"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-003",
                "tracking_number": "AUTO-ROBOT-RAIL-1"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017", "status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_028",
        instruction="The Toy Box needs 1000 units of Malbec Wine (BEVG-WINE-P16). Find a warehouse with the type 'Beverage Distribution', check inventory, and create order for 1000 units from that warehouse to 789 Playtime Ave, Orlando, FL (tracking number: TOY-EAST-1000) with 'Air' carrier 'CARR-014' and coordinate deliveries for toy store.",
        actions=[
            Action(name="find_warehouses", kwargs={}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-15",
                "sku": "BEVG-WINE-P16"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "The Toy Box",
                "warehouse_id": "WH-15",
                "items": [{"sku": "BEVG-WINE-P16", "quantity": 1000}],
                "shipping_address": "789 Playtime Ave, Orlando, FL"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "TOY-EAST-1000"
            }),
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_029",
        instruction="The Cellar wine shop needs climate-controlled delivery: 100 Red Wine (BEVG-WINE-P16). First find Temperature Controlled (10-15°C) warehouses, check inventory for the wine at a suitable location, create order for The Cellar to 123 Vino Way, Napa, CA, (tracking number: WINE-TEMP-100) and arrange temperature-controlled, Next Day Air shipping.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "Temperature Control (10-15°C)"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-15"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-15",
                "sku": "BEVG-WINE-P16"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "The Cellar",
                "warehouse_id": "WH-15",
                "items": [
                    {"sku": "BEVG-WINE-P16", "quantity": 100},
                ],
                "shipping_address": "123 Vino Way, Napa, CA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "WINE-TEMP-100"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_030",
        instruction="Handle critical hazmat shipment for ChemCorp requiring 100 Industrial Solvent (CHEM-SOLV-K11). First find Chemical suppliers and get performance data, locate USA hazmat certified warehouses, create inbound shipment from best supplier to hazmat warehouse using top (highest on-time-delivery percentage) Sea carrier for arrival 2024-08-15, verify hazmat compliance, get detailed warehouse capabilities, and confirm all safety protocols are met.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Chemicals"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1013"}),
            Action(name="find_warehouses", kwargs={
                "country": "USA",
                "special_capability": "Hazmat Certified (Classes 3, 6.1, 9)"
            }),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-13"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Sea"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-012"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1013",
                "destination_warehouse_id": "WH-13",
                "carrier_id": "CARR-012",
                "items": [{"sku": "CHEM-SOLV-K11", "quantity": 100}],
                "estimated_arrival_date": "2024-08-15"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"})
        ],
        outputs=['"shipment_id": "SHIP-0031", "supplier_id": "SUP-1013", "destination_warehouse_id": "WH-13", "carrier_id": "CARR-012"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_031",
        instruction="Luxury Retail Group places premium order for 50 Leather Handbags (APRL-BAG-E5) and 100 Automatic Watch Movements (LUX-WATCH-L12). First find High-Value Cage warehouses, and choose the one with the lower utilization percentage. Then, check inventory for both luxury items at secure facility, create order for Luxury Retail Group to 1 Rodeo Drive, Beverly Hills, CA, find Air carriers and ship with carrier 'CARR-006' using tracking EK-CARGO-456, and provide complete order details.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "High-Value Cage"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-07",
                "sku": "APRL-BAG-E5"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-07",
                "sku": "LUX-WATCH-L12"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Luxury Retail Group",
                "warehouse_id": "WH-07",
                "items": [
                    {"sku": "APRL-BAG-E5", "quantity": 50},
                    {"sku": "LUX-WATCH-L12", "quantity": 100}
                ],
                "shipping_address": "1 Rodeo Drive, Beverly Hills, CA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-006"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "EK-CARGO-456"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=['"order_id": "ORD-0017", "status": "Shipped", "warehouse_id": "WH-07"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_032",
        instruction="Chicago Parts Depot (WH-03) earthquake damage assessment and recovery. 10% of AUTO-PAD-B2 and 5% of AUTO-GLAS-U21 inventory damaged. First check current inventory for both products at WH-03, calculate damage quantities (80 B2, 10 U21), adjust inventory for both with reason 'Damaged in Natural Disaster', check total inventory across all warehouses for both SKUs, if any SKU below 1000 total, find Automotive supplier with the lowest standard lead time, create emergency shipment of 500 each low SKU to Los Angeles (WH-01) via FedEx arriving 2024-08-10, and verify emergency shipment creation.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-PAD-B2"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-PAD-B2",
                "quantity_change": -80,
                "reason": "Damaged in Natural Disaster"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-GLAS-U21"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-GLAS-U21",
                "quantity_change": -10,
                "reason": "Damaged in Natural Disaster"
            }),
            Action(name="get_inventory_by_sku", kwargs={"sku": "AUTO-PAD-B2"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "AUTO-GLAS-U21"}),
            Action(name="find_suppliers", kwargs={"product_categories": ["Automotive"]}),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1023",
                "destination_warehouse_id": "WH-01",
                "carrier_id": "CARR-007",
                "items": [
                    {"sku": "AUTO-PAD-B2", "quantity": 500},
                    {"sku": "AUTO-GLAS-U21", "quantity": 500}
                ],
                "estimated_arrival_date": "2024-08-10"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"})
        ],
        outputs=['"shipment_id": "SHIP-0031", "supplier_id": "SUP-1023", "destination_warehouse_id": "WH-01"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_033",
        instruction="Consolidate 8-Bit Microcontroller (ELEC-CHIP-A1) inventory for flash sale preparation. First check total inventory across all locations, identify all warehouses with this SKU, transfer all units from other warehouses to Los Angeles (WH-01) with reason 'Internal Transfer to WH-01', create internal shipment records for transfers arriving on 2024-07-26 respectively. Receive the shipment. Verify inventory adjustments and shipment creations, and confirm consolidated inventory at WH-01.",
        actions=[
            Action(name="get_inventory_by_sku", kwargs={"sku": "ELEC-CHIP-A1"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-03",
                "sku": "ELEC-CHIP-A1",
                "quantity_change": -8000,
                "reason": "Internal Transfer to WH-01"
            }),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "Internal",
                "destination_warehouse_id": "WH-01",
                "carrier_id": "Internal Transfer",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 8000}],
                "estimated_arrival_date": "2024-07-26"
            }),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0031",
                "items_received": [{"sku": "ELEC-CHIP-A1", "quantity": 8000}]
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "ELEC-CHIP-A1"
            })
        ],
        outputs=['"inventory_id": "INV-0001", "sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01", "quantity_on_hand": 16200}']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_034",
        instruction="A customer, 'AutoRestore', has returned 15 'Automatic Watch Movement' (LUX-WATCH-L12) from order ORD-0008 due to a mismatch. The items are undamaged. First, get the order details to confirm the origin warehouse (WH-07). Adjust the inventory at WH-07, adding the 15 sets back with reason 'Customer Return - Resalable'. Then, create a new outbound order for the correct part, 'Leather Handbag' (APRL-BAG-E5), for 15 units to the same customer at '555 Repair Lane, Chicago, IL'. Ship it via 'UPS' (CARR-014) with tracking 'CORRECT-PART-555'.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0008"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "LUX-WATCH-L12"}),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-07",
                "sku": "LUX-WATCH-L12",
                "quantity_change": 15,
                "reason": "Customer Return - Resalable"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "APRL-BAG-E5"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "AutoRestore",
                "warehouse_id": "WH-07",
                "items": [{"sku": "APRL-BAG-E5", "quantity": 15}],
                "shipping_address": "555 Repair Lane, Chicago, IL"
            }),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-014"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "CORRECT-PART-555"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017", "status": "Shipped"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_035",
        instruction="VIP Global Tech needs urgent 2 Automatic Watches (LUX-WATCH-L12) with premium service. First find High-Value Cage and 24/7 Security Detail warehouses for secure storage, check inventory at secure facility, create VIP order for Global Tech to 1 Quantum Way, Palo Alto, CA, find the highest-rated Air carrier service with High-Value service level, ship with premium carrier using tracking EK-VIP-789, and provide complete order confirmation.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capabilities": ["High-Value Cage", "24/7 Security Detail"]}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-07",
                "sku": "LUX-WATCH-L12"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Global Tech",
                "warehouse_id": "WH-07",
                "items": [{"sku": "LUX-WATCH-L12", "quantity": 2}],
                "shipping_address": "1 Quantum Way, Palo Alto, CA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-006"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "EK-VIP-789"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=['"order_id": "ORD-0017", "status": "Shipped", "warehouse_id": "WH-07"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_036",
        instruction="Global Construction emergency order for heavy equipment: 35 Diamond Core Drill Bits (HEVY-DRIL-I9) and 180 Automotive Windshields (AUTO-GLAS-U21). First find Heavy Equipment and Automotive suppliers and check performance ratings, verify inventory for drill bits at WH-11 and windshields at WH-03, create separate orders for both items to 123 Construction Site, Denver, CO, find Rail carrier (CARR-008) for drill bits and Truck carrier (CARR-014) for windshields, ship drill bits via Rail with tracking CN-RAIL-789 and windshields via Truck with tracking UPS-TRUCK-101, verify both shipments created successfully.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Heavy Equipment"]}),
            Action(name="find_suppliers", kwargs={"product_categories": ["Automotive"]}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-11",
                "sku": "HEVY-DRIL-I9"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-GLAS-U21"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Global Construction",
                "warehouse_id": "WH-11",
                "items": [{"sku": "HEVY-DRIL-I9", "quantity": 35}],
                "shipping_address": "123 Construction Site, Denver, CO"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Global Construction",
                "warehouse_id": "WH-03",
                "items": [{"sku": "AUTO-GLAS-U21", "quantity": 180}],
                "shipping_address": "123 Construction Site, Denver, CO"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Rail"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-008",
                "tracking_number": "CN-RAIL-789"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0018",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "UPS-TRUCK-101"
            })
        ],
        outputs=['"order_id": "ORD-0017", "new_status": "Shipped"',
                 '"order_id": "ORD-0018", "new_status": "Shipped"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_037",
        instruction="Establish new supply chain for Global Construction's 10 Heavy-Duty Excavators (HEVY-EXCV-T5). First find Heavy Equipment suppliers and evaluate their performance metrics, select top supplier and get detailed information, find all Rail carriers and select CARR-008, create comprehensive inbound shipment to WH-11 using optimal Rail carrier for arrival 2024-09-15, verify shipment setup, get complete carrier service details, and confirm supply chain establishment.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Heavy Equipment"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1011"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Rail"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-008"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-11"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1011",
                "destination_warehouse_id": "WH-11",
                "carrier_id": "CARR-008",
                "items": [{"sku": "HEVY-EXCV-T5", "quantity": 10}],
                "estimated_arrival_date": "2024-09-15"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"}),
        ],
        outputs=['"shipment_id": "SHIP-0031", "supplier_id": "SUP-1011", "destination_warehouse_id": "WH-11", "carrier_id": "CARR-008"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_038",
        instruction="Comprehensive inventory audit and discrepancy correction for SHIP-0018 containing Argentinian Malbec Wine (BEVG-WINE-P16). Shipment expected 900 cases but only 850 received at WH-15. First get complete shipment details, receive actual quantity (850 cases), check updated inventory levels, write off 50 missing cases with reason 'Shipping Discrepancy', verify adjustment applied, get final inventory confirmation, and document complete audit trail.",
        actions=[
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0018"}),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0018",
                "items_received": [{"sku": "BEVG-WINE-P16", "quantity": 850}]
            }),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-15"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-15",
                "sku": "BEVG-WINE-P16"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-15",
                "sku": "BEVG-WINE-P16",
                "quantity_change": -50,
                "reason": "Shipping Discrepancy"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-15",
                "sku": "BEVG-WINE-P16"
            }),
        ],
        outputs=['"warehouse_id": "WH-15"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_039",
        instruction="Multi-phase pharmaceutical distribution setup for critical medicines. Hospital client needs temperature-controlled distribution of 500 units of Influenza Vaccine (PHRM-VACC-D4) and 200 Oncology Drug A (PHRM-DRUG-S19). First find the pharmaceutical supplier with the lowest standard lead time in days, get detailed supplier performance data, find the Cold Chain (2-8°C) warehouse with the lowest number of docks, verify inventory availability for both medications at suitable facility, create priority medical order for Metro General Hospital to 456 Medical Center Dr, Chicago, IL, find specialized medical carrier (CARR-006), and arrange expedited cold chain delivery with tracking MED-CRITICAL-001.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Pharmaceuticals"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1006"}),
            Action(name="find_warehouses", kwargs={"special_capability": "Cold Chain (2-8°C)"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-06",
                "sku": "PHRM-VACC-D4"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-06",
                "sku": "PHRM-DRUG-S19"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Metro General Hospital",
                "warehouse_id": "WH-06",
                "items": [
                    {"sku": "PHRM-VACC-D4", "quantity": 500},
                    {"sku": "PHRM-DRUG-S19", "quantity": 200}
                ],
                "shipping_address": "456 Medical Center Dr, Chicago, IL"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-006"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "MED-CRITICAL-001"
            })
        ],
        outputs=['"order_id": "ORD-0017"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_040",
        instruction="Complete supply chain optimization for Tech Innovation Hub requiring specialized components: 25 Lithium-Ion Batteries (TECH-BATT-Q17), 15 Robotic Arms (TECH-ROBO-N14), and 50 8-Bit Microcontrollers (ELEC-CHIP-A1). First find Electronics suppliers and evaluate their high-tech capabilities, get detailed supplier performance and specialization data. Choose the supplier with the highest performance rating. Find Heavy Equipment Handling warehouses for secure component storage, verify availability for all three components at secure facility, create comprehensive order for Tech Innovation Hub to 789 Silicon Valley Blvd, San Jose, CA, analyze Air carriers for expedited tech shipping, ship with carrier 'CARR-006' using tracking TECH-INNOVATION-001, and provide complete delivery confirmation with security protocols.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Electronics"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1002"}),
            Action(name="find_warehouses", kwargs={"special_capability": "Heavy Equipment Handling"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "TECH-BATT-Q17"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "TECH-ROBO-N14"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Tech Innovation Hub",
                "warehouse_id": "WH-03",
                "items": [
                    {"sku": "TECH-BATT-Q17", "quantity": 25},
                    {"sku": "TECH-ROBO-N14", "quantity": 15},
                    {"sku": "ELEC-CHIP-A1", "quantity": 50}
                ],
                "shipping_address": "789 Silicon Valley Blvd, San Jose, CA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-006"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "TECH-INNOVATION-001"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=['"order_id": "ORD-0017"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_041",
        instruction="Establish luxury goods distribution network for Premium Fashion Boutique requiring high-security handling of 30 Leather Handbags (APRL-BAG-E5), and 20 Luxury Watches (LUX-WATCH-L12). First find luxury goods suppliers and assess their security protocols, get comprehensive supplier information including certifications. Use supplier 'SUP-1007'. Find High-Value Cage and 24/7 Security Detail warehouses with jewelry handling capabilities, verify secure inventory for all luxury items, create high-priority order for Premium Fashion Boutique to 1 Luxury Lane, Beverly Hills, CA, evaluate specialized Air carriers for valuable cargo transport, select carrier 'CARR-006', arrange secure shipping with tracking LUXURY-SECURE-001. Display order information",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Luxury Goods"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1007"}),
            Action(name="find_warehouses", kwargs={"special_capabilities": ["High-Value Cage", "24/7 Security Detail"]}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-07"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-07",
                "sku": "APRL-BAG-E5"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-07",
                "sku": "LUX-WATCH-L12"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Premium Fashion Boutique",
                "warehouse_id": "WH-07",
                "items": [
                    {"sku": "APRL-BAG-E5", "quantity": 30},
                    {"sku": "LUX-WATCH-L12", "quantity": 20},
                ],
                "shipping_address": "1 Luxury Lane, Beverly Hills, CA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-006"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "LUXURY-SECURE-001"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=['"order_id": "ORD-0017"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_042",
        instruction="Execute complex international food distribution for Gourmet Restaurant Chain requiring temperature-controlled logistics for 200 units of Coffee Beans (FOOD-COFF-C3), and 150 Olive Oil bottles (FOOD-OLIV-V22). First find Groceries and Beverage suppliers specializing in gourmet items and evaluate their cold chain capabilities, get detailed supplier certifications and performance data, find warehouses with Temperature Controlled and Pest Control capabilities, verify fresh inventory availability for all gourmet items, create priority order for Gourmet Restaurant Chain to 456 Culinary Ave, New York, NY, research specialized Truck food carriers with temperature monitoring, select carrier 'CARR-014', arrange refrigerated transport with tracking GOURMET-FRESH-001, and confirm complete cold chain integrity documentation.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Groceries", "Beverages"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1005"}),
            Action(name="find_warehouses", kwargs={"special_capabilities": ["Temperature Control (Ambient)", "Pest Control Program"]}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-05",
                "sku": "FOOD-COFF-C3"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-05",
                "sku": "FOOD-OLIV-V22"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Gourmet Restaurant Chain",
                "warehouse_id": "WH-05",
                "items": [
                    {"sku": "FOOD-COFF-C3", "quantity": 200},
                    {"sku": "FOOD-OLIV-V22", "quantity": 150},
                ],
                "shipping_address": "456 Culinary Ave, New York, NY"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-014"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "GOURMET-FRESH-001"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=['"order_id": "ORD-0017"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_043",
        instruction="Comprehensive Beverage supply chain for Industrial Safety Corp requiring specialized handling of 75 Cork Stoppers (MATR-CORK-T20), and 50 Wine Bottles (BEVG-WINE-P16). First find Groceries and Beverage suppliers specializing in alcohol supply, get detailed supplier credentials and performance ratings. Find warehouses with Temperature Controlled capabilities and verify inventory availability for all items. Create order for Industrial Safety Corp to 789 Safety Blvd, Houston, TX, research specialized Truck food carriers with temperature monitoring, select carrier 'CARR-014', arrange shipping with tracking SAFETY-WINE-001.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Groceries", "Beverages"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1005"}),
            Action(name="find_warehouses", kwargs={"special_capabilities": ["Temperature Control (10-15°C)"]}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-15"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-15",
                "sku": "MATR-CORK-T20"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-15",
                "sku": "BEVG-WINE-P16"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Industrial Safety Corp",
                "warehouse_id": "WH-15",
                "items": [
                    {"sku": "MATR-CORK-T20", "quantity": 75},
                    {"sku": "BEVG-WINE-P16", "quantity": 50},
                ],
                "shipping_address": "789 Safety Blvd, Houston, TX"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-014"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "SAFETY-WINE-001"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=['"order_id": "ORD-0017"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_044",
        instruction="Multi-tier automotive parts distribution for Premium Auto Dealership requiring 40 Ceramic Brake Pad Sets (AUTO-PAD-B2), and 25 Automotive Windshields (AUTO-GLAS-U21). First find Automotive suppliers and assess their performance parts specialization, get comprehensive supplier capabilities and quality certifications. Choose the supplier with the highest performance rating. Find warehouses suitable for Heavy Equipment Handling with adequate space, verify inventory for all performance parts at suitable facility, create high-priority automotive order for Premium Auto Dealership to 123 Auto Mile, Detroit, MI, research Truck carriers specializing in automotive transport, evaluate carrier automotive handling experience, select carrier 'CARR-014', arrange specialized automotive shipping with tracking AUTO-PREMIUM-001, and provide complete automotive parts delivery confirmation with handling specifications.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Automotive"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1003"}),
            Action(name="find_warehouses", kwargs={"special_capability": "Heavy Equipment Handling"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-PAD-B2"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-GLAS-U21"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Premium Auto Dealership",
                "warehouse_id": "WH-03",
                "items": [
                    {"sku": "AUTO-PAD-B2", "quantity": 40},
                    {"sku": "AUTO-GLAS-U21", "quantity": 25},
                ],
                "shipping_address": "123 Auto Mile, Detroit, MI"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-014"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "AUTO-PREMIUM-001"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=['"order_id": "ORD-0017"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_045",
        instruction="Advanced electronics distribution for Research Laboratory requiring handling of 20 8-Bit Microcontrollers (ELEC-CHIP-A1), 15 Lithium-Ion Batteries (TECH-BATT-Q17), and 10 Robotic Arms (TECH-ROBO-N14). First find Electronics and Components suppliers and get detailed supplier certifications, find warehouses with heavy equipment handling, verify inventory availability for all laboratory equipment at suitable facility, create critical research order for Research Laboratory to 456 Science Park, Boston, MA. Using carrier 'CARR-006', arrange specialized scientific shipping with tracking RESEARCH-LAB-001.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Electronics", "Components"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1001"}),
            Action(name="find_warehouses", kwargs={"special_capability": "Heavy Equipment Handling"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "TECH-BATT-Q17"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "TECH-ROBO-N14"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Research Laboratory",
                "warehouse_id": "WH-03",
                "items": [
                    {"sku": "ELEC-CHIP-A1", "quantity": 20},
                    {"sku": "TECH-BATT-Q17", "quantity": 15},
                    {"sku": "TECH-ROBO-N14", "quantity": 10}
                ],
                "shipping_address": "456 Science Park, Boston, MA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-006"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "RESEARCH-LAB-001"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"})
        ],
        outputs=['"order_id": "ORD-0017"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_046",
        instruction="A critical 'Hazmat' shipment of 100 units of 'Industrial Solvent' (CHEM-SOLV-K11) is needed for a client, 'ChemCorp'. Find a supplier for this product category. Then, find a warehouse with 'Hazmat Certified' capabilities in the USA. Finally, create an inbound shipment record for the items from the supplier to the hazmat warehouse, expected to arrive on '2025-08-15'. Use the best-rated 'Sea' carrier (highest performance rating, then alphabetical name for ties). Confirm the shipment details.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Chemicals"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1013"}),
            Action(name="find_warehouses", kwargs={"country": "USA", "special_capability": "Hazmat Certified (Classes 3, 6.1, 9)"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-13"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Sea"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-012"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1013",
                "destination_warehouse_id": "WH-13",
                "carrier_id": "CARR-012",
                "items": [{"sku": "CHEM-SOLV-K11", "quantity": 100}],
                "estimated_arrival_date": "2025-08-15"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"}),
        ],
        outputs=['"shipment_id": "SHIP-0031"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_047",
        instruction="A major customer, 'Luxury Retail Group', wants to place a large order for 50 'Leather Handbag' (APRL-BAG-E5) and 100 'Automatic Watch Movement' (LUX-WATCH-L12). Both are high-value. Find a warehouse with 'High-Value Cage' capability. Check if it has enough stock for both items. If stock is sufficient, create the order for 'Luxury Retail Group' shipping to '1 Rodeo Drive, Beverly Hills, CA', ship it with the best 'Air' carrier (highest on-time-delivery percentage, then alphabetical name for ties). Use tracking number EK-CARGO-456 and report the final order ID.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "High-Value Cage"}),
            # no inventory in WH-01
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-01", "sku": "APRL-BAG-E5"}),
            # no inventory in WH-01
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-01", "sku": "LUX-WATCH-L12"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "APRL-BAG-E5"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "LUX-WATCH-L12"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Luxury Retail Group",
                "warehouse_id": "WH-07",
                "items": [
                    {"sku": "APRL-BAG-E5", "quantity": 50},
                    {"sku": "LUX-WATCH-L12", "quantity": 100}
                ],
                "shipping_address": "1 Rodeo Drive, Beverly Hills, CA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "EK-CARGO-456"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_048",
        instruction="The 'Los Angeles Distribution Center' (WH-01) was damaged in a minor earthquake. 10% of the '8-bit Microcontroller' (SKU: ELEC-CHIP-A1) isdamaged. First, get current inventory for the SKU in WH-01 to calculate the loss. Adjust the inventory for the SKU with the reason 'Damaged in Natural Disaster'. Then, check the new total stock for the SKU across all warehouses. If the total for the SKU is below 20,000, find the primary supplier for 'Electronics' (ID 'SUP-1001') and create a new inbound shipment of 5,000 units for the SKU that is low, to be delivered to the 'Chicago Parts Depot' (WH-03) by 'FedEx' (CARR-007) on '2025-08-10'. Confirm the new shipment ID.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-01", "sku": "ELEC-CHIP-A1"}),
            Action(name="adjust_inventory", kwargs={"warehouse_id": "WH-01", "sku": "ELEC-CHIP-A1", "quantity_change": -1500, "reason": "Damaged in Natural Disaster"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "ELEC-CHIP-A1"}),
            Action(name="find_suppliers", kwargs={"product_categories": ["Electronics"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1001"}),
            # Conditional action: if total stock < 20000 for the SKU
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1001",
                "destination_warehouse_id": "WH-03",
                "carrier_id": "CARR-007",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 5000}],
                "estimated_arrival_date": "2025-08-10"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"}),
        ],
        outputs=['"shipment_id": "SHIP-0031"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_049",
        instruction="An ongoing inventory audit reveals that 'PHRM-DRUG-S19' has an incorrect quantity in 'WH-06'. The physical count is 50 units, but the system shows 500. First, get the current system quantity, then apply an inventory adjustment to match the physical count with reason 'Audit Adjustment'. Then, check the reorder point for 'PHRM-DRUG-S19' in 'WH-06'. If the new quantity is below the reorder point, initiate a new inbound shipment of 100 units from 'SUP-1006' via 'DHL Express' (CARR-009) with ETA '2025-08-15'. Confirm final quantity and new shipment ID if created.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-DRUG-S19"}),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-06",
                "sku": "PHRM-DRUG-S19",
                "quantity_change": -450,
                "reason": "Audit Adjustment"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-DRUG-S19"}), # Check new quantity and reorder point
            # Conditional: if new quantity (50) < reorder point (100) - this
            # example will trigger the shipment
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1006"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1006",
                "destination_warehouse_id": "WH-06",
                "carrier_id": "CARR-009",
                "items": [{"sku": "PHRM-DRUG-S19", "quantity": 100}],
                "estimated_arrival_date": "2025-08-15"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"}),
        ],
        outputs=['"shipment_id": "SHIP-0031"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_050",
        instruction="An emergency order for 'BuildFast Corp' requires 35 'Diamond Core Drill Bit' (HEVY-DRIL-I9) and 180 'Automotive Windshield' (AUTO-GLAS-U21). Find supplier for 'Heavy Equipment' parts. Check their ratings. Find warehouses that can handle these items (WH-11 for heavy equipment, WH-03 for glass). Check stock for both items in their respective warehouses. If stock is sufficient, create two separate orders. Ship the drill bits from WH-11 using the best 'Rail' carrier (highest performance rating, then alphabetical name for ties) and the windshields from WH-03 using the best 'Truck' carrier (highest performance rating, then alphabetical name for ties). Use tracking numbers 'CN-RAIL-789' and 'UPS-TRUCK-101'. Report both order IDs.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Heavy Equipment"]}),
            # Assuming SUP-1011 for Heavy Equipment, SUP-1010 for Automotive
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1011"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-11", "sku": "HEVY-DRIL-I9"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "AUTO-GLAS-U21"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "BuildFast Corp",
                "warehouse_id": "WH-11",
                "items": [{"sku": "HEVY-DRIL-I9", "quantity": 35}],
                "shipping_address": "123 Construction Site, Denver, CO"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "BuildFast Corp",
                "warehouse_id": "WH-03",
                "items": [{"sku": "AUTO-GLAS-U21", "quantity": 180}],
                "shipping_address": "123 Construction Site, Denver, CO"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Rail"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            # Assuming CARR-012 (KNLU) is best Rail, CARR-014 (UPS) is best Truck
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017", # Derived from first create_outbound_order
                "new_status": "Shipped",
                "carrier_id": "CARR-012",
                "tracking_number": "CN-RAIL-789"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0018", # Derived from second create_outbound_order
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "UPS-TRUCK-101"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0018"}),
        ],
        outputs=['"order_id": "ORD-0017"',
                 '"order_id": "ORD-0018"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_051",
        instruction="A recall has been issued for '8-Bit Microcontroller' (SKU: ELEC-CHIP-A1). Find all warehouses with this product. Adjust the inventory to zero for this SKU in all affected warehouses, with the reason 'Product Recall'. Confirm the adjusted quantities for each warehouse.",
        actions=[
            Action(name="get_inventory_by_sku", kwargs={"sku": "ELEC-CHIP-A1"}),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-01",
                "sku": "ELEC-CHIP-A1",
                "quantity_change": -15000,
                "reason": "Product Recall"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-03",
                "sku": "ELEC-CHIP-A1",
                "quantity_change": -8000, # Adjust to zero
                "reason": "Product Recall"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-01", "sku": "ELEC-CHIP-A1"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "ELEC-CHIP-A1"}),
        ],
        outputs=['{"inventory_id": "INV-0001", "sku": "ELEC-CHIP-A1", "warehouse_id": "WH-01"}',
                 '{"inventory_id": "INV-0025", "sku": "ELEC-CHIP-A1", "warehouse_id": "WH-03"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_052",
        instruction="A VIP customer 'Global Tech' has an urgent order for 2 '8-Bit Microcontrollers' (SKU: ELEC-CHIP-A1). Find warehouses with 'High-Value Cage' and select the one with the most number of docks, and check for stock. If available, create the order. Then, select the 'Air' carrier 'CARR-006' and ship the order to '1 Quantum Way, Palo Alto, CA' with tracking number 'EK-VIP-789' . Finally, confirm the order status.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "High-Value Cage"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-01", "sku": "ELEC-CHIP-A1"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Global Tech",
                "warehouse_id": "WH-01",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 2}],
                "shipping_address": "1 Quantum Way, Palo Alto, CA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017", # Derived from create_outbound_order
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "EK-VIP-789"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017", "status": "Shipped", "warehouse_id": "WH-01"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_053",
        instruction="A fire at 'Detroit Packaging Supplies' (WH-08) damaged 25% of the 'Industrial Paper Roll' (MANU-PAPR-F6) inventory. Calculate the loss, adjust the inventory with reason 'Damaged by Fire'. Check the total stock across all locations. If the total quantity is now below 500 rolls, find the supplier 'Toronto Paper Mills' (SUP-1008), and place an emergency inbound order of 200 rolls to the 'Chicago Parts Depot' (WH-03) via the best-rated 'Rail' carrier 'CARR-012', to arrive by '2025-08-12'.",
        actions=[
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-08"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-08", "sku": "MANU-PAPR-F6"}),
            Action(name="adjust_inventory", kwargs={"warehouse_id": "WH-08", "sku": "MANU-PAPR-F6", "quantity_change": -75, "reason": "Damaged by Fire"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "MANU-PAPR-F6"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1008"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Rail"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-012"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1008",
                "destination_warehouse_id": "WH-03",
                "carrier_id": "CARR-012",
                "items": [{"sku": "MANU-PAPR-F6", "quantity": 200}],
                "estimated_arrival_date": "2025-08-12"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"}),
        ],
        outputs=['"shipment_id": "SHIP-0031"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_054",
        instruction="A customer 'Fashion Forward' returns a faulty 'Organic Cotton Tshirt' (SKU: APRL-TSHT-O15). The order ID is 'ORD-0005'. The dress is unrepairable. Update the inventory in warehouse WH-04 by adding 1 unit (customer return), then immediately adjusting it by -1 unit with reason 'Unrepairable Damage'. Then, find the primary supplier for 'Apparel' (SUP-1002) and create an inbound shipment with supplier ID 'WH-04' (the warehouse acts as a supplier) and destination warehouse ID 'SUP-1002-returns' to send the damaged dress back to them for disposal. Ship with 'Air' carrier 'CARR-007' (FedEx) and ETA '2025-08-10'. Confirm the final inventory adjustment and the return shipment ID.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0005"}),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-04",
                "sku": "APRL-TSHT-O15",
                "quantity_change": 1,
                "reason": "Customer Return"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-04",
                "sku": "APRL-TSHT-O15",
                "quantity_change": -1,
                "reason": "Unrepairable Damage"
            }),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1002"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="create_inbound_shipment", kwargs={ # Inbound shipment to supplier for disposal
                "supplier_id": "WH-04", # Our warehouse acts as supplier
                "destination_warehouse_id": "SUP-1002-returns", # Example: supplier's returns address
                "carrier_id": "CARR-007",
                "items": [{"sku": "APRL-TSHT-O15", "quantity": 1}],
                "estimated_arrival_date": "2025-08-10"
            }),
        ],
        outputs=['"shipment_id": "SHIP-0031", "supplier_id": "WH-04"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_055",
        instruction="A customer 'Home Appliances Inc.' wants to order 15 'Luxury Watch' (SKU: LUX-WATCH-L12) and 10 'Leather Handbag' (SKU: APRL-BAG-E5). Find the US warehouse that has both High-Value Cage and 24/7 Security Detail capabilities and has sufficient stock. Create the order and ship to '456 Appliance Way, Seattle, WA' using carrier 'CARR-006' and tracking 'GLOBAL-APRL-001'. Confirm the order details and the new available quantities in the warehouse.",
        actions=[
            Action(name="find_warehouses", kwargs={"country": "USA", "special_capabilities": ["High-Value Cage", "24/7 Security Detail"]}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "LUX-WATCH-L12"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "APRL-BAG-E5"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Home Appliances Inc.",
                "warehouse_id": "WH-07",
                "items": [
                    {"sku": "LUX-WATCH-L12", "quantity": 15},
                    {"sku": "APRL-BAG-E5", "quantity": 10}
                ],
                "shipping_address": "456 Appliance Way, Seattle, WA"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "GLOBAL-APRL-001"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "LUX-WATCH-L12"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "APRL-BAG-E5"}), ],
        outputs=['{"inventory_id": "INV-0012", "sku": "LUX-WATCH-L12", "warehouse_id": "WH-07"}',
                 '{"inventory_id": "INV-0005", "sku": "APRL-BAG-E5", "warehouse_id": "WH-07"}']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_056",
        instruction="A customer 'PharmaPlus' wants to order 50 'Insulin Pens' (SKU: PHRM-DRUG-S19) and 20 'Syringes' (SKU: PHRM-VACC-D4). Find a warehouse with 'Cold Chain' and 'Pharmaceutical Handling' capabilities and the highest current utilization percentage. Create the order to be shipped to '1 Medical Way, Philadelphia, PA'. Immediately after, check the new available quantities of both SKUs in that warehouse.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capabilities": ["Cold Chain (2-8°C)", "Pharmaceutical Handling"]}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-DRUG-S19"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-VACC-D4"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "PharmaPlus",
                "warehouse_id": "WH-06",
                "items": [
                    {"sku": "PHRM-DRUG-S19", "quantity": 50},
                    {"sku": "PHRM-VACC-D4", "quantity": 20}
                ],
                "shipping_address": "1 Medical Way, Philadelphia, PA"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-DRUG-S19"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-VACC-D4"}),
        ],
        outputs=['{"inventory_id": "INV-0019", "sku": "PHRM-DRUG-S19", "warehouse_id": "WH-06"}',
                 '{"inventory_id": "INV-0004", "sku": "PHRM-VACC-D4", "warehouse_id": "WH-06"}']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_057",
        instruction="A major customer 'Global Retail Inc.' wants to order 200 'Cotton Tshirts' (SKU: APRL-TSHT-O15) and 150 'Raw Cotton Bale' (SKU: MATR-COTT-R18). Find a warehouse with Garment on Hanger (GOH) capability. Check if it has both items in stock. If stock is sufficient, create the order to be shipped to '777 Retail Way, Houston, TX'. Then update the order to use 'Air' carrier (CARR-006) and tracking number 'GLOBAL-APRL-001'. Confirm the updated order status and the chosen warehouse's utilization.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "Garment on Hanger (GOH)"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-04"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-04", "sku": "APRL-TSHT-O15"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-04", "sku": "MATR-COTT-R18"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Global Retail Inc.",
                "warehouse_id": "WH-04",
                "items": [
                    {"sku": "APRL-TSHT-O15", "quantity": 200},
                    {"sku": "MATR-COTT-R18", "quantity": 150}
                ],
                "shipping_address": "777 Retail Way, Houston, TX"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017", # New order ID
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "GLOBAL-APRL-001"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-04"}),
        ],
        outputs=['"order_id": "ORD-0017", "status": "Shipped", "warehouse_id": "WH-04"',
                 '"warehouse_id": "WH-04", "warehouse_name": "Newark Apparel Hub"']
    ),

    Task(
        annotator="samarthkulshrestha",
        user_id="USR_058",
        instruction="A client, 'ChemSolutions', requires an urgent shipment of 150 units of 'Industrial Solvent' (CHEM-SOLV-K11). Find a warehouse in the USA with 'Hazmat Certified (Classes 3, 6.1, 9)' capabilities. Check for stock and if sufficient, create an order to be shipped to '123 Chemical Lane, Houston, TX'. Use the 'Air' carrier 'CARR-022' and tracking number 'CHEM-URGENT-001'. Confirm the order ID.",
        actions=[
            Action(name="find_warehouses", kwargs={"country": "USA", "special_capability": "Hazmat Certified (Classes 3, 6.1, 9)"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-13"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-13", "sku": "CHEM-SOLV-K11"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "ChemSolutions",
                "warehouse_id": "WH-13",
                "items": [{"sku": "CHEM-SOLV-K11", "quantity": 150}],
                "shipping_address": "123 Chemical Lane, Houston, TX"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-022"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-022",
                "tracking_number": "CHEM-URGENT-001"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_059",
        instruction="A restaurant 'The Gilded Spoon' needs 50 'Frozen Tuna Loins' (FOOD-FISH-H8). Find a warehouse with 'Perishables Handling' and check for stock. Create an order to '789 Gourmet Ave, San Francisco, CA'. Ship it using a 'Reefer' truck from the best-rated carrier that supports it. Use tracking 'GILDED-FISH-001'.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "Perishables Handling"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-10", "sku": "FOOD-FISH-H8"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "The Gilded Spoon",
                "warehouse_id": "WH-10",
                "items": [{"sku": "FOOD-FISH-H8", "quantity": 50}],
                "shipping_address": "789 Gourmet Ave, San Francisco, CA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-001",
                "tracking_number": "GILDED-FISH-001"
            }),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_060",
        instruction="A mining company 'DigDeep Corp' needs 10 'Diamond Core Drill Bits' (HEVY-DRIL-I9). Find supplier 'SUP-1011' for 'Heavy Equipment' and check their performance. Then, check inventory at 'WH-11'. If stock is sufficient, create an order for 'DigDeep Corp' to '999 Mine Road, Denver, CO' and ship via 'Rail' carrier 'CARR-008' with tracking 'DIG-RAIL-002'.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Heavy Equipment"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1011"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-11", "sku": "HEVY-DRIL-I9"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "DigDeep Corp",
                "warehouse_id": "WH-11",
                "items": [{"sku": "HEVY-DRIL-I9", "quantity": 10}],
                "shipping_address": "999 Mine Road, Denver, CO"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Rail"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-008",
                "tracking_number": "DIG-RAIL-002"
            }),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_061",
        instruction="A customer returned a 'Leather Handbag' (APRL-BAG-E5) from order 'ORD-0001' to 'WH-07'. The item is in perfect condition. Add it back to the inventory with reason 'Customer Return - Resalable'. Verify the final inventory count.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0001"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "APRL-BAG-E5"}),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-07",
                "sku": "APRL-BAG-E5",
                "quantity_change": 1,
                "reason": "Customer Return - Resalable"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "APRL-BAG-E5"}),
        ],
        outputs=['{"inventory_id": "INV-0005", "sku": "APRL-BAG-E5", "quantity_available": 121}']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_062",
        instruction="A construction company 'BuildRight' needs 5000 'Ceramic Floor Tiles' (BLDG-TILE-J10). Find warehouses with 'Bulk Storage' capability and choose the one with the highest current utilization percentage. Check inventory. Create an order to '456 Construction Ave, Miami, FL' and ship via 'Truck' carrier 'CARR-007' with tracking 'BUILD-TILE-5000'.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "Bulk Storage"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-12", "sku": "BLDG-TILE-J10"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "BuildRight",
                "warehouse_id": "WH-12",
                "items": [{"sku": "BLDG-TILE-J10", "quantity": 5000}],
                "shipping_address": "456 Construction Ave, Miami, FL"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-007"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-007",
                "tracking_number": "BUILD-TILE-5000"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_063",
        instruction="Transfer 50 'Automotive Windshields' (AUTO-GLAS-U21) from 'WH-03' to 'WH-01'. These are fragile. Reduce inventory at the source, create an inbound shipment for the destination with ETA '2025-08-01', and use a carrier that supports 'Truck' transport (CARR-014). Confirm the final inventory at WH-03.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "AUTO-GLAS-U21"}),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-GLAS-U21",
                "quantity_change": -50,
                "reason": "Internal Transfer to WH-01"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "Internal",
                "destination_warehouse_id": "WH-01",
                "carrier_id": "CARR-014",
                "items": [{"sku": "AUTO-GLAS-U21", "quantity": 50}],
                "estimated_arrival_date": "2025-08-01"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "AUTO-GLAS-U21"}),
        ],
        outputs=['{"inventory_id": "INV-0021", "quantity_on_hand": 150}']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_064",
        instruction="An e-commerce client 'GadgetGo' needs 200 'Smartphone Model X' (ELEC-SMART-W23). Find a warehouse with 'E-commerce Fulfillment' capability. Check stock. Create an order to '123 E-com St, Seattle, WA' and ship via 'Parcel' using carrier 'CARR-014' with tracking 'GADGET-ECOM-200'.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capability": "E-commerce Fulfillment"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-02"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-02", "sku": "ELEC-SMART-W23"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "GadgetGo",
                "warehouse_id": "WH-02",
                "items": [{"sku": "ELEC-SMART-W23", "quantity": 200}],
                "shipping_address": "123 E-com St, Seattle, WA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Parcel"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-014"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "GADGET-ECOM-200"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_065",
        instruction="A client 'BioChem Corp' needs 10 'Industrial Solvent' (CHEM-SOLV-K11) and 50 'Ceramic Brake Pad Set' (AUTO-PAD-B2). Find a warehouse that has both. If none, find two warehouses (WH-13 and WH-03) and create two separate orders to '789 Lab Ave, Cleveland, OH'. Ship both via 'Truck' carrier ID 'CARR-007'. Use tracking 'BIO-HAZ-001' for the solvent and 'BIO-AUTO-001' for the pads.",
        actions=[
            Action(name="get_inventory_by_sku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "AUTO-PAD-B2"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "BioChem Corp",
                "warehouse_id": "WH-13",
                "items": [{"sku": "CHEM-SOLV-K11", "quantity": 10}],
                "shipping_address": "789 Lab Ave, Cleveland, OH"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "BioChem Corp",
                "warehouse_id": "WH-03",
                "items": [{"sku": "AUTO-PAD-B2", "quantity": 50}],
                "shipping_address": "789 Lab Ave, Cleveland, OH"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-007",
                "tracking_number": "BIO-HAZ-001"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0018",
                "new_status": "Shipped",
                "carrier_id": "CARR-007",
                "tracking_number": "BIO-AUTO-001"
            }),
        ],
        outputs=['"order_id": "ORD-0017"', '"order_id": "ORD-0018"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_066",
        instruction="Receive an inbound shipment 'SHIP-0020' of 'Raw Cotton Bale' (MATR-COTT-R18) at 'WH-04'. The shipment contains 1100 units. After receiving, perform a quality check by adjusting out 10 units as 'Damaged on Arrival'. Confirm the final available quantity.",
        actions=[
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0020"}),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0020",
                "items_received": [{"sku": "MATR-COTT-R18", "quantity": 1100}]
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-04",
                "sku": "MATR-COTT-R18",
                "quantity_change": -10,
                "reason": "Damaged on Arrival"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-04", "sku": "MATR-COTT-R18"}),
        ],
        outputs=['{"inventory_id": "INV-0018", "quantity_on_hand": 1290}']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_067",
        instruction="A customer 'Style Maven' needs 50 'Organic Cotton T-Shirt' (APRL-TSHT-O15) and 10 'Leather Handbag' (APRL-BAG-E5). The T-shirts are in 'WH-04' and handbags in 'WH-07'. Create two separate orders shipping to '1 Fashionista Way, New York, NY'. Use Air carrier 'UPS' for both with tracking numbers 'STYLE-TSHIRT-001' and 'STYLE-BAG-001'.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-04", "sku": "APRL-TSHT-O15"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-07", "sku": "APRL-BAG-E5"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Style Maven",
                "warehouse_id": "WH-04",
                "items": [{"sku": "APRL-TSHT-O15", "quantity": 50}],
                "shipping_address": "1 Fashionista Way, New York, NY"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Style Maven",
                "warehouse_id": "WH-07",
                "items": [{"sku": "APRL-BAG-E5", "quantity": 10}],
                "shipping_address": "1 Fashionista Way, New York, NY"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "STYLE-TSHIRT-001"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0018",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "STYLE-BAG-001"
            }),
        ],
        outputs=['"order_id": "ORD-0017"', '"order_id": "ORD-0018"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_068",
        instruction="A shipment of 1200 units of 'Solar Panel 450W' (TECH-SOLR-G7) has arrived at 'WH-09' via shipment 'SHIP-0009'. Immediately cross-dock 100 panels to fulfill order 'ORD-0010' for 'Kappa Books Pvt Ltd.'. Update the order status to 'Shipped' with carrier 'CARR-007' and tracking 'CROSSDOCK-SOLAR-01'.",
        actions=[
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-09"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-09", "sku": "TECH-SOLR-G7"}),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0009",
                "items_received": [{"sku": "TECH-SOLR-G7", "quantity": 1200}]
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id":
                                                              "WH-09", "sku":
                                                              "TECH-SOLR-G7"}),
            # just received 1200 units so on-hand-quantity must be 2400
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-09",
                "sku": "TECH-SOLR-G7",
                "quantity_change": -100,
                "reason": "Cross-dock for ORD-0010"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0010"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-007"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0010",
                "new_status": "Shipped",
                "carrier_id": "CARR-007",
                "tracking_number": "CROSSDOCK-SOLAR-01"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0010"}),
        ],
        outputs=['"order_id": "ORD-0010", "status": "Shipped"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_069",
        instruction="A customer 'DIY Garage' needs 20 'Ceramic Brake Pad Set' (AUTO-PAD-B2) and 10 'Automotive Windshield' (AUTO-GLAS-U21). Find a warehouse that has both items (WH-03).  Create two separate orders for 'DIY Garage' to '789 DIY Ave, Denver, CO'. Ship both orders using the 'Truck' carrier with the best on-time delivery percentage ('UPS' - CARR-014). Use tracking numbers 'DIY-BRAKES-01' and 'DIY-GLASS-02'.",
        actions=[
            Action(name="get_inventory_by_sku", kwargs={"sku": "AUTO-PAD-B2"}),
            Action(name="get_inventory_by_sku", kwargs={"sku": "AUTO-GLAS-U21"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "AUTO-PAD-B2"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "AUTO-GLAS-U21"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "DIY Garage",
                "warehouse_id": "WH-03",
                "items": [{"sku": "AUTO-PAD-B2", "quantity": 20}],
                "shipping_address": "789 DIY Ave, Denver, CO"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "DIY Garage",
                "warehouse_id": "WH-03",
                "items": [{"sku": "AUTO-GLAS-U21", "quantity": 10}],
                "shipping_address": "789 DIY Ave, Denver, CO"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0017", "new_status": "Shipped", "carrier_id": "CARR-014", "tracking_number": "DIY-BRAKES-01"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0018", "new_status": "Shipped", "carrier_id": "CARR-014", "tracking_number": "DIY-GLASS-02"}),
        ],
        outputs=['"order_id": "ORD-0017"', '"order_id": "ORD-0018"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_070",
        instruction="A shipment (SHIP-0029) of 'Fresh Cut Roses' (FOOD-FLWR-X24) has arrived at 'San Francisco Fresh Foods DC' (WH-10). The shipment contains 65 units. Receive the shipment. Immediately, a customer 'Petal Pushers' places an order (ORD-0017) for 50 bouquets to '45 Rose St, Portland, OR'. Check the inventory to ensure stock, create the order, and ship it using the 'Air' carrier with the highest on-time delivery, 'Emirates SkyCargo' (CARR-006), with tracking 'PETAL-AIR-50'.",
        actions=[
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0029"}),
            Action(name="receive_inbound_shipment", kwargs={"shipment_id": "SHIP-0029", "items_received": [{"sku": "FOOD-FLWR-X24", "quantity": 65}]}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-10", "sku": "FOOD-FLWR-X24"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Petal Pushers",
                "warehouse_id": "WH-10",
                "items": [{"sku": "FOOD-FLWR-X24", "quantity": 50}],
                "shipping_address": "45 Rose St, Portland, OR"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "PETAL-AIR-50"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017", "status": "Shipped"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_071",
        instruction="A customer 'RoboBuilders' needs 5 'Robotic Kits'. Each kit consists of 1 'Articulated Robotic Arm' (TECH-ROBO-N14) and 2 'Lithium-Ion Battery Pack' (TECH-BATT-Q17). Check inventory for both components at 'WH-03'. If available, create an order for the 5 kits (5 arms, 10 batteries) to '789 Robot Way, Pittsburgh, PA' and ship via 'Rail' carrier 'CARR-008' with tracking 'ROBO-KIT-005'.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "TECH-ROBO-N14"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "TECH-BATT-Q17"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "RoboBuilders",
                "warehouse_id": "WH-03",
                "items": [
                    {"sku": "TECH-ROBO-N14", "quantity": 5},
                    {"sku": "TECH-BATT-Q17", "quantity": 10}
                ],
                "shipping_address": "789 Robot Way, Pittsburgh, PA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Rail"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-008",
                "tracking_number": "ROBO-KIT-005"
            }),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_072",
        instruction="An international shipment 'SHIP-0004' of textiles is delayed. Update its status to 'Delayed - Customs Hold'. Check the status of order 'ORD-0005' which depends on this stock. Then, find an alternative 'Air' carrier 'CARR-016' to expedite a replacement shipment of 100 'Organic Cotton T-Shirt' (APRL-TSHT-O15) from 'SUP-1004' to 'WH-04' with ETA '2025-07-30'.",
        actions=[
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0004", "status": "Delayed - Customs Hold"}),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0005"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1004",
                "destination_warehouse_id": "WH-04",
                "carrier_id": "CARR-016",
                "items": [{"sku": "APRL-TSHT-O15", "quantity": 100}],
                "estimated_arrival_date": "2025-07-30"
            }),
        ],
        outputs=['"shipment_id": "SHIP-0031"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_073",
        instruction="A customer 'EcoBuild' needs 1000 'Solar Panel 450W' (TECH-SOLR-G7). The 'Phoenix Renewable Warehouse' (WH-09) has stock. Create the order for 'EcoBuild' to '321 Green Energy Way, Austin, TX'. This is an oversized shipment. Find a 'Truck' carrier that supports 'Freight LTL' and has the highest average rating. Ship the order with this carrier (CARR-014) and tracking 'ECO-SOLAR-LTL-321'. After shipping, verify the warehouse's details.",
        actions=[
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-09"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-09", "sku": "TECH-SOLR-G7"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "EcoBuild",
                "warehouse_id": "WH-09",
                "items": [{"sku": "TECH-SOLR-G7", "quantity": 1000}],
                "shipping_address": "321 Green Energy Way, Austin, TX"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-014"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "ECO-SOLAR-LTL-321"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-09"}),
        ],
        outputs=['"warehouse_id": "WH-09"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_074",
        instruction="A customer 'Flash Electronics' needs a rush order of 500 '8-bit Microcontroller' (ELEC-CHIP-A1). Find the warehouse with the most stock. Then find the 'Air' carrier with the highest on-time delivery percentage. Create the order to '1 Speed St, Austin, TX' and ship with the selected carrier. Use tracking 'FLASH-RUSH-01'.",
        actions=[
            Action(name="get_inventory_by_sku", kwargs={"sku": "ELEC-CHIP-A1"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-01"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Flash Electronics",
                "warehouse_id": "WH-01",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 500}],
                "shipping_address": "1 Speed St, Austin, TX"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-014"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "FLASH-RUSH-01"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_075",
        instruction="A customer 'Arctic Research Station' in Greenland needs 5 'Solar Panel 450W' (TECH-SOLR-G7). Find a warehouse with stock. Research and find an 'Air' carrier (CARR-022) with global coverage. Create the order to '1 Research Base, Nuuk, Greenland' and ship with the selected carrier. Tracking 'ARCTIC-SOLAR-01'.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-09", "sku": "TECH-SOLR-G7"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Arctic Research Station",
                "warehouse_id": "WH-09",
                "items": [{"sku": "TECH-SOLR-G7", "quantity": 5}],
                "shipping_address": "1 Research Base, Nuuk, Greenland"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-022",
                "tracking_number": "ARCTIC-SOLAR-01"
            }),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_076",
        instruction="A new art gallery, 'Canvas Dreams', needs 10 'Teak Wood Dining Chairs' (FURN-CHAIR-M13) and 50 'Organic Cotton T-Shirts' (APRL-TSHT-O15) for their opening event. The items are in different warehouses (WH-14 and WH-04). Create two separate orders for 'Canvas Dreams' shipping to '1 Art Plaza, New York, NY'. Find a 'Parcel' carrier and a 'Truck' carrier. Ship the chairs via the truck carrier (CARR-007) with tracking 'ART-CHAIR-NYC' and the t-shirts via the parcel carrier (CARR-014) with tracking 'ART-TSHIRT-NYC'.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-14", "sku": "FURN-CHAIR-M13"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-04", "sku": "APRL-TSHT-O15"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Canvas Dreams",
                "warehouse_id": "WH-14",
                "items": [{"sku": "FURN-CHAIR-M13", "quantity": 10}],
                "shipping_address": "1 Art Plaza, New York, NY"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Canvas Dreams",
                "warehouse_id": "WH-04",
                "items": [{"sku": "APRL-TSHT-O15", "quantity": 50}],
                "shipping_address": "1 Art Plaza, New York, NY"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Parcel"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0017", "new_status": "Shipped", "carrier_id": "CARR-007", "tracking_number": "ART-CHAIR-NYC"}),
            Action(name="update_outbound_order_status", kwargs={"order_id": "ORD-0018", "new_status": "Shipped", "carrier_id": "CARR-014", "tracking_number": "ART-TSHIRT-NYC"}),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0018"}),
        ],
        outputs=['"order_id": "ORD-0017"', '"order_id": "ORD-0018"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_077",
        instruction="Two LTL orders exist for 'AutoStop' parts (SKU AUTO-PAD-B2) from 'WH-03' to Chicago. Consolidate them into a single FTL shipment. Cancel orders 'ORD-0003' and 'ORD-0009'. Create a new order for 'Consolidated Auto' for 25 units of 'AUTO-PAD-B2' to '1 Central Depot, Chicago, IL'. Ship via 'Truck' carrier 'CARR-007' with tracking 'FTL-AUTO-CHICAGO-01'.",
        actions=[
            Action(name="cancel_outbound_order", kwargs={"order_id": "ORD-0003"}),
            Action(name="cancel_outbound_order", kwargs={"order_id": "ORD-0009"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "AUTO-PAD-B2"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Consolidated Auto",
                "warehouse_id": "WH-03",
                "items": [{"sku": "AUTO-PAD-B2", "quantity": 25}],
                "shipping_address": "1 Central Depot, Chicago, IL"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-007",
                "tracking_number": "FTL-AUTO-CHICAGO-01"
            }),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_078",
        instruction="Shipment 'SHIP-0012' of tiles arrived at 'WH-12', but 100 units of 'BLDG-TILE-J10' were damaged. Receive the shipment with the correct quantity (1100 units), and adjust the inventory to write off the 100 damaged units with reason 'Damaged in Transit'. Confirm the final inventory.",
        actions=[
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0012"}),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0012",
                "items_received": [{"sku": "BLDG-TILE-J10", "quantity": 1100}]
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-12",
                "sku": "BLDG-TILE-J10",
                "quantity_change": -100,
                "reason": "Damaged in Transit"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-12", "sku": "BLDG-TILE-J10"}),
        ],
        outputs=['{"inventory_id": "INV-0010", "quantity_on_hand": 19000}']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_079",
        instruction="An order 'ORD-0010' was created with the wrong SKU. It should be for 'Industrial Paper Roll' (MANU-PAPR-F6), not books. Cancel the incorrect order. Create a new order for 'Kappa Books Pvt Ltd.' for 50 units of 'MANU-PAPR-F6' from 'WH-08' to the same address. Ship via 'Truck' carrier 'CARR-003' with tracking 'PAPER-REORDER-01'.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0010"}),
            Action(name="cancel_outbound_order", kwargs={"order_id": "ORD-0010"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-08"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-08", "sku": "MANU-PAPR-F6"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Kappa Books Pvt Ltd.",
                "warehouse_id": "WH-08",
                "items": [{"sku": "MANU-PAPR-F6", "quantity": 50}],
                "shipping_address": "12 Writer's Block, Mumbai, India"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-003"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-003",
                "tracking_number": "PAPER-REORDER-01"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_080",
        instruction="The carrier for shipment 'SHIP-0004' with carrier ID 'CARR-004', is inactive. Find an alternative 'Sea' carrier with the highest rating (CARR-002). Update the shipment to use the new carrier. Then, update the shipment status to 'In Transit'.",
        actions=[
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-004"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-002"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Sea"}),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0004",
                "carrier_id": "CARR-002",
                "carrier_name": "Nippon Express",
                "carrier_scac": "NPEX"
            }),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0004", "status": "In Transit"}),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0004"}),
        ],
        outputs=['{"shipment_id": "SHIP-0004", "carrier_id": "CARR-002", "status": "In Transit"}']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_081",
        instruction="An order 'ORD-0015' has an invalid shipping address. Cancel the order. Then, create a new order for 'Omicron Trading Ltd.' for the same items (100 units of 'FURN-CHAIR-M13') from 'WH-14' with the corrected address '123 Commerce St, Riyadh, Saudi Arabia'. Ship via 'Truck' carrier 'CARR-003' with tracking 'ADDRESS-FIX-01'.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0015"}),
            Action(name="cancel_outbound_order", kwargs={"order_id": "ORD-0015"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-14"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-14", "sku": "FURN-CHAIR-M13"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Omicron Trading Ltd.",
                "warehouse_id": "WH-14",
                "items": [{"sku": "FURN-CHAIR-M13", "quantity": 100}],
                "shipping_address": "123 Commerce St, Riyadh, Saudi Arabia"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-003"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-003",
                "tracking_number": "ADDRESS-FIX-01"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_082",
        instruction="Inventory of 'Organic Arabica Coffee Beans' (FOOD-COFF-C3) at 'WH-05' is approaching its expiration date ('2025-05-20'). Create a promotional outbound order for 'Theta Foods SA' for 100 units to '200 Avenida Paulista, São Paulo, Brazil'. Ship via 'Air' carrier 'CARR-020' with tracking 'COFFEE-PROMO-01'.",
        actions=[
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-05", "sku": "FOOD-COFF-C3"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Theta Foods SA",
                "warehouse_id": "WH-05",
                "items": [{"sku": "FOOD-COFF-C3", "quantity": 100}],
                "shipping_address": "200 Avenida Paulista, São Paulo, Brazil",
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-020"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-020",
                "tracking_number": "COFFEE-PROMO-01"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_083",
        instruction="A large order for 20,000 '8-bit Microcontroller' (ELEC-CHIP-A1) comes from 'MegaCorp'. 'WH-01' only has 12,500 units. Fulfill what you can from 'WH-01', and fulfill the remaining 7,500 from 'WH-03'. Create two orders for 'MegaCorp' to '1 Mega Plaza, New York, NY'. Ship both via 'CARR-014' with tracking numbers 'MEGA-NY-1' and 'MEGA-NY-2'.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-01", "sku": "ELEC-CHIP-A1"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "ELEC-CHIP-A1"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "MegaCorp",
                "warehouse_id": "WH-01",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 12500}],
                "shipping_address": "1 Mega Plaza, New York, NY"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "MegaCorp",
                "warehouse_id": "WH-03",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 7500}],
                "shipping_address": "1 Mega Plaza, New York, NY"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "MEGA-NY-1"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0018",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "MEGA-NY-2"
            }),
        ],
        outputs=['"order_id": "ORD-0017"', '"order_id": "ORD-0018"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_084",
        instruction="A customer returns a 'Lithium-Ion Battery Pack' (TECH-BATT-Q17) from order 'ORD-0016'. This product was recalled. Adjust the inventory at 'WH-03' to add the unit back with reason 'Recalled Product Return', then immediately adjust it out with reason 'Disposal of Recalled Item'. Confirm final inventory.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0016"}),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-03",
                "sku": "TECH-BATT-Q17",
                "quantity_change": 1,
                "reason": "Recalled Product Return"
            }),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-03",
                "sku": "TECH-BATT-Q17",
                "quantity_change": -1,
                "reason": "Disposal of Recalled Item"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "TECH-BATT-Q17"}),
        ],
        outputs=['{"inventory_id": "INV-0017", "quantity_on_hand": 1500}']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_085",
        instruction="A manufacturing run at 'RoboMation' requires 20 'Articulated Robotic Arm' (TECH-ROBO-N14) to arrive exactly on '2025-09-01'. Find the supplier 'SUP-1016' and create a just-in-time inbound shipment to 'WH-03'. Select an 'Air' carrier that has the best on-time delivery percentage to ensure timeliness.",
        actions=[
            Action(name="find_suppliers", kwargs={"product_categories": ["Automation"]}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1016"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1016",
                "destination_warehouse_id": "WH-03",
                "carrier_id": "CARR-014",
                "items": [{"sku": "TECH-ROBO-N14", "quantity": 20}],
                "estimated_arrival_date": "2025-09-01",
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"})
        ],
        outputs=['"shipment_id": "SHIP-0031"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_086",
        instruction="An inbound shipment of 5000 'Solar Panel 450W' (TECH-SOLR-G7) is planned for 'WH-09', but it is over capacity (currently 85% utilization). Find an alternative warehouse with 'Outdoor Storage' and the lowest utilization. Re-route the shipment 'SHIP-0009' to the new warehouse.",
        actions=[
            Action(name="get_inventory_by_sku", kwargs={
                "sku": "TECH-SOLR-G7"
            }),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-09"}),
            Action(name="find_warehouses", kwargs={"special_capability": "Outdoor Storage"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-11"}),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0009",
                "destination_warehouse_id": "WH-11",
                "destination_warehouse_name": "Denver Heavy Equipment Yard",
                "destination_address": "950 Quarry Rd",
                "destination_city": "Denver",
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0009"}),
        ],
        outputs=['{"shipment_id": "SHIP-0009", "destination_warehouse_id": "WH-11"}']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_087",
        instruction="A quality issue was found with 'Ceramic Brake Pad Set' (AUTO-PAD-B2) from supplier 'SUP-1003'. Cancel the outbound order (ORD-0010). Then, make a return of all 750 units to the supplier (use customer name 'SUP-1003-RETURNS') from warehouse 'WH-03'. Create an outbound shipment to the supplier to the address 'Friedrichstraße 100, Berlin, Germany'. Use 'Air' carrier 'CARR-003' and tracking number 'RETURN-SUP1003-01'. Retrieve the final order details",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0010"}),
            Action(name="cancel_outbound_order", kwargs={"order_id": "ORD-0010"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1003"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-PAD-B2"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "SUP-1003-RETURNS",
                "warehouse_id": "WH-03",
                "items": [{"sku": "AUTO-PAD-B2", "quantity": 750}],
                "shipping_address": "Friedrichstraße 100, Berlin, Germany"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-003"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-003",
                "tracking_number": "RETURN-SUP1003-01"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_088",
        instruction="A hospital in a remote area, 'Mountain View Clinic', needs 20 'Influenza Vaccine' (PHRM-VACC-D4). Find a warehouse with 'Cold Chain (2-8°C)' and 'Pharmaceutical Handling' capability. Choose the warehouse with the highest utilization percentage. Create an order to '15 Mountain Pass, Aspen, CO'. The delivery requires 'Air' transport. Use carrier 'CARR-016'. Ship to address 15 Mountain Pass, Aspen, CO with tracking 'REMOTE-VAX-01'.",
        actions=[
            Action(name="find_warehouses", kwargs={"special_capabilities": ["Cold Chain (2-8°C)", "Pharmaceutical Handling"]}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-06", "sku": "PHRM-VACC-D4"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Mountain View Clinic",
                "warehouse_id": "WH-06",
                "items": [{"sku": "PHRM-VACC-D4", "quantity": 20}],
                "shipping_address": "15 Mountain Pass, Aspen, CO"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-016"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-016",
                "tracking_number": "REMOTE-VAX-01"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_089",
        instruction="Coordinate a multi-modal shipment of 10,000 'Raw Cotton Bale' (MATR-COTT-R18) from 'SUP-1020' in Egypt to 'WH-08' in Detroit. The shipment will travel to 'SUP-1013' (use destination warehouse ID as 'SUP-1013') via 'Rail' 'CARR-001' with ETA '2025-09-20'. Then to Detroit (supplier ID: SUP-1013, destination warehouse: WH-08) via 'Rail' 'CARR-008' with ETA '2025-09-25'. Create the initial inbound shipment to 'SUP-1013', then create a transfer shipment from there to WH-08.",
        actions=[
            Action(name="get_product_by_sku", kwargs={"sku": "MATR-COTT-R18"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Rail"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1020"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1020",
                "destination_warehouse_id": "SUP-1013", # Use supplier's warehouse
                "carrier_id": "CARR-001",
                "items": [{"sku": "MATR-COTT-R18", "quantity": 10000}],
                "estimated_arrival_date": "2025-09-20",
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Rail"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1013"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1013",
                "destination_warehouse_id": "WH-08",
                "carrier_id": "CARR-008",
                "items": [{"sku": "MATR-COTT-R18", "quantity": 10000}],
                "estimated_arrival_date": "2025-09-25",
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"}),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0032"}),
        ],
        outputs=['"shipment_id": "SHIP-0031"', '"shipment_id": "SHIP-0032"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_090",
        instruction="Set up a new distribution lane to Alaska for 'The North Store'. They need 100 'Teak Wood Dining Chair' (FURN-CHAIR-M13). Use warehouse WH-14. Create the order to '1 Ice Road, Anchorage, AK' and ship with 'Air' carrier 'CARR-007'. Tracking 'ALASKA-FURN-01'.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-14", "sku": "FURN-CHAIR-M13"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "The North Store",
                "warehouse_id": "WH-14",
                "items": [{"sku": "FURN-CHAIR-M13", "quantity": 100}],
                "shipping_address": "1 Ice Road, Anchorage, AK"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-007",
                "tracking_number": "ALASKA-FURN-01"
            }),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_091",
        instruction="A drop-shipping order for 'OnlineMart' needs 10 'Smartphone Model X' (ELEC-SMART-W23) to be sent directly from the supplier 'SUP-1030' to the end customer at '123 Main St, Anytown, USA'. First check inventory and supplier details, then create an outbound order with the supplier as the 'warehouse' and ship via 'Truck' using 'DHL Express' (CARR-022) and tracking number 'DROPSHIP-SMART-01'.",
        actions=[
            Action(name="get_inventory_by_sku", kwargs={
                "sku": "ELEC-SMART-W23"
            }),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1030"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "OnlineMart",
                "warehouse_id": "SUP-1030", # Using supplier as source
                "items": [{"sku": "ELEC-SMART-W23", "quantity": 10}],
                "shipping_address": "123 Main St, Anytown, USA"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-022"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-022",
                "tracking_number": "DROPSHIP-SMART-01"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_092",
        instruction="A customer 'DIY Auto' needs 10 'Brake Kits'. Each kit needs 1 'Ceramic Brake Pad Set' (AUTO-PAD-B2) from supplier 'SUP-1003' and 1 'Automotive Windshield' (AUTO-GLAS-U21) from supplier 'SUP-1023'. Create two inbound shipments to 'WH-03' using 'CARR-003' and 'CARR-007' respectively, both with ETA 2025-08-01. Once both have arrived, create an outbound order for the 10 kits to '789 DIY Garage, Detroit, MI' with ETA 2025-08-01.",
        actions=[
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1003"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1003",
                "destination_warehouse_id": "WH-03",
                "carrier_id": "CARR-003",
                "items": [{"sku": "AUTO-PAD-B2", "quantity": 10}],
                "estimated_arrival_date": "2025-08-01"
            }),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1023"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1023",
                "destination_warehouse_id": "WH-03",
                "carrier_id": "CARR-007",
                "items": [{"sku": "AUTO-GLAS-U21", "quantity": 10}],
                "estimated_arrival_date": "2025-08-01"
            }),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0031",
                "items_received": [{"sku": "AUTO-PAD-B2", "quantity": 10}],
            }),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0032",
                "items_received": [{"sku": "AUTO-GLAS-U21", "quantity": 10}],
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-PAD-B2"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-GLAS-U21"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "DIY Auto",
                "warehouse_id": "WH-03",
                "items": [
                    {"sku": "AUTO-PAD-B2", "quantity": 10},
                    {"sku": "AUTO-GLAS-U21", "quantity": 10}
                ],
                "shipping_address": "789 DIY Garage, Detroit, MI"
            }),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_093",
        instruction="Test two carriers for the LA to NYC lane. Send 10 '8-bit Microcontroller' (ELEC-CHIP-A1) from 'WH-01' to 'Test Customer A' at '1 Test St, New York, NY' via 'UPS' (CARR-014), tracking number 'AB-TEST-UPS-01'. Send another 10 units to 'Test Customer B' at '2 Test St, New York, NY' via 'FedEx' (CARR-007), tracking number 'AB-TEST-FEDEX-01'. Retrieve details for both orders.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Test Customer A",
                "warehouse_id": "WH-01",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 10}],
                "shipping_address": "1 Test St, New York, NY"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-01",
                "sku": "ELEC-CHIP-A1"
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Test Customer B",
                "warehouse_id": "WH-01",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 10}],
                "shipping_address": "2 Test St, New York, NY"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-014",
                "tracking_number": "AB-TEST-UPS-01"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0018",
                "new_status": "Shipped",
                "carrier_id": "CARR-007",
                "tracking_number": "AB-TEST-FEDEX-01"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0018"}),
        ],
        outputs=['"order_id": "ORD-0017"', '"order_id": "ORD-0018"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_094",
        instruction="Based on a sales forecast, we need to increase inventory for 'Solar Panel 450W' (TECH-SOLR-G7) at 'WH-09'. The forecast predicts a need for 2000 units next month. Current stock is 1200. Verify warehouse and supplier details and order the difference from the primary supplier 'SUP-1009' to arrive by '2025-08-20' via 'Sea' carrier 'CARR-009'.",
        actions=[
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-09"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-09", "sku": "TECH-SOLR-G7"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1009"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1009",
                "destination_warehouse_id": "WH-09",
                "carrier_id": "CARR-009",
                "items": [{"sku": "TECH-SOLR-G7", "quantity": 800}],
                "estimated_arrival_date": "2025-08-20"
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"}),
        ],
        outputs=['"shipment_id": "SHIP-0031"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_095",
        instruction="A trade show in Las Vegas needs 5 'Articulated Robotic Arm' (TECH-ROBO-N14) and 20 'Lithium-Ion Battery Pack' (TECH-BATT-Q17) from 'WH-03'. Create an order for 'Trade Show Logistics' to 'Las Vegas Convention Center, Las Vegas, NV'. This is a time-critical shipment, so use the 'Air' carrier 'CARR-006' with tracking number 'TRADESHOW-LV-01'.",
        actions=[
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "TECH-ROBO-N14"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-03", "sku": "TECH-BATT-Q17"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Trade Show Logistics",
                "warehouse_id": "WH-03",
                "items": [
                    {"sku": "TECH-ROBO-N14", "quantity": 5},
                    {"sku": "TECH-BATT-Q17", "quantity": 20}
                ],
                "shipping_address": "Las Vegas Convention Center, Las Vegas, NV"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Air"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-006",
                "tracking_number": "TRADESHOW-LV-01"
            }),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_096",
        instruction="The '8-Bit Microcontroller' (ELEC-CHIP-A1) is slow-moving at 'WH-03'. To optimize space, move 200 units to the 'Los Angeles Distribution Center' (WH-01) with ETA '2025-08-10'. Adjust inventory at both locations via an internal transfer.",
        actions=[
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-01"}),
            Action(name="adjust_inventory", kwargs={
                "warehouse_id": "WH-03",
                "sku": "ELEC-CHIP-A1",
                "quantity_change": -200,
                "reason": "Internal Transfer to WH-01 for space optimization"
            }),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "Internal",
                "destination_warehouse_id": "WH-01",
                "carrier_id": "Internal Transfer",
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 200}],
                "estimated_arrival_date": "2025-08-10"
            }),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0031",
                "items_received": [{"sku": "ELEC-CHIP-A1", "quantity": 200}],
            }),
        ],
        outputs=['"shipment_id": "SHIP-0031", "status": "Received"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_097",
        instruction="A customer 'Book Depository' has order 'ORD-0010' which is still pending. They want to add 10 units of 'Industrial Paper Roll' (MANU-PAPR-F6) to this order. Cancel the existing order and create a new one with the updated quantity (210 units) to the same address. Ship via 'Truck' carrier 'CARR-003' with tracking number 'BOOK-DEPOT-UPDATE-01'.",
        actions=[
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0010"}),
            Action(name="cancel_outbound_order", kwargs={"order_id": "ORD-0010"}),
            Action(name="get_inventory_by_sku", kwargs={
                "sku": "MANU-PAPR-F6"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-08", "sku": "MANU-PAPR-F6"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Book Depository",
                "warehouse_id": "WH-08",
                "items": [{"sku": "MANU-PAPR-F6", "quantity": 210}],
                "shipping_address": "12 Writer's Block, Mumbai, India"
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-003",
                "tracking_number": "BOOK-DEPOT-UPDATE-01"
            }),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_098",
        instruction="A port strike has closed the port of Los Angeles. Inbound shipment 'SHIP-0001' must be re-routed. Use an alternative 'Sea' carrier. Update the shipment to use the new carrier 'CARR-011' and destination 'WH-02'. Then, create an inbound shipment with an 'Internal' supplied ID, which includes 1200 units of the item (SKU: ELEC-CHIP-A1) and has an ETA of '2025-07-05'. Then, use 'Truck' transport carrier 'CARR-014' from Seattle to the original destination 'WH-01'.",
        actions=[
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0001"}),
            Action(name="find_carriers", kwargs={"transport_mode": "Sea"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-011"}),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-02"}),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0001",
                "carrier_id": "CARR-011",
                "carrier_name": "MSC Mediterranean Shipping Company",
                "carrier_scac": "MSCU",
                "destination_warehouse_id": "WH-02",
                "destination_warehouse_name": "Seattle Fulfillment Center",
                "destination_address": "789 Harbor Way S",
                "destination_city": "Seattle",
            }),
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-01"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-014"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "Internal",
                "destination_warehouse_id": "WH-01",
                "carrier_id": "CARR-014", # UPS Truck
                "items": [{"sku": "ELEC-CHIP-A1", "quantity": 1200}],
                "estimated_arrival_date": "2025-07-05",
            }),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0001"}),
            Action(name="get_inbound_shipment_details", kwargs={"shipment_id": "SHIP-0031"}),
        ],
        outputs=['"shipment_id": "SHIP-0001"',
                 '"shipment_id": "SHIP-0031"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_099",
        instruction="A customer 'Vintage Cars Club' needs 5 'Ceramic Brake Pad Set' (AUTO-PAD-B2). The stored units of this product are obsolete. Find the supplier 'SUP-1003' and check their details. Create an inbound shipment to 'WH-03' for new units of the product using carrier 'CARR-003' with ETA '2025-08-20' and then fulfill the order to '1 Classic Car Lane, Monterey, CA' using carrier 'CARR-008' and tracking number 'VINTAGE-PADS-09'.",
        actions=[
            Action(name="get_product_by_sku", kwargs={"sku": "AUTO-PAD-B2"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "SUP-1003"}),
            Action(name="create_inbound_shipment", kwargs={
                "supplier_id": "SUP-1003",
                "destination_warehouse_id": "WH-03",
                "carrier_id": "CARR-003",
                "items": [{"sku": "AUTO-PAD-B2", "quantity": 5}],
                "estimated_arrival_date": "2025-08-20"
            }),
            Action(name="get_inventory_in_warehouse", kwargs={
                "warehouse_id": "WH-03",
                "sku": "AUTO-PAD-B2"
            }),
            Action(name="receive_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0031",
                "items_received": [{"sku": "AUTO-PAD-B2", "quantity": 5}],
            }),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Vintage Cars Club",
                "warehouse_id": "WH-03",
                "items": [{"sku": "AUTO-PAD-B2", "quantity": 5}],
                "shipping_address": "1 Classic Car Lane, Monterey, CA"
            }),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-008",
                "tracking_number": "VINTAGE-PADS-09"
            }),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
    Task(
        annotator="samarthkulshrestha",
        user_id="USR_100",
        instruction="A charity 'Goodwill Givers' is receiving a donation of 1000 'Organic Cotton T-Shirt' (APRL-TSHT-O15). Create an order from 'WH-04' to '1 Charity Plaza, Washington D.C.' with the order\'s total value being 0. Ship via 'Truck' carrier 'CARR-008' and tracking number 'DONATION-DC-01'.",
        actions=[
            Action(name="get_warehouse_info", kwargs={"warehouse_id": "WH-04"}),
            Action(name="get_inventory_in_warehouse", kwargs={"warehouse_id": "WH-04", "sku": "APRL-TSHT-O15"}),
            Action(name="create_outbound_order", kwargs={
                "customer_name": "Goodwill Givers",
                "warehouse_id": "WH-04",
                "items": [{"sku": "APRL-TSHT-O15", "quantity": 1000}],
                "total_value": 0,
                "shipping_address": "1 Charity Plaza, Washington D.C.",
            }),
            Action(name="find_carriers", kwargs={"transport_mode": "Truck"}),
            Action(name="get_carrier_details", kwargs={"carrier_id": "CARR-008"}),
            Action(name="update_outbound_order_status", kwargs={
                "order_id": "ORD-0017",
                "new_status": "Shipped",
                "carrier_id": "CARR-008",
                "tracking_number": "DONATION-DC-01"
            }),
            Action(name="get_outbound_order_status", kwargs={"order_id": "ORD-0017"}),
        ],
        outputs=['"order_id": "ORD-0017"']
    ),
]
