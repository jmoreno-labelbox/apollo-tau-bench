from domains.dto import Task, Action


TASKS = [
    # Task 1
    Task(
        annotator="0",
        user_id="U01",
        instruction="Your name is Sarah, the inventory manager for the Los Angeles Distribution Center. Today is 2024-06-10. You just got an alert that the stock of 8-bit Microcontrollers is below the reorder point. Please create a purchase order with our primary supplier, Global Components Inc., to replenish the stock. The order quantity should be double the reorder point. The inbound shipment should be made by sea freight to our warehouse.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Distribution Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="find_carrier_by_method_of_transport",
                kwargs={
                    "method_of_transport": "sea",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1001",
                    "current_date": "2024-06-10",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1001",
                    "supplier_name": "Global Components Inc.",
                    "destination_warehouse_id": "WH-01",
                    "destination_warehouse_name": "Los Angeles Distribution Center",
                    "order_quantity": 8000,
                    "unit_cost": 2.50,
                    "unit_weight": 0.01,
                    "expected_arrival_date": "2024-07-05",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 8000,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 2
    Task(
        annotator="0",
        user_id="U02",
        instruction="You are a logistics specialist. Today is June 12, 2024. We've just received a high-priority order (SO-2024-0011) from a customer, Lambda Healthcare Pty, in Cape Town, South Africa. They need 1,800 units of the Influenza Vaccine. This is a high priority, critical shipment that must be maintained in 5°C. Our Atlanta Cold Chain Center is designated for fulfilling these types of orders. Please process this order: allocate the necessary inventory from the Atlanta warehouse and create the outbound shipment record. Use the fastest available air freight option that supports pharmaceutical cold chain logistics.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Influenza Vaccine",
                },
            ),
            Action(
                name="get_product_details",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Atlanta Cold Chain Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Pharma",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0011",
                    "customer_name": "Lambda Healthcare Pty",
                    "destination_city": "Cape Town",
                    "destination_country": "South Africa",
                    "warehouse_id": "WH-06",
                    "carrier_scac": "UAE",
                    "mode_of_transport": "Air",
                    "shipping_service_level": "Express",
                    "total_units": 1800,
                    "total_weight_kg": 90.0,
                    "temperature_control_required": True,
                    "temperature_celsius": 5,
                    "hazmat": True,
                    "hazmat_class": "6.2",
                    "priority_level": "High",
                    "order_date": "2024-06-12",
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "quantity_to_allocate": 1800,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 3
    Task(
        annotator="0",
        user_id="U03",
        instruction="You are a supply chain analyst, and today is June 18, 2024. There are growing concerns about potential stock-outs for our '8-bit Microcontroller' due to a recent spike in demand. Please conduct a full inventory assessment for this product across all our warehouses. Review all inbound shipments for this product to see if any are delayed. If you find a relevant inbound shipment that is past its expected arrival date, please update its record with a high-priority note: 'URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.'",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="find_inbound_shipments_by_warehouse",
                kwargs={
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="find_inbound_shipments_by_warehouse",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0003",
                    "new_note": "URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0023",
                    "new_note": "URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0019",
                    "new_note": "URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0016",
                    "new_note": "URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0030",
                    "new_note": "URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 4
    Task(
        annotator="0",
        user_id="U04",
        instruction="You are a procurement manager. Today is June 20, 2024. I'm concerned about a delayed shipment of 'Agglomerated Cork Stopper' from our supplier, 'Lisbon Cork Products', which is heading to the 'Los Angeles Beverage DC'. First, find this specific delayed shipment and report its total value and currency. Second, because of this delay, I need you to check the current available inventory and add the following status: 'Critical: Inbound shipment delayed' for this product at the destination warehouse. Finally, as a contingency plan for future orders, find the name of the highest-rated active carrier for 'Sea' transport. Your final answer should be the delayed shipment's value, the current available quantity, and the name of the alternative carrier.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Agglomerated Cork Stopper",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Lisbon Cork Products",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1022",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Beverage DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "MATR-CORK-T20",
                    "warehouse_id": "WH-15",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0020",
                    "new_status": "Critical: Inbound shipment delayed",
                },
            ),
            Action(
                name="find_carrier_by_method_of_transport",
                kwargs={
                    "method_of_transport": "Sea",
                },
            ),
        ],
        outputs=[
            "75000.0 EUR",
            "450000",
            "Nippon Express",
        ],
    ),
    # Task 5
    Task(
        annotator="0",
        user_id="U05",
        instruction="You are a fulfillment coordinator. Today is October 28, 2024. Please process a new sales order, SO-2024-0046, for our customer 'Beta Retail GmbH' for 30 'Leather Handbag' units. This order must be fulfilled from the 'NYC Luxury Vault' and shipped via 'FedEx'. After creating the outbound order, please ensure you update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Leather Handbag",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "NYC Luxury Vault",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "FedEx",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0046",
                    "customer_name": "Beta Retail GmbH",
                    "warehouse_id": "WH-07",
                    "carrier_name": "FedEx",
                    "carrier_scac": "FDEG",
                    "order_date": "2024-10-28",
                    "total_units": 30,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                    "quantity_to_allocate": 30,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 6
    Task(
        annotator="0",
        user_id="U06",
        instruction="You are a purchasing agent. Today is October 25, 2024. Please create a new purchase order for 100 units of the 'Teak Wood Dining Chair' from our supplier, 'Bangkok Furniture Co.'. The shipment should be delivered to the 'Dallas Home Goods DC'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "destination_warehouse_id": "WH-14",
                    "order_quantity": 100,
                    "unit_cost": 120.0,
                    "unit_weight": 8.0,
                    "expected_arrival_date": "2024-11-29",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_add": 100,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
        ],
    ),
    # Task 7
    Task(
        annotator="0",
        user_id="U07",
        instruction="You are a supply chain analyst. Today is June 22, 2024. The manager of the NYC Luxury Vault has completed a cycle count for the 'Automatic Watch Movement' and found a physical quantity of 498 units. Please process this inventory adjustment. You need to update the system to reflect this new physical count and ensure the 'current date' is updated to today.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Automatic Watch Movement",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "NYC Luxury Vault",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="perform_inventory_adjustment",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "new_physical_count": 498,
                    "current_date": "2024-06-22",
                    "reason_note": "Cycle Count Adjustment",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 8
    Task(
        annotator="0",
        user_id="U08",
        instruction="You are a customer service logistics specialist. Today is June 24, 2024. We've just received an urgent call from our customer, Beta Retail GmbH, regarding their sales order SO-2024-0002. The shipment is currently in transit to Hamburg, but they need to divert it to their new central distribution center at 'Gateway Gardens, Frankfurt am Main, 60549, Germany'. Please update the order record to reflect this new destination address and change its status to 'Diverted'. Append a note to the order indicating that the diversion was requested by the customer on today's date.",
        actions=[
            Action(
                name="find_outbound_order_by_so",
                kwargs={
                    "sales_order_number": "SO-2024-0002",
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0002",
                    "destination_address": "Gateway Gardens",
                    "destination_city": "Frankfurt am Main",
                    "destination_country": "Germany",
                    "status": "Diverted",
                    "notes": "Diversion requested by customer on 2024-06-24.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 9
    Task(
        annotator="0",
        user_id="U09",
        instruction="You are a purchasing agent. Today is November 12, 2024. Please create a new purchase order for 50 units of 'Industrial Solvent' from our supplier, 'Helsinki Chemicals Oy'. The shipment should be delivered to the 'Cleveland Chemical Storage' warehouse. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Industrial Solvent",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Helsinki Chemicals Oy",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Cleveland Chemical Storage",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1013",
                    "destination_warehouse_id": "WH-13",
                    "order_quantity": 50,
                    "unit_cost": 150.0,
                    "unit_weight": 20.0,
                    "expected_arrival_date": "2024-11-27",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
        ],
    ),
    # Task 10
    Task(
        annotator="0",
        user_id="U10",
        instruction="You are a specialized logistics coordinator for high-value pharmaceuticals. Today is June 8, 2024. We need to arrange a critical  shipment for a new product, 'Oncology Drug A', from our supplier, 'Stockholm Pharma AB', to our client, 'Delta Pharma Inc.', located in Boston, USA. First, you must create a purchase order for 250 boxes of this drug. Important to note, this product must be maintained at a temperature of 5°C. This shipment needs to be sent to our 'Atlanta Cold Chain Center' warehouse, which is equipped to handle such sensitive materials. Please calculate the expected arrival date at the Atlanta warehouse based on the supplier's standard lead time. You'll need to find the best-rated 'Air' carrier that offers a 'Pharma' service level for this inbound leg. Once the inbound shipment is created, you must immediately update the inventory record at the Atlanta warehouse to show these 250 boxes as 'inbound'.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Oncology Drug A",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Stockholm Pharma AB",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Atlanta Cold Chain Center",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "current_date": "2024-06-08",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Pharma",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "supplier_name": "Stockholm Pharma AB",
                    "destination_warehouse_id": "WH-06",
                    "destination_warehouse_name": "Atlanta Cold Chain Center",
                    "order_quantity": 250,
                    "unit_cost": 1800.00,
                    "unit_weight": 0.5,
                    "expected_arrival_date": "2024-06-16",
                    "carrier_name": "Emirates SkyCargo",
                    "mode_of_transport": "Air",
                    "temperature_control_required": True,
                    "temperature_celsius": 5,
                    "hazmat": False,
                    "priority_level": "Critical",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06",
                    "quantity_to_add": 250,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 11
    Task(
        annotator="0",
        user_id="U11",
        instruction='You are an inventory control specialist. Today is June 6, 2024. A cycle count was just performed for the "Ceramic Brake Pad Set" at our "Chicago Parts Depot". The new physical count is 180 sets. Your first task is to perform an inventory adjustment in the system to reflect this new count. It\'s critical that you account for any currently allocated stock to ensure the new \'quantity available\' is calculated correctly. Please log the reason for this change as "Cycle Count Correction" with today\'s date. After the adjustment is complete, check if the new available quantity for this product has fallen below its reorder point. If it has, you must immediately create a new purchase order to replenish the stock. The order should be for 200 sets from our supplier, "Berlin Auto Parts GmbH", destined for the Chicago Parts Depot. Once the purchase order is created, update the product\'s inventory record to reflect this new inbound quantity.',
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Ceramic Brake Pad Set",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                },
            ),
            Action(
                name="perform_inventory_adjustment",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "new_physical_count": 180,
                    "current_allocated_quantity": 50,
                    "current_date": "2024-06-06",
                    "reason_note": "Cycle Count Correction",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Berlin Auto Parts GmbH",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1003",
                    "supplier_name": "Berlin Auto Parts GmbH",
                    "destination_warehouse_id": "WH-03",
                    "destination_warehouse_name": "Chicago Parts Depot",
                    "order_quantity": 200,
                    "unit_cost": 45.0,
                    "unit_weight": 2.5,
                    "expected_arrival_date": "2024-06-16",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "quantity_to_add": 200,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 12
    Task(
        annotator="0",
        user_id="U12",
        instruction="You are a fulfillment coordinator. Today is November 13, 2024. Please process a new sales order, SO-2024-0052, for our customer 'Beta Retail GmbH' for 30 'Leather Handbag' units. This order should be fulfilled from the 'NYC Luxury Vault'. For this urgent shipment, please select the highest-rated carrier that offers 'Express' service via 'Air'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Leather Handbag",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "NYC Luxury Vault",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Express",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0052",
                    "customer_name": "Beta Retail GmbH",
                    "warehouse_id": "WH-07",
                    "carrier_name": "Emirates SkyCargo",
                    "carrier_scac": "UAE",
                    "order_date": "2024-11-13",
                    "total_units": 30,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                    "quantity_to_allocate": 30,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 13
    Task(
        annotator="0",
        user_id="U13",
        instruction='You are a Quality Control Logistics Manager. Today is June 7, 2024. We have received a quality alert regarding lot number \'LOT202405A\' for the "8-bit Microcontroller". You must find all inventory records for this product across all warehouses that match this exact lot number and update their status to \'Quarantined\'. After you have quarantined all affected stock, you must raise an urgent replacement purchase order for 15,000 units of the "8-bit Microcontroller" from our trusted supplier, "Tokyo Electronics Ltd.", with high priority. This replacement order should be sent to the "Los Angeles Distribution Center". Please find the highest-rated \'Air\' carrier for this urgent shipment, calculate the expected arrival date, and ensure the inbound quantity for the product at the Los Angeles warehouse is updated to reflect this new order.',
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0001",
                    "new_status": "Quarantined",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Tokyo Electronics Ltd.",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Distribution Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "current_date": "2024-06-07",
                },
            ),
            Action(
                name="find_carrier_by_method_of_transport",
                kwargs={
                    "method_of_transport": "Air",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "supplier_name": "Tokyo Electronics Ltd.",
                    "destination_warehouse_id": "WH-01",
                    "destination_warehouse_name": "Los Angeles Distribution Center",
                    "order_quantity": 15000,
                    "unit_cost": 2.5,
                    "unit_weight": 0.01,
                    "expected_arrival_date": "2024-06-22",
                    "carrier_name": "Emirates SkyCargo",
                    "mode_of_transport": "Air",
                    "priority_level": "High",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 15000,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 14
    Task(
        annotator="0",
        user_id="U14",
        instruction="You are an order fulfillment specialist. Today is June 8, 2024. Our customer, 'Alpha Electronics LLC', located in San Jose, USA, has placed a new order (Sales Order SO-2024-7788) for 8,000 units of the \"8-bit Microcontroller\" and 1,000 units of the \"Lithium-Ion Battery Pack\". The entire order must be fulfilled from a single warehouse. Please identify a warehouse that has sufficient available stock for both products. Once you've found a suitable warehouse, create a single outbound order using the most economical (cheapest) 'Truck' carrier that offers 'LTL' service. Since this shipment contains hazardous materials, ensure the order is flagged appropriately (hazmat class 9). Finally, after creating the order, make sure to allocate the stock for both products from the chosen warehouse.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Lithium-Ion Battery Pack",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-7788",
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "destination_country": "USA",
                    "warehouse_id": "WH-03",
                    "carrier_name": "FedEx",
                    "carrier_scac": "FDEG",
                    "mode_of_transport": "Truck",
                    "shipping_service_level": "LTL",
                    "total_units": 9000,
                    "total_weight_kg": 780.0,
                    "hazmat": True,
                    "hazmat_class": "9",
                    "order_date": "2024-06-08",
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 8000,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 1000,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 15
    Task(
        annotator="0",
        user_id="U15",
        instruction="You are a logistics coordinator. Today is June 9, 2024. Our customer, 'Gamma Construction Ltd.' in Denver, has placed an order (SO-2024-8801) for 10 'Articulated Robotic Arm' units. This is a heavy and fragile product. First, find a warehouse that has at least 10 units available and also has 'Heavy Equipment Handling' as a special capability. Once you have identified the correct warehouse, create the outbound order. For shipping, you must find the highest-rated 'Rail' carrier that offers 'Intermodal' service. After creating the order, please ensure you allocate the 10 units from the source warehouse's inventory.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Rail",
                    "service_level": "Intermodal",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-8801",
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "destination_country": "USA",
                    "warehouse_id": "WH-03",
                    "carrier_name": "Maersk",
                    "carrier_scac": "MAEU",
                    "mode_of_transport": "Rail",
                    "shipping_service_level": "Intermodal",
                    "total_units": 10,
                    "order_date": "2024-06-09",
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 10,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 16
    Task(
        annotator="0",
        user_id="U16",
        instruction="You are a supply chain analyst. Today is June 19, 2024. An alert has been raised for a delayed shipment from 'Seoul Textiles Co.' to our 'Newark Apparel Hub'. Please find this shipment. The current note likely mentions a typhoon, but I need you to perform a root cause analysis by checking the operational status of the assigned carrier. Update the shipment's notes with your findings (e.g., 'Root cause: Carrier is inactive'). After updating the shipment, I need a financial risk assessment for a different critical product at the Newark Apparel Hub: the 'Raw Cotton Bale'. Please calculate the total current value of all on-hand inventory for this specific product at that warehouse. Your final answer should be only this total dollar amount.",
        actions=[
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Seoul Textiles Co.",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Newark Apparel Hub",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1004",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "Hanjin",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0004",
                    "new_note": "Root cause: Carrier is inactive.",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Raw Cotton Bale",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                },
            ),
        ],
        outputs=[
            "160000.0",
        ],
    ),
    # Task 17
    Task(
        annotator="0",
        user_id="U17",
        instruction="You are a purchasing agent. Today is October 29, 2024. Please create a new purchase order for 200 'Solar Panel 450W' units from our supplier, 'Beijing Solar Tech'. The shipment should be delivered to the 'Phoenix Renewable Warehouse'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Solar Panel 450W",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Beijing Solar Tech",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1009",
                    "destination_warehouse_id": "WH-09",
                    "order_quantity": 200,
                    "unit_cost": 180.0,
                    "unit_weight": 22.0,
                    "expected_arrival_date": "2024-11-28",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "quantity_to_add": 200,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
        ],
    ),
    # Task 18
    Task(
        annotator="0",
        user_id="U18",
        instruction="You are a fulfillment coordinator. Today is October 30, 2024. Please process a new sales order, SO-2024-0047, for our customer 'Gamma Construction Ltd.' for 20 'Automotive Windshield' units. This order should be fulfilled from the 'Chicago Parts Depot' and shipped via 'UPS'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Automotive Windshield",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "UPS",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0047",
                    "customer_name": "Gamma Construction Ltd.",
                    "warehouse_id": "WH-03",
                    "carrier_name": "UPS",
                    "carrier_scac": "UPSN",
                    "order_date": "2024-10-30",
                    "total_units": 20,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 20,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 19
    Task(
        annotator="0",
        user_id="U19",
        instruction="You are a purchasing agent. Today is October 31, 2024. Please create a new purchase order for 50 'Raw Cotton Bale' units from our supplier, 'Cairo Cotton Co.'. The shipment should be delivered to the 'Newark Apparel Hub'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Raw Cotton Bale",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Cairo Cotton Co.",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Newark Apparel Hub",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1020",
                    "destination_warehouse_id": "WH-04",
                    "order_quantity": 50,
                    "unit_cost": 800.0,
                    "unit_weight": 227.0,
                    "expected_arrival_date": "2024-11-25",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
        ],
    ),
    # Task 20
    Task(
        annotator="0",
        user_id="U20",
        instruction="You are a fulfillment coordinator. Today is November 1, 2024. Please process a new sales order, SO-2024-0048, for our customer 'Theta Foods SA' for 100 'Frozen Tuna Loin' units. This order should be fulfilled from the 'San Francisco Fresh Foods DC' and shipped via 'Qantas Freight'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Frozen Tuna Loin",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "San Francisco Fresh Foods DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "Qantas Freight",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0048",
                    "customer_name": "Theta Foods SA",
                    "warehouse_id": "WH-10",
                    "carrier_name": "Qantas Freight",
                    "carrier_scac": "QFA",
                    "order_date": "2024-11-01",
                    "total_units": 100,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                    "quantity_to_allocate": 100,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 21
    Task(
        annotator="0",
        user_id="U21",
        instruction="You are an inventory planner for perishable goods. Today is June 10, 2024. The current stock of 'Fresh Cut Roses' at the 'San Francisco Fresh Foods DC' expires in two days. We need to proactively place a replenishment order for 5,000 bouquets from our supplier, 'Bogota Floral Exports'. For the shipment, you must select the highest-rated 'Air' carrier that offers a 'Perishables' service level. Create the purchase order with the correct details and then update the inbound inventory for the roses at the San Francisco warehouse.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Fresh Cut Roses",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "San Francisco Fresh Foods DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Bogota Floral Exports",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1029",
                    "current_date": "2024-06-10",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Perishables",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1029",
                    "supplier_name": "Bogota Floral Exports",
                    "destination_warehouse_id": "WH-10",
                    "destination_warehouse_name": "San Francisco Fresh Foods DC",
                    "order_quantity": 5000,
                    "unit_cost": 12.0,
                    "unit_weight": 0.5,
                    "expected_arrival_date": "2024-06-12",
                    "carrier_name": "Emirates SkyCargo",
                    "mode_of_transport": "Air",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                    "quantity_to_add": 5000,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 22
    Task(
        annotator="0",
        user_id="U22",
        instruction="You are a purchasing agent. Today is November 4, 2024. Please create a new purchase order for 50 'Automatic Watch Movement' units from our supplier, 'Zurich Watch Parts AG'. The shipment should be delivered to the 'NYC Luxury Vault'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Automatic Watch Movement",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Zurich Watch Parts AG",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "NYC Luxury Vault",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1014",
                    "destination_warehouse_id": "WH-07",
                    "order_quantity": 50,
                    "unit_cost": 300.0,
                    "unit_weight": 0.05,
                    "expected_arrival_date": "2024-11-09",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
        ],
    ),
    # Task 23
    Task(
        annotator="0",
        user_id="U23",
        instruction="You are a customer service logistics specialist. Today is June 11, 2024. Our customer, 'Alpha Electronics LLC', has contacted us about their order SO-2024-0001. They report that they received the wrong items. The order was for 300 '8-bit Microcontrollers'. Please verify the original order details and confirm that the fulfillment warehouse has enough available stock of the correct item to send a replacement. If stock is available, create a new, corrected outbound shipment for the 300 '8-bit Microcontrollers'. Use 'SO-2024-0001-CORRECTIVE' as the new sales order number. This replacement must be expedited, so please use the highest-rated 'Air' carrier that offers 'Express' service. After creating the new order, ensure you allocate the stock and add a note to the original order (ORD-0001) stating ''Corrective shipment ORD-0017 created on 2024-06-11 for 300 units of 8-bit Microcontroller.'",
        actions=[
            Action(
                name="find_outbound_order_by_so",
                kwargs={
                    "sales_order_number": "SO-2024-0001",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Express",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0001-CORRECTIVE",
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "destination_country": "USA",
                    "warehouse_id": "WH-01",
                    "carrier_name": "Emirates SkyCargo",
                    "carrier_scac": "UAE",
                    "mode_of_transport": "Air",
                    "shipping_service_level": "Express",
                    "total_units": 300,
                    "total_weight_kg": 3.0,
                    "temperature_control_required": False,
                    "temperature_celsius": None,
                    "hazmat": False,
                    "hazmat_class": None,
                    "priority_level": "High",
                    "order_date": "2024-06-11",
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 300,
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0001",
                    "notes": "Corrective shipment ORD-0017 created on 2024-06-11 for 300 units of 8-bit Microcontroller.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 24
    Task(
        annotator="0",
        user_id="U24",
        instruction="You are a purchasing agent. Today is November 8, 2024. Please create a new purchase order for 100,000 'Agglomerated Cork Stopper' units from our supplier, 'Lisbon Cork Products'. The shipment should be delivered to the 'Los Angeles Beverage DC'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Agglomerated Cork Stopper",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Lisbon Cork Products",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Beverage DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "MATR-CORK-T20",
                    "warehouse_id": "WH-15",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1022",
                    "destination_warehouse_id": "WH-15",
                    "order_quantity": 100000,
                    "unit_cost": 0.05,
                    "unit_weight": 0.005,
                    "expected_arrival_date": "2024-11-28",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "MATR-CORK-T20",
                    "warehouse_id": "WH-15",
                    "quantity_to_add": 100000,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
        ],
    ),
    # Task 25
    Task(
        annotator="0",
        user_id="U25",
        instruction="You are a fulfillment coordinator. Today is November 5, 2024. Please process a new sales order, SO-2024-0049, for our customer 'Gamma Construction Ltd.' for 30 'Industrial Paper Roll' units. This order should be fulfilled from the 'Detroit Packaging Supplies' warehouse. Please select the highest-rated carrier that offers 'LTL' service via 'Truck'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Industrial Paper Roll",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Detroit Packaging Supplies",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0049",
                    "customer_name": "Gamma Construction Ltd.",
                    "warehouse_id": "WH-08",
                    "carrier_name": "Nippon Express",
                    "carrier_scac": "NPEX",
                    "order_date": "2024-11-05",
                    "total_units": 30,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08",
                    "quantity_to_allocate": 30,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 26
    Task(
        annotator="0",
        user_id="U26",
        instruction="You are a purchasing agent. Today is November 6, 2024. Please create a new purchase order for 120 'Teak Wood Dining Chair' units from our supplier, 'Bangkok Furniture Co.'. The shipment should be delivered to the 'Dallas Home Goods DC'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "destination_warehouse_id": "WH-14",
                    "order_quantity": 120,
                    "unit_cost": 120.0,
                    "unit_weight": 8.0,
                    "expected_arrival_date": "2024-12-11",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_add": 120,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
        ],
    ),
    # Task 27
    Task(
        annotator="0",
        user_id="U27",
        instruction="You are a Quality Assurance Manager. Today is June 13, 2024. A critical quality alert has been issued for all of our '8-bit Microcontroller' stock. First, find every warehouse holding this product and update the inventory status to 'Quarantined'. Next, calculate the total value of all the stock you just quarantined. As a contingency, we will use our preferred supplier, 'Tokyo Electronics Ltd.', for replenishment. Place a new purchase order for 20,000 units from them. The shipment should be sent to the warehouse that had the largest quantity of the quarantined stock. Use the most economical 'Sea' freight carrier that offers 'FCL' service. Finally, after creating the purchase order, update the inbound inventory at the destination warehouse.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0001",
                    "new_status": "Quarantined",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0025",
                    "new_status": "Quarantined",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Tokyo Electronics Ltd.",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "current_date": "2024-06-13",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Sea",
                    "service_level": "FCL",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "supplier_name": "Tokyo Electronics Ltd.",
                    "destination_warehouse_id": "WH-01",
                    "destination_warehouse_name": "Los Angeles Distribution Center",
                    "order_quantity": 20000,
                    "unit_cost": 2.5,
                    "unit_weight": 0.01,
                    "expected_arrival_date": "2024-06-28",
                    "carrier_name": "COSCO",
                    "carrier_scac": "COSU",
                    "mode_of_transport": "Sea",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 20000,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 28
    Task(
        annotator="0",
        user_id="U28",
        instruction="You are a high-value logistics coordinator. Today is June 14, 2024. We have a priority order from our client, 'ChronoSwiss Retailers' in Geneva, Switzerland, for 50 'Automatic Watch Movement' units (Sales Order SO-2024-9951). This order must be fulfilled from a warehouse that is 'UL Certified Vault' and has 'High Security' capabilities. Please find a suitable warehouse with sufficient stock, select the highest-rated 'Air' carrier offering a 'High-Value' service level, and create the outbound order. After creating the order and allocating the stock, report back with the total value of the shipment in USD.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Automatic Watch Movement",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "High-Value",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-9951",
                    "customer_name": "ChronoSwiss Retailers",
                    "destination_city": "Geneva",
                    "destination_country": "Switzerland",
                    "warehouse_id": "WH-07",
                    "carrier_name": "Emirates SkyCargo",
                    "carrier_scac": "UAE",
                    "mode_of_transport": "Air",
                    "shipping_service_level": "High-Value",
                    "total_units": 50,
                    "total_weight_kg": 2.5,
                    "temperature_control_required": False,
                    "temperature_celsius": None,
                    "hazmat": False,
                    "hazmat_class": None,
                    "priority_level": "High",
                    "order_date": "2024-06-14",
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "quantity_to_allocate": 50,
                },
            ),
        ],
        outputs=[
            "25000.0",
        ],
    ),
    # Task 29
    Task(
        annotator="0",
        user_id="U29",
        instruction="You are a logistics coordinator. Today is June 20, 2024. Management has decided to increase our safety stock for 'Oncology Drug A' at the Atlanta Cold Chain Center. This is a product that requires strict temperature control of 5°C. Please initiate a new purchase order for 250 units from our supplier with a critical priority, Stockholm Pharma AB. You will need to find the highest-rated carrier that can handle a 'Pharma' service level via 'Air' transport. After creating the purchase order, ensure you update the inventory pipeline to reflect the new inbound quantity. As a final answer, please provide the newly generated Purchase Order number and the expected arrival date for the shipment.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Oncology Drug A",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Atlanta Cold Chain Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Stockholm Pharma AB",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "current_date": "2024-06-20",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Pharma",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "supplier_name": "Stockholm Pharma AB",
                    "destination_warehouse_id": "WH-06",
                    "destination_warehouse_name": "Atlanta Cold Chain Center",
                    "order_quantity": 250,
                    "unit_cost": 1200.0,
                    "unit_weight": 0.5,
                    "expected_arrival_date": "2024-06-28",
                    "carrier_name": "Emirates SkyCargo",
                    "mode_of_transport": "Air",
                    "priority_level": "Critical",
                    "temperature_control_required": True,
                    "temperature_celsius": 5,
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06",
                    "quantity_to_add": 250,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "2024-06-28",
        ],
    ),
    # Task 30
    Task(
        annotator="0",
        user_id="U30",
        instruction="You are a fulfillment coordinator. Today is November 7, 2024. Please process a new sales order, SO-2024-0050, for our customer 'Nu Energy AB' for 50 'Solar Panel 450W' units. This order should be fulfilled from the 'Phoenix Renewable Warehouse'. For this type of large, international shipment, please select the highest-rated carrier that offers 'Project Cargo' service via 'Sea'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Solar Panel 450W",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Sea",
                    "service_level": "Project Cargo",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0050",
                    "customer_name": "Nu Energy AB",
                    "warehouse_id": "WH-09",
                    "carrier_name": "CMA CGM",
                    "carrier_scac": "CMDU",
                    "order_date": "2024-11-07",
                    "total_units": 50,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "quantity_to_allocate": 50,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 31
    Task(
        annotator="0",
        user_id="U31",
        instruction="You are a fulfillment specialist. Today is June 22, 2024. We have a new order from 'Gamma Construction Ltd.', located in Denver, USA for 75 units of the 'Lithium-Ion Battery Pack', which must be shipped from our Chicago Parts Depot. This is a hazmat class 9 shipment, so first, you must confirm that the Chicago warehouse is certified to handle hazardous materials. Once confirmed, please find the most economical carrier that provides 'LTL' service for 'Truck' transport. After selecting the carrier, create the outbound order with sales order number SO-2024-0019 and allocate the inventory. Please respond with the new Order ID and the name of the assigned carrier.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Lithium-Ion Battery Pack",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0019",
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "destination_country": "USA",
                    "warehouse_id": "WH-03",
                    "carrier_name": "FedEx",
                    "carrier_scac": "FDEG",
                    "mode_of_transport": "Truck",
                    "shipping_service_level": "LTL",
                    "order_date": "2024-06-22",
                    "total_units": 75,
                    "total_weight_kg": 52.5,
                    "hazmat": True,
                    "hazmat_class": "9",
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 75,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "FedEx",
        ],
    ),
    # Task 32
    Task(
        annotator="0",
        user_id="U32",
        instruction="You are a supplier relationship manager. I'm concerned about the performance of 'Johannesburg Mining Equipment'. First, please retrieve their supplier details to verify if their performance rating is less than 4.5. Then, find any of their inbound shipments that are currently 'In Transit' and update the shipment's notes to add: 'Flagged for priority QA inspection upon arrival due to low supplier rating.' After flagging the shipment, I need you to calculate the total value of the 'Diamond Core Drill Bit' inventory currently on hand using the unit cost at that shipment's destination warehouse. Please return only the final calculated dollar amount.",
        actions=[
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Johannesburg Mining Equipment",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1011",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1011",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0011",
                    "new_note": "Flagged for priority QA inspection upon arrival due to low supplier rating.",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Diamond Core Drill Bit",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Denver Heavy Equipment Yard",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                },
            ),
        ],
        outputs=[
            "88000.0",
        ],
    ),
    # Task 33
    Task(
        annotator="0",
        user_id="U33",
        instruction="You are a warehouse manager at the San Francisco Fresh Foods DC. Today is June 23, 2024. A cycle count for 'Fresh Cut Roses' revealed a physical count of 2800 bouquets. Please perform an inventory adjustment in the system, noting the reason as 'Cycle count discrepancy'. After the adjustment, this leaves us with critically low stock. Please immediately initiate an emergency replenishment order from our preferred supplier, 'Bogota Floral Exports', to bring our on-hand quantity up to a target level of 5000 units. This is a highly perishable item, so you must select the highest-rated 'Air' carrier that offers a 'Perishables' service level and a temperature control of 4 degrees Celsius. Once the purchase order is created and the inventory pipeline is updated, respond with the new PO number and the name of the carrier you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Fresh Cut Roses",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "San Francisco Fresh Foods DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "FOOD-FLWR-X24", "warehouse_id": "WH-10"},
            ),
            Action(
                name="perform_inventory_adjustment",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                    "new_physical_count": 2800,
                    "current_date": "2024-06-23",
                    "reason_note": "Cycle count discrepancy",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Bogota Floral Exports",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1029",
                    "current_date": "2024-06-23",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Perishables",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1029",
                    "supplier_name": "Bogota Floral Exports",
                    "destination_warehouse_id": "WH-10",
                    "destination_warehouse_name": "San Francisco Fresh Foods DC",
                    "order_quantity": 2200,
                    "unit_cost": 12.0,
                    "unit_weight": 0.5,
                    "expected_arrival_date": "2024-06-25",
                    "carrier_name": "Emirates SkyCargo",
                    "mode_of_transport": "Air",
                    "temperature_control_required": True,
                    "temperature_celsius": 4,
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                    "quantity_to_add": 2200,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "Emirates SkyCargo",
        ],
    ),
    # Task 34
    Task(
        annotator="0",
        user_id="U34",
        instruction="You are a senior logistics coordinator. Today is June 24, 2024. We have an urgent order from Alpha Electronics LLC for 50 drums of 'Industrial Solvent'. Their default fulfillment site is the Los Angeles Distribution Center, but I need you to first confirm if they even stock it. If not, find an alternative warehouse that has sufficient available stock. Because this is a hazardous material, you MUST verify that the alternative warehouse is certified to handle Hazmat Class 3 products before proceeding. Once you've confirmed a suitable warehouse, select the highest-rated carrier for 'Truck' transport offering 'LTL' service. Finally, create the outbound order using sales order number SO-2024-0020 and allocate the inventory from the correct warehouse. Please respond with the new Order ID and the name of the warehouse you fulfilled the order from.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Industrial Solvent",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={"warehouse_name": "Los Angeles Distribution Center"},
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-13",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0020",
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "Cleveland",
                    "destination_country": "USA",
                    "warehouse_id": "WH-13",
                    "carrier_name": "Nippon Express",
                    "carrier_scac": "NPEX",
                    "mode_of_transport": "Truck",
                    "shipping_service_level": "LTL",
                    "order_date": "2024-06-24",
                    "total_units": 50,
                    "total_weight_kg": 1000.0,
                    "hazmat": True,
                    "hazmat_class": "3",
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "quantity_to_allocate": 50,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Cleveland Chemical Storage",
        ],
    ),
    # Task 35
    Task(
        annotator="0",
        user_id="U35",
        instruction="You are a logistics expansion manager. Today is June 25, 2024. We are expanding our furniture line and need to begin stocking the 'Teak Wood Dining Chair' at our Phoenix Renewable Warehouse. Please execute the full setup process. First, verify that no inventory record for this product exists at this warehouse. If none exists, create a new one. Then, place an initial stocking order for 150 chairs from our supplier, 'Bangkok Furniture Co.'. For this international shipment, please select the best-rated carrier for 'Sea' transport. After creating the purchase order, ensure the inventory pipeline for the new record is updated. To confirm completion, please respond with the new Purchase Order number and the new Inventory ID you created.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                },
            ),
            Action(
                name="create_inventory_record",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "current_date": "2024-06-25",
                },
            ),
            Action(
                name="find_carrier_by_method_of_transport",
                kwargs={
                    "method_of_transport": "Sea",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "supplier_name": "Bangkok Furniture Co.",
                    "destination_warehouse_id": "WH-09",
                    "destination_warehouse_name": "Phoenix Renewable Warehouse",
                    "order_quantity": 150,
                    "unit_cost": 120.0,
                    "unit_weight": 8.0,
                    "expected_arrival_date": "2024-07-30",
                    "carrier_name": "Nippon Express",
                    "mode_of_transport": "Sea",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-09",
                    "quantity_to_add": 150,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "INV-0026",
        ],
    ),
    # Task 36
    Task(
        annotator="0",
        user_id="U36",
        instruction="You are a logistics coordinator. Our customer, 'Gamma Construction Ltd.', has requested an urgent diversion for their order SO-2024-0003. The new destination is '555 Industrial Way, Salt Lake City, USA'. Please process this change. First, find the order. Then, find the cheapest carrier for its 'LCL' service level and 'Truck' mode of transport to handle the new route. Update the order with the new destination, the new carrier's details, change its status to 'Diverted', and add a note: 'Diverted to Salt Lake City per customer request. Carrier re-evaluated for new route.' After processing the diversion, I need you to calculate the total value of all other shipments currently 'In Transit' to the order's *original* fulfillment warehouse. Please ignore currency differences for this calculation and return only the final sum.",
        actions=[
            Action(
                name="find_outbound_order_by_so",
                kwargs={
                    "sales_order_number": "SO-2024-0003",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LCL",
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0003",
                    "destination_address": "555 Industrial Way",
                    "destination_city": "Salt Lake City",
                    "destination_country": "USA",
                    "status": "Diverted",
                    "carrier_name": "Maersk",
                    "carrier_scac": "MAEU",
                    "notes": "Diverted to Salt Lake City per customer request. Carrier re-evaluated for new route.",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Miami Building Materials",
                },
            ),
            Action(
                name="find_inbound_shipments_by_warehouse",
                kwargs={
                    "warehouse_id": "WH-12",
                },
            ),
        ],
        outputs=[
            "220000.0",
        ],
    ),
    # Task 37
    Task(
        annotator="0",
        user_id="U37",
        instruction="You are a quality assurance manager. We have a critical quality alert for lot number 'LOT202405A' of the '8-bit Microcontroller', which originated from the supplier 'Global Components Inc.'. Your first priority is to locate the specific inventory record for this lot and update its status to 'Quarantined'. After that, as a precaution, find any shipments from this same supplier that are currently 'In Transit' and add a note to them stating: 'Contains product from a lot number under quality review. Inspect upon arrival.' Please respond with the ID of the inventory record you quarantined and the ID of the shipment you flagged.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0001",
                    "new_status": "Quarantined",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1001",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "new_note": "Contains product from a lot number under quality review. Inspect upon arrival.",
                },
            ),
        ],
        outputs=[
            "INV-0001",
            "SHIP-0001",
        ],
    ),
    # Task 38
    Task(
        annotator="0",
        user_id="U38",
        instruction="You are a senior logistics analyst. Today is June 26, 2024. We have an escalated issue for a delayed order, SO-2024-0002, for 'Beta Retail GmbH'. To prevent a stock-out of other critical items at that warehouse, create a new purchase order for 2000 units of the 'Smartphone Model X' from our preferred supplier, 'Tokyo Electronics Ltd.'. Ship it using the best-rated 'Air' carrier.",
        actions=[
            Action(
                name="find_outbound_order_by_so",
                kwargs={
                    "sales_order_number": "SO-2024-0002",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Smartphone Model X",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Tokyo Electronics Ltd.",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "current_date": "2024-06-26",
                },
            ),
            Action(
                name="find_carrier_by_method_of_transport",
                kwargs={
                    "method_of_transport": "Air",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "supplier_name": "Tokyo Electronics Ltd.",
                    "destination_warehouse_id": "WH-02",
                    "destination_warehouse_name": "Seattle Fulfillment Center",
                    "order_quantity": 2000,
                    "unit_cost": 650.0,
                    "unit_weight": 0.4,
                    "expected_arrival_date": "2024-07-11",
                    "carrier_name": "Emirates SkyCargo",
                    "mode_of_transport": "Air",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "quantity_to_add": 2000,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 39
    Task(
        annotator="0",
        user_id="U39",
        instruction="You are a fulfillment coordinator. Today is November 11, 2024. Please process a new sales order, SO-2024-0051, for our customer 'Beta Retail GmbH' for 80 'Teak Wood Dining Chair' units. This order should be fulfilled from the 'Dallas Home Goods DC'. Please select the highest-rated carrier that offers 'LCL' service via 'Truck'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LCL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0051",
                    "customer_name": "Beta Retail GmbH",
                    "warehouse_id": "WH-14",
                    "carrier_name": "Maersk",
                    "carrier_scac": "MAEU",
                    "order_date": "2024-11-11",
                    "total_units": 80,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_allocate": 80,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 40
    Task(
        annotator="0",
        user_id="U40",
        instruction="You are an inventory planner. Today is June 27, 2024. I'm reviewing our stock levels and see that the 'Ceramic Floor Tile' at the Miami Building Materials warehouse is approaching its reorder point. Place a replenishment order from our supplier, 'Madrid Ceramic Tiles', for a quantity sufficient to bring our 'quantity_available' up to 20,000 units. Find the cheapest carrier that offers 'FCL' service via 'Sea' for this shipment. After creating the purchase order and updating the inventory pipeline, please respond with the new PO number.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Ceramic Floor Tile",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Miami Building Materials",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Madrid Ceramic Tiles",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1012",
                    "current_date": "2024-06-27",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Sea",
                    "service_level": "FCL",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1012",
                    "supplier_name": "Madrid Ceramic Tiles",
                    "destination_warehouse_id": "WH-12",
                    "destination_warehouse_name": "Miami Building Materials",
                    "order_quantity": 5000,
                    "unit_cost": 3.5,
                    "unit_weight": 5.0,
                    "expected_arrival_date": "2024-07-22",
                    "carrier_name": "COSCO",
                    "carrier_scac": "COSU",
                    "mode_of_transport": "Sea",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                    "quantity_to_add": 5000,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
        ],
    ),
    # Task 41
    Task(
        annotator="0",
        user_id="U41",
        instruction="You are a supply chain risk manager. Today is June 29, 2024. We need to assess risks associated with our key Chinese suppliers: 'Global Components Inc.', 'Beijing Solar Tech', and 'Shanghai Electronics Co.'. For each of these suppliers, please check their performance rating. If a supplier's rating is below 4.7, find all of their inbound shipments that are currently 'In Transit' and add a note to each of those shipments: 'Flagged for priority QA inspection due to supplier performance review.' As a final answer, please provide a list of the shipment IDs you updated.",
        actions=[
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Beijing Solar Tech",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Shanghai Electronics Co.",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1001",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1009",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1025",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1001",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1009",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1025",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "new_note": "Flagged for priority QA inspection due to supplier performance review.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0009",
                    "new_note": "Flagged for priority QA inspection due to supplier performance review.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0025",
                    "new_note": "Flagged for priority QA inspection due to supplier performance review.",
                },
            ),
        ],
        outputs=[
            "SHIP-0001",
            "SHIP-0009",
            "SHIP-0025",
        ],
    ),
    # Task 42
    Task(
        annotator="0",
        user_id="U42",
        instruction="You are an inventory manager. Today is July 1, 2024. I need you to conduct a shelf-life audit on a few key products. Please review the inventory for 'Organic Arabica Coffee Beans', 'Influenza Vaccine', and 'Frozen Tuna Loin'. For each of these products, find their inventory records across all warehouses. If any specific inventory lot has an expiration date before June 30, 2025, please update its stock status to 'FEFO Audit Required'. Please respond with a list of the Inventory IDs that you updated.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Organic Arabica Coffee Beans",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Influenza Vaccine",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Frozen Tuna Loin",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0003",
                    "new_status": "FEFO Audit Required",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0008",
                    "new_status": "FEFO Audit Required",
                },
            ),
        ],
        outputs=[
            "INV-0003",
            "INV-0008",
        ],
    ),
    # Task 43
    Task(
        annotator="0",
        user_id="U43",
        instruction="You are a compliance manager. Today is July 5, 2024. As part of our quarterly audit, I need you to verify that all of our 'Preferred' suppliers are 'ISO 9001' certified. Please review each of our preferred partners: 'Tokyo Electronics Ltd.', 'São Paulo Coffee Exporters', 'Sydney Seafood Exporters', 'Helsinki Chemicals Oy', 'Osaka Robotics Corp.', 'Warsaw IT Components', and 'Bogota Floral Exports'. For any of these suppliers that are NOT ISO 9001 certified, find all of their inbound shipments that are currently in 'Planned' status and add a note to each one: 'Hold for Supplier Compliance Verification.' Please respond with a list of the Shipment IDs you updated.",
        actions=[
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Tokyo Electronics Ltd.",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "São Paulo Coffee Exporters",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Sydney Seafood Exporters",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Helsinki Chemicals Oy",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Osaka Robotics Corp.",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Warsaw IT Components",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Bogota Floral Exports",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1029",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1019",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1016",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1013",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1010",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1005",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1002",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1010",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1029",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1005",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0010",
                    "new_note": "Hold for Supplier Compliance Verification.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0029",
                    "new_note": "Hold for Supplier Compliance Verification.",
                },
            ),
        ],
        outputs=[
            "SHIP-0010",
            "SHIP-0029",
        ],
    ),
    # Task 44
    Task(
        annotator="0",
        user_id="U44",
        instruction="You are a regional logistics manager. Today is July 3, 2024. I'm concerned about potential congestion at our facilities. Please identify all warehouses where the current utilization is over 90%. For each of those warehouses, find all inbound shipments that are still in 'Planned' status and update their notes to say: 'High utilization warning. Confirm dock availability before arrival.' Please respond with a list of the shipment IDs that you have updated.",
        actions=[
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-02",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="find_inbound_shipments_by_warehouse",
                kwargs={
                    "warehouse_id": "WH-02",
                },
            ),
            Action(
                name="find_inbound_shipments_by_warehouse",
                kwargs={
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0010",
                    "new_note": "High utilization warning. Confirm dock availability before arrival.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0027",
                    "new_note": "High utilization warning. Confirm dock availability before arrival.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0029",
                    "new_note": "High utilization warning. Confirm dock availability before arrival.",
                },
            ),
        ],
        outputs=[
            "SHIP-0010",
            "SHIP-0027",
            "SHIP-0029",
        ],
    ),
    # Task 45
    Task(
        annotator="0",
        user_id="U45",
        instruction="You are a purchasing agent. Today is July 10, 2024. Please create a new purchase order for 100 units of the 'Ceramic Brake Pad Set' from our supplier 'Berlin Auto Parts GmbH'. The shipment should be delivered to the 'Chicago Parts Depot'. Please set the expected arrival date to July 25, 2024. After creating the order, respond with the new Purchase Order number.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Ceramic Brake Pad Set",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Berlin Auto Parts GmbH",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "AUTO-PAD-B2", "warehouse_id": "WH-03"},
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1003",
                    "supplier_name": "Berlin Auto Parts GmbH",
                    "destination_warehouse_id": "WH-03",
                    "destination_warehouse_name": "Chicago Parts Depot",
                    "order_quantity": 100,
                    "unit_cost": 45.00,
                    "unit_weight": 2.5,
                    "expected_arrival_date": "2024-07-25",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "quantity_to_add": 100,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
        ],
    ),
    # Task 46
    Task(
        annotator="0",
        user_id="U46",
        instruction="You are a fulfillment coordinator. Today is July 11, 2024. Please create a new outbound order for our customer, 'Epsilon Fashion Co.', located in Toronto, Canada, for 250 units of the 'Organic Cotton T-Shirt'. This order should be fulfilled from the 'Newark Apparel Hub' and shipped via 'FedEx' using their 'Ground' service. The sales order number is SO-2024-0022. Please respond with the new Order ID once it has been created.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Organic Cotton T-Shirt",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Newark Apparel Hub",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "FedEx",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0022",
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "destination_country": "Canada",
                    "warehouse_id": "WH-04",
                    "carrier_name": "FedEx",
                    "carrier_scac": "FDEG",
                    "mode_of_transport": "Truck",
                    "shipping_service_level": "Ground",
                    "order_date": "2024-07-11",
                    "total_units": 250,
                    "total_weight_kg": 50.0,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                    "quantity_to_allocate": 250,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 47
    Task(
        annotator="0",
        user_id="U47",
        instruction="You are a financial controller. Today is July 12, 2024. As part of a new internal control policy, I need you to audit our high-value technology inventory. Please review the inventory for the 'Smartphone Model X' and the 'Articulated Robotic Arm' across all warehouses. For each specific inventory location where the total on-hand value of either product exceeds $250,000, please update that inventory record's stock status to 'Cycle Count Pending'. Respond with a list of the Inventory IDs you have updated.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Smartphone Model X",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0023",
                    "new_status": "Cycle Count Pending",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0014",
                    "new_status": "Cycle Count Pending",
                },
            ),
        ],
        outputs=[
            "INV-0023",
            "INV-0014",
        ],
    ),
    # Task 48
    Task(
        annotator="0",
        user_id="U48",
        instruction="You are a logistics planner. Today is July 15, 2024. We need to prepare our cold chain facilities for the upcoming peak season. Please identify all of our warehouses that are of the 'Cold Storage' type. For each of these warehouses, select the ones that have as a special capability: 'Pharmaceutical Handling', review their inbound shipments and add a note to any 'Planned' or 'In Transit' shipment. The note should read: 'Action Required: Pre-allocate temperature-controlled dock for arrival.' Please respond with a list of the Shipment IDs that you have updated.",
        actions=[
            Action(
                name="get_all_warehouses",
                kwargs={
                    "filters": {"warehouse_type": "Cold Storage"},
                },
            ),
            Action(
                name="find_inbound_shipments_by_warehouse",
                kwargs={
                    "warehouse_id": "WH-16",
                },
            ),
            Action(
                name="find_inbound_shipments_by_warehouse",
                kwargs={
                    "warehouse_id": "WH-06",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "new_note": "Action Required: Pre-allocate temperature-controlled dock for arrival.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0021",
                    "new_note": "Action Required: Pre-allocate temperature-controlled dock for arrival.",
                },
            ),
        ],
        outputs=[
            "SHIP-0006",
            "SHIP-0021",
        ],
    ),
    # Task 49
    Task(
        annotator="0",
        user_id="U49",
        instruction="You are a fulfillment coordinator. Today is July 17, 2024. Please create a new outbound order for 'Zeta Tech Solutions', located on Yokohama, Japan, for 20 'Solar Panel 450W' units. This order, with sales order number SO-2024-0023, will be fulfilled from the 'Phoenix Renewable Warehouse'. Please use 'FedEx' with their 'Freight' service level via air for this shipment. After creating the order, make sure to allocate the inventory. Respond with the new Order ID to confirm creation.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Solar Panel 450W",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "FedEx",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0023",
                    "customer_name": "Zeta Tech Solutions",
                    "destination_city": "Yokohama",
                    "destination_country": "Japan",
                    "warehouse_id": "WH-09",
                    "carrier_name": "FedEx",
                    "carrier_scac": "FDEG",
                    "mode_of_transport": "Air",
                    "shipping_service_level": "Freight",
                    "order_date": "2024-07-17",
                    "total_units": 20,
                    "total_weight_kg": 440.0,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "quantity_to_allocate": 20,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 50
    Task(
        annotator="0",
        user_id="U50",
        instruction="You are a purchasing agent. Today is July 18, 2024. Please create a new purchase order for 50 'Industrial Paper Roll' units from our supplier, 'Toronto Paper Mills'. This shipment needs to be delivered to the 'Detroit Packaging Supplies' warehouse, and the required arrival date is August 1, 2024. After creating the purchase order, please ensure the inventory pipeline is updated. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Industrial Paper Roll",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Toronto Paper Mills",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Detroit Packaging Supplies",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={"sku": "MANU-PAPR-F6", "warehouse_id": "WH-08"},
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1008",
                    "supplier_name": "Toronto Paper Mills",
                    "destination_warehouse_id": "WH-08",
                    "destination_warehouse_name": "Detroit Packaging Supplies",
                    "order_quantity": 50,
                    "unit_cost": 250.0,
                    "unit_weight": 500.0,
                    "expected_arrival_date": "2024-08-01",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
        ],
    ),
    # Task 51
    Task(
        annotator="0",
        user_id="U51",
        instruction="You are a warehouse manager. Today is July 19, 2024. We've had a spoilage event in the Houston Food-Grade Warehouse involving our 'Extra Virgin Olive Oil'. The new physical count is 145 units. Please perform an inventory adjustment to reflect this, with the reason 'Spoilage due to container damage'. After the adjustment, check if the new stock level is below the reorder point. If it is, create a replenishment purchase order for 800 units from the supplier 'Athens Olive Oil Co.'. Please assign this shipment to the carrier 'CMA CGM' and ship it through sea. After creating the PO and updating the inventory pipeline, respond with the Inventory ID of the adjusted record and the new Purchase Order number.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Extra Virgin Olive Oil",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Houston Food-Grade Warehouse",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FOOD-OLIV-V22",
                    "warehouse_id": "WH-05",
                },
            ),
            Action(
                name="perform_inventory_adjustment",
                kwargs={
                    "sku": "FOOD-OLIV-V22",
                    "warehouse_id": "WH-05",
                    "new_physical_count": 145,
                    "current_date": "2024-07-19",
                    "reason_note": "Spoilage due to container damage",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Athens Olive Oil Co.",
                },
            ),
            Action(
                name="calculate_expected_arrival_date",
                kwargs={
                    "supplier_id": "SUP-1024",
                    "current_date": "2024-07-19",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "CMA CGM",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1024",
                    "supplier_name": "Athens Olive Oil Co.",
                    "destination_warehouse_id": "WH-05",
                    "destination_warehouse_name": "Houston Food-Grade Warehouse",
                    "order_quantity": 800,
                    "unit_cost": 40.0,
                    "unit_weight": 4.8,
                    "expected_arrival_date": "2024-08-13",
                    "carrier_name": "CMA CGM",
                    "carrier_scac": "CMDU",
                    "mode_of_transport": "Sea",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FOOD-OLIV-V22",
                    "warehouse_id": "WH-05",
                    "quantity_to_add": 800,
                },
            ),
        ],
        outputs=[
            "INV-0022",
            "PO-2024-0031",
        ],
    ),
    # Task 52
    Task(
        annotator="0",
        user_id="U52",
        instruction="You are a purchasing agent. Today is July 23, 2024. Please create a standard replenishment purchase order for 250 units of the 'Automotive Windshield'. This order should be placed with our supplier, 'Mexico City Auto Glass', and is destined for the 'Chicago Parts Depot'. You must use the supplier's standard lead time to calculate the expected arrival date. Ensure you retrieve the correct unit cost from the inventory record before creating the PO. After creating the inbound shipment, update the inventory pipeline accordingly.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Automotive Windshield",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Mexico City Auto Glass",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1023",
                    "destination_warehouse_id": "WH-03",
                    "order_quantity": 250,
                    "unit_cost": 150.0,
                    "unit_weight": 14.0,
                    "expected_arrival_date": "2024-07-27",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "quantity_to_add": 250,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 53
    Task(
        annotator="0",
        user_id="U53",
        instruction="You are a procurement officer. Today is July 24, 2024. Please initiate a purchase order for 5 'Articulated Robotic Arm' units from the supplier 'Osaka Robotics Corp.'. The destination for this shipment is our 'Chicago Parts Depot'. You need to calculate the expected arrival date using the supplier's standard lead time and use the specific unit cost from the Chicago inventory record for the PO. After creating the inbound shipment, please update the inventory pipeline.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Osaka Robotics Corp.",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1016",
                    "destination_warehouse_id": "WH-03",
                    "order_quantity": 5,
                    "unit_cost": 12000.0,
                    "unit_weight": 250.0,
                    "expected_arrival_date": "2024-08-13",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                    "quantity_to_add": 5,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 54
    Task(
        annotator="0",
        user_id="U54",
        instruction="You are a procurement specialist. Today is July 25, 2024. I need you to place a standard purchase order for 20 units of 'Industrial Solvent', which is a hazmat product, from our supplier, 'Helsinki Chemicals Oy'. The shipment must be delivered to our 'Cleveland Chemical Storage' facility. Please use the supplier's standard lead time to determine the expected arrival date and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Industrial Solvent",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Helsinki Chemicals Oy",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Cleveland Chemical Storage",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1013",
                    "destination_warehouse_id": "WH-13",
                    "order_quantity": 20,
                    "unit_cost": 150.0,
                    "unit_weight": 20.0,
                    "expected_arrival_date": "2024-08-09",
                    "hazmat": True,
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "quantity_to_add": 20,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 55
    Task(
        annotator="0",
        user_id="U55",
        instruction="You are a procurement manager. Today is July 26, 2024. Please place a replenishment purchase order for 300 units of 'Argentinian Malbec Wine' from the supplier 'Buenos Aires Wine Producers'. This shipment is for our 'Los Angeles Beverage DC'. You must calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Argentinian Malbec Wine",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Buenos Aires Wine Producers",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Beverage DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "BEVG-WINE-P16",
                    "warehouse_id": "WH-15",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1018",
                    "destination_warehouse_id": "WH-15",
                    "order_quantity": 300,
                    "unit_cost": 18.0,
                    "unit_weight": 1.3,
                    "expected_arrival_date": "2024-08-23",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "BEVG-WINE-P16",
                    "warehouse_id": "WH-15",
                    "quantity_to_add": 300,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 56
    Task(
        annotator="0",
        user_id="U56",
        instruction="You are a procurement specialist for luxury goods. Today is July 29, 2024. I need you to place a purchase order for 50 'Automatic Watch Movement' units from our supplier, 'Zurich Watch Parts AG'. The delivery destination is the 'NYC Luxury Vault'. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. Also, mark the order with critical priority. After creating the inbound shipment, ensure the inventory pipeline is updated.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Automatic Watch Movement",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Zurich Watch Parts AG",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "NYC Luxury Vault",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1014",
                    "destination_warehouse_id": "WH-07",
                    "order_quantity": 50,
                    "unit_cost": 300.0,
                    "unit_weight": 0.05,
                    "expected_arrival_date": "2024-08-03",
                    "priority_level": "Critical",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 57
    Task(
        annotator="0",
        user_id="U57",
        instruction="You are a procurement manager. Today is July 30, 2024. I need you to place a purchase order for 30 'Raw Cotton Bale' units from our supplier, 'Cairo Cotton Co.'. The destination for this shipment is our 'Newark Apparel Hub'. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Raw Cotton Bale",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Cairo Cotton Co.",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Newark Apparel Hub",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1020",
                    "destination_warehouse_id": "WH-04",
                    "order_quantity": 30,
                    "unit_cost": 800.0,
                    "unit_weight": 227.0,
                    "expected_arrival_date": "2024-08-24",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "quantity_to_add": 30,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "2024-08-24",
        ],
    ),
    # Task 58
    Task(
        annotator="0",
        user_id="U58",
        instruction="You are a procurement specialist. Today is August 1, 2024. I need you to place a purchase order for 500 units of 'Organic Arabica Coffee Beans' from our supplier, 'São Paulo Coffee Exporters'. The shipment should be delivered to our 'Houston Food-Grade Warehouse' and is of high priority. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Organic Arabica Coffee Beans",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "São Paulo Coffee Exporters",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Houston Food-Grade Warehouse",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1005",
                    "destination_warehouse_id": "WH-05",
                    "order_quantity": 500,
                    "unit_cost": 22.0,
                    "unit_weight": 1.0,
                    "expected_arrival_date": "2024-08-31",
                    "priority_level": "High",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "quantity_to_add": 500,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "2024-08-31",
        ],
    ),
    # Task 59
    Task(
        annotator="0",
        user_id="U59",
        instruction="You are a procurement manager. Today is August 2, 2024. Please place a purchase order for 10 'Diamond Core Drill Bit' units from our supplier, 'Johannesburg Mining Equipment'. The shipment is destined for the 'Denver Heavy Equipment Yard'. You must calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. Add a note to the shipment saying 'Fragile. Handle with care.' After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Diamond Core Drill Bit",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Johannesburg Mining Equipment",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Denver Heavy Equipment Yard",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1011",
                    "destination_warehouse_id": "WH-11",
                    "order_quantity": 10,
                    "unit_cost": 2200.0,
                    "unit_weight": 15.0,
                    "expected_arrival_date": "2024-09-16",
                    "notes": "Fragile. Handle with care.",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "quantity_to_add": 10,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "2024-09-16",
        ],
    ),
    # Task 60
    Task(
        annotator="0",
        user_id="U60",
        instruction="You are a procurement manager. Today is August 5, 2024. Please place a purchase order for 100 'Solar Panel 450W' units from our supplier, 'Beijing Solar Tech'. The shipment is destined for the 'Phoenix Renewable Warehouse'. You must calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Solar Panel 450W",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Beijing Solar Tech",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1009",
                    "destination_warehouse_id": "WH-09",
                    "order_quantity": 100,
                    "unit_cost": 180.0,
                    "unit_weight": 22.0,
                    "expected_arrival_date": "2024-09-04",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "quantity_to_add": 100,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "2024-09-04",
        ],
    ),
    # Task 61
    Task(
        annotator="0",
        user_id="U61",
        instruction="You are a risk analyst. Today is August 7, 2024. I need you to perform a performance review of carriers handling our international shipments. Please find all outbound orders with a destination country different from their origin country. For each of these orders, check the assigned carrier's average performance rating. If the rating is below 4.8, please update the order with a note: 'Proactive Communication Recommended: Carrier performance rating is below 4.8.' Please respond with a list of the Order IDs that you have updated.",
        actions=[
            Action(
                name="get_all_outbound_orders",
                kwargs={},
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "DHL Express",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "UPS",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "Maersk",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "COSCO",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "LATAM Cargo",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "DB Schenker",
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0006",
                    "notes": "Proactive Communication Recommended: Carrier performance rating is below 4.8.",
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0007",
                    "notes": "Proactive Communication Recommended: Carrier performance rating is below 4.8.",
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0008",
                    "notes": "Proactive Communication Recommended: Carrier performance rating is below 4.8.",
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0009",
                    "notes": "Proactive Communication Recommended: Carrier performance rating is below 4.8.",
                },
            ),
        ],
        outputs=[
            "ORD-0006",
            "ORD-0007",
            "ORD-0008",
            "ORD-0009",
        ],
    ),
    # Task 62
    Task(
        annotator="0",
        user_id="U62",
        instruction="You are a security auditor. Today is August 8, 2024. I need you to perform a security compliance audit on our high-value inventory. Please review the storage locations for the following products: 'Leather Handbag', 'Diamond Core Drill Bit', 'Articulated Robotic Arm', and 'Oncology Drug A'. For each inventory record of these products, check the special capabilities of its warehouse. If the warehouse does NOT have either 'High-Value Cage' or 'High Security' as a capability, you must update that specific inventory record's status to 'Security Review Pending'. Please respond with a list of the Inventory IDs that you have updated.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Leather Handbag",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Diamond Core Drill Bit",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Oncology Drug A",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "APRL-BAG-E5",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-11",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-06",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0009",
                    "new_status": "Security Review Pending",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0014",
                    "new_status": "Security Review Pending",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0019",
                    "new_status": "Security Review Pending",
                },
            ),
        ],
        outputs=[
            "INV-0009",
            "INV-0014",
            "INV-0019",
        ],
    ),
    # Task 63
    Task(
        annotator="0",
        user_id="U63",
        instruction="You are a procurement manager. Today is August 9, 2024. I need you to conduct a lead time audit for our key European suppliers: 'Berlin Auto Parts GmbH', 'Helsinki Chemicals Oy', 'Paris Luxury Goods', 'Madrid Ceramic Tiles', and 'Istanbul Apparel Ltd.'. For each of these suppliers, check their standard lead time. If it is longer than 10 days, find all of their 'In Transit' or 'Planned' inbound shipments and add a note to each: 'Extended lead time supplier. Monitor ETA closely.' Please respond with a list of the Shipment IDs that you have updated.",
        actions=[
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Berlin Auto Parts GmbH",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Helsinki Chemicals Oy",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Paris Luxury Goods",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Madrid Ceramic Tiles",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Istanbul Apparel Ltd.",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1017",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1013",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1012",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "new_note": "Extended lead time supplier. Monitor ETA closely.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0012",
                    "new_note": "Extended lead time supplier. Monitor ETA closely.",
                },
            ),
        ],
        outputs=[
            "SHIP-0013",
            "SHIP-0012",
        ],
    ),
    # Task 64
    Task(
        annotator="0",
        user_id="U64",
        instruction="You are a procurement manager. Today is August 12, 2024. I need you to place a purchase order for 80 'Teak Wood Dining Chair' units from our supplier, 'Bangkok Furniture Co.'. The shipment is destined for the 'Dallas Home Goods DC'. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. Add a note stating 'Standard replenishment of furniture stock.' After creating the inbound shipment, ensure the inventory pipeline is updated.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "destination_warehouse_id": "WH-14",
                    "order_quantity": 80,
                    "unit_cost": 120.0,
                    "unit_weight": 8.0,
                    "expected_arrival_date": "2024-09-16",
                    "notes": "Standard replenishment of furniture stock.",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_add": 80,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 65
    Task(
        annotator="0",
        user_id="U65",
        instruction="You are a procurement specialist. Today is August 13, 2024. I need you to place a replenishment purchase order for 100 'Frozen Tuna Loin' units from our supplier, 'Sydney Seafood Exporters'. The shipment is destined for the 'San Francisco Fresh Foods DC'. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Frozen Tuna Loin",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Sydney Seafood Exporters",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "San Francisco Fresh Foods DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1010",
                    "destination_warehouse_id": "WH-10",
                    "order_quantity": 100,
                    "unit_cost": 35.0,
                    "unit_weight": 2.0,
                    "expected_arrival_date": "2024-08-16",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                    "quantity_to_add": 100,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "2024-08-16",
        ],
    ),
    # Task 66
    Task(
        annotator="0",
        user_id="U66",
        instruction="You are a pharmaceutical procurement specialist. Today is August 14, 2024. I need you to place a replenishment purchase order for 2000 units of 'Influenza Vaccine' from our supplier, 'Mumbai Pharma Supplies'. The shipment is destined for the 'Atlanta Cold Chain Center'. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. Be wary that this is a critical shipment. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Influenza Vaccine",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Mumbai Pharma Supplies",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Atlanta Cold Chain Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1006",
                    "destination_warehouse_id": "WH-06",
                    "order_quantity": 2000,
                    "unit_cost": 15.5,
                    "unit_weight": 0.05,
                    "expected_arrival_date": "2024-08-21",
                    "priority_level": "Critical",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "quantity_to_add": 2000,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "2024-08-21",
        ],
    ),
    # Task 67
    Task(
        annotator="0",
        user_id="U67",
        instruction="You are a procurement manager. Today is August 15, 2024. I need you to place a replenishment purchase order for 3000 units of 'Ceramic Floor Tile' from our supplier, 'Madrid Ceramic Tiles'. The shipment is destined for the 'Miami Building Materials' warehouse. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Ceramic Floor Tile",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Madrid Ceramic Tiles",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Miami Building Materials",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1012",
                    "destination_warehouse_id": "WH-12",
                    "order_quantity": 3000,
                    "unit_cost": 3.5,
                    "unit_weight": 5.0,
                    "expected_arrival_date": "2024-09-09",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                    "quantity_to_add": 3000,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "2024-09-09",
        ],
    ),
    # Task 68
    Task(
        annotator="0",
        user_id="U68",
        instruction="You are a fulfillment specialist. Today is August 16, 2024. Please process sales order SO-2024-0024 for our customer, 'Alpha Electronics LLC'. The order is for 2500 '8-bit Microcontroller' units to be fulfilled from the 'Los Angeles Distribution Center'. The customer has specifically requested we use 'UPS' for this shipment. Please verify that we have sufficient available stock, then create the outbound order and allocate the inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Distribution Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "UPS",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0024",
                    "customer_name": "Alpha Electronics LLC",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "UPSN",
                    "order_date": "2024-08-16",
                    "total_units": 2500,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 2500,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 69
    Task(
        annotator="0",
        user_id="U69",
        instruction="You are a fulfillment specialist. Today is August 19, 2024. We have a specific request from our customer, 'Iota Automotive SAS', for an order of 50 'Ceramic Brake Pad Set' units. They require that the products come specifically from lot number 'LOT202403B'. Please locate the warehouse that holds this specific lot and fulfill the order from there. Use 'DB Schenker' as the carrier. Create the outbound order with sales order number SO-2024-0026, allocate the inventory, and then add a note to the newly created order confirming 'Fulfilled using lot LOT202403B as per customer request.' Please respond with the new Order ID.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Ceramic Brake Pad Set",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "DB Schenker",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0026",
                    "customer_name": "Iota Automotive SAS",
                    "warehouse_id": "WH-03",
                    "carrier_name": "DB Schenker",
                    "carrier_scac": "DBSG",
                    "order_date": "2024-08-19",
                    "total_units": 50,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 50,
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0017",
                    "notes": "Fulfilled using lot LOT202403B as per customer request.",
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 70
    Task(
        annotator="0",
        user_id="U70",
        instruction="You are a fulfillment specialist. Today is August 20, 2024. We have a new sales order, SO-2024-0027, from 'Zeta Tech Solutions' for 5,000 '8-bit Microcontroller' units. This product is stocked in multiple locations. Please identify the warehouse with the highest available quantity for this product and fulfill the order from there. The customer has requested 'Nippon Express' as the carrier. After creating the order and allocating the inventory, please respond with the new Order ID and the name of the warehouse you selected for fulfillment.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "Nippon Express",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0027",
                    "customer_name": "Zeta Tech Solutions",
                    "warehouse_id": "WH-01",
                    "carrier_name": "Nippon Express",
                    "carrier_scac": "NPEX",
                    "order_date": "2024-08-20",
                    "total_units": 5000,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 5000,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Los Angeles Distribution Center",
        ],
    ),
    # Task 71
    Task(
        annotator="0",
        user_id="U71",
        instruction="You are a fulfillment specialist. Today is August 21, 2024. Please process sales order SO-2024-0028 for our customer, 'Epsilon Fashion Co.'. The order is for 1500 'Organic Cotton T-Shirt' units to be fulfilled from the 'Newark Apparel Hub'. To minimize costs, please find the cheapest available carrier that offers 'LCL' service via 'Truck'. After selecting the carrier, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the economical carrier you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Organic Cotton T-Shirt",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Newark Apparel Hub",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LCL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0028",
                    "customer_name": "Epsilon Fashion Co.",
                    "warehouse_id": "WH-04",
                    "carrier_scac": "MAEU",
                    "order_date": "2024-08-21",
                    "total_units": 1500,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                    "quantity_to_allocate": 1500,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Maersk",
        ],
    ),
    # Task 72
    Task(
        annotator="0",
        user_id="U72",
        instruction="You are a fulfillment specialist. Today is August 22, 2024. We have a large order, SO-2024-0029, from 'Iota Automotive SAS' for 20 'Automotive Windshield' units. This is a heavy, oversized product that needs to be shipped from our 'Chicago Parts Depot'. Before you proceed, you must verify that this warehouse has the special capabilities required for handling heavy goods. Once confirmed, find the highest-rated carrier that offers 'FTL' service via 'Truck'. Then, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the carrier you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Automotive Windshield",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "FTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0029",
                    "customer_name": "Iota Automotive SAS",
                    "warehouse_id": "WH-03",
                    "carrier_name": "DB Schenker",
                    "carrier_scac": "DBSG",
                    "order_date": "2024-08-22",
                    "total_units": 20,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 20,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "DB Schenker",
        ],
    ),
    # Task 73
    Task(
        annotator="0",
        user_id="U73",
        instruction="You are a fulfillment specialist. Today is August 23, 2024. We have a new sales order, SO-2024-0030, from 'Alpha Electronics LLC' for 1000 '8-bit Microcontroller' units. The customer has a strict requirement that the components must be sourced from Taiwan. Please first verify the product's country of origin from the product master data. Then, identify the optimal warehouse for fulfillment based on the highest available stock. Ship the order using the best-rated 'Parcel' carrier. After creating the order and allocating the inventory, please respond with the new Order ID and the name of the warehouse you fulfilled the order from.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="find_carrier_by_method_of_transport",
                kwargs={
                    "method_of_transport": "Parcel",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0030",
                    "customer_name": "Alpha Electronics LLC",
                    "warehouse_id": "WH-01",
                    "carrier_name": "UPS",
                    "carrier_scac": "UPSN",
                    "order_date": "2024-08-23",
                    "total_units": 1000,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 1000,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Los Angeles Distribution Center",
        ],
    ),
    # Task 74
    Task(
        annotator="0",
        user_id="U74",
        instruction="You are a senior fulfillment specialist. Today is August 26, 2024. Please process a new sales order, SO-2024-0031, for 'Iota Automotive SAS' for 5 'Articulated Robotic Arm' units. This order has special fulfillment constraints. You must ship it from a warehouse that is both company-owned AND has 'Heavy Equipment Handling' capabilities. Additionally, you must select the cheapest carrier that provides 'FTL' service via 'Truck'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the warehouse you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="get_all_warehouses",
                kwargs={
                    "filters": {
                        "ownership_status": "Owned",
                        "special_capabilities": "Heavy Equipment Handling",
                    }
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "FTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0031",
                    "customer_name": "Iota Automotive SAS",
                    "warehouse_id": "WH-03",
                    "carrier_name": "DB Schenker",
                    "carrier_scac": "DBSG",
                    "order_date": "2024-08-26",
                    "total_units": 5,
                    "total_weight_kg": 1250.0,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 5,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Chicago Parts Depot",
        ],
    ),
    # Task 75
    Task(
        annotator="0",
        user_id="U75",
        instruction="You are a senior fulfillment specialist for our pharmaceutical division. Today is August 27, 2024. Please process a new high-priority sales order, SO-2024-0032, for 'Delta Pharma Inc.' for 2000 'Influenza Vaccine' units. This order has strict fulfillment constraints. You must ship it from a warehouse that is both 'FDA Registered' AND has 'Cold Chain (2-8°C)' capabilities. You must also select the highest-rated carrier that provides 'Pharma' service via 'Air'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the carrier you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Influenza Vaccine",
                },
            ),
            Action(
                name="get_all_warehouses",
                kwargs={
                    "filters": {
                        "certifications": "FDA Registered",
                        "special_capabilities": "Cold Chain (2-8°C)",
                    }
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Pharma",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0032",
                    "customer_name": "Delta Pharma Inc.",
                    "warehouse_id": "WH-06",
                    "carrier_scac": "UAE",
                    "order_date": "2024-08-27",
                    "total_units": 2000,
                    "temperature_control_required": True,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "quantity_to_allocate": 2000,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Emirates SkyCargo",
        ],
    ),
    # Task 76
    Task(
        annotator="0",
        user_id="U76",
        instruction="You are a fulfillment specialist. Today is August 28, 2024. Please process a new sales order, SO-2024-0033, for 'Theta Foods SA' for 5000 units of 'Organic Arabica Coffee Beans'. This order has special fulfillment constraints. You must ship it from a warehouse that is 'Organic Certified'. You must also select the cheapest carrier that provides temperature controled 'Reefer' service via 'Sea'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the warehouse you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Organic Arabica Coffee Beans",
                },
            ),
            Action(
                name="get_all_warehouses",
                kwargs={
                    "filters": {
                        "certifications": "Organic Certified",
                    }
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Sea",
                    "service_level": "Reefer",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0033",
                    "customer_name": "Theta Foods SA",
                    "warehouse_id": "WH-05",
                    "carrier_scac": "MAEU",
                    "order_date": "2024-08-28",
                    "total_units": 5000,
                    "temperature_control_required": True,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "quantity_to_allocate": 5000,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Houston Food-Grade Warehouse",
        ],
    ),
    # Task 77
    Task(
        annotator="0",
        user_id="U77",
        instruction="You are a fulfillment specialist. Today is August 29, 2024. Please process a new sales order, SO-2024-0034, for 'Mu Agro SA de CV' for 80 'Teak Wood Dining Chair' units. Per our regional fulfillment policy, this order must be shipped from a warehouse located in Texas (TX). Please identify the correct warehouse, then select the highest-rated carrier that provides 'LTL' service via 'Truck'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the Texas warehouse you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="get_all_warehouses",
                kwargs={
                    "filters": {
                        "state_province": "TX",
                    }
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0034",
                    "customer_name": "Mu Agro SA de CV",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "NPEX",
                    "order_date": "2024-08-29",
                    "total_units": 80,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_allocate": 80,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Dallas Home Goods DC",
        ],
    ),
    # Task 78
    Task(
        annotator="0",
        user_id="U78",
        instruction="You are a fulfillment specialist. Today is August 30, 2024. Please process a new sales order, SO-2024-0035, for 'Zeta Tech Solutions' for 12,500 '8-bit Microcontroller' units. Due to the customer's compliance requirements, this order must be fulfilled from a 'C-TPAT' certified warehouse. Please identify a compliant warehouse that has sufficient stock. Then, select the highest-rated carrier that provides 'FCL' service via 'Sea'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the compliant warehouse you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="get_all_warehouses",
                kwargs={
                    "filters": {
                        "certifications": "C-TPAT",
                    }
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Sea",
                    "service_level": "FCL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0035",
                    "customer_name": "Zeta Tech Solutions",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "MAEU",
                    "order_date": "2024-08-30",
                    "total_units": 12500,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 12500,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Los Angeles Distribution Center",
        ],
    ),
    # Task 79
    Task(
        annotator="0",
        user_id="U79",
        instruction="You are a fulfillment specialist. Today is September 2, 2024. Please process a new sales order, SO-2024-0036, for 'Alpha Electronics LLC' for 500 'Smartphone Model X' units. This order requires kitting, so it must be fulfilled from a warehouse with 'Kitting & Assembly' capabilities. Please identify a compliant warehouse that has sufficient stock. Then, select the highest-rated carrier for 'Parcel' transport. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the warehouse you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Smartphone Model X",
                },
            ),
            Action(
                name="get_all_warehouses",
                kwargs={
                    "filters": {
                        "special_capabilities": "Kitting & Assembly",
                    }
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                },
            ),
            Action(
                name="find_carrier_by_method_of_transport",
                kwargs={
                    "method_of_transport": "Parcel",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0036",
                    "customer_name": "Alpha Electronics LLC",
                    "warehouse_id": "WH-02",
                    "carrier_scac": "UPSN",
                    "order_date": "2024-09-02",
                    "total_units": 500,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "quantity_to_allocate": 500,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Seattle Fulfillment Center",
        ],
    ),
    # Task 80
    Task(
        annotator="0",
        user_id="U80",
        instruction="You are a fulfillment specialist. Today is September 3, 2024. We have a high-priority sales order, SO-2024-0037, from 'Pi Ceramics SRL' for 200 'Teak Wood Dining Chair' units. To expedite this large order, it must be fulfilled from a warehouse that has 'Cross-Docking' capabilities. Please identify a compliant warehouse that has sufficient stock. Then, select the highest-rated carrier that provides 'LTL' service via 'Truck'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the warehouse you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="get_all_warehouses",
                kwargs={
                    "filters": {
                        "special_capabilities": "Cross-Docking",
                    }
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0037",
                    "customer_name": "Pi Ceramics SRL",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "NPEX",
                    "order_date": "2024-09-03",
                    "total_units": 200,
                    "priority_level": "High",
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_allocate": 200,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "Dallas Home Goods DC",
        ],
    ),
    # Task 81
    Task(
        annotator="0",
        user_id="U81",
        instruction="You are a logistics analyst. Today is September 4, 2024. We've just received an alert about severe port congestion affecting all terminals in Los Angeles. I need you to identify all our warehouses located in the city of Los Angeles. For each of those warehouses, find all inbound sea shipments that are currently 'In Transit' and update their notes with the following flag: 'RISK: LA port congestion. Evaluate for potential diversion.' Please respond with a list of the Shipment IDs that you have flagged.",
        actions=[
            Action(
                name="get_all_warehouses",
                kwargs={
                    "filters": {
                        "city": "Los Angeles",
                    }
                },
            ),
            Action(
                name="find_inbound_shipments_by_warehouse",
                kwargs={
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="find_inbound_shipments_by_warehouse",
                kwargs={
                    "warehouse_id": "WH-15",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "new_note": "RISK: LA port congestion. Evaluate for potential diversion.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0025",
                    "new_note": "RISK: LA port congestion. Evaluate for potential diversion.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0018",
                    "new_note": "RISK: LA port congestion. Evaluate for potential diversion.",
                },
            ),
        ],
        outputs=[
            "SHIP-0001",
            "SHIP-0025",
            "SHIP-0018",
        ],
    ),
    Task(
        annotator="0",
        user_id="U82",
        instruction="You are an inventory control specialist. Today is September 6, 2024. A new, high-priority sales order, SO-2024-0038, has just been created for 10,000 units of the '8-bit Microcontroller' to be fulfilled from our 'Los Angeles Distribution Center'. I need you to assess the impact of this order on our stock levels. First, check the current available quantity and the reorder point for this product at that warehouse. If fulfilling this 10,000-unit order will cause the available quantity to drop below the reorder point, you must immediately initiate a replenishment purchase order for a standard quantity of 5,000 units from the supplier 'Global Components Inc.'. Please use their standard lead time to calculate the arrival date.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Distribution Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1001",
                    "destination_warehouse_id": "WH-01",
                    "order_quantity": 5000,
                    "unit_cost": 2.5,
                    "unit_weight": 0.01,
                    "expected_arrival_date": "2024-10-01",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 5000,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 83
    Task(
        annotator="0",
        user_id="U83",
        instruction="You are a logistics project manager. Today is September 12, 2024, and you are tasked with the initial stocking of our new 'Dallas Home Goods DC'. To start, we need to establish inventory for a key product. Order 5000 'Organic Cotton T-Shirt' units from 'Istanbul Apparel Ltd.'. For the product, you must first create a new inventory record at the Dallas warehouse. Then, create the corresponding purchase order using the supplier's standard lead time to calculate the arrival date. Finally, ensure the new inventory records are updated with the inbound quantities.",
        actions=[
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Organic Cotton T-Shirt",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                },
            ),
            Action(
                name="create_inventory_record",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Istanbul Apparel Ltd.",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1017",
                    "destination_warehouse_id": "WH-14",
                    "order_quantity": 5000,
                    "unit_cost": 8.0,
                    "unit_weight": 0.2,
                    "expected_arrival_date": "2024-09-27",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-14",
                    "quantity_to_add": 5000,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 84
    Task(
        annotator="0",
        user_id="U84",
        instruction="You are a strategic sourcing manager. Today is September 10, 2024. We are deactivating 'Johannesburg Mining Equipment' due to performance issues. First, find any of their inbound shipments that are currently 'In Transit'. You must then cancel this shipment by updating its notes to 'CANCELLED - Supplier Deactivated. Re-sourcing.' Next, you must reverse the inbound quantity for the 'Diamond Core Drill Bit' at the 'Denver Heavy Equipment Yard' to reflect this cancellation. Finally, create a new replacement purchase order for the same quantity (20 units) from our new preferred supplier, 'Berlin Auto Parts GmbH', and update the inventory pipeline accordingly. Please respond with the ID of the cancelled shipment and the new Purchase Order number.",
        actions=[
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Johannesburg Mining Equipment",
                },
            ),
            Action(
                name="find_inbound_shipments_by_supplier",
                kwargs={
                    "supplier_id": "SUP-1011",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0011",
                    "new_note": "CANCELLED - Supplier Deactivated. Re-sourcing.",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Diamond Core Drill Bit",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Denver Heavy Equipment Yard",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "quantity_to_add": -20,
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Berlin Auto Parts GmbH",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1003",
                    "destination_warehouse_id": "WH-11",
                    "order_quantity": 20,
                    "unit_cost": 2200.0,
                    "unit_weight": 15.0,
                    "expected_arrival_date": "2024-09-20",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "quantity_to_add": 20,
                },
            ),
        ],
        outputs=[
            "SHIP-0011",
            "PO-2024-0031",
        ],
    ),
    # Task 85
    Task(
        annotator="0",
        user_id="U85",
        instruction="You are a regional inventory manager. Today is September 11, 2024. We need to perform an inter-warehouse stock transfer to balance our inventory. Our Los Angeles Distribution Center has a surplus of '8-bit Microcontrollers', while our Chicago Parts Depot is running low. Please create a transfer shipment of 5,000 units from Los Angeles to Chicago. First, verify that the LA warehouse has sufficient available stock. Then, select the most economical carrier that offers 'LTL' service via 'Truck'. You will need to create an outbound order using the sales order number 'IBT-LAX-ORD-01' where the customer is the 'Chicago Parts Depot'. After creating the order and allocating the inventory, update the new order's notes to specify: 'Internal Stock Transfer from Los Angeles Distribution Center to Chicago Parts Depot.'",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Distribution Center",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "IBT-LAX-ORD-01",
                    "customer_name": "Chicago Parts Depot",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "FDEG",
                    "order_date": "2024-09-11",
                    "total_units": 5000,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 5000,
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0017",
                    "notes": "Internal Stock Transfer from Los Angeles Distribution Center to Chicago Parts Depot.",
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "FedEx",
        ],
    ),
    # Task 86
    Task(
        annotator="0",
        user_id="U86",
        instruction="You are a quality control manager. Today is September 13, 2024. A critical quality failure has occurred. The recently received lot 'LOT202406B' of 'Frozen Tuna Loin' at our San Francisco Fresh Foods DC has failed its temperature inspection. Your first task is to find the specific inventory record for this lot and update its status to 'Quarantined'. Since this will create a stock-out, you must then immediately create an emergency replacement purchase order for the same quantity from the supplier, 'Sydney Seafood Exporters' with critical priority. Select the highest-rated carrier that offers 'Perishables' service via 'Air'. After creating the PO and updating the inventory pipeline, respond with the new Purchase Order number and the ID of the inventory record you quarantined.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Frozen Tuna Loin",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "San Francisco Fresh Foods DC",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0008",
                    "new_status": "Quarantined",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Sydney Seafood Exporters",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="find_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Perishables",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1010",
                    "destination_warehouse_id": "WH-10",
                    "order_quantity": 2500,
                    "unit_cost": 35.0,
                    "unit_weight": 2.0,
                    "expected_arrival_date": "2024-09-16",
                    "carrier_name": "Emirates SkyCargo",
                    "carrier_scac": "UAE",
                    "priority_level": "Critical",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                    "quantity_to_add": 2500,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "INV-0008",
        ],
    ),
    # Task 87
    Task(
        annotator="0",
        user_id="U87",
        instruction="You are a product safety manager. Today is September 18, 2024. We are issuing an immediate recall for all 'Ceramic Floor Tile' units due to a critical manufacturing defect. Your first task is to find all inventory of this product and update its status to 'Recalled - Do Not Ship'. Second, you must find any outbound orders from the warehouses that store this product that are currently 'Shipped' or 'In Transit' and update their status to 'Recalled', adding a note: 'URGENT RECALL: Intercept and return to origin.' Finally, to begin recovery, you must place an emergency replenishment purchase order for the entire recalled on-hand quantity from a different supplier, 'Global Components Inc.', to the original warehouse. Use their standard lead time to calculate the arrival date.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Ceramic Floor Tile",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0010",
                    "new_status": "Recalled - Do Not Ship",
                },
            ),
            Action(
                name="get_all_outbound_orders",
                kwargs={"filters": {"warehouse_id": "WH-12", "status": "Shipped"}},
            ),
            Action(
                name="get_all_outbound_orders",
                kwargs={
                    "filters": {
                        "warehouse_id": "WH-12",
                        "status": "In Transit",
                    }
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0003",
                    "status": "Recalled",
                    "notes": "URGENT RECALL: Intercept and return to origin.",
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0013",
                    "status": "Recalled",
                    "notes": "URGENT RECALL: Intercept and return to origin.",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1001",
                    "destination_warehouse_id": "WH-12",
                    "order_quantity": 18000,
                    "unit_cost": 3.5,
                    "unit_weight": 5.0,
                    "expected_arrival_date": "2024-10-13",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                    "quantity_to_add": 18000,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 88
    Task(
        annotator="0",
        user_id="U88",
        instruction="You are a crisis response manager. Today is September 19, 2024. A fire has made our 'Chicago Parts Depot' completely non-operational. Your first priority is to manage the inbound pipeline. Find all inbound shipments currently 'In Transit' or 'Planned' for this warehouse and update their notes with the following high-priority message: 'URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.' After flagging the shipments, you must assess the financial impact of the inaccessible inventory. Calculate the total value of all 'Articulated Robotic Arm' units currently on hand at the Chicago facility. Please respond with a list of the Shipment IDs you flagged for diversion and the total calculated value of the at-risk inventory.",
        actions=[
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="find_inbound_shipments_by_warehouse",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0003",
                    "new_note": "URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0016",
                    "new_note": "URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0019",
                    "new_note": "URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.",
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0023",
                    "new_note": "URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                },
            ),
        ],
        outputs=[
            "Flagged shipments: SHIP-0003, SHIP-0016, SHIP-0019, SHIP-0023",
            "Total at-risk inventory value: $300000.00",
        ],
    ),
    # Task 89
    Task(
        annotator="0",
        user_id="U89",
        instruction="You are a product launch manager. Today is September 20, 2024. I am planning the initial stocking of 500 'Teak Wood Dining Chair' units at our 'Phoenix Renewable Warehouse'. Your first task is to conduct a capacity check. You must calculate the total cubic meters required for this new inventory and verify if the warehouse has enough available space. If, and only if, the capacity check passes, you must proceed with the full setup: create a new inventory record for this product at the warehouse, then create the purchase order from the supplier 'Bangkok Furniture Co.', and finally, update the new inventory record's pipeline. Please respond with the new Purchase Order number and the new Inventory ID. If the capacity check fails, you must report the space deficit in cubic meters.",
        actions=[
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="get_warehouse_details",
                kwargs={
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                },
            ),
            Action(
                name="create_inventory_record",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "destination_warehouse_id": "WH-09",
                    "order_quantity": 500,
                    "unit_cost": 120.0,
                    "unit_weight": 8.0,
                    "total_volume_cbm": 123.75,
                    "expected_arrival_date": "2024-10-25",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-09",
                    "quantity_to_add": 500,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "INV-0026",
        ],
    ),
    # Task 90
    Task(
        annotator="0",
        user_id="U90",
        instruction="You are an inventory quality auditor. Today is September 23, 2024. Please conduct a shelf-life audit on our 'Fresh Cut Roses' inventory across all warehouses. For any specific inventory lot that has already passed its expiration date, you must perform an inventory adjustment to write off the entire on-hand quantity, using the reason 'Expired Stock Write-Off'. Immediately after processing the write-off, you must create an emergency replenishment purchase order with critical priority for the exact quantity you just wrote off. Source this from the supplier 'Bogota Floral Exports' and use their standard lead time for the arrival date. Please respond with the ID of the inventory record you adjusted and the new Purchase Order number.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Fresh Cut Roses",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                },
            ),
            Action(
                name="perform_inventory_adjustment",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                    "new_physical_count": 0,
                    "current_date": "2024-09-23",
                    "reason_note": "Expired Stock Write-Off",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Bogota Floral Exports",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1029",
                    "destination_warehouse_id": "WH-10",
                    "order_quantity": 3000,
                    "unit_cost": 12.0,
                    "unit_weight": 0.5,
                    "expected_arrival_date": "2024-09-25",
                    "priority_level": "Critical",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                    "quantity_to_add": 3000,
                },
            ),
        ],
        outputs=[
            "INV-0024",
            "PO-2024-0031",
        ],
    ),
    # Task 91
    Task(
        annotator="0",
        user_id="U91",
        instruction="You are a strategic sourcing manager. Today is September 25, 2024. We are sourcing a new product, the 'Automotive Windshield', for our 'Chicago Parts Depot'. I have two potential suppliers: 'Mexico City Auto Glass' and 'Toronto Paper Mills'. You must evaluate both based on the following criteria: they must be in the 'Automotive' product category, located in North America (Mexico or Canada), and have a performance rating above 4.4. Select the best supplier that meets all criteria, then create an initial purchase order for 100 units. Use the supplier's standard lead time to calculate the arrival date.",
        actions=[
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Mexico City Auto Glass",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Toronto Paper Mills",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1023",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1008",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Automotive Windshield",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1023",
                    "destination_warehouse_id": "WH-03",
                    "order_quantity": 100,
                    "unit_cost": 150.0,
                    "unit_weight": 14.0,
                    "expected_arrival_date": "2024-09-29",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "quantity_to_add": 100,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 92
    Task(
        annotator="0",
        user_id="U92",
        instruction="You are a senior logistics specialist. Today is September 26, 2024. We need to resolve a short-shipment claim for sales order SO-2024-0001 from 'Alpha Electronics LLC'. They were shorted 50 units of the '8-bit Microcontroller'. A cycle count at the fulfillment warehouse, 'Los Angeles Distribution Center', has confirmed a physical count of 15,050 units, revealing the missing items. Your first task is to perform an inventory adjustment to correct the system quantity. Then, create a new, high-priority outbound order for the 50 missing units using sales order number 'SO-2024-0042' and the original carrier, 'UPS'. After creating the new order and allocating the inventory, you must update the original order (ORD-0001) with a note: 'Short-shipment of 50 units confirmed. Corrective shipment sent via order [New Order ID].'",
        actions=[
            Action(
                name="find_outbound_order_by_so",
                kwargs={
                    "sales_order_number": "SO-2024-0001",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Distribution Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="perform_inventory_adjustment",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "new_physical_count": 15050,
                    "current_date": "2024-09-26",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "UPS",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0042",
                    "customer_name": "Alpha Electronics LLC",
                    "warehouse_id": "WH-01",
                    "carrier_name": "UPS",
                    "carrier_scac": "UPSN",
                    "order_date": "2024-09-26",
                    "total_units": 50,
                    "priority_level": "High",
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 50,
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0001",
                    "notes": "Short-shipment of 50 units confirmed. Corrective shipment sent via order ORD-0017.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 93
    Task(
        annotator="0",
        user_id="U93",
        instruction="You are a logistics project manager. Today is September 27, 2024. We are launching 'Project Unify' to consolidate all inventory of the '8-bit Microcontroller' into our central hub, the 'Chicago Parts Depot'. Your task is to execute this consolidation. First, identify all satellite warehouses that currently stock this product. Then, for each of these locations, you must create an inter-warehouse stock transfer to move the entire available quantity to the Chicago hub. Use the most economical 'LTL' 'Truck' carrier for these transfers. Use a sales order number format like 'CONSOL-[SourceWH-ID]-01' for each transfer. After creating the order and allocating the stock, add a note to each new order: 'Project Unify - Inventory Consolidation'. Please respond with a list of the new Order IDs you created.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "CONSOL-WH-01-01",
                    "customer_name": "Chicago Parts Depot",
                    "destination_city": "Chicago",
                    "destination_country": "USA",
                    "warehouse_id": "WH-01",
                    "carrier_name": "FedEx",
                    "carrier_scac": "FDEG",
                    "order_date": "2024-09-27",
                    "total_units": 12500,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 12500,
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0017",
                    "notes": "Project Unify - Inventory Consolidation",
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 94
    Task(
        annotator="0",
        user_id="U94",
        instruction="You are a senior procurement specialist. Today is September 28, 2024. We have a critical stock-out. A new high-priority order requires 600 'Teak Wood Dining Chair' units, but our 'Dallas Home Goods DC' only has 520 available. The lead time from our primary supplier, 'Bangkok Furniture Co.', is too long. I need you to evaluate an alternate supplier, 'Paris Luxury Goods'. You must verify two things: that they are in the 'Furniture' product category and that their performance rating is above 4.5. If they do not meet these criteria, you must revert to ordering the full 600 units from the primary supplier, 'Bangkok Furniture Co.'. Create the necessary purchase order from the chosen supplier and update the inventory pipeline. Please respond with the new Purchase Order number and the name of the supplier you selected.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Paris Luxury Goods",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1007",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "destination_warehouse_id": "WH-14",
                    "order_quantity": 600,
                    "unit_cost": 120.0,
                    "unit_weight": 8.0,
                    "expected_arrival_date": "2024-11-02",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_add": 600,
                },
            ),
        ],
        outputs=[
            "PO-2024-0031",
            "Bangkok Furniture Co.",
        ],
    ),
    # Task 95
    Task(
        annotator="0",
        user_id="U95",
        instruction="You are a logistics analyst. Today is September 30, 2024. We are analyzing freight costs and believe we are inefficiently shipping 'Organic Cotton T-Shirt' units from our Newark Apparel Hub to our West Coast customer, 'Alpha Electronics LLC'. Your first task is to confirm this by checking our outbound orders. Then, we will set up a new stocking location. Check if an inventory record for this product already exists at the 'Seattle Fulfillment Center'. If not, create one. Then, initiate a bulk stock transfer of 3,000 units from Newark to Seattle. Use the sales order number 'IBT-NWK-SEA-01' for this transfer, with the 'Seattle Fulfillment Center' as the customer. Select the most economical 'LTL' truck carrier. After creating the transfer order and allocating the stock, add a note to the new order: 'Strategic stock placement to reduce West Coast freight costs.' Please respond with the new Order ID and the new Inventory ID you created.",
        actions=[
            Action(
                name="get_all_outbound_orders",
                kwargs={},
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Organic Cotton T-Shirt",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Newark Apparel Hub",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Seattle Fulfillment Center",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                },
            ),
            Action(
                name="create_inventory_record",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-02",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "IBT-NWK-SEA-01",
                    "customer_name": "Seattle Fulfillment Center",
                    "destination_city": "Seattle",
                    "destination_country": "USA",
                    "warehouse_id": "WH-04",
                    "carrier_name": "FedEx",
                    "carrier_scac": "FDEG",
                    "order_date": "2024-09-30",
                    "total_units": 3000,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                    "quantity_to_allocate": 3000,
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0017",
                    "notes": "Strategic stock placement to reduce West Coast freight costs.",
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "INV-0026",
        ],
    ),
    # Task 96
    Task(
        annotator="0",
        user_id="U96",
        instruction="You are a quality control manager. Today is October 15, 2024. Our inbound shipment SHIP-0002 from 'Tokyo Electronics Ltd.' containing 'Smartphone Model X' has failed its quality inspection upon arrival at the 'Seattle Fulfillment Center'. You must process this failure. First, find the corresponding inventory record and update its status to 'Quarantined - Awaiting RTV'. Next, you must create a Return-to-Vendor (RTV) shipment for the entire quantity of 2300 units. To do this, create an outbound order with the supplier, 'Tokyo Electronics Ltd.', as the customer, using the sales order number 'RTV-SHIP-0002'. Select the most economical 'LTL' truck carrier for this return. After creating the RTV order and allocating the quarantined inventory, you must update the notes on the original inbound shipment (SHIP-0002) to state: 'Goods failed inspection. RTV processed via order [New Order ID].' Please respond with the ID of the inventory record you quarantined and the new Order ID for the return shipment.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Smartphone Model X",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Seattle Fulfillment Center",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0023",
                    "new_status": "Quarantined - Awaiting RTV",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Tokyo Electronics Ltd.",
                },
            ),
            Action(
                name="get_supplier_details",
                kwargs={
                    "supplier_id": "SUP-1002",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "RTV-SHIP-0002",
                    "customer_name": "Tokyo Electronics Ltd.",
                    "destination_city": "Chuo-ku, Tokyo",
                    "destination_country": "Japan",
                    "warehouse_id": "WH-02",
                    "carrier_name": "FedEx",
                    "carrier_scac": "FDEG",
                    "order_date": "2024-10-15",
                    "total_units": 2300,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "quantity_to_allocate": 2300,
                },
            ),
            Action(
                name="update_shipment_notes",
                kwargs={
                    "shipment_id": "SHIP-0002",
                    "new_note": "Goods failed inspection. RTV processed via order ORD-0017.",
                },
            ),
        ],
        outputs=[
            "Inventory Record Quarantined: INV-0023",
            "RTV Order ID: ORD-0017",
        ],
    ),
    # Task 97
    Task(
        annotator="0",
        user_id="U97",
        instruction="You are a data integrity specialist. Today is October 8, 2024. Our audit has found a redundant inventory record for the '8-bit Microcontroller' at the 'Chicago Parts Depot'; all stock should be consolidated at our primary 'Los Angeles Distribution Center'. Please execute this consolidation. First, you must create an inter-warehouse stock transfer to move the entire on-hand quantity from Chicago to Los Angeles. Use the sales order number 'CONSOL-001' for this transfer, with the 'Los Angeles Distribution Center' as the customer, and select the most economical 'LTL' truck carrier. After creating the transfer order and allocating the stock, you must perform an inventory adjustment on the Chicago record to write its physical count down to zero, noting the reason as 'Consolidated to WH-01'. Finally, update the status of the Chicago inventory record to 'Deactivated'. Please respond with the new Order ID for the transfer and the ID of the inventory record you deactivated.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Distribution Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="find_cheapest_carrier_by_service",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "CONSOL-001",
                    "customer_name": "Los Angeles Distribution Center",
                    "destination_city": "Los Angeles",
                    "destination_country": "USA",
                    "warehouse_id": "WH-03",
                    "carrier_name": "FedEx",
                    "carrier_scac": "FDEG",
                    "order_date": "2024-10-08",
                    "total_units": 8000,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 8000,
                },
            ),
            Action(
                name="perform_inventory_adjustment",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03",
                    "new_physical_count": 0,
                    "current_date": "2024-10-08",
                    "reason_note": "Consolidated to WH-01",
                },
            ),
            Action(
                name="update_inventory_status",
                kwargs={
                    "inventory_id": "INV-0025",
                    "new_status": "Deactivated",
                },
            ),
        ],
        outputs=[
            "ORD-0017",
            "INV-0025",
        ],
    ),
    # Task 98
    Task(
        annotator="0",
        user_id="U98",
        instruction="You are a reverse logistics coordinator. Today is October 9, 2024. Our customer, 'Alpha Electronics LLC', has requested to return 50 units of the '8-bit Microcontroller' from their original sales order, SO-2024-0001. Please process this return. First, you must update the original order's return status to 'Return Initiated'. Then, create a new inbound shipment record to track the return, treating the customer as the supplier. The return should be directed to the original fulfillment warehouse, the 'Los Angeles Distribution Center'. Select the highest-rated 'Parcel' carrier to handle the return shipment and set the expected arrival for 3 days from today. Add a note to the new shipment: 'Customer Return Authorization for ORD-0001'. Finally, ensure the inventory pipeline at the receiving warehouse is updated to reflect this incoming return. Please respond with the ID of the original order you updated and the new Shipment ID for the return.",
        actions=[
            Action(
                name="find_outbound_order_by_so",
                kwargs={
                    "sales_order_number": "SO-2024-0001",
                },
            ),
            Action(
                name="update_outbound_order_details",
                kwargs={
                    "order_id": "ORD-0001",
                    "return_status": "Return Initiated",
                },
            ),
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Distribution Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="find_carrier_by_method_of_transport",
                kwargs={
                    "method_of_transport": "Parcel",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "CUST-2001",
                    "supplier_name": "Alpha Electronics LLC",
                    "destination_warehouse_id": "WH-01",
                    "order_quantity": 50,
                    "unit_cost": 2.5,
                    "unit_weight": 0.01,
                    "expected_arrival_date": "2024-10-12",
                    "carrier_name": "UPS",
                    "mode_of_transport": "Parcel",
                    "notes": "Customer Return Authorization for ORD-0001.",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[
            "Original Order Updated: ORD-0001",
            "Return Shipment ID: SHIP-0031",
        ],
    ),
    # Task 99
    Task(
        annotator="0",
        user_id="U99",
        instruction="You are a fulfillment coordinator. Today is October 24, 2024. Please process a new sales order, SO-2024-0045, for our customer 'Gamma Construction Ltd.' for 150 'Ceramic Brake Pad Set' units. This order should be fulfilled from the 'Chicago Parts Depot' and shipped via 'FedEx'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm the process is complete.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "Ceramic Brake Pad Set",
                },
            ),
            Action(
                name="find_inventory_by_sku",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Chicago Parts Depot",
                },
            ),
            Action(
                name="get_carrier_details_by_name",
                kwargs={
                    "carrier_name": "FedEx",
                },
            ),
            Action(
                name="create_outbound_order",
                kwargs={
                    "sales_order_number": "SO-2024-0045",
                    "customer_name": "Gamma Construction Ltd.",
                    "warehouse_id": "WH-03",
                    "carrier_name": "FedEx",
                    "carrier_scac": "FDEG",
                    "order_date": "2024-10-24",
                    "total_units": 150,
                },
            ),
            Action(
                name="update_inventory_allocated_quantity",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 150,
                },
            ),
        ],
        outputs=[
            "ORD-0017",
        ],
    ),
    # Task 100
    Task(
        annotator="0",
        user_id="U100",
        instruction="You are a VMI Analyst. Today is October 18, 2024. I'm reconciling a VMI report from 'Global Components Inc.' for the '8-bit Microcontroller' at our 'Los Angeles Distribution Center'. Their report shows an on-hand quantity of 3,900 units, which is lower than our system's value. A physical count has just confirmed their number is correct. Your first task is to perform an inventory adjustment to update our on-hand quantity to 3,900, noting the reason as 'VMI Reconciliation'. After this adjustment, you must check if the new available quantity is below the reorder point for this item. If it is, you must immediately create a high priority replenishment purchase order for 5,000 units from the same supplier. Please respond with the ID of the inventory record you adjusted and the new Purchase Order number if one was created.",
        actions=[
            Action(
                name="find_product_by_name",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="find_warehouse_by_name",
                kwargs={
                    "warehouse_name": "Los Angeles Distribution Center",
                },
            ),
            Action(
                name="get_inventory_details",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="perform_inventory_adjustment",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "new_physical_count": 3900,
                    "current_date": "2024-10-18",
                    "reason_note": "VMI Reconciliation",
                },
            ),
            Action(
                name="find_supplier_by_name",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="create_inbound_shipment",
                kwargs={
                    "supplier_id": "SUP-1001",
                    "destination_warehouse_id": "WH-01",
                    "order_quantity": 5000,
                    "unit_cost": 2.5,
                    "unit_weight": 0.01,
                    "expected_arrival_date": "2024-11-12",
                    "priority_level": "High",
                },
            ),
            Action(
                name="update_inventory_inbound_quantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 5000,
                },
            ),
        ],
        outputs=[
            "Inventory Record Adjusted: INV-0001",
            "New PO Number: PO-2024-0031",
        ],
    ),
]
