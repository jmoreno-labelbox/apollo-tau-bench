from tau_bench.types import Action, Task


TASKS = [
    # Task 1
    Task(
        annotator="0",
        user_id="U01",
        instruction="Your name is Sarah, and you are the inventory manager at the West Coast Distribution Hub. The date is 2024-06-10. An alert has informed you that the stock level of 8-bit Microcontrollers is below the reorder threshold. Please initiate a purchase order with our primary supplier, Global Components Inc., to replenish this inventory. The order quantity must be twice the reorder point, and the inbound shipment should arrive via sea freight to our warehouse.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "West Coast Distribution Hub",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="FindCarrierByMethodOfTransport",
                kwargs={
                    "method_of_transport": "sea",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1001",
                    "current_date": "2024-06-10",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1001",
                    "supplier_name": "Global Components Inc.",
                    "destination_warehouse_id": "WH-01",
                    "destination_warehouse_name": "West Coast Distribution Hub",
                    "order_quantity": 8000,
                    "unit_cost": 2.50,
                    "unit_weight": 0.01,
                    "expected_arrival_date": "2024-07-05",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 8000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 2
    Task(
        annotator="0",
        user_id="U02",
        instruction="Your role is as a logistics specialist. Today is June 12, 2024. We've just obtained a high-priority order (SO-2024-0011) from Lambda Healthcare Pty in Cape Town, South Africa, for 1,800 units of the Influenza Vaccine. This shipment is critical and must be kept at 5°C. The Charlotte Cold Chain Center is assigned to handle these orders. Please proceed with processing this order: allocate the necessary stock from the Charlotte warehouse and record the outbound shipment. Use the quickest air freight option available that accommodates pharmaceutical cold chain logistics.'ve just received a high-priority order (SO-2024-0011) from a customer, Lambda Healthcare Pty, in Cape Town, South Africa. They need 1,800 units of the Influenza Vaccine. This is a high priority, critical shipment that must be maintained in 5°C. Our Charlotte Cold Chain Center is designated for fulfilling these types of orders. Please process this order: allocate the necessary inventory from the Charlotte warehouse and create the outbound shipment record. Use the fastest available air freight option that supports pharmaceutical cold chain logistics.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Influenza Vaccine",
                },
            ),
            Action(
                name="GetProductDetails",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Charlotte Cold Chain Center",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Pharma",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0011",
                    "customer_name": "Lambda Healthcare Pty",
                    "destination_city": "Cape Town",
                    "destination_country": "South Africa",
                    "warehouse_id": "WH-06",
                    "carrier_scac": "DFC",
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
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "quantity_to_allocate": 1800,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 3
    Task(
        annotator="0",
        user_id="U03",
        instruction="Your position is supply chain analyst, and the date is June 18, 2024. There are concerns over potential stock-outs of our '8-bit Microcontroller' due to a recent surge in demand. Please perform a complete inventory evaluation for this item across all our warehouses. Review all incoming shipments for potential delays. Should you identify any shipment that is overdue, update its record with this urgent note: 'URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.''8-bit Microcontroller' due to a recent spike in demand. Please conduct a full inventory assessment for this product across all our warehouses. Review all inbound shipments for this product to see if any are delayed. If you find a relevant inbound shipment that is past its expected arrival date, please update its record with a high-priority note: 'URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.'",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="FindInboundShipmentsByWarehouse",
                kwargs={
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="FindInboundShipmentsByWarehouse",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0003",
                    "new_note": "URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0023",
                    "new_note": "URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0019",
                    "new_note": "URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0016",
                    "new_note": "URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0030",
                    "new_note": "URGENT: Potential stock-out risk due to shipment delay. Please expedite and provide updated ETA.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 4
    Task(
        annotator="0",
        user_id="U04",
        instruction="You are the procurement manager. On June 20, 2024, you are worried about a delayed shipment of 'Agglomerated Cork Stopper' from our supplier 'Lisbon Cork Products' destined for the 'San Diego Beverage DC'. First, locate this specific delayed shipment and report its total value and currency. Then, due to the delay, check the available inventory and tag it with 'Critical: Inbound shipment delayed' status for this product at the destination warehouse. Lastly, as a backup for future shipments, identify the top-rated active carrier for 'Sea' transport. Respond with the delayed shipment's value, available quantity, and alternate carrier's name.'m concerned about a delayed shipment of 'Agglomerated Cork Stopper' from our supplier, 'Lisbon Cork Products', which is heading to the 'San Diego Beverage DC'. First, find this specific delayed shipment and report its total value and currency. Second, because of this delay, I need you to check the current available inventory and add the following status: 'Critical: Inbound shipment delayed' for this product at the destination warehouse. Finally, as a contingency plan for future orders, find the name of the highest-rated active carrier for 'Sea' transport. Your final answer should be the delayed shipment's value, the current available quantity, and the name of the alternative carrier.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Agglomerated Cork Stopper",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Lisbon Cork Products",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1022",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "San Diego Beverage DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "MATR-CORK-T20",
                    "warehouse_id": "WH-15",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0020",
                    "new_status": "Critical: Inbound shipment delayed",
                },
            ),
            Action(
                name="FindCarrierByMethodOfTransport",
                kwargs={
                    "method_of_transport": "Sea",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 5
    Task(
        annotator="0",
        user_id="U05",
        instruction="You are functioning as a fulfillment coordinator. Today's date is October 28, 2024. Process a new sales order, SO-2024-0046, for our customer 'Beta Retail GmbH' for 30 'Leather Handbag' units. This order must be processed from the 'NYC Luxury Vault' and shipped using 'SwiftDelivery'. Once you've created the outbound order, ensure the inventory allocation is updated. Reply with the new Order ID for confirmation.'Beta Retail GmbH' for 30 'Leather Handbag' units. This order must be fulfilled from the 'NYC Luxury Vault' and shipped via 'SwiftDelivery'. After creating the outbound order, please ensure you update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Leather Handbag",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "NYC Luxury Vault",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "SwiftDelivery",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0046",
                    "customer_name": "Beta Retail GmbH",
                    "warehouse_id": "WH-07",
                    "carrier_name": "SwiftDelivery",
                    "carrier_scac": "SWDL",
                    "order_date": "2024-10-28",
                    "total_units": 30,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                    "quantity_to_allocate": 30,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 6
    Task(
        annotator="0",
        user_id="U06",
        instruction="Act as a purchasing agent. Today is October 25, 2024. Initiate a purchase order for 100 units of the 'Teak Wood Dining Chair' from our supplier, 'Bangkok Furniture Co.'. Arrange for the shipment to be delivered to the 'Dallas Home Goods DC'. Once the purchase order is created, ensure the inventory's inbound quantity is updated. Confirm the creation by responding with the new Purchase Order number.'Teak Wood Dining Chair' from our supplier, 'Bangkok Furniture Co.'. The shipment should be delivered to the 'Dallas Home Goods DC'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_add": 100,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 7
    Task(
        annotator="0",
        user_id="U07",
        instruction="Function as a supply chain analyst. Today is June 22, 2024. The manager of the NYC Luxury Vault has performed a cycle count for the 'Automatic Watch Movement', noting a physical count of 498 units. Proceed to process this inventory adjustment. Update the system with this new physical count and make certain the 'current date' is set to today.'Automatic Watch Movement' and found a physical quantity of 498 units. Please process this inventory adjustment. You need to update the system to reflect this new physical count and ensure the 'current date' is updated to today.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Automatic Watch Movement",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "NYC Luxury Vault",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="PerformInventoryAdjustment",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "new_physical_count": 498,
                    "current_date": "2024-06-22",
                    "reason_note": "Cycle Count Adjustment",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 8
    Task(
        annotator="0",
        user_id="U08",
        instruction="Take on the role of a customer service logistics specialist. Today is June 24, 2024. We've received an urgent call from our customer, Beta Retail GmbH, regarding their sales order SO-2024-0002. Although the shipment is en route to Munich, it must be redirected to their new central distribution center at 'Gateway Gardens, Frankfurt am Main, 60549, Deutschland'. Amend the order record to show this new destination and change its status to 'Diverted'. Include a note on the order that the customer requested the diversion on today's date.'ve just received an urgent call from our customer, Beta Retail GmbH, regarding their sales order SO-2024-0002. The shipment is currently in transit to Munich, but they need to divert it to their new central distribution center at 'Gateway Gardens, Frankfurt am Main, 60549, Deutschland'. Please update the order record to reflect this new destination address and change its status to 'Diverted'. Append a note to the order indicating that the diversion was requested by the customer on today's date.",
        actions=[
            Action(
                name="FindOutboundOrderBySo",
                kwargs={
                    "sales_order_number": "SO-2024-0002",
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0002",
                    "destination_address": "Gateway Gardens",
                    "destination_city": "Frankfurt am Main",
                    "destination_country": "Deutschland",
                    "status": "Diverted",
                    "notes": "Diversion requested by customer on 2024-06-24.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 9
    Task(
        annotator="0",
        user_id="U09",
        instruction="Serve as a purchasing agent. Today is November 12, 2024. Formulate a purchase order for 50 units of 'Industrial Solvent' from our supplier, 'Helsinki Chemicals Oy'. Ensure the shipment is directed to the 'Cleveland Chemical Storage' warehouse. Once the purchase order is set, be sure to update the inventory's inbound quantity. Validate by providing the new Purchase Order number.'Industrial Solvent' from our supplier, 'Helsinki Chemicals Oy'. The shipment should be delivered to the 'Cleveland Chemical Storage' warehouse. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Industrial Solvent",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Helsinki Chemicals Oy",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Cleveland Chemical Storage",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 10
    Task(
        annotator="0",
        user_id="U10",
        instruction="Work as a specialized logistics coordinator for high-value pharmaceuticals. Today is June 8, 2024. Arrange for a crucial shipment of a new product, 'Oncology Drug A', sourced from our supplier, 'Stockholm Pharma AB', to our client, 'Delta Pharma Inc.' in Boston, United States. First, draft a purchase order for 250 boxes of this drug. It's imperative the product is kept at 5°C. This shipment should be dispatched to our 'Charlotte Cold Chain Center' warehouse, equipped for managing such sensitive goods. Estimate the arrival date at the Charlotte warehouse based on the supplier's standard lead time. Choose the top-rated 'Air' carrier providing a 'Pharma' service level for this leg of the journey. Once the inbound shipment is set, promptly update the inventory record at the Charlotte warehouse to indicate these 250 boxes as 'inbound'.'Oncology Drug A', from our supplier, 'Stockholm Pharma AB', to our client, 'Delta Pharma Inc.', located in Boston, United States. First, you must create a purchase order for 250 boxes of this drug. Important to note, this product must be maintained at a temperature of 5°C. This shipment needs to be sent to our 'Charlotte Cold Chain Center' warehouse, which is equipped to handle such sensitive materials. Please calculate the expected arrival date at the Charlotte warehouse based on the supplier's standard lead time. You'll need to find the best-rated 'Air' carrier that offers a 'Pharma' service level for this inbound leg. Once the inbound shipment is created, you must immediately update the inventory record at the Charlotte warehouse to show these 250 boxes as 'inbound'.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Oncology Drug A",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Stockholm Pharma AB",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Charlotte Cold Chain Center",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "current_date": "2024-06-08",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Pharma",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "supplier_name": "Stockholm Pharma AB",
                    "destination_warehouse_id": "WH-06",
                    "destination_warehouse_name": "Charlotte Cold Chain Center",
                    "order_quantity": 250,
                    "unit_cost": 1800.00,
                    "unit_weight": 0.5,
                    "expected_arrival_date": "2024-06-16",
                    "carrier_name": "Desert Falcon Cargo",
                    "mode_of_transport": "Air",
                    "temperature_control_required": True,
                    "temperature_celsius": 5,
                    "hazmat": False,
                    "priority_level": "Critical",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06",
                    "quantity_to_add": 250,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 11
    Task(
        annotator="0",
        user_id="U11",
        instruction='Handle the responsibilities of an inventory control specialist. Today\'s date is June 6, 2024. A cycle count has just been completed for the "Ceramic Brake Pad Set" at our "Midwest Parts Warehouse". There are now 180 sets physically counted. Your initial task is to coordinate an inventory adjustment in the system to reflect this updated count. It\'s imperative to calculate the new "quantity available" accurately by considering any currently allocated stock. Log the reason as "Cycle Count Correction" with today\'s date. After finalizing the adjustment, determine if the new available quantity has dropped below the reorder point for this product. If so, you must promptly generate a new purchase order for 200 sets from our supplier, "Bavaria Parts GmbH", intended for the Midwest Parts Warehouse. Upon creation of the purchase order, update the product\'s inventory record with this incoming quantity.',
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Ceramic Brake Pad Set",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                },
            ),
            Action(
                name="PerformInventoryAdjustment",
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
                name="GetInventoryDetails",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bavaria Parts GmbH",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1003",
                    "supplier_name": "Bavaria Parts GmbH",
                    "destination_warehouse_id": "WH-03",
                    "destination_warehouse_name": "Midwest Parts Warehouse",
                    "order_quantity": 200,
                    "unit_cost": 45.0,
                    "unit_weight": 2.5,
                    "expected_arrival_date": "2024-06-16",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "quantity_to_add": 200,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 12
    Task(
        annotator="0",
        user_id="U12",
        instruction="Coordinate fulfillment tasks as a coordinator. Today is November 13, 2024. Proceed to handle a new sales order, SO-2024-0052, from our customer 'Beta Retail GmbH' for 30 'Leather Handbag' units. This order is to be fulfilled from the 'NYC Luxury Vault'. For this urgent delivery, choose the highest-rated carrier offering 'Express' service via 'Air'. Following the outbound order creation, ensure that you update the allocated inventory. Confirm by responding with the new Order ID.'Beta Retail GmbH' for 30 'Leather Handbag' units. This order should be fulfilled from the 'NYC Luxury Vault'. For this urgent shipment, please select the highest-rated carrier that offers 'Express' service via 'Air'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Leather Handbag",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "NYC Luxury Vault",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Express",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0052",
                    "customer_name": "Beta Retail GmbH",
                    "warehouse_id": "WH-07",
                    "carrier_name": "Desert Falcon Cargo",
                    "carrier_scac": "DFC",
                    "order_date": "2024-11-13",
                    "total_units": 30,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "APRL-BAG-E5",
                    "warehouse_id": "WH-07",
                    "quantity_to_allocate": 30,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 13
    Task(
        annotator="0",
        user_id="U13",
        instruction='Manage quality control logistics as a Manager. Today\'s date is June 7, 2024. We have been notified of a quality alert concerning EAC number "LOT202405A" for the "8-bit Microcontroller". Locate all inventory records matching this specific EAC number across all warehouses and update their status to "Quarantined". After quarantining the affected stock, initiate an urgent replacement purchase order for 15,000 units of the "8-bit Microcontroller" from our reliable supplier, "Osaka Electronics Ltd.", on high priority. Direct this replacement order to the "West Coast Distribution Hub". Ensure you identify the highest-rated "Air" carrier for this urgent shipment, determine the expected arrival date, and update the inbound quantity for the product at the San Diego warehouse to include this order.',
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0001",
                    "new_status": "Quarantined",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Osaka Electronics Ltd.",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "West Coast Distribution Hub",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "current_date": "2024-06-07",
                },
            ),
            Action(
                name="FindCarrierByMethodOfTransport",
                kwargs={
                    "method_of_transport": "Air",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "supplier_name": "Osaka Electronics Ltd.",
                    "destination_warehouse_id": "WH-01",
                    "destination_warehouse_name": "West Coast Distribution Hub",
                    "order_quantity": 15000,
                    "unit_cost": 2.5,
                    "unit_weight": 0.01,
                    "expected_arrival_date": "2024-06-22",
                    "carrier_name": "Desert Falcon Cargo",
                    "mode_of_transport": "Air",
                    "priority_level": "High",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 15000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 14
    Task(
        annotator="0",
        user_id="U14",
        instruction="Oversee tasks as an order fulfillment specialist. Today is June 8, 2024. Our customer, 'Alpha Electronics LLC', located in San Jose, United States, has initiated a new order (Sales Order SO-2024-7788) for 8,000 units of the \"8-bit Microcontroller\" and 1,000 units of the \"Lithium-Ion Battery Pack\". Fulfill the entire order from a single warehouse. Identify a warehouse with sufficient available stock for both products. Once a suitable warehouse is located, create a single outbound order using the most economical 'Truck' carrier offering 'LTL' service. Due to the shipment containing hazardous materials, flag the order appropriately (hazmat class 9). Finally, ensure that the stock for both products is allocated from the chosen warehouse after order creation.'Alpha Electronics LLC', located in San Jose, United States, has placed a new order (Sales Order SO-2024-7788) for 8,000 units of the \"8-bit Microcontroller\" and 1,000 units of the \"Lithium-Ion Battery Pack\". The entire order must be fulfilled from a single warehouse. Please identify a warehouse that has sufficient available stock for both products. Once you've found a suitable warehouse, create a single outbound order using the most economical (cheapest) 'Truck' carrier that offers 'LTL' service. Since this shipment contains hazardous materials, ensure the order is flagged appropriately (hazmat class 9). Finally, after creating the order, make sure to allocate the stock for both products from the chosen warehouse.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Lithium-Ion Battery Pack",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-7788",
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "destination_country": "United States",
                    "warehouse_id": "WH-03",
                    "carrier_name": "SwiftDelivery",
                    "carrier_scac": "SWDL",
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
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 8000,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 1000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 15
    Task(
        annotator="0",
        user_id="U15",
        instruction="Handle logistics coordination duties. Today's date is June 9, 2024. Our customer, 'Gamma Construction Ltd.' in Denver, has placed an order (SO-2024-8801) for 10 'Articulated Robotic Arm' units, a heavy and fragile product. Firstly, locate a warehouse that has a minimum of 10 units on hand and offers 'Heavy Equipment Handling' as a special capability. After identifying the appropriate warehouse, proceed to create the outbound order. For shipping, select the highest-rated 'Rail' carrier that provides 'Intermodal' service. Ensure you allocate the 10 units from the inventory of the source warehouse after creating the order.'Gamma Construction Ltd.' in Denver, has placed an order (SO-2024-8801) for 10 'Articulated Robotic Arm' units. This is a heavy and fragile product. First, find a warehouse that has at least 10 units available and also has 'Heavy Equipment Handling' as a special capability. Once you have identified the correct warehouse, create the outbound order. For shipping, you must find the highest-rated 'Rail' carrier that offers 'Intermodal' service. After creating the order, please ensure you allocate the 10 units from the source warehouse's inventory.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Rail",
                    "service_level": "Intermodal",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-8801",
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "destination_country": "United States",
                    "warehouse_id": "WH-03",
                    "carrier_name": "NorthStar Shipping",
                    "carrier_scac": "NSTS",
                    "mode_of_transport": "Rail",
                    "shipping_service_level": "Intermodal",
                    "total_units": 10,
                    "order_date": "2024-06-09",
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 10,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 16
    Task(
        annotator="0",
        user_id="U16",
        instruction="You are a supply chain analyst. Today is June 19, 2024. An alert has been raised for a delayed shipment from 'Busan Textiles Co.' to our 'East Coast Fashion Center'. Locate this shipment. The current note likely mentions a typhoon, but I need you to handle a root cause analysis by checking the operational status of the assigned carrier. Record your conclusions in the shipment's notes (e.g., 'Root cause: Carrier is inactive'). After this, I require a financial risk assessment for a different critical product at the East Coast Fashion Center: the 'Raw Cotton Bale'. Determine the total current value of all on-hand inventory for this particular product at that warehouse. Your final answer should be only this total dollar amount.'Busan Textiles Co.' to our 'East Coast Fashion Center'. Please find this shipment. The current note likely mentions a typhoon, but I need you to perform a root cause analysis by checking the operational status of the assigned carrier. Update the shipment's notes with your findings (e.g., 'Root cause: Carrier is inactive'). After updating the shipment, I need a financial risk assessment for a different critical product at the East Coast Fashion Center: the 'Raw Cotton Bale'. Please calculate the total current value of all on-hand inventory for this specific product at that warehouse. Your final answer should be only this total dollar amount.",
        actions=[
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Busan Textiles Co.",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "East Coast Fashion Center",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1004",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Pacific Ocean Lines",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0004",
                    "new_note": "Root cause: Carrier is inactive.",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Raw Cotton Bale",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 17
    Task(
        annotator="0",
        user_id="U17",
        instruction="You are a purchasing agent. Today is October 29, 2024. Coordinate the creation of a new purchase order for 200 'Solar Panel 450W' units from our supplier, 'Beijing Solar Tech'. The shipment should be routed to the 'Phoenix Renewable Warehouse'. Following the creation of the purchase order, make sure the inventory's inbound quantity is updated. Reply with the new Purchase Order number to confirm.'Solar Panel 450W' units from our supplier, 'Beijing Solar Tech'. The shipment should be delivered to the 'Phoenix Renewable Warehouse'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Solar Panel 450W",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Beijing Solar Tech",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "quantity_to_add": 200,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 18
    Task(
        annotator="0",
        user_id="U18",
        instruction="You are a fulfillment coordinator. Today is October 30, 2024. Please process a new sales order, SO-2024-0047, for our customer 'Gamma Construction Ltd.' for 20 'Automotive Windshield' units. This order is to be fulfilled from the 'Midwest Parts Warehouse' and shipped via 'Global Parcel Service'. After setting up the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.'Gamma Construction Ltd.' for 20 'Automotive Windshield' units. This order should be fulfilled from the 'Midwest Parts Warehouse' and shipped via 'Global Parcel Service'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Automotive Windshield",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Global Parcel Service",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0047",
                    "customer_name": "Gamma Construction Ltd.",
                    "warehouse_id": "WH-03",
                    "carrier_name": "Global Parcel Service",
                    "carrier_scac": "GPLS",
                    "order_date": "2024-10-30",
                    "total_units": 20,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 20,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 19
    Task(
        annotator="0",
        user_id="U19",
        instruction="You are a purchasing agent. Today is October 31, 2024. Initiate a new purchase order for 50 'Raw Cotton Bale' units from our supplier, 'Cairo Cotton Co.'. The shipment should be delivered to the 'East Coast Fashion Center'. After generating the purchase order, ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.'Raw Cotton Bale' units from our supplier, 'Cairo Cotton Co.'. The shipment should be delivered to the 'East Coast Fashion Center'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Raw Cotton Bale",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Cairo Cotton Co.",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "East Coast Fashion Center",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 20
    Task(
        annotator="0",
        user_id="U20",
        instruction="You are a fulfillment coordinator. Today is November 1, 2024. Manage the processing of a new sales order, SO-2024-0048, for our customer 'Theta Foods SA' for 100 'Frozen Tuna Loin' units. This order should be completed from the 'San Francisco Fresh Foods DC' and shipped via 'Southern Cross Freight'. Following the creation of the outbound order, ensure the allocated inventory is updated. Respond with the new Order ID to confirm.'Theta Foods SA' for 100 'Frozen Tuna Loin' units. This order should be fulfilled from the 'San Francisco Fresh Foods DC' and shipped via 'Southern Cross Freight'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Frozen Tuna Loin",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "San Francisco Fresh Foods DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Southern Cross Freight",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0048",
                    "customer_name": "Theta Foods SA",
                    "warehouse_id": "WH-10",
                    "carrier_name": "Southern Cross Freight",
                    "carrier_scac": "SCF",
                    "order_date": "2024-11-01",
                    "total_units": 100,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                    "quantity_to_allocate": 100,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 21
    Task(
        annotator="0",
        user_id="U21",
        instruction="As an inventory planner for perishable goods, today is June 10, 2024. The current stock of 'Fresh Cut Roses' at the 'San Francisco Fresh Foods DC' will expire in two days. Kindly place a replenishment order for 5,000 bouquets with our supplier, 'Bogota Floral Exports', ahead of time. For shipping, choose the highest-rated 'Air' carrier that offers a 'Perishables' service level. Proceed to create the purchase order with accurate information and then update the inbound inventory for the roses at the San Francisco warehouse.'Fresh Cut Roses' at the 'San Francisco Fresh Foods DC' expires in two days. We need to proactively place a replenishment order for 5,000 bouquets from our supplier, 'Bogota Floral Exports'. For the shipment, you must select the highest-rated 'Air' carrier that offers a 'Perishables' service level. Create the purchase order with the correct details and then update the inbound inventory for the roses at the San Francisco warehouse.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Fresh Cut Roses",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "San Francisco Fresh Foods DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bogota Floral Exports",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1029",
                    "current_date": "2024-06-10",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Perishables",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1029",
                    "supplier_name": "Bogota Floral Exports",
                    "destination_warehouse_id": "WH-10",
                    "destination_warehouse_name": "San Francisco Fresh Foods DC",
                    "order_quantity": 5000,
                    "unit_cost": 12.0,
                    "unit_weight": 0.5,
                    "expected_arrival_date": "2024-06-12",
                    "carrier_name": "Desert Falcon Cargo",
                    "mode_of_transport": "Air",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                    "quantity_to_add": 5000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 22
    Task(
        annotator="0",
        user_id="U22",
        instruction="Acting as a purchasing agent, today is November 4, 2024. Proceed to create a new purchase order for 50 'Automatic Watch Movement' units from our supplier, 'Zurich Watch Parts AG'. Ensure the shipment is sent to the 'NYC Luxury Vault'. After the purchase order is created, make sure to update the inbound quantity in the inventory. Provide the new Purchase Order number as confirmation.'Automatic Watch Movement' units from our supplier, 'Zurich Watch Parts AG'. The shipment should be delivered to the 'NYC Luxury Vault'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Automatic Watch Movement",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Zurich Watch Parts AG",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "NYC Luxury Vault",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 23
    Task(
        annotator="0",
        user_id="U23",
        instruction="Being a customer service logistics specialist, today is June 11, 2024. Our customer, 'Alpha Electronics LLC', reported receiving incorrect items for order SO-2024-0001. They had ordered 300 '8-bit Microcontrollers'. Please verify the original order and confirm if the fulfillment warehouse has sufficient stock of the correct item for a replacement. If available, initiate a corrected outbound shipment for the 300 '8-bit Microcontrollers'. Utilize 'SO-2024-0001-CORRECTIVE' for the new sales order number. This replacement requires expediting, so opt for the highest-rated 'Air' carrier with 'Express' service. After placing the new order, ensure stock allocation and append a note to the original order (ORD-0001) saying ''Corrective shipment ORD-0017 created on 2024-06-11 for 300 units of 8-bit Microcontroller.''Alpha Electronics LLC', has contacted us about their order SO-2024-0001. They report that they received the wrong items. The order was for 300 '8-bit Microcontrollers'. Please verify the original order details and confirm that the fulfillment warehouse has enough available stock of the correct item to send a replacement. If stock is available, create a new, corrected outbound shipment for the 300 '8-bit Microcontrollers'. Use 'SO-2024-0001-CORRECTIVE' as the new sales order number. This replacement must be expedited, so please use the highest-rated 'Air' carrier that offers 'Express' service. After creating the new order, ensure you allocate the stock and add a note to the original order (ORD-0001) stating ''Corrective shipment ORD-0017 created on 2024-06-11 for 300 units of 8-bit Microcontroller.'",
        actions=[
            Action(
                name="FindOutboundOrderBySo",
                kwargs={
                    "sales_order_number": "SO-2024-0001",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Express",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0001-CORRECTIVE",
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "San Jose",
                    "destination_country": "United States",
                    "warehouse_id": "WH-01",
                    "carrier_name": "Desert Falcon Cargo",
                    "carrier_scac": "DFC",
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
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 300,
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0001",
                    "notes": "Corrective shipment ORD-0017 created on 2024-06-11 for 300 units of 8-bit Microcontroller.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 24
    Task(
        annotator="0",
        user_id="U24",
        instruction="As a purchasing agent, today is November 8, 2024. Go ahead and create a new purchase order for 100,000 'Agglomerated Cork Stopper' units from our supplier, 'Lisbon Cork Products'. Ensure the shipment reaches the 'San Diego Beverage DC'. Once the purchase order is created, confirm you update the inbound quantity in the inventory. Provide the new Purchase Order number for confirmation.'Agglomerated Cork Stopper' units from our supplier, 'Lisbon Cork Products'. The shipment should be delivered to the 'San Diego Beverage DC'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Agglomerated Cork Stopper",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Lisbon Cork Products",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "San Diego Beverage DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "MATR-CORK-T20",
                    "warehouse_id": "WH-15",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "MATR-CORK-T20",
                    "warehouse_id": "WH-15",
                    "quantity_to_add": 100000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 25
    Task(
        annotator="0",
        user_id="U25",
        instruction="As a fulfillment coordinator, today is November 5, 2024. Proceed to process a new sales order, SO-2024-0049, for our customer 'Gamma Construction Ltd.' for 30 'Industrial Paper Roll' units. Fulfill this order from the 'Detroit Packaging Supplies' warehouse. Choose the highest-rated carrier with 'LTL' service via 'Truck'. Upon creating the outbound order, ensure the allocated inventory is updated. Confirm by responding with the new Order ID.'Gamma Construction Ltd.' for 30 'Industrial Paper Roll' units. This order should be fulfilled from the 'Detroit Packaging Supplies' warehouse. Please select the highest-rated carrier that offers 'LTL' service via 'Truck'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Industrial Paper Roll",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Detroit Packaging Supplies",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0049",
                    "customer_name": "Gamma Construction Ltd.",
                    "warehouse_id": "WH-08",
                    "carrier_name": "Sakura Express",
                    "carrier_scac": "SKEX",
                    "order_date": "2024-11-05",
                    "total_units": 30,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08",
                    "quantity_to_allocate": 30,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 26
    Task(
        annotator="0",
        user_id="U26",
        instruction="You are a purchasing agent. Today is November 6, 2024. Kindly initiate a purchase order for 120 'Teak Wood Dining Chair' units from our supplier, 'Bangkok Furniture Co.'. The consignment should be sent to the 'Dallas Home Goods DC'. Once the purchase order is created, make sure to update the inventory's inbound quantity. Provide the new Purchase Order number to verify completion.'Teak Wood Dining Chair' units from our supplier, 'Bangkok Furniture Co.'. The shipment should be delivered to the 'Dallas Home Goods DC'. After creating the purchase order, please ensure you update the inventory's inbound quantity. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_add": 120,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 27
    Task(
        annotator="0",
        user_id="U27",
        instruction="You are a Quality Assurance Manager. Today is June 13, 2024. A vital quality alert has been issued for all '8-bit Microcontroller' stock in our possession. Begin by locating every warehouse carrying this product and change the inventory status to 'Quarantined'. Then, compute the full value of the stock you've just placed under quarantine. Our preferred supplier, 'Osaka Electronics Ltd.', will be used for replenishment. Make a new purchase order for 20,000 units with them. The delivery should be directed to the warehouse housing the most quarantined stock. Choose the most cost-effective 'Sea' freight carrier with 'FCL' service. Lastly, after creating the purchase order, update the inbound inventory at the target warehouse.'8-bit Microcontroller' stock. First, find every warehouse holding this product and update the inventory status to 'Quarantined'. Next, calculate the total value of all the stock you just quarantined. As a contingency, we will use our preferred supplier, 'Osaka Electronics Ltd.', for replenishment. Place a new purchase order for 20,000 units from them. The shipment should be sent to the warehouse that had the largest quantity of the quarantined stock. Use the most economical 'Sea' freight carrier that offers 'FCL' service. Finally, after creating the purchase order, update the inbound inventory at the destination warehouse.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0001",
                    "new_status": "Quarantined",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0025",
                    "new_status": "Quarantined",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Osaka Electronics Ltd.",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "current_date": "2024-06-13",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Sea",
                    "service_level": "FCL",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "supplier_name": "Osaka Electronics Ltd.",
                    "destination_warehouse_id": "WH-01",
                    "destination_warehouse_name": "West Coast Distribution Hub",
                    "order_quantity": 20000,
                    "unit_cost": 2.5,
                    "unit_weight": 0.01,
                    "expected_arrival_date": "2024-06-28",
                    "carrier_name": "Ocean Bridge",
                    "carrier_scac": "OCBR",
                    "mode_of_transport": "Sea",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 20000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 28
    Task(
        annotator="0",
        user_id="U28",
        instruction="You are a high-value logistics coordinator. Today is June 14, 2024. We have a critical order from our client, 'ChronoSwiss Retailers' in Zurich, Helvetia, for 50 'Automatic Watch Movement' units (Sales Order SO-2024-9951). This order demands fulfillment from a warehouse certified as a 'UL Certified Vault' with 'High Security' capability. Identify a suitable warehouse with adequate stock, opt for the top-rated 'Air' carrier with 'High-Value' service level, and create the outbound order. After making the order and allocating the stock, return with the shipment's total value in USD.'ChronoSwiss Retailers' in Zurich, Helvetia, for 50 'Automatic Watch Movement' units (Sales Order SO-2024-9951). This order must be fulfilled from a warehouse that is 'UL Certified Vault' and has 'High Security' capabilities. Please find a suitable warehouse with sufficient stock, select the highest-rated 'Air' carrier offering a 'High-Value' service level, and create the outbound order. After creating the order and allocating the stock, report back with the total value of the shipment in USD.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Automatic Watch Movement",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "High-Value",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-9951",
                    "customer_name": "ChronoSwiss Retailers",
                    "destination_city": "Zurich",
                    "destination_country": "Helvetia",
                    "warehouse_id": "WH-07",
                    "carrier_name": "Desert Falcon Cargo",
                    "carrier_scac": "DFC",
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
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "quantity_to_allocate": 50,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 29
    Task(
        annotator="0",
        user_id="U29",
        instruction="You are a logistics coordinator. Today is June 20, 2024. Management has decided to bolster our safety stock for 'Oncology Drug A' at the Charlotte Cold Chain Center. This product requires stringent temperature regulation of 5°C. Begin a purchase order for 250 units from our supplier with high priority, Stockholm Pharma AB. You must select the top-rated carrier capable of executing a 'Pharma' service level through 'Air' transport. Following purchase order creation, ensure you update the inventory pipeline to include the new inbound quantity. Finally, please supply the newly generated Purchase Order number and the projected arrival date for the shipment.'Oncology Drug A' at the Charlotte Cold Chain Center. This is a product that requires strict temperature control of 5°C. Please initiate a new purchase order for 250 units from our supplier with a critical priority, Stockholm Pharma AB. You will need to find the highest-rated carrier that can handle a 'Pharma' service level via 'Air' transport. After creating the purchase order, ensure you update the inventory pipeline to reflect the new inbound quantity. As a final answer, please provide the newly generated Purchase Order number and the expected arrival date for the shipment.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Oncology Drug A",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Charlotte Cold Chain Center",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Stockholm Pharma AB",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "current_date": "2024-06-20",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Pharma",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1021",
                    "supplier_name": "Stockholm Pharma AB",
                    "destination_warehouse_id": "WH-06",
                    "destination_warehouse_name": "Charlotte Cold Chain Center",
                    "order_quantity": 250,
                    "unit_cost": 1200.0,
                    "unit_weight": 0.5,
                    "expected_arrival_date": "2024-06-28",
                    "carrier_name": "Desert Falcon Cargo",
                    "mode_of_transport": "Air",
                    "priority_level": "Critical",
                    "temperature_control_required": True,
                    "temperature_celsius": 5,
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                    "warehouse_id": "WH-06",
                    "quantity_to_add": 250,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 30
    Task(
        annotator="0",
        user_id="U30",
        instruction="You are a fulfillment coordinator. Today is November 7, 2024. Process a new sales order, SO-2024-0050, for our customer 'Nu Energy AB' for 50 'Solar Panel 450W' units. This order should be executed from the 'Phoenix Renewable Warehouse'. For this large, international shipment, select the most highly-rated carrier providing 'Project Cargo' service by 'Sea'. After executing the outbound order, ensure to update the inventory allocation. Confirm by providing the new Order ID.'Nu Energy AB' for 50 'Solar Panel 450W' units. This order should be fulfilled from the 'Phoenix Renewable Warehouse'. For this type of large, international shipment, please select the highest-rated carrier that offers 'Project Cargo' service via 'Sea'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Solar Panel 450W",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Sea",
                    "service_level": "Project Cargo",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0050",
                    "customer_name": "Nu Energy AB",
                    "warehouse_id": "WH-09",
                    "carrier_name": "Mediterranean Lines",
                    "carrier_scac": "MEDL",
                    "order_date": "2024-11-07",
                    "total_units": 50,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "quantity_to_allocate": 50,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 31
    Task(
        annotator="0",
        user_id="U31",
        instruction="As a fulfillment specialist, today, June 22, 2024, we've received a new order from 'Gamma Construction Ltd.', based in Denver, United States for 75 units of the 'Lithium-Ion Battery Pack', to be dispatched from our Midwest Parts Warehouse. This shipment falls under hazmat class 9, thus, initially verify the Milwaukee warehouse's certification for handling hazardous materials. Once verified, identify the most cost-effective carrier offering 'LTL' service for 'Truck' transport. Choose the carrier, generate the outbound order with the sales order number SO-2024-0019, and allocate the inventory. Please reply with the new Order ID and the carrier's name assigned to this order.'Gamma Construction Ltd.', located in Denver, United States for 75 units of the 'Lithium-Ion Battery Pack', which must be shipped from our Midwest Parts Warehouse. This is a hazmat class 9 shipment, so first, you must confirm that the Milwaukee warehouse is certified to handle hazardous materials. Once confirmed, please find the most economical carrier that provides 'LTL' service for 'Truck' transport. After selecting the carrier, create the outbound order with sales order number SO-2024-0019 and allocate the inventory. Please respond with the new Order ID and the name of the assigned carrier.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Lithium-Ion Battery Pack",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0019",
                    "customer_name": "Gamma Construction Ltd.",
                    "destination_city": "Denver",
                    "destination_country": "United States",
                    "warehouse_id": "WH-03",
                    "carrier_name": "SwiftDelivery",
                    "carrier_scac": "SWDL",
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
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "TECH-BATT-Q17",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 75,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 32
    Task(
        annotator="0",
        user_id="U32",
        instruction="As a supplier relationship manager, there's a concern regarding 'Johannesburg Mining Equipment's performance. Begin by retrieving their supplier details to check if their performance rating is below 4.5. Next, locate any of their inbound shipments currently marked 'In Transit' and update the shipment notes to include: 'Flagged for priority QA inspection upon arrival due to low supplier rating.' Following this, calculate the total value of the 'Diamond Core Drill Bit' inventory currently available using the unit cost at the shipment's destination warehouse. Return only the final calculated dollar amount.'m concerned about the performance of 'Johannesburg Mining Equipment'. First, please retrieve their supplier details to verify if their performance rating is less than 4.5. Then, find any of their inbound shipments that are currently 'In Transit' and update the shipment's notes to add: 'Flagged for priority QA inspection upon arrival due to low supplier rating.' After flagging the shipment, I need you to calculate the total value of the 'Diamond Core Drill Bit' inventory currently on hand using the unit cost at that shipment's destination warehouse. Please return only the final calculated dollar amount.",
        actions=[
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Johannesburg Mining Equipment",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1011",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1011",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0011",
                    "new_note": "Flagged for priority QA inspection upon arrival due to low supplier rating.",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Diamond Core Drill Bit",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Denver Heavy Equipment Yard",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 33
    Task(
        annotator="0",
        user_id="U33",
        instruction="In your role as the warehouse manager at the San Francisco Fresh Foods DC, today, on June 23, 2024, a cycle count for 'Fresh Cut Roses' showed a physical inventory count of 2800 bouquets. Adjust the inventory in the system, stating the reason as 'Cycle count discrepancy'. This adjustment results in critically low stock, necessitating the immediate initiation of an emergency replenishment order from our preferred supplier, 'Bogota Floral Exports', to restore our on-hand quantity to 5000 units. Given the high perishability, choose the top-rated 'Air' carrier providing 'Perishables' service level with a temperature control of 4 degrees Celsius. Once the purchase order is created and the inventory pipeline updated, reply with the new PO number and the carrier's name.'Fresh Cut Roses' revealed a physical count of 2800 bouquets. Please perform an inventory adjustment in the system, noting the reason as 'Cycle count discrepancy'. After the adjustment, this leaves us with critically low stock. Please immediately initiate an emergency replenishment order from our preferred supplier, 'Bogota Floral Exports', to bring our on-hand quantity up to a target level of 5000 units. This is a highly perishable item, so you must select the highest-rated 'Air' carrier that offers a 'Perishables' service level and a temperature control of 4 degrees Celsius. Once the purchase order is created and the inventory pipeline is updated, respond with the new PO number and the name of the carrier you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Fresh Cut Roses",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "San Francisco Fresh Foods DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={"sku": "FOOD-FLWR-X24", "warehouse_id": "WH-10"},
            ),
            Action(
                name="PerformInventoryAdjustment",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                    "new_physical_count": 2800,
                    "current_date": "2024-06-23",
                    "reason_note": "Cycle count discrepancy",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bogota Floral Exports",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1029",
                    "current_date": "2024-06-23",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Perishables",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1029",
                    "supplier_name": "Bogota Floral Exports",
                    "destination_warehouse_id": "WH-10",
                    "destination_warehouse_name": "San Francisco Fresh Foods DC",
                    "order_quantity": 2200,
                    "unit_cost": 12.0,
                    "unit_weight": 0.5,
                    "expected_arrival_date": "2024-06-25",
                    "carrier_name": "Desert Falcon Cargo",
                    "mode_of_transport": "Air",
                    "temperature_control_required": True,
                    "temperature_celsius": 4,
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                    "quantity_to_add": 2200,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 34
    Task(
        annotator="0",
        user_id="U34",
        instruction="As a senior logistics coordinator, today, June 24, 2024, we have a time-sensitive order from Alpha Electronics LLC for 50 drums of 'Industrial Solvent'. Their default fulfillment center is the West Coast Distribution Hub, but initially, verify if it is stocked there. If absent, find an alternative warehouse with adequate stock. Since this is a hazardous material, confirm the alternate warehouse's certification for Hazmat Class 3 products before proceeding. Once a suitable warehouse is confirmed, choose the highest-rated carrier for 'Truck' transport offering 'LTL' service. Create the outbound order using sales order number SO-2024-0020 and allocate the inventory appropriately. Please reply with the new Order ID and the name of the warehouse used for fulfillment.'Industrial Solvent'. Their default fulfillment site is the West Coast Distribution Hub, but I need you to first confirm if they even stock it. If not, find an alternative warehouse that has sufficient available stock. Because this is a hazardous material, you MUST verify that the alternative warehouse is certified to handle Hazmat Class 3 products before proceeding. Once you've confirmed a suitable warehouse, select the highest-rated carrier for 'Truck' transport offering 'LTL' service. Finally, create the outbound order using sales order number SO-2024-0020 and allocate the inventory from the correct warehouse. Please respond with the new Order ID and the name of the warehouse you fulfilled the order from.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Industrial Solvent",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={"warehouse_name": "West Coast Distribution Hub"},
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-13",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0020",
                    "customer_name": "Alpha Electronics LLC",
                    "destination_city": "Cleveland",
                    "destination_country": "United States",
                    "warehouse_id": "WH-13",
                    "carrier_name": "Sakura Express",
                    "carrier_scac": "SKEX",
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
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "quantity_to_allocate": 50,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 35
    Task(
        annotator="0",
        user_id="U35",
        instruction="In your capacity as a logistics expansion manager, today is June 25, 2024, and we are broadening our furniture line, requiring stocking of the 'Teak Wood Dining Chair' at our Phoenix Renewable Warehouse. Begin the full setup process by confirming there's no existing inventory record for this item at this warehouse. If absent, establish a new one, and proceed with placing an initial stocking order for 150 chairs from 'Bangkok Furniture Co.'. For this international shipment, select the top-rated 'Sea' transport carrier. After creating the purchase order, ensure the new inventory record's pipeline is updated. Confirm completion by providing the new Purchase Order number and the Inventory ID created.'Teak Wood Dining Chair' at our Phoenix Renewable Warehouse. Please execute the full setup process. First, verify that no inventory record for this product exists at this warehouse. If none exists, create a new one. Then, place an initial stocking order for 150 chairs from our supplier, 'Bangkok Furniture Co.'. For this international shipment, please select the best-rated carrier for 'Sea' transport. After creating the purchase order, ensure the inventory pipeline for the new record is updated. To confirm completion, please respond with the new Purchase Order number and the new Inventory ID you created.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                },
            ),
            Action(
                name="CreateInventoryRecord",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "current_date": "2024-06-25",
                },
            ),
            Action(
                name="FindCarrierByMethodOfTransport",
                kwargs={
                    "method_of_transport": "Sea",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1015",
                    "supplier_name": "Bangkok Furniture Co.",
                    "destination_warehouse_id": "WH-09",
                    "destination_warehouse_name": "Phoenix Renewable Warehouse",
                    "order_quantity": 150,
                    "unit_cost": 120.0,
                    "unit_weight": 8.0,
                    "expected_arrival_date": "2024-07-30",
                    "carrier_name": "Sakura Express",
                    "mode_of_transport": "Sea",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-09",
                    "quantity_to_add": 150,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 36
    Task(
        annotator="0",
        user_id="U36",
        instruction="As a logistics coordinator, manage an urgent diversion request from our customer, 'Gamma Construction Ltd.', for order SO-2024-0003. Alter the destination to '555 Industrial Way, Salt Lake City, United States'. Begin by identifying the order, then seek out the most economical carrier for the 'LCL' service level and 'Truck' transport mode to cover the new route. Amend the order with the updated destination, include the new carrier's information, adjust its status to 'Diverted', and annotate with: 'Diverted to Salt Lake City per customer request. Carrier re-evaluated for new route.' Once the diversion is processed, compute the overall value of all other shipments presently 'In Transit' to the original fulfillment warehouse of the order. Disregard currency variations for this computation and provide just the final total.'Gamma Construction Ltd.', has requested an urgent diversion for their order SO-2024-0003. The new destination is '555 Industrial Way, Salt Lake City, United States'. Please process this change. First, find the order. Then, find the cheapest carrier for its 'LCL' service level and 'Truck' mode of transport to handle the new route. Update the order with the new destination, the new carrier's details, change its status to 'Diverted', and add a note: 'Diverted to Salt Lake City per customer request. Carrier re-evaluated for new route.' After processing the diversion, I need you to calculate the total value of all other shipments currently 'In Transit' to the order's *original* fulfillment warehouse. Please ignore currency differences for this calculation and return only the final sum.",
        actions=[
            Action(
                name="FindOutboundOrderBySo",
                kwargs={
                    "sales_order_number": "SO-2024-0003",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LCL",
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0003",
                    "destination_address": "555 Industrial Way",
                    "destination_city": "Salt Lake City",
                    "destination_country": "United States",
                    "status": "Diverted",
                    "carrier_name": "NorthStar Shipping",
                    "carrier_scac": "NSTS",
                    "notes": "Diverted to Salt Lake City per customer request. Carrier re-evaluated for new route.",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Fort Lauderdale Building Materials",
                },
            ),
            Action(
                name="FindInboundShipmentsByWarehouse",
                kwargs={
                    "warehouse_id": "WH-12",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 37
    Task(
        annotator="0",
        user_id="U37",
        instruction="As a quality assurance manager, address a critical quality alert concerning EAC number 'LOT202405A' of the '8-bit Microcontroller', sourced from 'Global Components Inc.'. Your primary task is to identify the specific inventory record for this EAC and change its status to 'Quarantined'. Subsequently, as a preventative measure, locate any shipments from the same supplier that are now 'In Transit' and add a note: 'Contains product from a EAC number under quality review. Inspect upon arrival.' Please provide the ID of the inventory record you quarantined and the ID of the shipment you flagged.'LOT202405A' of the '8-bit Microcontroller', which originated from the supplier 'Global Components Inc.'. Your first priority is to locate the specific inventory record for this EAC and update its status to 'Quarantined'. After that, as a precaution, find any shipments from this same supplier that are currently 'In Transit' and add a note to them stating: 'Contains product from a EAC number under quality review. Inspect upon arrival.' Please respond with the ID of the inventory record you quarantined and the ID of the shipment you flagged.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0001",
                    "new_status": "Quarantined",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1001",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "new_note": "Contains product from a EAC number under quality review. Inspect upon arrival.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 38
    Task(
        annotator="0",
        user_id="U38",
        instruction="As a senior logistics analyst, on this day, June 26, 2024, address an escalated issue regarding a delayed order, SO-2024-0002, for 'Beta Retail GmbH'. To avert running out of critical items at that warehouse, initiate a new purchase order for 2000 units of the 'Smartphone Model X' from our preferred supplier, 'Osaka Electronics Ltd.'. Utilize the best-rated 'Air' carrier for shipping.'Beta Retail GmbH'. To prevent a stock-out of other critical items at that warehouse, create a new purchase order for 2000 units of the 'Smartphone Model X' from our preferred supplier, 'Osaka Electronics Ltd.'. Ship it using the best-rated 'Air' carrier.",
        actions=[
            Action(
                name="FindOutboundOrderBySo",
                kwargs={
                    "sales_order_number": "SO-2024-0002",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Smartphone Model X",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Osaka Electronics Ltd.",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "current_date": "2024-06-26",
                },
            ),
            Action(
                name="FindCarrierByMethodOfTransport",
                kwargs={
                    "method_of_transport": "Air",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1002",
                    "supplier_name": "Osaka Electronics Ltd.",
                    "destination_warehouse_id": "WH-02",
                    "destination_warehouse_name": "Northwest Fulfillment Center",
                    "order_quantity": 2000,
                    "unit_cost": 650.0,
                    "unit_weight": 0.4,
                    "expected_arrival_date": "2024-07-11",
                    "carrier_name": "Desert Falcon Cargo",
                    "mode_of_transport": "Air",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "quantity_to_add": 2000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 39
    Task(
        annotator="0",
        user_id="U39",
        instruction="In the role of a fulfillment coordinator, manage a new sales order, SO-2024-0051, for our customer 'Beta Retail GmbH' involving 80 units of 'Teak Wood Dining Chair'. Fulfill this order from the 'Dallas Home Goods DC'. Opt for the highest-rated carrier providing 'LCL' service via 'Truck'. After setting up the outbound order, ensure the allocated inventory is updated. Confirm with the new Order ID.'Beta Retail GmbH' for 80 'Teak Wood Dining Chair' units. This order should be fulfilled from the 'Dallas Home Goods DC'. Please select the highest-rated carrier that offers 'LCL' service via 'Truck'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LCL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0051",
                    "customer_name": "Beta Retail GmbH",
                    "warehouse_id": "WH-14",
                    "carrier_name": "NorthStar Shipping",
                    "carrier_scac": "NSTS",
                    "order_date": "2024-11-11",
                    "total_units": 80,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_allocate": 80,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 40
    Task(
        annotator="0",
        user_id="U40",
        instruction="As an inventory planner, on June 27, 2024, determine that 'Ceramic Floor Tile' stock at the Fort Lauderdale Building Materials warehouse is nearing its reorder point. Arrange a replenishment order with 'Madrid Ceramic Tiles' to increase 'quantity_available' to 20,000 units. Select the most cost-effective carrier offering 'FCL' service via 'Sea' for the shipment. Upon creating the purchase order and updating the inventory pipeline, reply with the new PO number.'m reviewing our stock levels and see that the 'Ceramic Floor Tile' at the Fort Lauderdale Building Materials warehouse is approaching its reorder point. Place a replenishment order from our supplier, 'Madrid Ceramic Tiles', for a quantity sufficient to bring our 'quantity_available' up to 20,000 units. Find the cheapest carrier that offers 'FCL' service via 'Sea' for this shipment. After creating the purchase order and updating the inventory pipeline, please respond with the new PO number.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Ceramic Floor Tile",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Fort Lauderdale Building Materials",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Madrid Ceramic Tiles",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1012",
                    "current_date": "2024-06-27",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Sea",
                    "service_level": "FCL",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1012",
                    "supplier_name": "Madrid Ceramic Tiles",
                    "destination_warehouse_id": "WH-12",
                    "destination_warehouse_name": "Fort Lauderdale Building Materials",
                    "order_quantity": 5000,
                    "unit_cost": 3.5,
                    "unit_weight": 5.0,
                    "expected_arrival_date": "2024-07-22",
                    "carrier_name": "Ocean Bridge",
                    "carrier_scac": "OCBR",
                    "mode_of_transport": "Sea",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                    "quantity_to_add": 5000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 41
    Task(
        annotator="0",
        user_id="U41",
        instruction="As a supply chain risk manager, it is essential today, June 29, 2024, to evaluate the risks linked with our primary Chinese suppliers: 'Global Components Inc.', 'Beijing Solar Tech', and 'Shanghai Electronics Co.'. Check the performance rating for each supplier. Should any supplier hold a rating under 4.7, locate all their inbound shipments currently marked 'In Transit' and append a note to each: 'Flagged for priority QA inspection due to supplier performance review.' Finally, supply a list of the shipment IDs you have modified.'Global Components Inc.', 'Beijing Solar Tech', and 'Shanghai Electronics Co.'. For each of these suppliers, please check their performance rating. If a supplier's rating is below 4.7, find all of their inbound shipments that are currently 'In Transit' and add a note to each of those shipments: 'Flagged for priority QA inspection due to supplier performance review.' As a final answer, please provide a list of the shipment IDs you updated.",
        actions=[
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Beijing Solar Tech",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Shanghai Electronics Co.",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1001",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1009",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1025",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1001",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1009",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1025",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "new_note": "Flagged for priority QA inspection due to supplier performance review.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0009",
                    "new_note": "Flagged for priority QA inspection due to supplier performance review.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0025",
                    "new_note": "Flagged for priority QA inspection due to supplier performance review.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 42
    Task(
        annotator="0",
        user_id="U42",
        instruction="Acting as an inventory manager on July 1, 2024, it is necessary to perform a shelf-life audit on several key products. Inspect the inventory for 'Organic Arabica Coffee Beans', 'Influenza Vaccine', and 'Frozen Tuna Loin'. For each product, assess their inventory records across all warehouses. If an inventory EAC's expiration date falls before June 30, 2025, change its stock status to 'FEFO Audit Required'. Please reply with a compilation of the Inventory IDs that were updated.'Organic Arabica Coffee Beans', 'Influenza Vaccine', and 'Frozen Tuna Loin'. For each of these products, find their inventory records across all warehouses. If any specific inventory EAC has an expiration date before June 30, 2025, please update its stock status to 'FEFO Audit Required'. Please respond with a list of the Inventory IDs that you updated.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Organic Arabica Coffee Beans",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Influenza Vaccine",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Frozen Tuna Loin",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0003",
                    "new_status": "FEFO Audit Required",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0008",
                    "new_status": "FEFO Audit Required",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 43
    Task(
        annotator="0",
        user_id="U43",
        instruction="In your role as a compliance manager today, July 5, 2024, participate in our quarterly audit by confirming that all 'Preferred' suppliers hold 'ISO 9001' certification. Review each preferred partner including: 'Osaka Electronics Ltd.', 'Rio Grande Coffee Traders', 'Melbourne Seafood Exporters', 'Helsinki Chemicals Oy', 'Osaka Robotics Corp.', 'Krakow IT Components', and 'Bogota Floral Exports'. Should any supplier lack the ISO 9001 certification, search for all their inbound shipments in 'Planned' status and notate each with: 'Hold for Supplier Compliance Verification.' Provide a list of the Shipment IDs that have been updated.'Preferred' suppliers are 'ISO 9001' certified. Please review each of our preferred partners: 'Osaka Electronics Ltd.', 'Rio Grande Coffee Traders', 'Melbourne Seafood Exporters', 'Helsinki Chemicals Oy', 'Osaka Robotics Corp.', 'Krakow IT Components', and 'Bogota Floral Exports'. For any of these suppliers that are NOT ISO 9001 certified, find all of their inbound shipments that are currently in 'Planned' status and add a note to each one: 'Hold for Supplier Compliance Verification.' Please respond with a list of the Shipment IDs you updated.",
        actions=[
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Osaka Electronics Ltd.",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Rio Grande Coffee Traders",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Melbourne Seafood Exporters",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Helsinki Chemicals Oy",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Osaka Robotics Corp.",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Krakow IT Components",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bogota Floral Exports",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1029",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1019",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1016",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1013",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1010",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1005",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1002",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1010",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1029",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1005",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0010",
                    "new_note": "Hold for Supplier Compliance Verification.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0029",
                    "new_note": "Hold for Supplier Compliance Verification.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 44
    Task(
        annotator="0",
        user_id="U44",
        instruction="Functioning as a regional logistics manager on July 3, 2024, examine the potential for congestion in our facilities. Detect warehouses where utilization exceeds 90%. For those warehouses, locate all inbound shipments still in 'Planned' status and adjust their notes to read: 'High utilization warning. Confirm dock availability before arrival.' List the shipment IDs you have updated in your response.'m concerned about potential congestion at our facilities. Please identify all warehouses where the current utilization is over 90%. For each of those warehouses, find all inbound shipments that are still in 'Planned' status and update their notes to say: 'High utilization warning. Confirm dock availability before arrival.' Please respond with a list of the shipment IDs that you have updated.",
        actions=[
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-02",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="FindInboundShipmentsByWarehouse",
                kwargs={
                    "warehouse_id": "WH-02",
                },
            ),
            Action(
                name="FindInboundShipmentsByWarehouse",
                kwargs={
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0010",
                    "new_note": "High utilization warning. Confirm dock availability before arrival.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0027",
                    "new_note": "High utilization warning. Confirm dock availability before arrival.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0029",
                    "new_note": "High utilization warning. Confirm dock availability before arrival.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 45
    Task(
        annotator="0",
        user_id="U45",
        instruction="In the capacity of a purchasing agent, today being July 10, 2024, initiate a new purchase order for 100 units of the 'Ceramic Brake Pad Set' from 'Bavaria Parts GmbH'. Arrange for the delivery to the 'Midwest Parts Warehouse', setting the expected arrival for July 25, 2024. After order creation, provide the newly assigned Purchase Order number in your reply.'Ceramic Brake Pad Set' from our supplier 'Bavaria Parts GmbH'. The shipment should be delivered to the 'Midwest Parts Warehouse'. Please set the expected arrival date to July 25, 2024. After creating the order, respond with the new Purchase Order number.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Ceramic Brake Pad Set",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bavaria Parts GmbH",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={"sku": "AUTO-PAD-B2", "warehouse_id": "WH-03"},
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1003",
                    "supplier_name": "Bavaria Parts GmbH",
                    "destination_warehouse_id": "WH-03",
                    "destination_warehouse_name": "Midwest Parts Warehouse",
                    "order_quantity": 100,
                    "unit_cost": 45.00,
                    "unit_weight": 2.5,
                    "expected_arrival_date": "2024-07-25",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "quantity_to_add": 100,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 46
    Task(
        annotator="0",
        user_id="U46",
        instruction="As a fulfillment coordinator for today, July 11, 2024, handle the creation of a new outbound order for our client, 'Epsilon Fashion Co.', based in Toronto, Maple Nation. This involves arranging for 250 units of the 'Organic Cotton T-Shirt' to be fulfilled from the 'East Coast Fashion Center' and dispatched via 'SwiftDelivery' utilizing their 'Ground' service. The sales order reference is SO-2024-0022. Once you've established the new Order ID, please send a response with it.'Epsilon Fashion Co.', located in Toronto, Maple Nation, for 250 units of the 'Organic Cotton T-Shirt'. This order should be fulfilled from the 'East Coast Fashion Center' and shipped via 'SwiftDelivery' using their 'Ground' service. The sales order number is SO-2024-0022. Please respond with the new Order ID once it has been created.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Organic Cotton T-Shirt",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "East Coast Fashion Center",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "SwiftDelivery",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0022",
                    "customer_name": "Epsilon Fashion Co.",
                    "destination_city": "Toronto",
                    "destination_country": "Maple Nation",
                    "warehouse_id": "WH-04",
                    "carrier_name": "SwiftDelivery",
                    "carrier_scac": "SWDL",
                    "mode_of_transport": "Truck",
                    "shipping_service_level": "Ground",
                    "order_date": "2024-07-11",
                    "total_units": 250,
                    "total_weight_kg": 50.0,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                    "quantity_to_allocate": 250,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 47
    Task(
        annotator="0",
        user_id="U47",
        instruction="Serving as a financial controller today, July 12, 2024, it is your task to comply with our new internal control policy by auditing our high-value technology inventory. Carefully inspect the stocks for both the 'Smartphone Model X' and the 'Articulated Robotic Arm' in all storage locations. For any inventory point where the combined on-hand value surpasses $250,000, update the inventory record's stock status to 'Cycle Count Pending'. Afterwards, provide a list of the Inventory IDs that you've revised.'Smartphone Model X' and the 'Articulated Robotic Arm' across all warehouses. For each specific inventory location where the total on-hand value of either product exceeds $250,000, please update that inventory record's stock status to 'Cycle Count Pending'. Respond with a list of the Inventory IDs you have updated.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Smartphone Model X",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0023",
                    "new_status": "Cycle Count Pending",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0014",
                    "new_status": "Cycle Count Pending",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 48
    Task(
        annotator="0",
        user_id="U48",
        instruction="Act in your role as a logistics planner today, July 15, 2024, to gear up our cold chain facilities for the forthcoming peak period. Determine all warehouses categorized under 'Cold Storage'. Focus on those with the 'Pharmaceutical Handling' speciality, examine their incoming shipments, and append a note to any shipment marked as 'Planned' or 'In Transit'. The note should state: 'Action Required: Pre-allocate temperature-controlled dock for arrival.' After completing this, respond with a list of the updated Shipment IDs.'Cold Storage' type. For each of these warehouses, select the ones that have as a special capability: 'Pharmaceutical Handling', review their inbound shipments and add a note to any 'Planned' or 'In Transit' shipment. The note should read: 'Action Required: Pre-allocate temperature-controlled dock for arrival.' Please respond with a list of the Shipment IDs that you have updated.",
        actions=[
            Action(
                name="GetAllWarehouses",
                kwargs={
                    "filters": {"warehouse_type": "Cold Storage"},
                },
            ),
            Action(
                name="FindInboundShipmentsByWarehouse",
                kwargs={
                    "warehouse_id": "WH-16",
                },
            ),
            Action(
                name="FindInboundShipmentsByWarehouse",
                kwargs={
                    "warehouse_id": "WH-06",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0006",
                    "new_note": "Action Required: Pre-allocate temperature-controlled dock for arrival.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0021",
                    "new_note": "Action Required: Pre-allocate temperature-controlled dock for arrival.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 49
    Task(
        annotator="0",
        user_id="U49",
        instruction="As a fulfillment coordinator today, July 17, 2024, your duty is to organize a new outbound order for 'Zeta Tech Solutions' in Yokohama, Nippon, involving 20 'Solar Panel 450W' units. This order, under sales order SO-2024-0023, is to be dispatched from the 'Phoenix Renewable Warehouse', utilizing 'SwiftDelivery' with their 'Freight' air service. After making the order, ensure the inventory is allocated. Confirm execution by replying with the new Order ID.'Zeta Tech Solutions', located on Yokohama, Nippon, for 20 'Solar Panel 450W' units. This order, with sales order number SO-2024-0023, will be fulfilled from the 'Phoenix Renewable Warehouse'. Please use 'SwiftDelivery' with their 'Freight' service level via air for this shipment. After creating the order, make sure to allocate the inventory. Respond with the new Order ID to confirm creation.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Solar Panel 450W",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "SwiftDelivery",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0023",
                    "customer_name": "Zeta Tech Solutions",
                    "destination_city": "Yokohama",
                    "destination_country": "Nippon",
                    "warehouse_id": "WH-09",
                    "carrier_name": "SwiftDelivery",
                    "carrier_scac": "SWDL",
                    "mode_of_transport": "Air",
                    "shipping_service_level": "Freight",
                    "order_date": "2024-07-17",
                    "total_units": 20,
                    "total_weight_kg": 440.0,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "quantity_to_allocate": 20,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 50
    Task(
        annotator="0",
        user_id="U50",
        instruction="Today, as a purchasing agent on July 18, 2024, proceed with creating a purchase order for 50 'Industrial Paper Roll' units from the supplier 'Toronto Paper Mills'. Arrange for this shipment to arrive at the 'Detroit Packaging Supplies' warehouse by August 1, 2024. After order creation, update the inventory pipeline accordingly. Validate completion by responding with the new Purchase Order number.'Industrial Paper Roll' units from our supplier, 'Toronto Paper Mills'. This shipment needs to be delivered to the 'Detroit Packaging Supplies' warehouse, and the required arrival date is August 1, 2024. After creating the purchase order, please ensure the inventory pipeline is updated. Respond with the new Purchase Order number to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Industrial Paper Roll",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Toronto Paper Mills",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Detroit Packaging Supplies",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={"sku": "MANU-PAPR-F6", "warehouse_id": "WH-08"},
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "MANU-PAPR-F6",
                    "warehouse_id": "WH-08",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 51
    Task(
        annotator="0",
        user_id="U51",
        instruction="As a warehouse manager, today's date is July 19, 2024. We've encountered a spoilage event at the Gulf Coast Food Storage involving our 'Extra Virgin Olive Oil'. The new physical count stands at 145 units. Please handle an inventory adjustment to reflect this, with the reason stated as 'Spoilage due to container damage'. Following the adjustment, verify if the new stock level is below the reorder point. If so, coordinate a replenishment purchase order for 800 units from the supplier 'Athens Olive Oil Co.'. Assign this shipment to the carrier 'Mediterranean Lines' for sea transport. After creating the PO and updating the inventory pipeline, provide the Inventory ID of the adjusted record and the new Purchase Order number.'ve had a spoilage event in the Gulf Coast Food Storage involving our 'Extra Virgin Olive Oil'. The new physical count is 145 units. Please perform an inventory adjustment to reflect this, with the reason 'Spoilage due to container damage'. After the adjustment, check if the new stock level is below the reorder point. If it is, create a replenishment purchase order for 800 units from the supplier 'Athens Olive Oil Co.'. Please assign this shipment to the carrier 'Mediterranean Lines' and ship it through sea. After creating the PO and updating the inventory pipeline, respond with the Inventory ID of the adjusted record and the new Purchase Order number.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Extra Virgin Olive Oil",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Gulf Coast Food Storage",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FOOD-OLIV-V22",
                    "warehouse_id": "WH-05",
                },
            ),
            Action(
                name="PerformInventoryAdjustment",
                kwargs={
                    "sku": "FOOD-OLIV-V22",
                    "warehouse_id": "WH-05",
                    "new_physical_count": 145,
                    "current_date": "2024-07-19",
                    "reason_note": "Spoilage due to container damage",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Athens Olive Oil Co.",
                },
            ),
            Action(
                name="CalculateExpectedArrivalDate",
                kwargs={
                    "supplier_id": "SUP-1024",
                    "current_date": "2024-07-19",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Mediterranean Lines",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1024",
                    "supplier_name": "Athens Olive Oil Co.",
                    "destination_warehouse_id": "WH-05",
                    "destination_warehouse_name": "Gulf Coast Food Storage",
                    "order_quantity": 800,
                    "unit_cost": 40.0,
                    "unit_weight": 4.8,
                    "expected_arrival_date": "2024-08-13",
                    "carrier_name": "Mediterranean Lines",
                    "carrier_scac": "MEDL",
                    "mode_of_transport": "Sea",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FOOD-OLIV-V22",
                    "warehouse_id": "WH-05",
                    "quantity_to_add": 800,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 52
    Task(
        annotator="0",
        user_id="U52",
        instruction="As a purchasing agent, today's date is July 23, 2024. Please handle the creation of a standard replenishment purchase order for 250 units of the 'Automotive Windshield'. This order should be placed with our supplier, 'Mexico City Auto Glass', and is intended for the 'Midwest Parts Warehouse'. Use the supplier's standard lead time to estimate the expected arrival date. Ensure you extract the correct unit cost from the inventory record before you create the PO. After the inbound shipment is created, update the inventory pipeline accordingly.'Automotive Windshield'. This order should be placed with our supplier, 'Mexico City Auto Glass', and is destined for the 'Midwest Parts Warehouse'. You must use the supplier's standard lead time to calculate the expected arrival date. Ensure you retrieve the correct unit cost from the inventory record before creating the PO. After creating the inbound shipment, update the inventory pipeline accordingly.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Automotive Windshield",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Mexico City Auto Glass",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "quantity_to_add": 250,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 53
    Task(
        annotator="0",
        user_id="U53",
        instruction="As a procurement officer, today's date is July 24, 2024. Please commence a purchase order for 5 'Articulated Robotic Arm' units from the supplier 'Osaka Robotics Corp.'. The shipment destination is our 'Midwest Parts Warehouse'. Calculate the expected arrival date by referring to the supplier's standard lead time and utilize the specific unit cost from the Milwaukee inventory record for the PO. Once the inbound shipment is created, update the inventory pipeline.'Articulated Robotic Arm' units from the supplier 'Osaka Robotics Corp.'. The destination for this shipment is our 'Midwest Parts Warehouse'. You need to calculate the expected arrival date using the supplier's standard lead time and use the specific unit cost from the Milwaukee inventory record for the PO. After creating the inbound shipment, please update the inventory pipeline.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Osaka Robotics Corp.",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                    "quantity_to_add": 5,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 54
    Task(
        annotator="0",
        user_id="U54",
        instruction="As a procurement specialist, today's date is July 25, 2024. I require you to initiate a standard purchase order for 20 units of 'Industrial Solvent', a hazmat product, from our supplier, 'Helsinki Chemicals Oy'. The shipment should be directed to our 'Cleveland Chemical Storage' facility. Use the supplier's standard lead time to determine the expected arrival date and apply the unit cost from the inventory record for the PO. Once the inbound shipment is created, ensure the inventory pipeline is updated.'Industrial Solvent', which is a hazmat product, from our supplier, 'Helsinki Chemicals Oy'. The shipment must be delivered to our 'Cleveland Chemical Storage' facility. Please use the supplier's standard lead time to determine the expected arrival date and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Industrial Solvent",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Helsinki Chemicals Oy",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Cleveland Chemical Storage",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "CHEM-SOLV-K11",
                    "warehouse_id": "WH-13",
                    "quantity_to_add": 20,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 55
    Task(
        annotator="0",
        user_id="U55",
        instruction="Acting as a procurement manager, today's date is July 26, 2024. Please execute the placement of a replenishment purchase order for 300 units of 'Argentinian Malbec Wine' from the supplier 'Buenos Aires Wine Producers'. This shipment is intended for our 'San Diego Beverage DC'. Calculate the expected arrival date using the supplier's standard lead time and refer to the unit cost from the inventory record for the PO. After creating the inbound shipment, make sure the inventory pipeline is updated.'Argentinian Malbec Wine' from the supplier 'Buenos Aires Wine Producers'. This shipment is for our 'San Diego Beverage DC'. You must calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Argentinian Malbec Wine",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Buenos Aires Wine Producers",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "San Diego Beverage DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "BEVG-WINE-P16",
                    "warehouse_id": "WH-15",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "BEVG-WINE-P16",
                    "warehouse_id": "WH-15",
                    "quantity_to_add": 300,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 56
    Task(
        annotator="0",
        user_id="U56",
        instruction="Serve as a procurement specialist for luxury goods. Today is July 29, 2024. I need you to initiate a purchase order for 50 'Automatic Watch Movement' units from our supplier, 'Zurich Watch Parts AG'. The delivery target is the 'NYC Luxury Vault'. Please ascertain the expected arrival date using the supplier's standard lead time and apply the unit cost from the inventory record for the PO. Additionally, classify the order with critical priority. Following the creation of the inbound shipment, ensure the inventory pipeline reflects the update.'Automatic Watch Movement' units from our supplier, 'Zurich Watch Parts AG'. The delivery destination is the 'NYC Luxury Vault'. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. Also, mark the order with critical priority. After creating the inbound shipment, ensure the inventory pipeline is updated.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Automatic Watch Movement",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Zurich Watch Parts AG",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "NYC Luxury Vault",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "LUX-WATCH-L12",
                    "warehouse_id": "WH-07",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 57
    Task(
        annotator="0",
        user_id="U57",
        instruction="Act as a procurement manager. Today is July 30, 2024. I need you to initiate a purchase order for 30 'Raw Cotton Bale' units from our supplier, 'Cairo Cotton Co.'. The shipping destination is our 'East Coast Fashion Center'. Please determine the expected arrival date using the supplier's standard lead time and apply the unit cost from the inventory record for the PO. Once the inbound shipment is created, ensure the inventory pipeline reflects the update. Respond with the new Purchase Order number and the calculated expected arrival date.'Raw Cotton Bale' units from our supplier, 'Cairo Cotton Co.'. The destination for this shipment is our 'East Coast Fashion Center'. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Raw Cotton Bale",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Cairo Cotton Co.",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "East Coast Fashion Center",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "MATR-COTT-R18",
                    "warehouse_id": "WH-04",
                    "quantity_to_add": 30,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 58
    Task(
        annotator="0",
        user_id="U58",
        instruction="Take on the role of a procurement specialist. Today is August 1, 2024. I need you to initiate a purchase order for 500 units of 'Organic Arabica Coffee Beans' from our supplier, 'Rio Grande Coffee Traders'. The shipment should be dispatched to our 'Gulf Coast Food Storage' and is a high priority. Please establish the expected arrival date using the supplier's standard lead time and apply the unit cost from the inventory record for the PO. After forming the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.'Organic Arabica Coffee Beans' from our supplier, 'Rio Grande Coffee Traders'. The shipment should be delivered to our 'Gulf Coast Food Storage' and is of high priority. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Organic Arabica Coffee Beans",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Rio Grande Coffee Traders",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Gulf Coast Food Storage",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "quantity_to_add": 500,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 59
    Task(
        annotator="0",
        user_id="U59",
        instruction="Function as a procurement manager. Today is August 2, 2024. Please initiate a purchase order for 10 'Diamond Core Drill Bit' units from our supplier, 'Johannesburg Mining Equipment'. The shipment is intended for the 'Denver Heavy Equipment Yard'. You must ascertain the expected arrival date using the supplier's standard lead time and apply the unit cost from the inventory record for the PO. Add a note to the shipment: 'Fragile. Handle with care.' Once the inbound shipment is formed, ensure the inventory pipeline reflects the update. Respond with the new Purchase Order number and the calculated expected arrival date.'Diamond Core Drill Bit' units from our supplier, 'Johannesburg Mining Equipment'. The shipment is destined for the 'Denver Heavy Equipment Yard'. You must calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. Add a note to the shipment saying 'Fragile. Handle with care.' After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Diamond Core Drill Bit",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Johannesburg Mining Equipment",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Denver Heavy Equipment Yard",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "quantity_to_add": 10,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 60
    Task(
        annotator="0",
        user_id="U60",
        instruction="Operate as a procurement manager. Today is August 5, 2024. Please initiate a purchase order for 100 'Solar Panel 450W' units from our supplier, 'Beijing Solar Tech'. The shipment is scheduled for the 'Phoenix Renewable Warehouse'. You must determine the expected arrival date using the supplier's standard lead time and apply the unit cost from the inventory record for the PO. After the inbound shipment is formed, ensure the inventory pipeline reflects the update. Respond with the new Purchase Order number and the calculated expected arrival date.'Solar Panel 450W' units from our supplier, 'Beijing Solar Tech'. The shipment is destined for the 'Phoenix Renewable Warehouse'. You must calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Solar Panel 450W",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Beijing Solar Tech",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "TECH-SOLR-G7",
                    "warehouse_id": "WH-09",
                    "quantity_to_add": 100,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 61
    Task(
        annotator="0",
        user_id="U61",
        instruction="You are a risk analyst. Today is August 7, 2024. I require you to handle a performance review of carriers dealing with our international shipments. Identify all outbound orders where the destination country differs from the origin country. For each of these orders, examine the assigned carrier's average performance rating. Should the rating fall below 4.8, update the order with a memo: 'Proactive Communication Recommended: Carrier performance rating is below 4.8.' Please return a list of the Order IDs that have been modified.'s average performance rating. If the rating is below 4.8, please update the order with a note: 'Proactive Communication Recommended: Carrier performance rating is below 4.8.' Please respond with a list of the Order IDs that you have updated.",
        actions=[
            Action(
                name="GetAllOutboundOrders",
                kwargs={},
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Express World Delivery",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Global Parcel Service",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "NorthStar Shipping",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Ocean Bridge",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Andean Air Freight",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "DeutschLogistik",
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0006",
                    "notes": "Proactive Communication Recommended: Carrier performance rating is below 4.8.",
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0007",
                    "notes": "Proactive Communication Recommended: Carrier performance rating is below 4.8.",
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0008",
                    "notes": "Proactive Communication Recommended: Carrier performance rating is below 4.8.",
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0009",
                    "notes": "Proactive Communication Recommended: Carrier performance rating is below 4.8.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 62
    Task(
        annotator="0",
        user_id="U62",
        instruction="You are a security auditor. Today is August 8, 2024. I require you to coordinate a security compliance audit on our high-value inventory. Evaluate the storage locations for these products: 'Leather Handbag', 'Diamond Core Drill Bit', 'Articulated Robotic Arm', and 'Oncology Drug A'. For each inventory record of these items, assess the special capabilities of the warehouse. If the warehouse does NOT possess 'High-Value Cage' or 'High Security' as a capability, update the inventory record's status to 'Security Review Pending'. Kindly provide a list of the Inventory IDs that were altered.'Leather Handbag', 'Diamond Core Drill Bit', 'Articulated Robotic Arm', and 'Oncology Drug A'. For each inventory record of these products, check the special capabilities of its warehouse. If the warehouse does NOT have either 'High-Value Cage' or 'High Security' as a capability, you must update that specific inventory record's status to 'Security Review Pending'. Please respond with a list of the Inventory IDs that you have updated.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Leather Handbag",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Diamond Core Drill Bit",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Oncology Drug A",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "APRL-BAG-E5",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "PHRM-DRUG-S19",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-07",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-11",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-06",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0009",
                    "new_status": "Security Review Pending",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0014",
                    "new_status": "Security Review Pending",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0019",
                    "new_status": "Security Review Pending",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 63
    Task(
        annotator="0",
        user_id="U63",
        instruction="You are a procurement manager. Today is August 9, 2024. I require you to execute a lead time audit for our major European suppliers: 'Bavaria Parts GmbH', 'Helsinki Chemicals Oy', 'Paris Luxury Goods', 'Madrid Ceramic Tiles', and 'Ankara Apparel Ltd.'. For each supplier, examine their standard lead time. If it extends beyond 10 days, locate all their 'In Transit' or 'Planned' inbound shipments and append a note to each: 'Extended lead time supplier. Monitor ETA closely.' Please send a list of the Shipment IDs that you have updated.'Bavaria Parts GmbH', 'Helsinki Chemicals Oy', 'Paris Luxury Goods', 'Madrid Ceramic Tiles', and 'Ankara Apparel Ltd.'. For each of these suppliers, check their standard lead time. If it is longer than 10 days, find all of their 'In Transit' or 'Planned' inbound shipments and add a note to each: 'Extended lead time supplier. Monitor ETA closely.' Please respond with a list of the Shipment IDs that you have updated.",
        actions=[
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bavaria Parts GmbH",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Helsinki Chemicals Oy",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Paris Luxury Goods",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Madrid Ceramic Tiles",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Ankara Apparel Ltd.",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1017",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1013",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1012",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0013",
                    "new_note": "Extended lead time supplier. Monitor ETA closely.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0012",
                    "new_note": "Extended lead time supplier. Monitor ETA closely.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 64
    Task(
        annotator="0",
        user_id="U64",
        instruction="You are a procurement manager. Today is August 12, 2024. I require you to organize a purchase order for 80 'Teak Wood Dining Chair' units from our supplier, 'Bangkok Furniture Co.'. The shipment is destined for the 'Dallas Home Goods DC'. Calculate the expected arrival date utilizing the supplier's standard lead time and reference the unit cost from the inventory record for the PO. Attach a note stating 'Standard replenishment of furniture stock.' Once the inbound shipment is created, ensure the inventory pipeline is updated.'Teak Wood Dining Chair' units from our supplier, 'Bangkok Furniture Co.'. The shipment is destined for the 'Dallas Home Goods DC'. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. Add a note stating 'Standard replenishment of furniture stock.' After creating the inbound shipment, ensure the inventory pipeline is updated.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_add": 80,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 65
    Task(
        annotator="0",
        user_id="U65",
        instruction="You are a procurement specialist. Today is August 13, 2024. I require you to arrange a replenishment purchase order for 100 'Frozen Tuna Loin' units from our supplier, 'Melbourne Seafood Exporters'. The shipment is destined for the 'San Francisco Fresh Foods DC'. Calculate the expected arrival date based on the supplier's standard lead time and apply the unit cost from the inventory record for the PO. After forming the inbound shipment, verify that the inventory pipeline is updated. Respond with the new Purchase Order number and the computed expected arrival date.'Frozen Tuna Loin' units from our supplier, 'Melbourne Seafood Exporters'. The shipment is destined for the 'San Francisco Fresh Foods DC'. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Frozen Tuna Loin",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Melbourne Seafood Exporters",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "San Francisco Fresh Foods DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                    "quantity_to_add": 100,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 66
    Task(
        annotator="0",
        user_id="U66",
        instruction="As a pharmaceutical procurement specialist, today is August 14, 2024. I require you to handle a replenishment purchase order for 2000 units of 'Influenza Vaccine' from 'Mumbai Pharma Supplies'. The products are to be shipped to the 'Charlotte Cold Chain Center'. Determine the expected arrival date by referring to the supplier's standard lead time and apply the unit cost as per the inventory record for the PO. Take special note that this shipment is critical. Upon creating the inbound shipment, ensure that the inventory pipeline is revised accordingly. Provide the new Purchase Order number along with the calculated expected arrival date.'Influenza Vaccine' from our supplier, 'Mumbai Pharma Supplies'. The shipment is destined for the 'Charlotte Cold Chain Center'. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. Be wary that this is a critical shipment. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Influenza Vaccine",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Mumbai Pharma Supplies",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Charlotte Cold Chain Center",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "quantity_to_add": 2000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 67
    Task(
        annotator="0",
        user_id="U67",
        instruction="As a procurement manager, today is August 15, 2024. I need you to coordinate a replenishment purchase order for 3000 units of 'Ceramic Floor Tile' from 'Madrid Ceramic Tiles'. The shipment is intended for the 'Fort Lauderdale Building Materials' warehouse. Calculate the expected arrival date using the supplier's standard lead time and reference the unit cost from the inventory record for the PO. After setting up the inbound shipment, ensure the inventory pipeline reflects the update. Return with the new Purchase Order number and the calculated expected arrival date.'Ceramic Floor Tile' from our supplier, 'Madrid Ceramic Tiles'. The shipment is destined for the 'Fort Lauderdale Building Materials' warehouse. Please calculate the expected arrival date using the supplier's standard lead time and use the unit cost from the inventory record for the PO. After creating the inbound shipment, ensure the inventory pipeline is updated. Respond with the new Purchase Order number and the calculated expected arrival date.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Ceramic Floor Tile",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Madrid Ceramic Tiles",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Fort Lauderdale Building Materials",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                    "quantity_to_add": 3000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 68
    Task(
        annotator="0",
        user_id="U68",
        instruction="As a fulfillment specialist, today is August 16, 2024. Process sales order SO-2024-0024 for 'Alpha Electronics LLC' for 2500 '8-bit Microcontroller' units from the 'West Coast Distribution Hub'. The customer has expressly requested 'Global Parcel Service' for this shipment. Verify sufficient stock availability, then handle the creation of the outbound order and allocate the inventory. Confirm by responding with the new Order ID.'Alpha Electronics LLC'. The order is for 2500 '8-bit Microcontroller' units to be fulfilled from the 'West Coast Distribution Hub'. The customer has specifically requested we use 'Global Parcel Service' for this shipment. Please verify that we have sufficient available stock, then create the outbound order and allocate the inventory. Respond with the new Order ID to confirm.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "West Coast Distribution Hub",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Global Parcel Service",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0024",
                    "customer_name": "Alpha Electronics LLC",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "GPLS",
                    "order_date": "2024-08-16",
                    "total_units": 2500,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 2500,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 69
    Task(
        annotator="0",
        user_id="U69",
        instruction="As a fulfillment specialist, today is August 19, 2024. 'Iota Automotive NAC' has a request for 50 'Ceramic Brake Pad Set' units, requiring products from EAC number 'LOT202403B'. Locate the warehouse that holds this specific EAC to fulfill the order. Use 'DeutschLogistik' as the shipping carrier. Set up the outbound order with sales order number SO-2024-0026, allocate the inventory accordingly, and add a note to the new order confirming 'Fulfilled using EAC LOT202403B as per customer request.' Respond with the new Order ID.'Iota Automotive NAC', for an order of 50 'Ceramic Brake Pad Set' units. They require that the products come specifically from EAC number 'LOT202403B'. Please locate the warehouse that holds this specific EAC and fulfill the order from there. Use 'DeutschLogistik' as the carrier. Create the outbound order with sales order number SO-2024-0026, allocate the inventory, and then add a note to the newly created order confirming 'Fulfilled using EAC LOT202403B as per customer request.' Please respond with the new Order ID.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Ceramic Brake Pad Set",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "DeutschLogistik",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0026",
                    "customer_name": "Iota Automotive NAC",
                    "warehouse_id": "WH-03",
                    "carrier_name": "DeutschLogistik",
                    "carrier_scac": "DLOG",
                    "order_date": "2024-08-19",
                    "total_units": 50,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 50,
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0017",
                    "notes": "Fulfilled using EAC LOT202403B as per customer request.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 70
    Task(
        annotator="0",
        user_id="U70",
        instruction="As a fulfillment specialist, today is August 20, 2024. For a new sales order, SO-2024-0027, from 'Zeta Tech Solutions' for 5,000 '8-bit Microcontroller' units, you need to identify the warehouse with the largest available stock of this product for fulfillment. The customer requires 'Sakura Express' as the carrier. Once the order is created and the inventory allocated, respond with the new Order ID and the selected warehouse's name used for fulfillment.'Zeta Tech Solutions' for 5,000 '8-bit Microcontroller' units. This product is stocked in multiple locations. Please identify the warehouse with the highest available quantity for this product and fulfill the order from there. The customer has requested 'Sakura Express' as the carrier. After creating the order and allocating the inventory, please respond with the new Order ID and the name of the warehouse you selected for fulfillment.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Sakura Express",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0027",
                    "customer_name": "Zeta Tech Solutions",
                    "warehouse_id": "WH-01",
                    "carrier_name": "Sakura Express",
                    "carrier_scac": "SKEX",
                    "order_date": "2024-08-20",
                    "total_units": 5000,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 5000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 71
    Task(
        annotator="0",
        user_id="U71",
        instruction="Handle sales order SO-2024-0028 for our customer, 'Epsilon Fashion Co.', as a fulfillment specialist. The current date is August 21, 2024, and the task involves fulfilling 1500 'Organic Cotton T-Shirt' units from the 'East Coast Fashion Center'. To ensure cost efficiency, seek out the most inexpensive carrier that provides 'LCL' service via 'Truck'. Once the carrier is chosen, proceed to create the outbound order and allocate the inventory accordingly. Please reply with the new Order ID along with the name of the selected economical carrier.'Epsilon Fashion Co.'. The order is for 1500 'Organic Cotton T-Shirt' units to be fulfilled from the 'East Coast Fashion Center'. To minimize costs, please find the cheapest available carrier that offers 'LCL' service via 'Truck'. After selecting the carrier, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the economical carrier you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Organic Cotton T-Shirt",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "East Coast Fashion Center",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LCL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0028",
                    "customer_name": "Epsilon Fashion Co.",
                    "warehouse_id": "WH-04",
                    "carrier_scac": "NSTS",
                    "order_date": "2024-08-21",
                    "total_units": 1500,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                    "quantity_to_allocate": 1500,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 72
    Task(
        annotator="0",
        user_id="U72",
        instruction="Coordinate the processing of a large order, SO-2024-0029, from 'Iota Automotive NAC' for 20 'Automotive Windshield' units on August 22, 2024, as a fulfillment specialist. This significant and oversized product requires shipping from our 'Midwest Parts Warehouse'. Prior to moving forward, confirm that this warehouse can handle heavy merchandise. After confirmation, locate the highest-rated carrier offering 'FTL' service via 'Truck'. Subsequently, generate the outbound order and allocate the inventory. Kindly respond with the new Order ID and the name of the chosen carrier.'Iota Automotive NAC' for 20 'Automotive Windshield' units. This is a heavy, oversized product that needs to be shipped from our 'Midwest Parts Warehouse'. Before you proceed, you must verify that this warehouse has the special capabilities required for handling heavy goods. Once confirmed, find the highest-rated carrier that offers 'FTL' service via 'Truck'. Then, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the carrier you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Automotive Windshield",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "FTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0029",
                    "customer_name": "Iota Automotive NAC",
                    "warehouse_id": "WH-03",
                    "carrier_name": "DeutschLogistik",
                    "carrier_scac": "DLOG",
                    "order_date": "2024-08-22",
                    "total_units": 20,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 20,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 73
    Task(
        annotator="0",
        user_id="U73",
        instruction="As a fulfillment specialist, your task for today, August 23, 2024, involves a new sales order, SO-2024-0030, from 'Alpha Electronics LLC' for 1000 '8-bit Microcontroller' units. Ensure the components are sourced from Formosa as stipulated by the customer. Begin by confirming the origin of the product from the product master data. Then, pinpoint the optimal warehouse for fulfillment by evaluating the highest available stock. Utilize the top-rated 'Parcel' carrier for shipping. Upon creating the order and allocating the inventory, reply with the new Order ID and the warehouse used for fulfillment.'Alpha Electronics LLC' for 1000 '8-bit Microcontroller' units. The customer has a strict requirement that the components must be sourced from Formosa. Please first verify the product's country of origin from the product master data. Then, identify the optimal warehouse for fulfillment based on the highest available stock. Ship the order using the best-rated 'Parcel' carrier. After creating the order and allocating the inventory, please respond with the new Order ID and the name of the warehouse you fulfilled the order from.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="FindCarrierByMethodOfTransport",
                kwargs={
                    "method_of_transport": "Parcel",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0030",
                    "customer_name": "Alpha Electronics LLC",
                    "warehouse_id": "WH-01",
                    "carrier_name": "Global Parcel Service",
                    "carrier_scac": "GPLS",
                    "order_date": "2024-08-23",
                    "total_units": 1000,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 1000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 74
    Task(
        annotator="0",
        user_id="U74",
        instruction="On August 26, 2024, finalize processing a new sales order, SO-2024-0031, for 'Iota Automotive NAC' for 5 'Articulated Robotic Arm' units as a senior fulfillment specialist. This order has distinct fulfillment constraints necessitating shipment from a company-owned warehouse with 'Heavy Equipment Handling' abilities. Also, choose the most budget-friendly carrier offering 'FTL' service via 'Truck'. Solve these constraints, then proceed to draft the outbound order and allocate the inventory. Please return the new Order ID and the name of the selected warehouse.'Iota Automotive NAC' for 5 'Articulated Robotic Arm' units. This order has special fulfillment constraints. You must ship it from a warehouse that is both company-owned AND has 'Heavy Equipment Handling' capabilities. Additionally, you must select the cheapest carrier that provides 'FTL' service via 'Truck'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the warehouse you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="GetAllWarehouses",
                kwargs={
                    "filters": {
                        "ownership_status": "Owned",
                        "special_capabilities": "Heavy Equipment Handling",
                    }
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "FTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0031",
                    "customer_name": "Iota Automotive NAC",
                    "warehouse_id": "WH-03",
                    "carrier_name": "DeutschLogistik",
                    "carrier_scac": "DLOG",
                    "order_date": "2024-08-26",
                    "total_units": 5,
                    "total_weight_kg": 1250.0,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 5,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 75
    Task(
        annotator="0",
        user_id="U75",
        instruction="For the pharmaceutical division, act as a senior fulfillment specialist on August 27, 2024, to process the high-priority sales order, SO-2024-0032, for 'Delta Pharma Inc.' of 2000 'Influenza Vaccine' units. Adhere to the strict requirements by shipping from a warehouse that is 'FDA Registered' with 'Cold Chain (2-8°C)' capabilities. Additionally, pick the top-rated carrier offering 'Pharma' service via 'Air'. Once these constraints are met, proceed with creating the outbound order and allocating the inventory. Report back with the new Order ID and the name of the chosen carrier.'Delta Pharma Inc.' for 2000 'Influenza Vaccine' units. This order has strict fulfillment constraints. You must ship it from a warehouse that is both 'FDA Registered' AND has 'Cold Chain (2-8°C)' capabilities. You must also select the highest-rated carrier that provides 'Pharma' service via 'Air'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the carrier you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Influenza Vaccine",
                },
            ),
            Action(
                name="GetAllWarehouses",
                kwargs={
                    "filters": {
                        "certifications": "FDA Registered",
                        "special_capabilities": "Cold Chain (2-8°C)",
                    }
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Pharma",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0032",
                    "customer_name": "Delta Pharma Inc.",
                    "warehouse_id": "WH-06",
                    "carrier_scac": "DFC",
                    "order_date": "2024-08-27",
                    "total_units": 2000,
                    "temperature_control_required": True,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "PHRM-VACC-D4",
                    "warehouse_id": "WH-06",
                    "quantity_to_allocate": 2000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 76
    Task(
        annotator="0",
        user_id="U76",
        instruction="Your role is a fulfillment specialist. The date is August 28, 2024. Kindly handle a new sales order, SO-2024-0033, for 'Theta Foods SA' for 5000 units of 'Organic Arabica Coffee Beans'. This order has particular fulfillment requirements. Ensure it is shipped from a warehouse that is 'Organic Certified'. Additionally, choose the most economical carrier that offers temperature-controlled 'Reefer' service via 'Sea'. Once these conditions are addressed, coordinate the creation of the outbound order and allocate the inventory. Kindly reply with the new Order ID and the chosen warehouse name.'Theta Foods SA' for 5000 units of 'Organic Arabica Coffee Beans'. This order has special fulfillment constraints. You must ship it from a warehouse that is 'Organic Certified'. You must also select the cheapest carrier that provides temperature controled 'Reefer' service via 'Sea'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the warehouse you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Organic Arabica Coffee Beans",
                },
            ),
            Action(
                name="GetAllWarehouses",
                kwargs={
                    "filters": {
                        "certifications": "Organic Certified",
                    }
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Sea",
                    "service_level": "Reefer",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0033",
                    "customer_name": "Theta Foods SA",
                    "warehouse_id": "WH-05",
                    "carrier_scac": "NSTS",
                    "order_date": "2024-08-28",
                    "total_units": 5000,
                    "temperature_control_required": True,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "FOOD-COFF-C3",
                    "warehouse_id": "WH-05",
                    "quantity_to_allocate": 5000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 77
    Task(
        annotator="0",
        user_id="U77",
        instruction="Your position is a fulfillment specialist. The current date is August 29, 2024. Please handle a new sales order, SO-2024-0034, for 'Mu Agro SA de CV' for 80 'Teak Wood Dining Chair' units. According to our regional fulfillment policy, this order should be shipped from a Texas (OK) located warehouse. Identify the appropriate warehouse, then choose the highest-rated carrier offering 'LTL' service via 'Truck'. After resolving these matters, coordinate the creation of the outbound order and inventory allocation. Provide the new Order ID and the Texas warehouse you selected in your response.'Mu Agro SA de CV' for 80 'Teak Wood Dining Chair' units. Per our regional fulfillment policy, this order must be shipped from a warehouse located in Texas (OK). Please identify the correct warehouse, then select the highest-rated carrier that provides 'LTL' service via 'Truck'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the Texas warehouse you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="GetAllWarehouses",
                kwargs={
                    "filters": {
                        "state_province": "OK",
                    }
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0034",
                    "customer_name": "Mu Agro SA de CV",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "SKEX",
                    "order_date": "2024-08-29",
                    "total_units": 80,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_allocate": 80,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 78
    Task(
        annotator="0",
        user_id="U78",
        instruction="Acting as a fulfillment specialist, today is August 30, 2024. Please manage a new sales order, SO-2024-0035, for 'Zeta Tech Solutions' for 12,500 units of '8-bit Microcontroller'. This order must comply with the customer's requirements by being fulfilled from a 'C-TPAT' certified warehouse. Identify an appropriate warehouse with ample stock. Then, choose the highest-rated carrier offering 'FCL' service via 'Sea'. Once the constraints are addressed, coordinate the creation of the outbound order and inventory allocation. Respond with the new Order ID and the compliant warehouse name.'Zeta Tech Solutions' for 12,500 '8-bit Microcontroller' units. Due to the customer's compliance requirements, this order must be fulfilled from a 'C-TPAT' certified warehouse. Please identify a compliant warehouse that has sufficient stock. Then, select the highest-rated carrier that provides 'FCL' service via 'Sea'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the compliant warehouse you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="GetAllWarehouses",
                kwargs={
                    "filters": {
                        "certifications": "C-TPAT",
                    }
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Sea",
                    "service_level": "FCL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0035",
                    "customer_name": "Zeta Tech Solutions",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "NSTS",
                    "order_date": "2024-08-30",
                    "total_units": 12500,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 12500,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 79
    Task(
        annotator="0",
        user_id="U79",
        instruction="As a fulfillment specialist, the date is September 2, 2024. Please manage a new sales order, SO-2024-0036, for 'Alpha Electronics LLC' for 500 'Smartphone Model X' units. Due to the kitting requirement, ensure it is fulfilled from a warehouse with 'Kitting & Assembly' capabilities. Identify a suitable warehouse with enough stock. Then, select the highest-rated carrier for 'Parcel' transport. After addressing these requirements, coordinate the creation of the outbound order and inventory allocation. Reply with the new Order ID and the selected warehouse name.'Alpha Electronics LLC' for 500 'Smartphone Model X' units. This order requires kitting, so it must be fulfilled from a warehouse with 'Kitting & Assembly' capabilities. Please identify a compliant warehouse that has sufficient stock. Then, select the highest-rated carrier for 'Parcel' transport. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the warehouse you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Smartphone Model X",
                },
            ),
            Action(
                name="GetAllWarehouses",
                kwargs={
                    "filters": {
                        "special_capabilities": "Kitting & Assembly",
                    }
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                },
            ),
            Action(
                name="FindCarrierByMethodOfTransport",
                kwargs={
                    "method_of_transport": "Parcel",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0036",
                    "customer_name": "Alpha Electronics LLC",
                    "warehouse_id": "WH-02",
                    "carrier_scac": "GPLS",
                    "order_date": "2024-09-02",
                    "total_units": 500,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "quantity_to_allocate": 500,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 80
    Task(
        annotator="0",
        user_id="U80",
        instruction="Serving as a fulfillment specialist, today is September 3, 2024. We have an urgent sales order, SO-2024-0037, from 'Pi Ceramics SRL' for 200 'Teak Wood Dining Chair' units. To expedite this large order, it should be fulfilled from a warehouse with 'Cross-Docking' capabilities. Identify a compliant warehouse with adequate stock. Next, choose the highest-rated carrier offering 'LTL' service via 'Truck'. Once these issues are resolved, coordinate the creation of the outbound order and inventory allocation. Please provide the new Order ID and the warehouse you selected.'Pi Ceramics SRL' for 200 'Teak Wood Dining Chair' units. To expedite this large order, it must be fulfilled from a warehouse that has 'Cross-Docking' capabilities. Please identify a compliant warehouse that has sufficient stock. Then, select the highest-rated carrier that provides 'LTL' service via 'Truck'. After resolving these constraints, create the outbound order and allocate the inventory. Please respond with the new Order ID and the name of the warehouse you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="GetAllWarehouses",
                kwargs={
                    "filters": {
                        "special_capabilities": "Cross-Docking",
                    }
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0037",
                    "customer_name": "Pi Ceramics SRL",
                    "warehouse_id": "WH-14",
                    "carrier_scac": "SKEX",
                    "order_date": "2024-09-03",
                    "total_units": 200,
                    "priority_level": "High",
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_allocate": 200,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 81
    Task(
        annotator="0",
        user_id="U81",
        instruction="As a logistics analyst, today is September 4, 2024. We recently received an alert regarding severe congestion at all San Diego terminals. Your task is to locate all our warehouses in San Diego city. For each warehouse, identify inbound sea shipments currently marked as 'In Transit' and add the note to them: 'RISK: LA port congestion. Evaluate for potential diversion.' Please provide a list of the Shipment IDs you have updated with this flag.'ve just received an alert about severe port congestion affecting all terminals in San Diego. I need you to identify all our warehouses located in the city of San Diego. For each of those warehouses, find all inbound sea shipments that are currently 'In Transit' and update their notes with the following flag: 'RISK: LA port congestion. Evaluate for potential diversion.' Please respond with a list of the Shipment IDs that you have flagged.",
        actions=[
            Action(
                name="GetAllWarehouses",
                kwargs={
                    "filters": {
                        "city": "San Diego",
                    }
                },
            ),
            Action(
                name="FindInboundShipmentsByWarehouse",
                kwargs={
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="FindInboundShipmentsByWarehouse",
                kwargs={
                    "warehouse_id": "WH-15",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0001",
                    "new_note": "RISK: LA port congestion. Evaluate for potential diversion.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0025",
                    "new_note": "RISK: LA port congestion. Evaluate for potential diversion.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0018",
                    "new_note": "RISK: LA port congestion. Evaluate for potential diversion.",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="U82",
        instruction="In your role as an inventory control specialist, today is September 6, 2024. A new high-priority sales order, SO-2024-0038, has been created requiring 10,000 units of the '8-bit Microcontroller' from our 'West Coast Distribution Hub'. Assess the impact on stock levels: first check current availability and reorder point for this product in the warehouse. If fulfilling this order will reduce stock below the reorder point, promptly initiate a replenishment purchase order for 5,000 units from 'Global Components Inc.'. Utilize the standard lead time to determine the arrival date.'8-bit Microcontroller' to be fulfilled from our 'West Coast Distribution Hub'. I need you to assess the impact of this order on our stock levels. First, check the current available quantity and the reorder point for this product at that warehouse. If fulfilling this 10,000-unit order will cause the available quantity to drop below the reorder point, you must immediately initiate a replenishment purchase order for a standard quantity of 5,000 units from the supplier 'Global Components Inc.'. Please use their standard lead time to calculate the arrival date.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "West Coast Distribution Hub",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 5000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 83
    Task(
        annotator="0",
        user_id="U83",
        instruction="As a logistics project manager, on September 12, 2024, your assignment is to handle the initial stocking of our new 'Dallas Home Goods DC'. Start by ordering 5000 'Organic Cotton T-Shirt' units from 'Ankara Apparel Ltd.'. Begin by creating a new inventory record for this product at the Dallas warehouse. Next, proceed to generate the corresponding purchase order, using the supplier's lead time for arrival date estimation. Lastly, ensure the inbound quantities are reflected in the updated inventory records.'Dallas Home Goods DC'. To start, we need to establish inventory for a key product. Order 5000 'Organic Cotton T-Shirt' units from 'Ankara Apparel Ltd.'. For the product, you must first create a new inventory record at the Dallas warehouse. Then, create the corresponding purchase order using the supplier's standard lead time to calculate the arrival date. Finally, ensure the new inventory records are updated with the inbound quantities.",
        actions=[
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Organic Cotton T-Shirt",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                },
            ),
            Action(
                name="CreateInventoryRecord",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Ankara Apparel Ltd.",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-14",
                    "quantity_to_add": 5000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 84
    Task(
        annotator="0",
        user_id="U84",
        instruction="Acting as a strategic sourcing manager, on September 10, 2024, we are deactivating 'Johannesburg Mining Equipment' due to their performance issues. Initially, identify any 'In Transit' shipments from this supplier. Cancel these shipments by changing the notes to 'CANCELLED - Supplier Deactivated. Re-sourcing.' Following this, reverse the inbound quantity for the 'Diamond Core Drill Bit' at the 'Denver Heavy Equipment Yard'. Subsequently, create a replacement order of the same quantity (20 units) from 'Bavaria Parts GmbH' and update the inventory pipeline. Please provide the ID of the cancelled shipment and the new Purchase Order number.'Johannesburg Mining Equipment' due to performance issues. First, find any of their inbound shipments that are currently 'In Transit'. You must then cancel this shipment by updating its notes to 'CANCELLED - Supplier Deactivated. Re-sourcing.' Next, you must reverse the inbound quantity for the 'Diamond Core Drill Bit' at the 'Denver Heavy Equipment Yard' to reflect this cancellation. Finally, create a new replacement purchase order for the same quantity (20 units) from our new preferred supplier, 'Bavaria Parts GmbH', and update the inventory pipeline accordingly. Please respond with the ID of the cancelled shipment and the new Purchase Order number.",
        actions=[
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Johannesburg Mining Equipment",
                },
            ),
            Action(
                name="FindInboundShipmentsBySupplier",
                kwargs={
                    "supplier_id": "SUP-1011",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0011",
                    "new_note": "CANCELLED - Supplier Deactivated. Re-sourcing.",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Diamond Core Drill Bit",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Denver Heavy Equipment Yard",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "quantity_to_add": -20,
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bavaria Parts GmbH",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "HEVY-DRIL-I9",
                    "warehouse_id": "WH-11",
                    "quantity_to_add": 20,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 85
    Task(
        annotator="0",
        user_id="U85",
        instruction="As a regional inventory manager, today is September 11, 2024. We must conduct an inter-warehouse stock transfer for inventory balance. The West Coast Distribution Hub has an excess of '8-bit Microcontrollers', while the Midwest Parts Warehouse needs more. Initiate a transfer of 5,000 units from San Diego to Milwaukee. First, confirm sufficient stock at the LA warehouse. Then, choose the most cost-effective 'LTL' service by 'Truck'. Create an outbound order using sales order number 'IBT-LAX-ORD-01' with 'Midwest Parts Warehouse' as the customer. After setting up the order and allocating inventory, annotate the new order as follows: 'Internal Stock Transfer from West Coast Distribution Hub to Midwest Parts Warehouse.''8-bit Microcontrollers', while our Midwest Parts Warehouse is running low. Please create a transfer shipment of 5,000 units from San Diego to Milwaukee. First, verify that the LA warehouse has sufficient available stock. Then, select the most economical carrier that offers 'LTL' service via 'Truck'. You will need to create an outbound order using the sales order number 'IBT-LAX-ORD-01' where the customer is the 'Midwest Parts Warehouse'. After creating the order and allocating the inventory, update the new order's notes to specify: 'Internal Stock Transfer from West Coast Distribution Hub to Midwest Parts Warehouse.'",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "West Coast Distribution Hub",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "IBT-LAX-ORD-01",
                    "customer_name": "Midwest Parts Warehouse",
                    "warehouse_id": "WH-01",
                    "carrier_scac": "SWDL",
                    "order_date": "2024-09-11",
                    "total_units": 5000,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 5000,
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0017",
                    "notes": "Internal Stock Transfer from West Coast Distribution Hub to Midwest Parts Warehouse.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 86
    Task(
        annotator="0",
        user_id="U86",
        instruction="As a quality control manager, today on September 13, 2024, you are managing a significant quality issue. The EAC 'LOT202406B' of 'Frozen Tuna Loin' received at our San Francisco Fresh Foods DC has not passed its temperature inspection. Your initial step is to locate the specific inventory record for this EAC and change its status to 'Quarantined'. Given that this results in a stock-out, promptly initiate an emergency replacement purchase order for the same quantity from 'Melbourne Seafood Exporters' with critical priority. Choose the highest-rated carrier providing 'Perishables' service through 'Air'. Following the creation of the PO and the update of the inventory pipeline, reply with the newly generated Purchase Order number and the ID of the inventory record you quarantined.'LOT202406B' of 'Frozen Tuna Loin' at our San Francisco Fresh Foods DC has failed its temperature inspection. Your first task is to find the specific inventory record for this EAC and update its status to 'Quarantined'. Since this will create a stock-out, you must then immediately create an emergency replacement purchase order for the same quantity from the supplier, 'Melbourne Seafood Exporters' with critical priority. Select the highest-rated carrier that offers 'Perishables' service via 'Air'. After creating the PO and updating the inventory pipeline, respond with the new Purchase Order number and the ID of the inventory record you quarantined.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Frozen Tuna Loin",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "San Francisco Fresh Foods DC",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0008",
                    "new_status": "Quarantined",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Melbourne Seafood Exporters",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="FindCarrierByService",
                kwargs={
                    "mode_of_transport": "Air",
                    "service_level": "Perishables",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "SUP-1010",
                    "destination_warehouse_id": "WH-10",
                    "order_quantity": 2500,
                    "unit_cost": 35.0,
                    "unit_weight": 2.0,
                    "expected_arrival_date": "2024-09-16",
                    "carrier_name": "Desert Falcon Cargo",
                    "carrier_scac": "DFC",
                    "priority_level": "Critical",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FOOD-FISH-H8",
                    "warehouse_id": "WH-10",
                    "quantity_to_add": 2500,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 87
    Task(
        annotator="0",
        user_id="U87",
        instruction="As a product safety manager today on September 18, 2024, we are undertaking an urgent recall for all 'Ceramic Floor Tile' units due to a critical manufacturing defect. Your primary action is to identify all inventories of this product and set their status to 'Recalled - Do Not Ship'. Secondly, find any outbound orders concerning this product in the warehouses that are 'Shipped' or 'In Transit', updating their status to 'Recalled' and ensuring to add: 'URGENT RECALL: Intercept and return to origin.' To initiate recovery, place an emergency replenishment purchase order for the total recalled on-hand quantity from another supplier, 'Global Components Inc.', directing it to the original warehouse. Calculate the arrival date using their standard lead time.'Ceramic Floor Tile' units due to a critical manufacturing defect. Your first task is to find all inventory of this product and update its status to 'Recalled - Do Not Ship'. Second, you must find any outbound orders from the warehouses that store this product that are currently 'Shipped' or 'In Transit' and update their status to 'Recalled', adding a note: 'URGENT RECALL: Intercept and return to origin.' Finally, to begin recovery, you must place an emergency replenishment purchase order for the entire recalled on-hand quantity from a different supplier, 'Global Components Inc.', to the original warehouse. Use their standard lead time to calculate the arrival date.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Ceramic Floor Tile",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0010",
                    "new_status": "Recalled - Do Not Ship",
                },
            ),
            Action(
                name="GetAllOutboundOrders",
                kwargs={"filters": {"warehouse_id": "WH-12", "status": "Shipped"}},
            ),
            Action(
                name="GetAllOutboundOrders",
                kwargs={
                    "filters": {
                        "warehouse_id": "WH-12",
                        "status": "In Transit",
                    }
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0003",
                    "status": "Recalled",
                    "notes": "URGENT RECALL: Intercept and return to origin.",
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0013",
                    "status": "Recalled",
                    "notes": "URGENT RECALL: Intercept and return to origin.",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "BLDG-TILE-J10",
                    "warehouse_id": "WH-12",
                    "quantity_to_add": 18000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 88
    Task(
        annotator="0",
        user_id="U88",
        instruction="As a crisis response manager on September 19, 2024, deal with the situation that has made our 'Midwest Parts Warehouse' entirely non-functional due to a fire. Your foremost task is managing the inbound pipeline. Identify all inbound shipments listed as 'In Transit' or 'Planned' for this warehouse, and amend their notes with this high-priority message: 'URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.' After adjusting the shipments, evaluate the financial repercussions of the inactive inventory by calculating the total value of all 'Articulated Robotic Arm' units currently available at the Milwaukee location. Please provide a list of the Shipment IDs flagged for diversion along with the comprehensive estimated value of the inventory at risk.'Midwest Parts Warehouse' completely non-operational. Your first priority is to manage the inbound pipeline. Find all inbound shipments currently 'In Transit' or 'Planned' for this warehouse and update their notes with the following high-priority message: 'URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.' After flagging the shipments, you must assess the financial impact of the inaccessible inventory. Calculate the total value of all 'Articulated Robotic Arm' units currently on hand at the Milwaukee facility. Please respond with a list of the Shipment IDs you flagged for diversion and the total calculated value of the at-risk inventory.",
        actions=[
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="FindInboundShipmentsByWarehouse",
                kwargs={
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0003",
                    "new_note": "URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0016",
                    "new_note": "URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0019",
                    "new_note": "URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.",
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0023",
                    "new_note": "URGENT: Divert to Detroit (WH-08) - Origin WH non-operational.",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Articulated Robotic Arm",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "TECH-ROBO-N14",
                    "warehouse_id": "WH-03",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 89
    Task(
        annotator="0",
        user_id="U89",
        instruction="As a product launch manager on September 20, 2024, coordinate the initial stocking of 500 'Teak Wood Dining Chair' units at our 'Phoenix Renewable Warehouse'. Your first assignment is to execute a capacity check. Calculate the cubic meters needed for this fresh inventory and confirm if the warehouse's available space suffices. Assuming that the capacity check is successful, proceed with setting up: establish a new inventory record for this product at the warehouse, generate the purchase order from the supplier 'Bangkok Furniture Co.', and finally update the pipeline of the new inventory record. Kindly respond with the newly issued Purchase Order number and the Inventory ID. If the capacity check fails, specify the cubic meters of the space shortfall.'Teak Wood Dining Chair' units at our 'Phoenix Renewable Warehouse'. Your first task is to conduct a capacity check. You must calculate the total cubic meters required for this new inventory and verify if the warehouse has enough available space. If, and only if, the capacity check passes, you must proceed with the full setup: create a new inventory record for this product at the warehouse, then create the purchase order from the supplier 'Bangkok Furniture Co.', and finally, update the new inventory record's pipeline. Please respond with the new Purchase Order number and the new Inventory ID. If the capacity check fails, you must report the space deficit in cubic meters.",
        actions=[
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Phoenix Renewable Warehouse",
                },
            ),
            Action(
                name="GetWarehouseDetails",
                kwargs={
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                },
            ),
            Action(
                name="CreateInventoryRecord",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-09",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-09",
                    "quantity_to_add": 500,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 90
    Task(
        annotator="0",
        user_id="U90",
        instruction="As an inventory quality auditor on September 23, 2024, conduct a shelf-life analysis on our 'Fresh Cut Roses' inventory spanning all warehouses. For any specific inventory EAC that has surpassed its expiration date, coordinate an inventory adjustment to write off the entire on-hand quantity, citing the reason 'Expired Stock Write-Off'. Instantly after processing the write-off, create an emergency replenishment purchase order with critical priority for the exact amount written off, sourcing from 'Bogota Floral Exports' and utilizing their standard lead time to estimate the arrival date. Please provide the Inventory ID you adjusted alongside the newly created Purchase Order number.'Fresh Cut Roses' inventory across all warehouses. For any specific inventory EAC that has already passed its expiration date, you must perform an inventory adjustment to write off the entire on-hand quantity, using the reason 'Expired Stock Write-Off'. Immediately after processing the write-off, you must create an emergency replenishment purchase order with critical priority for the exact quantity you just wrote off. Source this from the supplier 'Bogota Floral Exports' and use their standard lead time for the arrival date. Please respond with the ID of the inventory record you adjusted and the new Purchase Order number.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Fresh Cut Roses",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                },
            ),
            Action(
                name="PerformInventoryAdjustment",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                    "new_physical_count": 0,
                    "current_date": "2024-09-23",
                    "reason_note": "Expired Stock Write-Off",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bogota Floral Exports",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FOOD-FLWR-X24",
                    "warehouse_id": "WH-10",
                    "quantity_to_add": 3000,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 91
    Task(
        annotator="0",
        user_id="U91",
        instruction="As a strategic sourcing manager, today is September 25, 2024. We are tasked with sourcing a new product, the 'Automotive Windshield', for our 'Midwest Parts Warehouse'. The potential suppliers on the table are 'Mexico City Auto Glass' and 'Toronto Paper Mills'. Your responsibility is to assess both suppliers using these considerations: they must belong to the 'Automotive' product category, be situated in North America (Mexico or Maple Nation), and possess a performance rating exceeding 4.4. Choose the supplier that fulfills all requirements, then draft an initial purchase order for 100 units. Utilize the supplier's regular lead time to determine the arrival date.'Automotive Windshield', for our 'Midwest Parts Warehouse'. I have two potential suppliers: 'Mexico City Auto Glass' and 'Toronto Paper Mills'. You must evaluate both based on the following criteria: they must be in the 'Automotive' product category, located in North America (Mexico or Maple Nation), and have a performance rating above 4.4. Select the best supplier that meets all criteria, then create an initial purchase order for 100 units. Use the supplier's standard lead time to calculate the arrival date.",
        actions=[
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Mexico City Auto Glass",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Toronto Paper Mills",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1023",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1008",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Automotive Windshield",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "AUTO-GLAS-U21",
                    "warehouse_id": "WH-03",
                    "quantity_to_add": 100,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 92
    Task(
        annotator="0",
        user_id="U92",
        instruction="In your role as a senior logistics specialist, today is September 26, 2024. We need to address a short-shipment claim regarding sales order SO-2024-0001 from 'Alpha Electronics LLC', which received 50 fewer '8-bit Microcontroller' units. A cycle check at the fulfillment warehouse, 'West Coast Distribution Hub', registered a physical count of 15,050 units, exposing the missing items. Your initial task is to adjust the inventory to correct the system quantity. Then, compile and expedite a fresh outbound order for the 50 absent units using sales order 'SO-2024-0042' with the original shipper, 'Global Parcel Service'. Post creation and allocation of the new order, update the original order (ORD-0001) with this note: 'Short-shipment of 50 units confirmed. Corrective shipment sent via order [New Order ID].''Alpha Electronics LLC'. They were shorted 50 units of the '8-bit Microcontroller'. A cycle count at the fulfillment warehouse, 'West Coast Distribution Hub', has confirmed a physical count of 15,050 units, revealing the missing items. Your first task is to perform an inventory adjustment to correct the system quantity. Then, create a new, high-priority outbound order for the 50 missing units using sales order number 'SO-2024-0042' and the original carrier, 'Global Parcel Service'. After creating the new order and allocating the inventory, you must update the original order (ORD-0001) with a note: 'Short-shipment of 50 units confirmed. Corrective shipment sent via order [New Order ID].'",
        actions=[
            Action(
                name="FindOutboundOrderBySo",
                kwargs={
                    "sales_order_number": "SO-2024-0001",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "West Coast Distribution Hub",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="PerformInventoryAdjustment",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "new_physical_count": 15050,
                    "current_date": "2024-09-26",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "Global Parcel Service",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0042",
                    "customer_name": "Alpha Electronics LLC",
                    "warehouse_id": "WH-01",
                    "carrier_name": "Global Parcel Service",
                    "carrier_scac": "GPLS",
                    "order_date": "2024-09-26",
                    "total_units": 50,
                    "priority_level": "High",
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 50,
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0001",
                    "notes": "Short-shipment of 50 units confirmed. Corrective shipment sent via order ORD-0017.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 93
    Task(
        annotator="0",
        user_id="U93",
        instruction="As a logistics project manager, the date is September 27, 2024. We are rolling out 'Project Unify' to centralize all '8-bit Microcontroller' inventory into our main hub, the 'Midwest Parts Warehouse'. Your duty is to implement this consolidation. Begin by pinpointing all satellite warehouses currently holding this product. Subsequently, for each location, prepare an inter-warehouse stock transfer to relocate the full available stock to the Milwaukee hub. Opt for the most cost-effective 'LTL' 'Truck' carrier for these transfers. Use a sales order format such as 'CONSOL-[SourceWH-ID]-01' for each transfer. Once the order is created and stock allocated, append this note to every new order: 'Project Unify - Inventory Consolidation'. Kindly return with a compilation of the new Order IDs you generated.'Project Unify' to consolidate all inventory of the '8-bit Microcontroller' into our central hub, the 'Midwest Parts Warehouse'. Your task is to execute this consolidation. First, identify all satellite warehouses that currently stock this product. Then, for each of these locations, you must create an inter-warehouse stock transfer to move the entire available quantity to the Milwaukee hub. Use the most economical 'LTL' 'Truck' carrier for these transfers. Use a sales order number format like 'CONSOL-[SourceWH-ID]-01' for each transfer. After creating the order and allocating the stock, add a note to each new order: 'Project Unify - Inventory Consolidation'. Please respond with a list of the new Order IDs you created.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "CONSOL-WH-01-01",
                    "customer_name": "Midwest Parts Warehouse",
                    "destination_city": "Milwaukee",
                    "destination_country": "United States",
                    "warehouse_id": "WH-01",
                    "carrier_name": "SwiftDelivery",
                    "carrier_scac": "SWDL",
                    "order_date": "2024-09-27",
                    "total_units": 12500,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_allocate": 12500,
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0017",
                    "notes": "Project Unify - Inventory Consolidation",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 94
    Task(
        annotator="0",
        user_id="U94",
        instruction="As a senior procurement specialist, today is September 28, 2024. We're dealing with an urgent stock-out. A pressing order calls for 600 'Teak Wood Dining Chair' units, yet our 'Dallas Home Goods DC' has only 520 available. The lead time from our primary vendor, 'Bangkok Furniture Co.', is excessively long. It is necessary for you to assess an alternative supplier, 'Paris Luxury Goods'. Ensure they fit two parameters: inclusion in the 'Furniture' product category and a performance rating above 4.5. Should they not satisfy these conditions, revert to placing an order for the entire 600 units from the main supplier, 'Bangkok Furniture Co.'. Formulate the necessary purchase order from the selected supplier and refresh the inventory pipeline. Inform us of the new Purchase Order number and the selected supplier's name.'Teak Wood Dining Chair' units, but our 'Dallas Home Goods DC' only has 520 available. The lead time from our primary supplier, 'Bangkok Furniture Co.', is too long. I need you to evaluate an alternate supplier, 'Paris Luxury Goods'. You must verify two things: that they are in the 'Furniture' product category and that their performance rating is above 4.5. If they do not meet these criteria, you must revert to ordering the full 600 units from the primary supplier, 'Bangkok Furniture Co.'. Create the necessary purchase order from the chosen supplier and update the inventory pipeline. Please respond with the new Purchase Order number and the name of the supplier you selected.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Teak Wood Dining Chair",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Dallas Home Goods DC",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Paris Luxury Goods",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1007",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Bangkok Furniture Co.",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "FURN-CHAIR-M13",
                    "warehouse_id": "WH-14",
                    "quantity_to_add": 600,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 95
    Task(
        annotator="0",
        user_id="U95",
        instruction="In your capacity as a logistics analyst, today is September 30, 2024. We are evaluating freight costs, suspecting inefficiency in shipping 'Organic Cotton T-Shirt' units from our East Coast Fashion Center to our West Coast client, 'Alpha Electronics LLC'. Your primary job is to substantiate this by examining our outbound orders. Next, establish a fresh stocking site. Ascertain whether an inventory record exists for this product at the 'Northwest Fulfillment Center'. If absent, create one. Then, commence a substantial stock transfer of 3,000 units from Jersey City to Portland. Use the sales order 'IBT-NWK-SEA-01' for this transfer, designating the 'Northwest Fulfillment Center' as the customer. Choose the most economical 'LTL' truck carrier. Post creation and allocation of the transfer order, add this note: 'Strategic stock placement to reduce West Coast freight costs.' Please provide the new Order ID and the newly created Inventory ID as your response.'Organic Cotton T-Shirt' units from our East Coast Fashion Center to our West Coast customer, 'Alpha Electronics LLC'. Your first task is to confirm this by checking our outbound orders. Then, we will set up a new stocking location. Check if an inventory record for this product already exists at the 'Northwest Fulfillment Center'. If not, create one. Then, initiate a bulk stock transfer of 3,000 units from Jersey City to Portland. Use the sales order number 'IBT-NWK-SEA-01' for this transfer, with the 'Northwest Fulfillment Center' as the customer. Select the most economical 'LTL' truck carrier. After creating the transfer order and allocating the stock, add a note to the new order: 'Strategic stock placement to reduce West Coast freight costs.' Please respond with the new Order ID and the new Inventory ID you created.",
        actions=[
            Action(
                name="GetAllOutboundOrders",
                kwargs={},
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Organic Cotton T-Shirt",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "East Coast Fashion Center",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Northwest Fulfillment Center",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                },
            ),
            Action(
                name="CreateInventoryRecord",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-02",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "IBT-NWK-SEA-01",
                    "customer_name": "Northwest Fulfillment Center",
                    "destination_city": "Portland",
                    "destination_country": "United States",
                    "warehouse_id": "WH-04",
                    "carrier_name": "SwiftDelivery",
                    "carrier_scac": "SWDL",
                    "order_date": "2024-09-30",
                    "total_units": 3000,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "APRL-TSHT-O15",
                    "warehouse_id": "WH-04",
                    "quantity_to_allocate": 3000,
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0017",
                    "notes": "Strategic stock placement to reduce West Coast freight costs.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 96
    Task(
        annotator="0",
        user_id="U96",
        instruction="As a quality control manager, today is October 15, 2024. Our receiving shipment SHIP-0002 from 'Osaka Electronics Ltd.' consisting of 'Smartphone Model X' did not pass its quality inspection upon arrival at the 'Northwest Fulfillment Center'. Handle this failure by first identifying the related inventory record and changing its status to 'Quarantined - Awaiting RTV'. Following that, coordinate a Return-to-Vendor (RTV) shipment for all 2300 units. For this, generate an outbound order designating 'Osaka Electronics Ltd.' as the customer, referring to sales order number 'RTV-SHIP-0002'. Opt for the most cost-effective 'LTL' truck carrier to manage this return. Once the RTV order is created and the quarantined inventory is allocated, append a note to the initial inbound shipment (SHIP-0002) stating: 'Goods failed inspection. RTV processed via order [New Order ID].' Kindly reply with the ID of the inventory record you placed on hold and the new Order ID for the return shipment.'Osaka Electronics Ltd.' containing 'Smartphone Model X' has failed its quality inspection upon arrival at the 'Northwest Fulfillment Center'. You must process this failure. First, find the corresponding inventory record and update its status to 'Quarantined - Awaiting RTV'. Next, you must create a Return-to-Vendor (RTV) shipment for the entire quantity of 2300 units. To do this, create an outbound order with the supplier, 'Osaka Electronics Ltd.', as the customer, using the sales order number 'RTV-SHIP-0002'. Select the most economical 'LTL' truck carrier for this return. After creating the RTV order and allocating the quarantined inventory, you must update the notes on the original inbound shipment (SHIP-0002) to state: 'Goods failed inspection. RTV processed via order [New Order ID].' Please respond with the ID of the inventory record you quarantined and the new Order ID for the return shipment.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Smartphone Model X",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Northwest Fulfillment Center",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0023",
                    "new_status": "Quarantined - Awaiting RTV",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Osaka Electronics Ltd.",
                },
            ),
            Action(
                name="GetSupplierDetails",
                kwargs={
                    "supplier_id": "SUP-1002",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "RTV-SHIP-0002",
                    "customer_name": "Osaka Electronics Ltd.",
                    "destination_city": "Minato-ku, Osaka",
                    "destination_country": "Nippon",
                    "warehouse_id": "WH-02",
                    "carrier_name": "SwiftDelivery",
                    "carrier_scac": "SWDL",
                    "order_date": "2024-10-15",
                    "total_units": 2300,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-SMART-W23",
                    "warehouse_id": "WH-02",
                    "quantity_to_allocate": 2300,
                },
            ),
            Action(
                name="UpdateShipmentNotes",
                kwargs={
                    "shipment_id": "SHIP-0002",
                    "new_note": "Goods failed inspection. RTV processed via order ORD-0017.",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 97
    Task(
        annotator="0",
        user_id="U97",
        instruction="As a data integrity specialist, today is October 8, 2024. Our audit discovered a duplicate inventory entry for the '8-bit Microcontroller' at the 'Midwest Parts Warehouse'; all stock should be centralized at our primary 'West Coast Distribution Hub'. Coordinate this consolidation by first initiating an inter-warehouse stock transfer to move the complete available quantity from Milwaukee to San Diego. Utilize the sales order number 'CONSOL-001' for this transfer, with the 'West Coast Distribution Hub' as the customer, and select the least expensive 'LTL' truck carrier. Following the creation of the transfer order and the allocation of stock, conduct an inventory adjustment on the Milwaukee record to reduce its physical count to zero, citing the reason as 'Consolidated to WH-01'. Finally, modify the status of the Milwaukee inventory record to 'Deactivated'. Please provide the new Order ID for the transfer and the ID of the inventory record you deactivated.'8-bit Microcontroller' at the 'Midwest Parts Warehouse'; all stock should be consolidated at our primary 'West Coast Distribution Hub'. Please execute this consolidation. First, you must create an inter-warehouse stock transfer to move the entire on-hand quantity from Milwaukee to San Diego. Use the sales order number 'CONSOL-001' for this transfer, with the 'West Coast Distribution Hub' as the customer, and select the most economical 'LTL' truck carrier. After creating the transfer order and allocating the stock, you must perform an inventory adjustment on the Milwaukee record to write its physical count down to zero, noting the reason as 'Consolidated to WH-01'. Finally, update the status of the Milwaukee inventory record to 'Deactivated'. Please respond with the new Order ID for the transfer and the ID of the inventory record you deactivated.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "West Coast Distribution Hub",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03",
                },
            ),
            Action(
                name="FindCheapestCarrierByService",
                kwargs={
                    "mode_of_transport": "Truck",
                    "service_level": "LTL",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "CONSOL-001",
                    "customer_name": "West Coast Distribution Hub",
                    "destination_city": "San Diego",
                    "destination_country": "United States",
                    "warehouse_id": "WH-03",
                    "carrier_name": "SwiftDelivery",
                    "carrier_scac": "SWDL",
                    "order_date": "2024-10-08",
                    "total_units": 8000,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 8000,
                },
            ),
            Action(
                name="PerformInventoryAdjustment",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-03",
                    "new_physical_count": 0,
                    "current_date": "2024-10-08",
                    "reason_note": "Consolidated to WH-01",
                },
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={
                    "inventory_id": "INV-0025",
                    "new_status": "Deactivated",
                },
            ),
        ],
        outputs=[]
    ),
    # Task 98
    Task(
        annotator="0",
        user_id="U98",
        instruction="Positioned as a reverse logistics coordinator, today is October 9, 2024. Our client, 'Alpha Electronics LLC', wishes to return 50 units of the '8-bit Microcontroller' from their original sales order, SO-2024-0001. Process this return by initially altering the original order's return status to 'Return Initiated'. Subsequently, formulate a new inbound shipment record to track the return, classifying the customer as the supplier. The return should head to the initial fulfillment warehouse, the 'West Coast Distribution Hub'. Opt for the highest-rated 'Parcel' carrier to oversee the return shipment and set the expected arrival for 3 days from the current date. Add a note to the new shipment: 'Customer Return Authorization for ORD-0001'. Finally, ensure the inventory pipeline at the receiving warehouse mirrors this incoming return. Please send the ID of the original order you modified and the new Shipment ID for the return.'Alpha Electronics LLC', has requested to return 50 units of the '8-bit Microcontroller' from their original sales order, SO-2024-0001. Please process this return. First, you must update the original order's return status to 'Return Initiated'. Then, create a new inbound shipment record to track the return, treating the customer as the supplier. The return should be directed to the original fulfillment warehouse, the 'West Coast Distribution Hub'. Select the highest-rated 'Parcel' carrier to handle the return shipment and set the expected arrival for 3 days from today. Add a note to the new shipment: 'Customer Return Authorization for ORD-0001'. Finally, ensure the inventory pipeline at the receiving warehouse is updated to reflect this incoming return. Please respond with the ID of the original order you updated and the new Shipment ID for the return.",
        actions=[
            Action(
                name="FindOutboundOrderBySo",
                kwargs={
                    "sales_order_number": "SO-2024-0001",
                },
            ),
            Action(
                name="UpdateOutboundOrderDetails",
                kwargs={
                    "order_id": "ORD-0001",
                    "return_status": "Return Initiated",
                },
            ),
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "West Coast Distribution Hub",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="FindCarrierByMethodOfTransport",
                kwargs={
                    "method_of_transport": "Parcel",
                },
            ),
            Action(
                name="CreateInboundShipment",
                kwargs={
                    "supplier_id": "CUST-2001",
                    "supplier_name": "Alpha Electronics LLC",
                    "destination_warehouse_id": "WH-01",
                    "order_quantity": 50,
                    "unit_cost": 2.5,
                    "unit_weight": 0.01,
                    "expected_arrival_date": "2024-10-12",
                    "carrier_name": "Global Parcel Service",
                    "mode_of_transport": "Parcel",
                    "notes": "Customer Return Authorization for ORD-0001.",
                },
            ),
            Action(
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 50,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 99
    Task(
        annotator="0",
        user_id="U99",
        instruction="In the role of a fulfillment coordinator, today is October 24, 2024. Process a new sales order, SO-2024-0045, for our client 'Gamma Construction Ltd.' for 150 'Ceramic Brake Pad Set' units. This order must be fulfilled from the 'Midwest Parts Warehouse' and dispatched via 'SwiftDelivery'. After generating the outbound order, ensure the allocated inventory is updated. Respond with the new Order ID to verify the process is finished.'Gamma Construction Ltd.' for 150 'Ceramic Brake Pad Set' units. This order should be fulfilled from the 'Midwest Parts Warehouse' and shipped via 'SwiftDelivery'. After creating the outbound order, please make sure to update the allocated inventory. Respond with the new Order ID to confirm the process is complete.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "Ceramic Brake Pad Set",
                },
            ),
            Action(
                name="FindInventoryBySku",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "Midwest Parts Warehouse",
                },
            ),
            Action(
                name="GetCarrierDetailsByName",
                kwargs={
                    "carrier_name": "SwiftDelivery",
                },
            ),
            Action(
                name="CreateOutboundOrder",
                kwargs={
                    "sales_order_number": "SO-2024-0045",
                    "customer_name": "Gamma Construction Ltd.",
                    "warehouse_id": "WH-03",
                    "carrier_name": "SwiftDelivery",
                    "carrier_scac": "SWDL",
                    "order_date": "2024-10-24",
                    "total_units": 150,
                },
            ),
            Action(
                name="UpdateInventoryAllocatedQuantity",
                kwargs={
                    "sku": "AUTO-PAD-B2",
                    "warehouse_id": "WH-03",
                    "quantity_to_allocate": 150,
                },
            ),
        ],
        outputs=[]
    ),
    # Task 100
    Task(
        annotator="0",
        user_id="U100",
        instruction="Functioning as a VMI Analyst, today is October 18, 2024. I'm aligning a VMI report from 'Global Components Inc.' for the '8-bit Microcontroller' at our 'West Coast Distribution Hub'. Their report indicates an on-hand quantity of 3,900 units, which is lower than our system's count. A physical check has confirmed their figure is accurate. Your initial step is to conduct an inventory adjustment to revise our on-hand quantity to 3,900, noting the reason as 'VMI Reconciliation'. After making this adjustment, verify if the new available quantity falls below the reorder threshold for this item. If it does, promptly initiate a high priority replenishment purchase order for 5,000 units from the same supplier. Please provide the ID of the inventory record you adjusted and the new Purchase Order number if one has been established.'m reconciling a VMI report from 'Global Components Inc.' for the '8-bit Microcontroller' at our 'West Coast Distribution Hub'. Their report shows an on-hand quantity of 3,900 units, which is lower than our system's value. A physical count has just confirmed their number is correct. Your first task is to perform an inventory adjustment to update our on-hand quantity to 3,900, noting the reason as 'VMI Reconciliation'. After this adjustment, you must check if the new available quantity is below the reorder point for this item. If it is, you must immediately create a high priority replenishment purchase order for 5,000 units from the same supplier. Please respond with the ID of the inventory record you adjusted and the new Purchase Order number if one was created.",
        actions=[
            Action(
                name="FindProductByName",
                kwargs={
                    "product_name": "8-bit Microcontroller",
                },
            ),
            Action(
                name="FindWarehouseByName",
                kwargs={
                    "warehouse_name": "West Coast Distribution Hub",
                },
            ),
            Action(
                name="GetInventoryDetails",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                },
            ),
            Action(
                name="PerformInventoryAdjustment",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "new_physical_count": 3900,
                    "current_date": "2024-10-18",
                    "reason_note": "VMI Reconciliation",
                },
            ),
            Action(
                name="FindSupplierByName",
                kwargs={
                    "supplier_name": "Global Components Inc.",
                },
            ),
            Action(
                name="CreateInboundShipment",
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
                name="UpdateInventoryInboundQuantity",
                kwargs={
                    "sku": "ELEC-CHIP-A1",
                    "warehouse_id": "WH-01",
                    "quantity_to_add": 5000,
                },
            ),
        ],
        outputs=[]
    ),
]
