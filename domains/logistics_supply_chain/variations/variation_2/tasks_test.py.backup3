from datetime import datetime

from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="ArpanMahatra1999",
        user_id="task_001",
        instruction="""
        Handle the role of logistics planner in charge of managing incoming shipments.
        Evaluate shipment SHIP-0004, ensuring the assigned carrier's operational status is verified.
        Your responsibility is to obtain the shipment details and ascertain the active status of the designated carrier.
        Should the carrier be inactive, it is essential to identify an alternative by accessing the list of active carriers, choosing the top-rated one, and updating the shipment with the change.
        If multiple carriers have identical top ratings, choose the one with the superior on-time delivery percentage as the replacement.
        After reassignment, make certain the shipment details accurately reflect the new carrier to uphold continuity in the supply chain process.
    """,
        actions=[
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "POCL"}),
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetTopRatedCarriers", kwargs={"list_of_scacs": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL", "OCBR",
                                             "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL",
                                             "EAC", "NAC", "ANAF", "NSC", "EWDL"]}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0004",
                "updates": {"carrier_name": "Global Parcel Service", "carrier_scac": "GPLS"}
            }),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
        ],
        outputs=['GPLS']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_002",
        instruction="""
            Coordinate a list of all active carriers in the system, organizing them by their average rating.
            Determine the overall minimum of these carriers' average ratings.
            For each carrier with a rating matching the overall minimum, update their profile by adding a new attribute called "warning" with the value "Least Rated".
            Subsequently, examine the updated profiles of all carriers flagged as least rated, and return the scacs of pertinent carriers.
        """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetTopRatedCarriers",
                   kwargs={"list_of_scacs": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL", "OCBR",
                                             "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL",
                                             "EAC", "NAC", "ANAF", "NSC", "EWDL"]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "min",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL", "OCBR",
                                             "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL",
                                             "EAC", "NAC", "ANAF", "NSC", "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SATL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
            Action(name="UpdateCarrier", kwargs={
                "carrier_scac": "MTRL",
                "updates": {"warning": "Least Rated"}
            }),
            Action(name="UpdateCarrier", kwargs={
                "carrier_scac": "PSLN",
                "updates": {"warning": "Least Rated"}
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["MTRL", "PSLN"]})
        ],
        outputs=['[\n  "MTRL",\n  "PSLN"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_003",
        instruction="""
        As a supply chain analyst in charge of overseeing inbound logistics as of June 5, 2024, your objective is to identify all inbound shipments that are delayed, signified by arrival dates that have elapsed without marking them as arrived.
        Generate this list and amend the status of each delayed shipment to “Delayed.
        ” After all relevant shipments are updated, concentrate on the last modified shipment and assess its carrier's status.
        If the carrier remains active, further action is unnecessary.
        In the event the carrier is inactive, identify the highest-rated active carrier by average rating.
        If multiple carriers hold the top rating, opt for the one with superior on-time delivery percentage.
        Amend the shipment's carrier to this leading carrier, and then retrieve the updated shipment details to verify all modifications are correctly applied.
    """,
        actions=[
            Action(name="GetDelayedShipments", kwargs={'today': '2024-06-05'}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0014"}),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0014",
                "updates": {"status": "Delayed"}
            }),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0014"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0014"}),
        ],
        outputs=['"status": "Delayed"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_004",
        instruction="""
        Organize a list of all carriers that are currently active in the system.
        Determine the overall minimum of these carriers' on-time delivery percentages.
        For each carrier whose rating meets the overall minimum, adjust their profile by adding a new attribute called "warning" with the value "Poor Delivery.
        " Following this, inspect the updated profiles of all carriers marked for poor delivery, followed by returning the scacs of the updated carriers.
    """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "min",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL", "OCBR",
                                "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL",
                                "EAC", "NAC", "ANAF", "NSC", "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SATL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
            Action(name="UpdateCarrier", kwargs={
                "carrier_scac": "MTRL",
                "updates": {"warning": "Poor Delivery"}
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["MTRL"]})
        ],
        outputs=['[\n  "MTRL"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_005",
        instruction="""
        Compile a list of all currently active carriers in the system and arrange them according to their average rating.
        Identify the overall maximum of these carriers' average ratings.
        For every carrier whose rating matches the overall maximum, enhance their record by adding a new attribute called "highlight" with the value "Best Rated.
        " Conclusively, review the modified details of all carriers highlighted as best rated, and ultimately return the scacs of these updated carriers.
    """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetTopRatedCarriers",
                   kwargs={"list_of_scacs": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL", "OCBR",
                                             "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL",
                                             "EAC", "NAC", "ANAF", "NSC", "EWDL"]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL", "OCBR",
                                "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL",
                                "EAC", "NAC", "ANAF", "NSC", "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SATL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
            Action(name="UpdateCarrier", kwargs={
                "carrier_scac": "DFC",
                "updates": {"highlight": "Best Rated"}
            }),
            Action(name="UpdateCarrier", kwargs={
                "carrier_scac": "GPLS",
                "updates": {"highlight": "Best Rated"}
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["DFC", "GPLS"]})
        ],
        outputs=['[\n  "DFC",\n  "GPLS"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_006",
        instruction="""
            Handle the listing of all carriers currently active in the system.
            Determine the overall maximum of their on-time delivery percentages.
            For each carrier with a rating matching this overall maximum, modify their record by adding a new attribute titled "highlight" with the value "Best Delivery.
            " Lastly, review the details of all carriers marked for best delivery.
            Conclude by returning the scacs of the updated carriers.
        """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL", "OCBR",
                                "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL",
                                "EAC", "NAC", "ANAF", "NSC", "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SATL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
            Action(name="UpdateCarrier", kwargs={
                "carrier_scac": "GPLS",
                "updates": {"highlight": "Best Delivery"}
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["GPLS"]})
        ],
        outputs=['[\n  "GPLS"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_007",
        instruction="""
        Coordinate the monitoring of inventory integrity as a warehouse inventory coordinator.
        Identify all inventory items with a damaged quantity greater than zero.
        Once identified, update their records to mark them for review, ensuring they are flagged for further inspection or action.
        After completing the updates, retrieve and review the details of one affected inventory record to confirm the changes.
    """,
        actions=[
            Action(name="GetInventoryWithDamage", kwargs={}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0001", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0002", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0003", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0005", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0006", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0007", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0010", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0013", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0015", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0016", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0017", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0018", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0020", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0021", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0022", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0023", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0024", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0025", "updates": {"status": "Under Review"}}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0025"})
        ],
        outputs=['"status": "Under Review"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_008",
        instruction="""
        As a warehouse operations analyst, you are responsible for monitoring storage utilization.
        Begin by retrieving the details of the owned warehouses.
        Evaluate their current utilization percentages, and if any percentage is found to be below (not equal but only below) 60%, update the warehouse record to include a flag indicating it is underused.
        After applying these updates, retrieve the warehouse details once more to ensure the flag has been correctly added.
    """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Owned"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-01"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-03"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-08"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-13"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-14"}),
            Action(name="UpdateWarehouse", kwargs={
                "warehouse_id": "WH-11",
                "updates": {"underused_flag": True}
            }),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-11"}),
        ],
        outputs=['"underused_flag": true']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_009",
        instruction="""
        Your role as a warehouse operations analyst involves monitoring storage utilization.
        Start by retrieving details of the leased warehouses.
        Check their current utilization percentages, and if any are found to be below (not equal but only below) 80%, update the warehouse record by including a flag to signify it is underused.
        Once these updates have been made, retrieve the warehouse details again to verify that the flag has been correctly added.
    """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Leased"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-02"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-06"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-09"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="UpdateWarehouse", kwargs={
                "warehouse_id": "WH-12",
                "updates": {"underused_flag": True}
            }),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
        ],
        outputs=['"underused_flag": true']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_010",
        instruction="""
        Acquire all outbound orders with a total value exceeding 100,000.
        Determine if these orders have a priority level of "High" or not.
        If the priority level is not high, alter their priority status to “High” for expedited processing.
        Verify details of the updated orders.
        Finally, report the ids of the revised orders.
    """,
        actions=[
            Action(name="GetHighValueOutboundOrders", kwargs={"min_value": 100000}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0002"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0005"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0006"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0007"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0008"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0009"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0010"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0011"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0013"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0015"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0016"}),
            Action(name="UpdateOutboundOrder",
                   kwargs={"order_id": "ORD-0005", "updates": {"priority_level": "High"}}),
            Action(name="UpdateOutboundOrder",
                   kwargs={"order_id": "ORD-0006", "updates": {"priority_level": "High"}}),
            Action(name="UpdateOutboundOrder",
                   kwargs={"order_id": "ORD-0007", "updates": {"priority_level": "High"}}),
            Action(name="UpdateOutboundOrder",
                   kwargs={"order_id": "ORD-0009", "updates": {"priority_level": "High"}}),
            Action(name="UpdateOutboundOrder",
                   kwargs={"order_id": "ORD-0010", "updates": {"priority_level": "High"}}),
            Action(name="UpdateOutboundOrder",
                   kwargs={"order_id": "ORD-0013", "updates": {"priority_level": "High"}}),
            Action(name="UpdateOutboundOrder",
                   kwargs={"order_id": "ORD-0015", "updates": {"priority_level": "High"}}),
            Action(name="UpdateOutboundOrder",
                   kwargs={"order_id": "ORD-0016", "updates": {"priority_level": "High"}}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0005"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0006"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0007"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0009"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0010"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0013"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0015"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0016"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["ORD-0005", "ORD-0006", "ORD-0007", "ORD-0009",
                                                              "ORD-0010", "ORD-0013", "ORD-0015", "ORD-0016"]})
        ],
        outputs=['[\n  "ORD-0005",\n  "ORD-0006",\n  "ORD-0007",\n  "ORD-0009",\n  "ORD-0010",\n  "ORD-0013",\n  "ORD-0015",\n  "ORD-0016"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_011",
        instruction="""
        As the logistics coordinator, your role is to oversee and handle shipment schedules.
        Consider only shipments categorized under priority_level medium.
        Access the shipment details and check their current status.
        If any shipment is labeled as “In Transit,” adjust the shipment's estimated arrival date by extending it by 3 days from the present expected arrival date.
        Upon updating, verify the new expected_arrival_date to ensure the modification has been implemented.
        Lastly, report the IDs of shipments where updates occurred.
    """,
        actions=[
            Action(name="FilterInboundShipments", kwargs={"key": "priority_level", "value": "Medium"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0001"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0003"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0005"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0015"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0018"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0023"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0025"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0028"}),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0001",
                "updates": {"expected_arrival_date": "2024-06-23"}
            }),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0003",
                "updates": {"expected_arrival_date": "2024-06-18"}
            }),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0005",
                "updates": {"expected_arrival_date": "2024-06-23"}
            }),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0009",
                "updates": {"expected_arrival_date": "2024-06-19"}
            }),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0011",
                "updates": {"expected_arrival_date": "2024-06-28"}
            }),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0015",
                "updates": {"expected_arrival_date": "2024-06-20"}
            }),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0018",
                "updates": {"expected_arrival_date": "2024-06-25"}
            }),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0023",
                "updates": {"expected_arrival_date": "2024-06-09"}
            }),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0025",
                "updates": {"expected_arrival_date": "2024-06-22"}
            }),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0028",
                "updates": {"expected_arrival_date": "2024-07-04"}
            }),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0001"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0003"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0005"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0015"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0018"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0023"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0025"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0028"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0009", "SHIP-0011",
                                                              "SHIP-0015", "SHIP-0018", "SHIP-0023", "SHIP-0025",
                                                              "SHIP-0028"
            ]})
        ],
        outputs=['[\n  "SHIP-0001",\n  "SHIP-0003",\n  "SHIP-0005",\n  "SHIP-0009",\n  "SHIP-0011",\n  "SHIP-0015",\n  "SHIP-0018",\n  "SHIP-0023",\n  "SHIP-0025",\n  "SHIP-0028"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_012",
        instruction="""
            You need to assess the performance of current carriers operating with the service mode Air.
            Initially, retrieve all carriers that are marked as active.
            Among these, identify carriers that specifically operate using Air transport.
            Determine the highest on-time delivery percentage and the top average rating for these air carriers.
            Multiple carriers might meet these criteria.
            If A and B achieve the highest on-time delivery percentage and B and C attain the highest average rating, consider all three for updates.
            For each of these carriers, modify their record by adding a note with the text "Best Performance by Air".
            Finally, provide the list of SCACs for all carriers whose records were updated with this note.
        """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetCarriersByMode", kwargs={"mode": "Air", "list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL",
                "OCBR", "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN",
                "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC", "EWDL"
            ]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["SKEX", "DLOG", "DFC", "SWDL", "SCF", "ALFS", "GPLS", "AAC", "EAC", "NAC", "ANAF", "NSC", "EWDL"]
            }),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["SKEX", "DLOG", "DFC", "SWDL", "SCF", "ALFS", "GPLS", "AAC", "EAC", "NAC", "ANAF", "NSC", "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "GPLS", "updates": {"notes": "Best Performance by Air"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "DFC", "updates": {"notes": "Best Performance by Air"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["GPLS", "DFC"]})

        ],
        outputs=['[\n  "GPLS",\n  "DFC"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_013",
        instruction="""
        As the inventory control specialist, it is your responsibility to ensure product quality and compliance.
        As of today's date, June 20, 2025, retrieve any inventory items that have surpassed their expiration date.
        For each item found to be expired, update its status in the inventory system to “Expired” to reflect its actual condition.
        After completing the updates, select one of these updated items to review its details and confirm the status change was properly executed.
    """,
        actions=[
            Action(name="GetExpiredInventory", kwargs={"today": "2025-06-20"}),
            Action(name="UpdateInventory", kwargs={
                "inventory_id": "INV-0003",
                "updates": {"status": "Expired"}
            }),
            Action(name="UpdateInventory", kwargs={
                "inventory_id": "INV-0008",
                "updates": {"status": "Expired"}
            }),
            Action(name="UpdateInventory", kwargs={
                "inventory_id": "INV-0024",
                "updates": {"status": "Expired"}
            }),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"})
        ],
        outputs=['"status": "Expired"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_014",
        instruction="""
            It is your task to assess the performance of active carriers operating with the service mode Sea.
            Start by acquiring all carriers that are currently listed as active.
            From there, pinpoint the carriers that specifically use the Sea mode of transport.
            For these sea carriers, compute both the highest on-time delivery percentage and the top average rating.
            There may be several carriers that fit these criteria.
            If A and B reach the highest on-time delivery percentage and B and C obtain the highest average rating, consider all three carriers for updates.
            For each of these outstanding carriers, change their record by appending a note with the phrase "Best Performance by Sea".
            Finally, compile a list of the SCACs for all carriers that were updated with this note.
        """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetCarriersByMode", kwargs={"mode": "Sea", "list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL",
                "OCBR", "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN",
                "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC", "EWDL"
            ]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "OCBR", "GOCN", "ALFS", "NRMC", "PSLN", "SATL"]
            }),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "OCBR", "GOCN", "ALFS", "NRMC", "PSLN", "SATL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SATL"}),
            Action(name="UpdateCarrier",
                   kwargs={"carrier_scac": "SKEX", "updates": {"notes": "Best Performance by Sea"}}),
            Action(name="UpdateCarrier",
                   kwargs={"carrier_scac": "ALFS", "updates": {"notes": "Best Performance by Sea"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["SKEX", "ALFS"]})

        ],
        outputs=['[\n  "SKEX",\n  "ALFS"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_015",
        instruction="""
                Your task is to evaluate the performance of active carriers operating with the service mode Truck.
                First, gather all carriers that are recognized as active.
                From this selection, filter for carriers that primarily operate with Truck transport.
                Within these truck carriers, assess both the highest on-time delivery percentage and the top average rating.
                Several carriers may fit these descriptors.
                If A and B achieve the maximum on-time delivery percentage and B and C achieve the maximum average rating, include all three carriers for updates.
                Update each of these high-performing carriers' records by inserting a note with the words "Best Performance by Truck".
                Finally, deliver a list of the SCACs for all carriers whose records included this note.
            """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetCarriersByMode", kwargs={"mode": "Truck", "list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL",
                "OCBR", "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN",
                "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC", "EWDL"
            ]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NSTS","SKEX", "DLOG", "MEDL", "SWDL", "MTRL", "ALFS", "GPLS", "EWDL"]
            }),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["NSTS","SKEX", "DLOG", "MEDL", "SWDL", "MTRL", "ALFS", "GPLS", "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
            Action(name="UpdateCarrier",
                   kwargs={"carrier_scac": "GPLS", "updates": {"notes": "Best Performance by Truck"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["GPLS"]})

        ],
        outputs=['[\n  "GPLS"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_016",
        instruction="""
        As the product data analyst, your task is to ensure correct storage classifications.
        Start by obtaining the information of all products classified under “Pharmaceuticals.
        ” Examine each product entry to assess whether refrigerated storage is needed.
        For those requiring it, update the product record to include a “Cold Chain” flag to reflect special handling needs.
        Once updates are made, gather and verify the details of one of the updated products to ensure the changes took effect.
    """,
        actions=[
            Action(name="GetProductsByCategory", kwargs={"category": "Pharmaceuticals"}),
            Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
            Action(name="GetProductBySku", kwargs={"sku": "PHRM-DRUG-S19"}),
            Action(name="GetProductsByStorageRequirement", kwargs={"keyword": "refrigerated"}),
            Action(name="UpdateProduct", kwargs={
                "sku": "PHRM-VACC-D4",
                "updates": {"cold_chain_flag": True}
            }),
            Action(name="UpdateProduct", kwargs={
                "sku": "PHRM-DRUG-S19",
                "updates": {"cold_chain_flag": True}
            }),
            Action(name="GetProductBySku", kwargs={"sku": "PHRM-DRUG-S19", })
        ],
        outputs=['"cold_chain_flag": true']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_017",
        instruction="""
        As the inventory quality control analyst, your job is to oversee warehouse stock conditions.
        Identify inventory items in warehouse WH-03 with any damaged quantity greater than zero.
        Acquire these items and modify their status to “Under Review” to start quality inspection processes.
        Following the record updates, compute and present the total units marked as damaged among these items for supporting further actions.
    """,
        actions=[
            Action(name="GetInventoryByWarehouse", kwargs={"warehouse_id": "WH-03"}),
            Action(name="GetInventoryWithDamage",
                   kwargs={"list_of_ids": ["INV-0002", "INV-0014", "INV-0017", "INV-0021", "INV-0025"]}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0002", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0017", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0021", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0025", "updates": {"status": "Under Review"}}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0002"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0017"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0021"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0025"}),
            Action(name="CalculateTotal", kwargs={
                "json": "inventory",
                "key": "inventory_id",
                "value": "quantity_damaged",
                "list_of_ids": ["INV-0002", "INV-0017", "INV-0021", "INV-0025"]
            })
        ],
        outputs=["22"]
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_018",
        instruction="""
                Your responsibility is to assess the active carriers' performance operating in the Rail service mode.
                Commence by collecting all carriers currently identified as active.
                From this selection, single out carriers that operate particularly using the Rail mode of transport.
                For these rail carriers, ascertain both the maximum on-time delivery percentage and the highest average rating.
                Multiple carriers may align with these criteria.
                If A and B match the max on-time delivery percentage and B and C match the max average rating, consider all three carriers for updates.
                Update the records of each top-performing carrier by appending an attribute notes with the value "Best Performance by Rail".
                Lastly, deliver a list comprising the SCACs of all carriers updated with this note.
            """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetCarriersByMode", kwargs={"mode": "Rail", "list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL",
                "OCBR", "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN",
                "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC", "EWDL"
            ]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MTRL", "GOCN", "ALFS"]
            }),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MTRL", "GOCN", "ALFS"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="UpdateCarrier",
                   kwargs={"carrier_scac": "SKEX", "updates": {"notes": "Best Performance by Rail"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="UpdateCarrier",
                   kwargs={"carrier_scac": "ALFS", "updates": {"notes": "Best Performance by Rail"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["SKEX", "ALFS"]})
        ],
        outputs=['[\n  "SKEX",\n  "ALFS"\n]']
    ),


    Task(
        annotator="ArpanMahatra1999",
        user_id="task_019",
        instruction="""
                Your responsibility is to assess the active carriers' performance operating in the Parcel service mode.
                Commence by collecting all carriers currently identified as active.
                From this selection, single out carriers that operate particularly using the Parcel mode of transport.
                For these parcel carriers, ascertain both the maximum on-time delivery percentage and the highest average rating.
                Multiple carriers may align with these criteria.
                If A and B match the max on-time delivery percentage and B and C match the max average rating, consider all three carriers for updates.
                Update the records of each top-performing carrier by appending an attribute notes with the value "Best Performance by Parcel".
                Lastly, deliver a list comprising the SCACs of all carriers updated with this note.
            """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetCarriersByMode", kwargs={"mode": "Parcel", "list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL",
                "OCBR", "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN",
                "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC", "EWDL"
            ]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["SWDL", "GPLS", "EWDL"]
            }),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["SWDL", "GPLS", "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
            Action(name="UpdateCarrier",
                   kwargs={"carrier_scac": "GPLS", "updates": {"notes": "Best Performance by Parcel"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["GPLS"]})
        ],
        outputs=['[\n  "GPLS"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_020",
        instruction="""
            In reviewing supplier compliance and performance, for both a particular case and broader preferred supplier evaluation, begin by acquiring supplier details for supplier ID SUP-1015.
            Determine if this supplier is designated as preferred and possesses at least one certification.
            Should either condition not be met, modify the supplier's record by including a compliance_alert attribute to indicate non-compliance.
            After updating, report the supplier's certifications, relationship_status, and the newly added compliance_alert.
            Then, examine all preferred suppliers within the system that also hold at least one certification.
            Identify the supplier(s) with the top performance rating among this group.
            If several suppliers share this peak performance rating, encompass all in the evaluation.
            Return the list of supplier IDs for these versatile, top-rated, preferred, and certified suppliers.
        """,
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1015"}),
            Action(name="UpdateSupplier", kwargs={
                "supplier_id": "SUP-1015",
                "updates": {"compliance_alert": True}
            }),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1015"}),
            Action(name="GetPreferredSuppliers", kwargs={}),
            Action(name="GetCertifiedSuppliers", kwargs={"list_of_ids": ["SUP-1002", "SUP-1005", "SUP-1010", "SUP-1013", "SUP-1016", "SUP-1019", "SUP-1029"]}),
            Action(name="CalculateAggregate", kwargs={
                        "agg": "max",
                        "json": "supplier_master",
                        "key": "supplier_id",
                        "value": "performance_rating",
                        "list_of_ids": ["SUP-1002", "SUP-1005", "SUP-1010", "SUP-1013", "SUP-1016", "SUP-1019", "SUP-1029"]
            }),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["SUP-1002", "SUP-1010", "SUP-1016", "SUP-1029"]})
        ],
        outputs=['["SUP-1002", "SUP-1010", "SUP-1016", "SUP-1029"]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_021",
        instruction="""
        As a logistics planner, you are tasked with optimizing carrier assignments for inbound shipments.
        Start by checking the shipment with ID SHIP-0021 to verify if the assigned carrier is currently active.
        Should the carrier be active, proceed to identify the active carrier with the best on-time delivery percentage.
        Reassign the shipment to this leading carrier.
        Upon completion of the update, confirm the modifications by retrieving and reviewing the updated shipment details.
    """,
        actions=[
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL", "OCBR", "SCF",
                                "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC",
                                "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="UpdateInboundShipment", kwargs={
                "shipment_id": "SHIP-0021",
                "updates": {
                    "carrier_scac": "GPLS",
                    "carrier_name": "Global Parcel Service"
                },
            }),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0021"}),
        ],
        outputs=[
            '"carrier_name": "Global Parcel Service"',
            '"carrier_scac": "GPLS"',
        ]
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_022",
            instruction="""
                As a logistics coordinator, your responsibility is to manage delayed inbound shipments.
                Start by pinpointing all inbound shipments presently marked as delayed and review their specifics.
                For each shipment, establish the associated warehouse.
                Next, evaluate the inventory stored within those warehouses.
                Among this inventory, find the one with the minimal number of damaged units.
                Select the shipment connected to the warehouse linked with this inventory.
                After pinpointing, change the status of that inbound shipment to "Planned" to reschedule its processing.
            """,
            actions=[
                Action(name="GetShipmentsByStatus", kwargs={"status": "Delayed"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0022"}),
                Action(name="GetInventoryByWarehouse", kwargs={"warehouse_id": "WH-04"}),
                Action(name="GetInventoryByWarehouse", kwargs={"warehouse_id": "WH-15"}),
                Action(name="GetInventoryWithDamage",
                       kwargs={"list_of_ids": ["INV-0015", "INV-0018", "INV-0016", "INV-0020"]}),
                Action(name="CalculateAggregate", kwargs={
                    "agg": "min",
                    "json": "inventory",
                    "key": "inventory_id",
                    "value": "quantity_damaged",
                    "list_of_ids": ["INV-0015", "INV-0018", "INV-0016", "INV-0020"]
                }),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0018"}),
                Action(name="UpdateInboundShipment", kwargs={
                    "shipment_id": "SHIP-0004",
                    "updates": {
                        "status": "Planned"
                    }
                }),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"})
            ],
            outputs=['"status": "Planned"']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_023",
        instruction="""
        Your role as a shipment analyst is to ensure the reliability of carrier assignments for outbound orders.
        Initiate by reviewing all outbound orders currently marked as “Shipped” and check if their assigned carriers are active.
        For any order linked to an inactive carrier, determine the top-rated active carrier from the available list.
        If two or more carriers share the top average rating, select the one with the superior on-time delivery percentage.
        Update the affected orders with the information of this top-rated carrier.
        Once all updates are finalized, confirm the modifications by reviewing the updated order data.
    """,
        actions=[
            Action(name="GetOrdersByStatus", kwargs={"status": "Shipped"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0003"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0006"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0007"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0012"}),
            Action(name="GetActiveCarriers", kwargs={"list_of_scacs": ["SWDL", "NSTS", "OCBR", "KCSM"]}),
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetTopRatedCarriers", kwargs={
                'list_of_scacs': ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL", "OCBR", "SCF",
                                  "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC",
                                  "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={
                "carrier_scac": "DFC"
            }),
            Action(name="GetCarrierByScac", kwargs={
                "carrier_scac": "GPLS"
            }),
            Action(name="UpdateOutboundOrder", kwargs={
                "order_id": "ORD-0012",
                "updates": {
                    "carrier_scac": "GPLS",
                    "carrier_name": "Global Parcel Service"
                }
            }),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0012"}),
        ],
        outputs=[
            '"carrier_name": "Global Parcel Service"',
            '"carrier_scac": "GPLS"'
        ]
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_024",
            instruction="""
                As a warehouse manager, you are responsible for assessing storage conditions and inventory quality.
                Begin your task by reviewing all expired inventory items that also have a damaged quantity exceeding 0, using 2025-06-20 as today's date for determining expiry.
                For each of these inventory items, change the status to "Replacement Needed" and find the associated warehouse.
                For each associated warehouse, update its status to "Needs Expansion".
                Lastly, verify the updates by examining the details of the affected inventories and warehouses.
                Return the list of updated inventories.
            """,
            actions=[
                Action(name="GetExpiredInventory", kwargs={'today': "2025-06-20"}),
                Action(name="GetInventoryWithDamage", kwargs={'list_of_ids': ["INV-0003", "INV-0008", "INV-0024"]}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0003"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0003",
                    "updates": {"status": "Replacement Needed"}
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0024",
                    "updates": {"status": "Replacement Needed"}
                }),
                Action(name="UpdateWarehouse", kwargs={
                    "warehouse_id": "WH-05",
                    "updates": {
                        "status": "Needs Expansion"
                    }
                }),
                Action(name="UpdateWarehouse", kwargs={
                    "warehouse_id": "WH-10",
                    "updates": {
                        "status": "Needs Expansion"
                    }
                }),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0003"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": ["INV-0003", "INV-0024"]})
            ],
            outputs=['[\n  "INV-0003",\n  "INV-0024"\n]']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_025",
        instruction="""
        As a supply chain analyst, your duty is to evaluate outbound orders valued over $100,000 that necessitate temperature control.
        For each order, check if the products are categorized as hazardous, fragile, or both.
        If an order includes hazardous products, append the note "BEWARE HAZARDOUS" to its extra notes.
        If it includes fragile products, append "BEWARE FRAGILE.
        " For orders that are both hazardous and fragile, append the combined note "BEWARE HAZARDOUS & FRAGILE.
        " After these updates, retrieve and verify the details of the updated orders to ensure the adjustments.
    """,
        actions=[
            Action(name="GetHighValueOutboundOrders", kwargs={"min_value": 100000}),
            Action(name="GetOrdersRequiringTemperatureControl", kwargs={
                "list_of_ids": [
                    "ORD-0002", "ORD-0005", "ORD-0006", "ORD-0007", "ORD-0008", "ORD-0009", "ORD-0010", "ORD-0011",
                    "ORD-0013", "ORD-0015", "ORD-0016"
                ]
            }),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0008"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0011"}),
            Action(name="UpdateOutboundOrder", kwargs={
                "order_id": "ORD-0011",
                "updates": {
                    "extra_note": "BEWARE FRAGILE"
                }
            }),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0011"}),
        ],
        outputs=['"extra_note": "BEWARE FRAGILE"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_026",
        instruction="""
        As a procurement specialist tasked with supplier qualifications oversight, examine the preferred suppliers roster to pinpoint those without valid ISO certifications.
        For any supplier missing this certification, adjust their certification_status to "ISO Certification Pending.
        " Once you've made these adjustments, fetch and verify the details for one of the amended suppliers to confirm the updates were applied accurately.
    """,
        actions=[
            Action(name="GetPreferredSuppliers", kwargs={}),
            Action(name="GetCertifiedSuppliers", kwargs={"certification": "ISO", "list_of_ids": [
                "SUP-1002", "SUP-1005", "SUP-1010", "SUP-1013", "SUP-1016", "SUP-1019", "SUP-1029"
            ]}),
            Action(name="UpdateSupplier", kwargs={
                "supplier_id": "SUP-1005",
                "updates": {
                    "certification_status": "ISO Certification Pending"
                }
            }),
            Action(name="UpdateSupplier", kwargs={
                "supplier_id": "SUP-1010",
                "updates": {
                    "certification_status": "ISO Certification Pending"
                }
            }),
            Action(name="UpdateSupplier", kwargs={
                "supplier_id": "SUP-1029",
                "updates": {
                    "certification_status": "ISO Certification Pending"
                }
            }),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1029"}),
        ],
        outputs=['"certification_status": "ISO Certification Pending"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_027",
        instruction="""
        Serving as an inventory controller focused on maintaining stock quality in warehouses, on May 25, 2025, evaluate all warehouses holding expired inventory items.
        For each such warehouse, change its status to “Restock Needed” and set all expired inventory to “On Hold” to stop further use.
        After executing these updates, fetch and review the inventory details to verify the status changes are correctly enacted.
    """,
        actions=[
            Action(name="GetExpiredInventory", kwargs={'today': '2025-05-25'}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0003"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
            Action(name="UpdateInventory", kwargs={
                "inventory_id": "INV-0003",
                "updates": {
                    "stock_status": "On Hold"
                }
            }),
            Action(name="UpdateInventory", kwargs={
                "inventory_id": "INV-0024",
                "updates": {
                    "stock_status": "On Hold"
                }
            }),
            Action(name="UpdateWarehouse", kwargs={
                "warehouse_id": "WH-05",
                "updates": {
                    "status": "Restock Needed"
                }
            }),
            Action(name="UpdateWarehouse", kwargs={
                "warehouse_id": "WH-10",
                "updates": {
                    "status": "Restock Needed"
                }
            }),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0003"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
        ],
        outputs=['"stock_status": "On Hold"']
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_028",
            instruction="""
                As a shipment auditor, your role is to ensure compliance of carriers handling inbound shipments.
                Initiate by examining all inbound shipments labeled as "In Transit.
                "
                For each one, confirm if the designated carrier is still active.
                Identify the active carrier with the top average rating.
                Check all shipments to find the one linked to this carrier and annotate those shipments with "Best Carrier.
                "
                After handling all relevant shipments, document the top average rating.
            """,
            actions=[
                Action(name="GetShipmentsByStatus", kwargs={"status": "In Transit"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0001"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0003"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0005"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0008"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0009"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0011"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0012"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0013"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0014"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0015"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0018"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0020"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0021"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0023"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0024"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0025"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0026"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0028"}),
                Action(name="GetActiveCarriers", kwargs={
                    "list_of_scacs": [
                        "NSTS", "DLOG", "MEDL", "MTRL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "SATL", "NAC"
                    ]
                }),
                Action(name="CalculateAggregate", kwargs={
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": ["NSTS", "DLOG", "MEDL", "MTRL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "SATL",
                                    "NAC"]
                }),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0014", "updates": {"notes": "Best Carrier"}}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0023", "updates": {"notes": "Best Carrier"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0014"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0023"}),
            ],
            outputs=['4.9']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_029",
            instruction="""
                In your role as a product manager reviewing pharmaceutical storage needs, first, obtain a list of products requiring refrigeration.
                Analyze the details, focusing on their weight specifically.
                Determine the product with the smallest weight.
                Upon identification, append a note labeled "LOW WEIGHT PRODUCT" to this product to emphasize its lightness.
                Lastly, review and validate the updated product details.
            """,
            actions=[
                Action(name="GetProductsByCategory", kwargs={"category": "Pharmaceuticals"}),
                Action(name="GetProductsByStorageRequirement",
                       kwargs={"keyword": "refrigerated", 'list_of_ids': ["PHRM-VACC-D4", "PHRM-DRUG-S19"]}),
                Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="GetProductBySku", kwargs={"sku": "PHRM-DRUG-S19"}),
                Action(name="CalculateAggregate", kwargs={
                    "agg": "min",
                    "json": "product_master",
                    "key": "sku",
                    "value": "weight_kg",
                    "list_of_ids": ["PHRM-VACC-D4", "PHRM-DRUG-S19"]
                }),
                Action(name="UpdateProduct", kwargs={"sku": "PHRM-VACC-D4", "updates": {
                    "notes": "LOW WEIGHT PRODUCT"
                }}),
                Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
            ],
            outputs=['"sku": "PHRM-VACC-D4"']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_030",
            instruction="""
                As an inventory specialist, your task is to manage damaged stock.
                Start by identifying all inventory entries where the damaged quantity exceeds 0.
                For each of these, revise the status attribute to "Pending Restock" to denote pending resolution or replacement.
                After the updates, check the details of the inventory items to assure the modifications are accurately applied.
                Finally, compile and return the updated inventory IDs.
            """,
            actions=[
                Action(name="GetInventoryWithDamage", kwargs={}),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0001",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0002",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0003",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0005",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0006",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0007",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0010",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0013",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0015",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0016",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0017",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0018",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0020",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0021",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0022",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0023",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0024",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="UpdateInventory", kwargs={
                    "inventory_id": "INV-0025",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0001"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0002"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0003"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0005"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0006"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0007"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0013"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0017"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0018"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0021"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0022"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0023"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0025"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": [
                    "INV-0001", "INV-0002", "INV-0003", "INV-0005", "INV-0006", "INV-0007",
                    "INV-0010", "INV-0013", "INV-0015", "INV-0016", "INV-0017", "INV-0018",
                    "INV-0020", "INV-0021", "INV-0022", "INV-0023", "INV-0024", "INV-0025"
                ]})
            ],
            outputs=['[\n  "INV-0001",\n  "INV-0002",\n  "INV-0003",\n  "INV-0005",\n  "INV-0006",\n  "INV-0007",\n  "INV-0010",\n  "INV-0013",\n  "INV-0015",\n  "INV-0016",\n  "INV-0017",\n  "INV-0018",\n  "INV-0020",\n  "INV-0021",\n  "INV-0022",\n  "INV-0023",\n  "INV-0024",\n  "INV-0025"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_031",
            instruction="""
                You are a carrier analyst.
                Your responsibility is to initiate by accessing the details of shipment SHIP-0004 and determine the designated carrier.
                Verify if this carrier is presently active.
                In case the carrier is not active, continue to search for an active carrier that utilizes the same mode of transport and possesses the highest average rating among those available.
                If two or more carriers share the highest average rating, select the carrier among them with the highest on-time delivery percentage.
                Upon identification, update the inbound shipment to allocate this top-rated active carrier.
            """,
            actions=[
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "POCL"}),
                Action(name="GetActiveCarriers", kwargs={}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SATL"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
                Action(name="CalculateAggregate", kwargs={
                    'agg': 'max',
                    'json': 'carriers',
                    'key': 'scac',
                    'value': 'performance_metrics',
                    'value2': 'average_rating',
                    'list_of_ids': ['NSTS', 'SKEX', 'DLOG', 'MEDL', 'DFC', 'SWDL', 'MTRL', 'OCBR', 'SCF', 'GOCN', 'ALFS', 'NRMC', 'GPLS', 'PSLN', 'AAC', 'SATL', 'EAC', 'NAC', 'ANAF', 'NSC', 'EWDL']
                }),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0004", "updates": {
                    "carrier_scac": "ALFS",
                    "carrier_name": "Alpine Freight Solutions",
                }}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
            ],
            outputs=['"carrier_scac": "ALFS"']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_032",
            instruction="""
                As an inventory manager, start by finding all warehouses with inventory records containing damaged items.
                Among these warehouses, ascertain which one exhibits the lowest current utilization percentage.
                Once identified, update that warehouse by adding an attribute note with the value "Lowest Utilization Percent" to flag it for operational review.
            """,
            actions=[
                Action(name="GetInventoryWithDamage", kwargs={}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0001"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0002"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0003"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0005"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0006"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0007"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0013"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0017"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0018"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0021"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0022"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0023"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0025"}),
                Action(name="CalculateAggregate", kwargs={
                    'agg': 'min',
                    'json': 'warehouses',
                    'key': "warehouse_id",
                    'value': 'current_utilization_percentage',
                    'list_of_ids': ['WH-01', 'WH-02', 'WH-03', 'WH-04',
                                    'WH-05', 'WH-07', 'WH-08', 'WH-09',
                                    'WH-10', 'WH-12', 'WH-14', 'WH-15']
                }),
                Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-07", "updates": {
                    "note": "Lowest Utilization Percent"
                }}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"})
            ],
            outputs=['"note": "Lowest Utilization Percent"']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_033",
            instruction="""
                You are a product compliance officer.
                Commence by locating all hazardous products listed in the inventory.
                Examine each of these products to confirm whether their storage requirements include the term "hazmat".
                For any product where this requirement is absent or incorrect, update the product record by adding a notes attribute with the value "BEWARE HAZMAT" to ensure proper handling protocols are followed.
                After updating, assess the details of the affected products.
                Check the inventories associated with these products and verify that those inventories have quantities available.
                Ultimately, return the list of SKUs of all products that were updated.
            """,
            actions=[
                Action(name="GetHazmatProducts", kwargs={}),
                Action(name="GetProductsByStorageRequirement", kwargs={"keyword": "hazmat", 'list_of_ids': [
                    "PHRM-VACC-D4",
                    "CHEM-SOLV-K11",
                    "TECH-BATT-Q17",
                    "ELEC-SMART-W23"
                ]}),
                Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="UpdateProduct", kwargs={"sku": "PHRM-VACC-D4",
                                                      'updates': {"notes": "BEWARE HAZMAT"}}),
                Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="GetProductBySku", kwargs={"sku": "ELEC-SMART-W23"}),
                Action(name="UpdateProduct", kwargs={"sku": "ELEC-SMART-W23",
                                                      'updates': {"notes": "BEWARE HAZMAT"}}),
                Action(name="GetProductBySku", kwargs={"sku": "ELEC-SMART-W23"}),
                Action(name="FilterInventory", kwargs={"key": "sku", "value": "PHRM-VACC-D4"}),
                Action(name="FilterInventory", kwargs={"key": "sku", "value": "ELEC-SMART-W23"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0023"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": ["PHRM-VACC-D4", "ELEC-SMART-W23"]})
            ],
            outputs=['[\n  "PHRM-VACC-D4",\n  "ELEC-SMART-W23"\n]']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_034",
        instruction="""
        As a shipment coordinator, your duty is to manage inbound shipments with a status of “Delayed.
        ” Examine all such shipments and identify any that are assigned to inactive carriers.
        For each affected shipment, reassign it to an active carrier to ensure timely handling.
        After completing the reassignments, obtain and examine the details of the updated shipments to confirm that the changes have been applied correctly.
    """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "Delayed"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0022"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "POCL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0004",
                                                           "updates": {"carrier_scac": "GOCN",
                                                                       "carrier_name": "Global Ocean Carriers"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"})
        ],
        outputs=['"carrier_scac": "GOCN"']
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_035",
            instruction="""
            As a supplier relations manager, scrutinize preferred suppliers and verify their certification status by reviewing details.
            If preferred suppliers lack ISO certifications, update them with the attribute note "ISO certification required".
            Among preferred suppliers with certifications "ISO",
            Identify the supplier with the least standard lead time days.
            Update the supplier with the attribute note "Least Standard Lead Time Days".
        """,
            actions=[
                Action(name="GetPreferredSuppliers", kwargs={}),
                Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1002"}),
                Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1005"}),
                Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1010"}),
                Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1013"}),
                Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1016"}),
                Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1019"}),
                Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1029"}),
                Action(name="GetCertifiedSuppliers", kwargs={"certification": "ISO", "list_of_ids": ["SUP-1002",
                                                                                                       "SUP-1005",
                                                                                                       "SUP-1010",
                                                                                                       "SUP-1013",
                                                                                                       "SUP-1016",
                                                                                                       "SUP-1019",
                                                                                                       "SUP-1029"]}),
                Action(name="UpdateSupplier",
                       kwargs={'supplier_id': "SUP-1005", "updates": {"note": "ISO certification required"}}),
                Action(name="GetSupplierById", kwargs={'supplier_id': "SUP-1005"}),
                Action(name="UpdateSupplier",
                       kwargs={'supplier_id': "SUP-1010", "updates": {"note": "ISO certification required"}}),
                Action(name="GetSupplierById", kwargs={'supplier_id': "SUP-1010"}),
                Action(name="UpdateSupplier",
                       kwargs={'supplier_id': "SUP-1029", "updates": {"note": "ISO certification required"}}),
                Action(name="GetSupplierById", kwargs={'supplier_id': "SUP-1029"}),
                Action(name="CalculateAggregate", kwargs={
                    'agg': 'min',
                    'json': 'supplier_master',
                    'key': 'supplier_id',
                    'value': 'standard_lead_time_days',
                    'list_of_ids': ["SUP-1002", "SUP-1013", "SUP-1016", "SUP-1019"]
                }),
                Action(name="UpdateSupplier",
                       kwargs={'supplier_id': "SUP-1019", "updates": {"note": "Least Standard Lead Time Days"}}),
                Action(name="GetSupplierById", kwargs={'supplier_id': "SUP-1019"})
            ],
            outputs=['"supplier_id": "SUP-1019"']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_036",
        instruction="""
        As a warehouse replenishment officer, handle the identification of all inventory with an available quantity less than 100, ensuring there is no damaged stock (quantity_damaged == 0).
        Such items must be flagged for replenishment by updating their status to “LOW STOCK”.
        After applying updates, verify a selection of them and ultimately return the ids of the inventory marked as LOW STOCK.
    """,
        actions=[
            Action(name="GetInventoryWithDamage", kwargs={"less_than_threshold": "True", "threshold": 1}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0008"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0009"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0011"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0012"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0014"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0019"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0009", "updates": {"status": "LOW STOCK"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0014", "updates": {"status": "LOW STOCK"}}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0009"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0014"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["INV-0009", "INV-0014"]})
        ],
        outputs=['[\n  "INV-0009",\n  "INV-0014"\n]']
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_037",
            instruction="""
            Taking on the role of a warehouse replenishment officer, your task is to pinpoint all inventory with an available quantity below 100 and damaged stock less than 10.
            These items should be identified for replenishment by setting their status to “LOW STOCK”.
            When the updates are completed, check a few and then provide the ids of the inventory noted as LOW STOCK.
        """,
            actions=[
                Action(name="GetInventoryWithDamage", kwargs={"less_than_threshold": "True", "threshold": 10}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0002"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0005"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0006"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0008"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0009"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0011"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0012"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0013"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0014"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0017"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0018"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0019"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0021"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0022"}),
                Action(name="UpdateInventory",
                       kwargs={"inventory_id": "INV-0009", "updates": {"status": "LOW STOCK"}}),
                Action(name="UpdateInventory",
                       kwargs={"inventory_id": "INV-0014", "updates": {"status": "LOW STOCK"}}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0009"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0014"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": ["INV-0009", "INV-0014"]})
            ],
            outputs=['[\n  "INV-0009",\n  "INV-0014"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_038",
            instruction="""
                As a warehouse operations manager, start by observing all warehouses that currently contain any inventory items with damage.
                Identify warehouses where at least one inventory item has a damaged quantity greater than zero.
                Modify the status of these warehouses to "Attention Required" to signal the necessity for inspection or corrective measures.
                Lastly, review and confirm all updated warehouse details to ensure that status changes have been accurately implemented.
            """,
            actions=[
                Action(name="GetInventoryWithDamage", kwargs={}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0001"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0002"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0003"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0005"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0006"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0007"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0013"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0017"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0018"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0021"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0022"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0023"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0025"}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-01", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-02", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-03", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-04", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-05", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-07", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-08", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-09", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-10", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-12", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-14", "updates": {"status": "Attention Required"}}),
                Action(name="UpdateWarehouse",
                       kwargs={"warehouse_id": "WH-15", "updates": {"status": "Attention Required"}}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-01"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-02"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-03"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-08"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-09"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-14"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": [
                    "WH-01", "WH-02", "WH-03", "WH-04", "WH-05",
                    "WH-07", "WH-08", "WH-09", "WH-10",
                    "WH-12", "WH-14", "WH-15"
                ]})
            ],
            outputs=['[\n  "WH-01",\n  "WH-02",\n  "WH-03",\n  "WH-04",\n  "WH-05",\n  "WH-07",\n  "WH-08",\n  "WH-09",\n  "WH-10",\n  "WH-12",\n  "WH-14",\n  "WH-15"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_039",
            instruction="""
            Acting as a product manager, locate products requiring "refrigerated" storage conditions while ensuring their lifecycle status is active.
            Assess the inventory associated with these products, and if the quantity damaged exceeds 0, append attribute notes "Replacement Required".
            Determine the maximum unit price among these products.
        """,
            actions=[
                Action(name="GetProductsByStorageRequirement", kwargs={"keyword": "refrigerated"}),
                Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="GetProductBySku", kwargs={"sku": "PHRM-DRUG-S19"}),
                Action(name="GetProductBySku", kwargs={"sku": "FOOD-FLWR-X24"}),
                Action(name="FilterInventory", kwargs={"key": "sku", "value": "PHRM-VACC-D4"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
                Action(name="FilterInventory", kwargs={"key": "sku", "value": "PHRM-DRUG-S19"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0019"}),
                Action(name="FilterInventory", kwargs={"key": "sku", "value": "FOOD-FLWR-X24"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
                Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0024", "updates": {"notes": "Replacement Required"}}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
                Action(name="CalculateAggregate", kwargs={
                    "agg": "max",
                    "json": "product_master",
                    "key": "sku",
                    "value": "unit_price",
                    "list_of_ids": ["PHRM-VACC-D4", "PHRM-DRUG-S19", "FOOD-FLWR-X24"]
                }),
            ],
            outputs=['"sku": "PHRM-DRUG-S19"', '"unit_price": 1800.0']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_040",
            instruction="""
                You must oversee the transfer of 300 units from inventory INV-0025 to an alternate one due to a problem with the original stock.
                Start by confirming that the source inventory possesses at least 300 units available.
                Then, identify another inventory bearing the same SKU but a distinct ID and review its present quantity.
                Deduct 300 units from the source and add them to the destination inventory.
                Add notes to both inventories regarding the changes so that employees could later adjust the total value.
                The total value corresponding to 300 units should be subtracted from the source inventory, so add the note "300 units removed, total value change pending".
                Similarly, the total value for 300 units should be included in the destination inventory, prompting the note "300 units added, total value change pending".
                Finally, verify that the updates are accurately reflected in both inventories and return the current quantity available in the destination inventory.
            """,
            actions=[
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0025"}),
                Action(name="FilterInventory", kwargs={"key": "sku", "value": "ELEC-CHIP-A1"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0001"}),
                Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0025", "updates": {
                    "quantity_on_hand": 7700, "quantity_available": 7700
                }}),
                Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0001", "updates": {
                    "quantity_on_hand": 15300, "quantity_available": 12800
                }}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0025"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0001"}),
                Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0025", "updates": {
                    "note": "300 units removed, total value change pending"
                }}),
                Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0001", "updates": {
                    "note": "300 units added, total value change pending"
                }}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0025"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0001"}),
            ],
            outputs=['12800']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_041",
            instruction="""
            As an order quality auditor, your task is to handle orders requiring temperature-controlled transport.
            Verify that assigned carriers fulfill these criteria and remain active.
            Distinguish between active and inactive assigned carriers within these orders.
            Substitute inactive carriers with the highest rated active carriers for these orders.
            If there's only one active carrier, you can skip checking for the highest rating.
            Update orders with inactive carriers by assigning them to a qualified top-rated active carrier based on average rating.
            Eventually, inspect the details of the modified orders and provide the list of those updated.
        """,
            actions=[
                Action(name="GetOrdersRequiringTemperatureControl", kwargs={}),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0004"}),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0008"}),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0011"}),
                Action(name="GetActiveCarriers", kwargs={"list_of_scacs": ["SWDL", "LTMG", "SAAW"]}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
                Action(name="UpdateOutboundOrder", kwargs={
                    "order_id": "ORD-0008",
                    "updates": {
                        "carrier_scac": "SWDL",
                        "carrier_name": "SwiftDelivery"
                    }
                }),
                Action(name="UpdateOutboundOrder", kwargs={
                    "order_id": "ORD-0011",
                    "updates": {
                        "carrier_scac": "SWDL",
                        "carrier_name": "SwiftDelivery"
                    }
                }),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0008"}),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0011"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": ["ORD-0008", "ORD-0011"]})
            ],
            outputs=['[\n  "ORD-0008",\n  "ORD-0011"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_042",
            instruction="""
            As an inventory replenishment coordinator, your role is to locate expired inventory while assuming today's date is "2026-07-20.
            "
            Mark inventory in need of replenishment with 'notes' stating 'Replenishment Needed.
            '
            After this step, inspect the details of the updated inventory.
            Provide the list of ids corresponding to the updated inventory.
        """,
            actions=[
                Action(name="GetExpiredInventory", kwargs={"today": "2026-07-20"}),
                Action(name="UpdateInventory",
                       kwargs={"inventory_id": "INV-0003", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="UpdateInventory",
                       kwargs={"inventory_id": "INV-0004", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="UpdateInventory",
                       kwargs={"inventory_id": "INV-0008", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="UpdateInventory",
                       kwargs={"inventory_id": "INV-0011", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="UpdateInventory",
                       kwargs={"inventory_id": "INV-0019", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="UpdateInventory",
                       kwargs={"inventory_id": "INV-0022", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="UpdateInventory",
                       kwargs={"inventory_id": "INV-0024", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0003"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0008"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0011"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0019"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0022"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": ["INV-0003", "INV-0004", "INV-0008", "INV-0011", "INV-0019", "INV-0022", "INV-0024"]})
            ],
            outputs=['[\n  "INV-0003",\n  "INV-0004",\n  "INV-0008",\n  "INV-0011",\n  "INV-0019",\n  "INV-0022",\n  "INV-0024"\n]']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_043",
        instruction="""
        You are a supplier compliance officer in charge of checking the certification status of preferred suppliers for IEC compliance.
        Pinpoint suppliers with expired or missing IEC certifications, and adjust their certification_status to "Compliance Review" to indicate the need for further action.
        After executing these updates, fetch and assess the details of one updated supplier to ensure the changes are accurately reflected.
    """,
        actions=[
            Action(name="GetPreferredSuppliers", kwargs={}),
            Action(name="GetCertifiedSuppliers", kwargs={"certification": "IEC", "list_of_ids": [
                "SUP-1002", "SUP-1005", "SUP-1010", "SUP-1013", "SUP-1016", "SUP-1019", "SUP-1029"
            ]}),
            Action(name="UpdateSupplier",
                   kwargs={"supplier_id": "SUP-1002", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="UpdateSupplier",
                   kwargs={"supplier_id": "SUP-1005", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="UpdateSupplier",
                   kwargs={"supplier_id": "SUP-1010", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="UpdateSupplier",
                   kwargs={"supplier_id": "SUP-1013", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="UpdateSupplier",
                   kwargs={"supplier_id": "SUP-1016", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="UpdateSupplier",
                   kwargs={"supplier_id": "SUP-1019", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="UpdateSupplier",
                   kwargs={"supplier_id": "SUP-1029", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1029"})
        ],
        outputs=['"certification_status": "Compliance Review"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_044",
        instruction="""
        Your duty as a warehouse performance analyst involves monitoring levels of inventory damage.
        Detect any inventory items with counts exceeding 100 damaged goods and monitor the warehousing locations of these items.
        For any warehouse that matches this condition, annotate it with a note indicating “High Damaged Goods.
        ” Once these updates are applied, examine and confirm the details of one of the highlighted warehouses to validate the note's presence.
    """,
        actions=[
            Action(name="GetInventoryWithDamage", kwargs={'threshold': 100}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
            Action(name="UpdateWarehouse",
                   kwargs={"warehouse_id": "WH-12", "updates": {"notes": "High Damaged Goods."}}),
            Action(name="UpdateWarehouse",
                   kwargs={"warehouse_id": "WH-04", "updates": {"notes": "High Damaged Goods."}}),
            Action(name="UpdateWarehouse",
                   kwargs={"warehouse_id": "WH-15", "updates": {"notes": "High Damaged Goods."}}),
            Action(name="UpdateWarehouse",
                   kwargs={"warehouse_id": "WH-10", "updates": {"notes": "High Damaged Goods."}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"})
        ],
        outputs=['"notes": "High Damaged Goods."']
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_045",
            instruction="""
            In the capacity of a product quality analyst, identify products marked as hazardous and evaluate each one individually.
            If there are no storage requirements regarding hazmat class, append notes saying "HAZMAT SPECIFICATION REQUIRED.
            "
            At the end, review the details of the updated products and compile the list of SKUs for these products.
        """,
            actions=[
                Action(name="GetHazmatProducts", kwargs={}),
                Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="GetProductBySku", kwargs={"sku": "CHEM-SOLV-K11"}),
                Action(name="GetProductBySku", kwargs={"sku": "TECH-BATT-Q17"}),
                Action(name="GetProductBySku", kwargs={"sku": "ELEC-SMART-W23"}),
                Action(name="UpdateProduct",
                       kwargs={"sku": "PHRM-VACC-D4", "updates": {"notes": "HAZMAT SPECIFICATION REQUIRED"}}),
                Action(name="UpdateProduct",
                       kwargs={"sku": "ELEC-SMART-W23", "updates": {"notes": "HAZMAT SPECIFICATION REQUIRED"}}),
                Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="GetProductBySku", kwargs={"sku": "ELEC-SMART-W23"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": ["PHRM-VACC-D4", "ELEC-SMART-W23"]})
            ],
            outputs=['[\n  "PHRM-VACC-D4",\n  "ELEC-SMART-W23"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_046",
            instruction="""
            You are a shipment officer.
            Examine inbound shipments marked as Planned.
            Ensure the assigned carriers are operational.
            Determine the highest average rating among the carriers.
            Modify all relevant planned shipments to use the carrier with the best rating.
            The goal is to select the optimal carrier for the planned shipments.
            Provide the list of IDs for the shipments that were updated.
        """,
            actions=[
                Action(name="GetShipmentsByStatus", kwargs={"status": "Planned"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0006"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0030"}),
                Action(name="GetActiveCarriers", kwargs={'list_of_scacs': [
                    "DFC", "SCF", "SKEX", "EAC", "NSC", "ANAF"
                ]}),
                Action(name="CalculateAggregate", kwargs={
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": ["DFC", "SCF", "SKEX", "EAC", "NSC", "ANAF"]
                }),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0010", "updates": {"carrier_scac": "DFC", "carrier_name": "Desert Falcon Cargo"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0016", "updates": {"carrier_scac": "DFC", "carrier_name": "Desert Falcon Cargo"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0019", "updates": {"carrier_scac": "DFC", "carrier_name": "Desert Falcon Cargo"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0027", "updates": {"carrier_scac": "DFC", "carrier_name": "Desert Falcon Cargo"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0029", "updates": {"carrier_scac": "DFC", "carrier_name": "Desert Falcon Cargo"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": ["SHIP-0010", "SHIP-0016", "SHIP-0019", "SHIP-0027", "SHIP-0029"]})
            ],
            outputs=['[\n  "SHIP-0010",\n  "SHIP-0016",\n  "SHIP-0019",\n  "SHIP-0027",\n  "SHIP-0029"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_047",
            instruction="""
            You are a shipment officer.
            Analyze inbound shipments labeled as Planned.
            Verify that the assigned carriers have active status.
            Identify the top insurance coverage limit among the carriers.
            Adjust all these planned shipments, except the one with the carrier having the highest insurance coverage, to use the leading carrier in terms of insurance coverage.
            The aim is to employ the best carrier for the planned shipments.
            Furnish the list of IDs for the updated shipments.
        """,
            actions=[
                Action(name="GetShipmentsByStatus", kwargs={"status": "Planned"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0006"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0030"}),
                Action(name="GetActiveCarriers", kwargs={'list_of_scacs': [
                    "DFC", "SCF", "SKEX", "EAC", "NSC", "ANAF"
                ]}),
                Action(name="CalculateAggregate", kwargs={
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "insurance_details",
                    "value2": "coverage_limit_usd",
                    "list_of_ids": ["DFC", "SCF", "SKEX", "EAC", "NSC", "ANAF"]
                }),
                Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "SKEX",
                                                                "list_of_ids": ["SHIP-0006", "SHIP-0010", "SHIP-0016", "SHIP-0019", "SHIP-0027", "SHIP-0029", "SHIP-0030"]}),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0006", "updates": {"carrier_scac": "SKEX", "carrier_name": "Sakura Express"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0010", "updates": {"carrier_scac": "SKEX", "carrier_name": "Sakura Express"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0019", "updates": {"carrier_scac": "SKEX", "carrier_name": "Sakura Express"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0027", "updates": {"carrier_scac": "SKEX", "carrier_name": "Sakura Express"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0029", "updates": {"carrier_scac": "SKEX", "carrier_name": "Sakura Express"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0030", "updates": {"carrier_scac": "SKEX", "carrier_name": "Sakura Express"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0030"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": ["SHIP-0006", "SHIP-0010", "SHIP-0019", "SHIP-0027", "SHIP-0029", "SHIP-0030"]})
            ],
            outputs=['[\n  "SHIP-0006",\n  "SHIP-0010",\n  "SHIP-0019",\n  "SHIP-0027",\n  "SHIP-0029",\n  "SHIP-0030"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_048",
            instruction="""
            You are a shipment officer.
            Inspect inbound shipments having Planned status.
            Check that assigned carriers are currently active.
            Ascertain the highest on-time delivery percentage from among the carriers.
            Revise all these planned shipments to utilize the carrier with the leading on-time delivery percentage.
            The purpose is to apply the best carrier for the planned shipments.
            Present the list of IDs for the shipments that have been updated.
        """,
            actions=[
                Action(name="GetShipmentsByStatus", kwargs={"status": "Planned"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0006"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0030"}),
                Action(name="GetActiveCarriers", kwargs={'list_of_scacs': [
                    "DFC", "SCF", "SKEX", "EAC", "NSC", "ANAF"
                ]}),
                Action(name="CalculateAggregate", kwargs={
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": ["DFC", "SCF", "SKEX", "EAC", "NSC", "ANAF"]
                }),
                Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0010", "updates": {"carrier_scac": "DFC", "carrier_name": "Desert Falcon Cargo"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0016", "updates": {"carrier_scac": "DFC", "carrier_name": "Desert Falcon Cargo"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0019", "updates": {"carrier_scac": "DFC", "carrier_name": "Desert Falcon Cargo"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0027", "updates": {"carrier_scac": "DFC", "carrier_name": "Desert Falcon Cargo"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0029", "updates": {"carrier_scac": "DFC", "carrier_name": "Desert Falcon Cargo"}}),
                Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": ["SHIP-0010", "SHIP-0016", "SHIP-0019", "SHIP-0027", "SHIP-0029"]})
            ],
            outputs=['[\n  "SHIP-0010",\n  "SHIP-0016",\n  "SHIP-0019",\n  "SHIP-0027",\n  "SHIP-0029"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_049",
            instruction="""
            You are a warehouse audit specialist.
            Evaluate inventory with damage counts exceeding 50.
            Analyze warehouse details of these damaged inventories to verify if their utilization percentage surpasses 50%.
            Subsequently, change the warehouse status to 'Audit Completed' once reviewed.
            Finally, identify the least number of damaged quantities from the inventories reviewed.
            The aim is to determine a better threshold for what constitutes damaged inventory.
        """,
            actions=[
                Action(name="GetInventoryWithDamage", kwargs={'threshold': 50}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
                Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
                Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
                Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-12", "updates": {"status": "Audit Completed"}}),
                Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-04", "updates": {"status": "Audit Completed"}}),
                Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-15", "updates": {"status": "Audit Completed"}}),
                Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-10", "updates": {"status": "Audit Completed"}}),
                Action(name="CalculateAggregate", kwargs={
                    "agg": "min",
                    "json": "inventory",
                    "key": "inventory_id",
                    "value": "quantity_damaged",
                    "list_of_ids": ["INV-0010", "INV-0015", "INV-0020", "INV-0024"]
                })
            ],
            outputs=['"quantity_damaged": 120']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_050",
            instruction="""
            You are an orders management officer.
            Locate all outbound orders necessitating temperature control.
            Examine the specifics of these outbound orders.
            Verify whether these orders are classified as hazmat.
            Focus on orders that are non-hazmat.
            Discover the maximum and minimum temperature considerations for these orders.
            If the difference between maximum and minimum temperatures is less than 10,
            tag these orders with the note "Could be Grouped Together".
            Finally, review the information of these amended orders and supply the list of IDs for these updated orders.
        """,
            actions=[
                Action(name="GetOrdersRequiringTemperatureControl", kwargs={}),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0004"}),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0008"}),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0011"}),
                Action(name="CalculateAggregate", kwargs={
                    "agg": "both",
                    "json": "outbound_orders",
                    "key": "order_id",
                    "value": "temperature_celsius",
                    "list_of_ids": ["ORD-0004", "ORD-0008", "ORD-0011"]
                }),
                Action(name="UpdateOutboundOrder", kwargs={"order_id": "ORD-0004", "updates": {
                    "notes": "Could be Grouped Together"
                }}),
                Action(name="UpdateOutboundOrder", kwargs={"order_id": "ORD-0008", "updates": {
                    "notes": "Could be Grouped Together"
                }}),
                Action(name="UpdateOutboundOrder", kwargs={"order_id": "ORD-0011", "updates": {
                    "notes": "Could be Grouped Together"
                }}),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0004"}),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0008"}),
                Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0011"}),
                Action(name="ReturnIds", kwargs={"list_of_ids": ["ORD-0004", "ORD-0008", "ORD-0011"]})
            ],
            outputs=['[\n  "ORD-0004",\n  "ORD-0008",\n  "ORD-0011"\n]']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_051",
        instruction="""
        You serve as a logistics coordinator tasked with overseeing planned inbound shipments.
        Start by examining all intended inbound shipments to single out the one with the earliest anticipated departure date.
        Evaluate the carrier associated with this shipment to verify whether the carrier is active.
        If the carrier is active, update the carrier with the note "Shipment of highest priority scheduled".
        Additionally, annotate the shipment with "Shipment of highest priority".
        As a final step, review the updated inbound shipment details to ensure the note has been correctly added.
    """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "Planned"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0006"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0010"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0016"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0019"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0027"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0029"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0030"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "ANAF", "updates": {
                "note": "Shipment of highest priority scheduled"
            }}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0029", "updates": {
                "note": "Shipment of highest priority"
            }}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0029"}),

        ],
        outputs=[
            '"note": "Shipment of highest priority"',
        ]
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_052",
        instruction="""
            You act as an inventory supervisor overseeing warehouse stock conditions.
            Identify all warehouses that hold inventory items with at least 200 damaged goods.
            For each warehouse identified, devise a restocking plan and update their status to “Restocking Planned” to ensure their prompt replenishment.
            After completing all updates, verify that the modifications have been applied successfully by examining the refreshed warehouse records.
        """,
        actions=[
            Action(name="GetInventoryWithDamage", kwargs={'threshold': 200}),
            Action(name='GetInventoryById', kwargs={"inventory_id": "INV-0010"}),
            Action(name='GetInventoryById', kwargs={"inventory_id": "INV-0020"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-12", "updates": {"status": "Restocking Planned"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-15", "updates": {"status": "Restocking Planned"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
        ],
        outputs=['"status": "Restocking Planned"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_053",
        instruction="""
            Your role as a product compliance specialist involves ensuring the correct handling of hazardous products.
            Begin by locating all products labeled as hazardous and confirm that their storage requirements are correctly documented.
            For any product lacking or having incorrect storage instructions, adjust the record as needed.
            If the storage requirements fail to include the Hazmat class information, append the note “Hazmat Class mentioned” to guarantee compliance.
            After making these updates, inspect the updated product details to verify the changes have been accurately implemented.
        """,
        actions=[
            Action(name="GetHazmatProducts", kwargs={}),
            Action(name="GetProductsByStorageRequirement", kwargs={"keyword": "hazmat",
                                                                       "list_of_ids": [
                                                                           "PHRM-VACC-D4",
                                                                           "CHEM-SOLV-K11",
                                                                           "TECH-BATT-Q17",
                                                                           "ELEC-SMART-W23"
                                                                       ]}),
            Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
            Action(name="GetProductBySku", kwargs={"sku": "ELEC-SMART-W23"}),
            Action(name="UpdateProduct", kwargs={"sku": "PHRM-VACC-D4", "updates": {"storage_requirements": "Hazmat Class mentioned"}}),
            Action(name="UpdateProduct", kwargs={"sku": "ELEC-SMART-W23", "updates": {"storage_requirements": "Hazmat Class mentioned"}}),
            Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
            Action(name="GetProductBySku", kwargs={"sku": "ELEC-SMART-W23"}),
        ],
        outputs=['"storage_requirements": "Hazmat Class mentioned"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_054",
        instruction="""
            You operate as a shipment performance analyst in charge of tracking delays in inbound shipments.
            Identify all delayed inbound shipments.
            Examine the carriers assigned to these shipments.
            Verify if the carrier is presently active.
            If active, no carrier replacement is required.
            If inactive, identify the top-rated carrier.
            Review carriers individually to find the highest-rated active carrier that employs the same mode of transportation and replace the current shipment carrier with this one.
            Lastly, acquire and review the updated inbound shipment details or the shipment with the most imminent departure date to ensure the changes are correctly reflected.
        """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "Delayed"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0022"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "POCL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetTopRatedCarriers", kwargs={}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0004",
                                                           "updates": {"carrier_scac": "SKEX", "carrier_name": "Sakura Express"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
        ],
        outputs=['"carrier_scac": "SKEX"', '"carrier_name": "Sakura Express"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_055",
        instruction="""
            Your position as a warehouse quality inspector requires you to pinpoint critical inventory issues.
            Identify all warehouses containing either expired inventory, using today's date as May 11, 2025, or inventory with at least 200 damaged goods.
            For each warehouse meeting these criteria, change its status to “IMMEDIATE ATTENTION NEEDED” to mark it for urgent inspection.
            After making the updates, verify them by reviewing the updated warehouse details.
        """,
        actions=[
            Action(name="GetExpiredInventory", kwargs={'today': "2025-05-11"}),
            Action(name="GetInventoryWithDamage", kwargs={'threshold': 200}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-12", "updates": {"status": "IMMEDIATE ATTENTION NEEDED"}}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-15", "updates": {"status": "IMMEDIATE ATTENTION NEEDED"}}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-10", "updates": {"status": "IMMEDIATE ATTENTION NEEDED"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"})
        ],
        outputs=['"status": "IMMEDIATE ATTENTION NEEDED"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_056",
        instruction="""
            As a carrier evaluation officer, your role is to assess risk and insurance coverage for transportation partners.
            Start by gathering the list of all active carriers in the system.
            Compute the highest insurance coverage limit among these carriers.
            Next, examine the insurance details of each active carrier to pinpoint those whose coverage limit equals this maximum.
            If several carriers achieve this limit, include each of them.
            Update each top carrier's record with a note: "Highest Insurance Coverage".
            This process aids in making informed decisions regarding risk exposure and ensures that sensitive or high-value shipments are matched with adequately covered carriers.
            Conclude by returning the carrier(s) with the highest insurance coverage.
        """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "insurance_details",
                "value2": "coverage_limit_usd",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL",  "MTRL", "OCBR", "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC", "EWDL"]
            }),
            ]+[
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": scac}) for scac in ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL",  "MTRL", "OCBR",
                                                                                           "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL",
                                                                                           "EAC", "NAC", "ANAF", "NSC", "EWDL"]
        ] + [
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "GPLS", "updates": {"notes": "Highest Insurance Coverage"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"})
        ],
        outputs=["GPLS"]
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_057",
        instruction="""
            As an inventory coordinator, your duties include analyzing product storage and pricing.
            Start by locating all products with storage requirements labeled as "Dry.
            "
            Narrow down this group to products with an active lifecycle status.
            Identify the minimum unit price among active products to aid inventory valuation and pricing strategy.
            Examine each product for having this minimum unit price.
            Products meeting this criterion should be updated with the note "Cheapest Product".
        """,
        actions=[
            Action(name="GetProductsByStorageRequirement", kwargs={"keyword": "Dry"})
        ]+[
            Action(name="CalculateAggregate", kwargs={
                "agg": "min",
                "json": "product_master",
                "key": "sku",
                "value": "unit_price",
                "list_of_ids": [
                "ELEC-CHIP-A1", "AUTO-PAD-B2", "FOOD-COFF-C3", "MANU-PAPR-F6",
                "HEVY-DRIL-I9", "FURN-CHAIR-M13", "TECH-ROBO-N14", "APRL-TSHT-O15", "MATR-COTT-R18",
                "MATR-CORK-T20", "FOOD-OLIV-V22"]
            })
        ]+[
            Action(name="GetProductBySku", kwargs={"sku": sku}) for sku in [
                "ELEC-CHIP-A1", "AUTO-PAD-B2", "FOOD-COFF-C3", "MANU-PAPR-F6",
                "HEVY-DRIL-I9", "FURN-CHAIR-M13", "TECH-ROBO-N14", "APRL-TSHT-O15", "MATR-COTT-R18",
                "MATR-CORK-T20", "FOOD-OLIV-V22"]
        ] + [
            Action(name="UpdateProduct", kwargs={"sku": "MATR-CORK-T20", "updates": {"notes": "Cheapest Product"}}),
            Action(name="GetProductBySku", kwargs={"sku": "MATR-CORK-T20"})
        ],
        outputs=['MATR-CORK-T20']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_058",
        instruction="""
            In your role as a supplier compliance officer, you are tasked with monitoring the performance and certification of preferred suppliers.
            Start by reviewing preferred suppliers to find those with at least one certification.
            From this refined list, identify which supplier boasts the highest on-time delivery percentage to reinforce reliable sourcing and compliance.
            Annotate this supplier's record with the note "Best on time delivery percentage" and review the updated supplier details.
        """,
        actions=[
            Action(name="GetPreferredSuppliers", kwargs={}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1002"}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1005"}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1010"}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1013"}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1016"}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1019"}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1029"}),
            Action(name="CalculateAggregate", kwargs={
                            "agg": "max",
                            "json": "supplier_master",
                            "key": "supplier_id",
                            "value": "on_time_delivery_percentage",
                            "list_of_ids": ["SUP-1002", "SUP-1005", "SUP-1010", "SUP-1013", "SUP-1016", "SUP-1019", "SUP-1029"]
                        }),
            Action(name="UpdateSupplier", kwargs={"supplier_id": "SUP-1016", "updates": {"notes": "Best on time delivery percentage"}}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "SUP-1016"}),],
        outputs=['"SUP-1016"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_059",
        instruction="""
            As the warehouse operations lead, your responsibility is to oversee inventory conditions and space utilization.
            Begin by finding all warehouses containing damaged inventory.
            For these warehouses, evaluate their current utilization percentage.
            Identify the warehouse with both damaged inventory and the highest utilization percentage to evaluate operational efficiency in constrained environments.
            Annotate the warehouse record with "Best Current Utilization Percentage, Damaged Inventory".
            Examine the details of this warehouse.
        """,
        actions=[
            Action(name="GetInventoryWithDamage", kwargs={}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0001"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0002"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0003"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0005"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0006"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0007"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0013"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0017"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0018"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0021"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0022"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0023"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0025"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "warehouses",
                "key": "warehouse_id",
                "value": "current_utilization_percentage",
                "list_of_ids": ["WH-01", "WH-02", "WH-03", "WH-04", "WH-05", "WH-07", "WH-08", "WH-09", "WH-10", "WH-12", "WH-14", "WH-15"]
            }),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-10", "updates": {"notes": "Best Current Utilization Percentage, Damaged Inventory"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
        ],
        outputs=['WH-10']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_060",
        instruction="""
            As a price analyst, you are responsible for verifying the prices and safety standards of grocery products in the market.
            Begin by evaluating all products categorized as "Groceries.
            "
            For each item, verify if its lifecycle status is active and if it's classified as hazardous.
            From the eligible non-hazardous grocery items with an active lifecycle, single out the product with the lowest price to facilitate pricing and safety analysis.
            Update the product details with the note "Cheapest Grocery" and inspect the product details.
        """,
        actions=[
            Action(name="GetProductsByCategory", kwargs={"category": "Groceries"}),
            Action(name="GetProductBySku", kwargs={"sku": "FOOD-COFF-C3"}),
            Action(name="GetProductBySku", kwargs={"sku": "FOOD-FISH-H8"}),
            Action(name="GetProductBySku", kwargs={"sku": "FOOD-OLIV-V22"}),
            Action(name="GetHazmatProducts", kwargs={"list_of_ids": ["FOOD-COFF-C3", "FOOD-FISH-H8", "FOOD-OLIV-V22"]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "min",
                "json": "product_master",
                "key": "sku",
                "value": "unit_price",
                "list_of_ids": ["FOOD-COFF-C3", "FOOD-FISH-H8", "FOOD-OLIV-V22"]
            }),
            Action(name="UpdateProduct", kwargs={"sku": "FOOD-COFF-C3", "updates": {"notes": "Cheapest Grocery"}}),
            Action(name="GetProductBySku", kwargs={"sku": "FOOD-COFF-C3"}),
        ],
        outputs=['FOOD-COFF-C3']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_061",
        instruction="""
            Handle the role of a shipment scheduler tasked with ensuring timely and dependable outbound deliveries.
            Start by identifying all outbound orders awaiting shipment.
            For each order, verify whether the assigned carrier remains active.
            Should the carrier be inactive or absent, obtain a list of other active carriers utilizing the same transportation mode.
            From this list, determine the carrier with the top average rating.
            Substitute the inactive or absent carrier in the pending order with this highly-rated active carrier.
            Lastly, examine the details of the revised pending order to verify that the modifications have been successfully implemented.
        """,
        actions=[
            Action(name="GetOrdersByStatus", kwargs={"status": "Pending"}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0010"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "BLUJ"}),
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SATL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "SWDL", "MTRL", "ALFS", "GPLS"]
            }),
            Action(name="UpdateOutboundOrder", kwargs={"order_id": "ORD-0010", "updates": {
                "carrier_scac": "GPLS",
                "carrier_name": "Global Parcel Service"
            }}),
            Action(name="GetOutboundOrderById", kwargs={"order_id": "ORD-0010"}),
        ],
        outputs=[
            '"carrier_name": "Global Parcel Service"',
            '"carrier_scac": "GPLS"'
        ]
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_062",
        instruction="""
            Coordinate evaluations as a carrier performance analyst responsible for assessing carrier efficiency and coverage.
            Start by examining all carriers with global regional coverage and active status.
            From this collection, pinpoint those operating via Air mode of transport.
            Ascertain the maximum and minimum on-time delivery percentages from these active global air carriers to gauge overall performance in this area.
            Verify if carriers with minimum and maximum percentages are linked to inbound shipments using Air mode of transport.
            If linked shipments lack Air mode of transport, append carriers with the attribute note "No Air Mode".
            Provide the list of scacs for updated carriers.
        """,
        actions=[
            Action(name="GetCarriersByRegion", kwargs={"region": "Global"}),
            Action(name="GetActiveCarriers", kwargs={"list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EWDL"
            ]}),
            Action(name="GetCarriersByMode", kwargs={"mode": "Air", "list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EWDL"
            ]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "both",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["SKEX", "DLOG", "DFC", "SWDL", "ALFS", "GPLS", "AAC", "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "DLOG"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "GPLS"}),
            Action(name="FilterInboundShipments", kwargs={"key": "mode_of_transport", "value": "Air"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "DLOG", "updates": {"note": "No Air Mode"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "GPLS", "updates": {"note": "No Air Mode"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["DLOG", "GPLS"]})
        ],
        outputs=['[\n  "DLOG",\n  "GPLS"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_063",
        instruction="""
            Coordinate evaluations as a carrier performance analyst responsible for assessing carrier efficiency and coverage.
            Start by examining all carriers with global regional coverage and active status.
            From this collection, pinpoint those operating via Sea mode of transport.
            Ascertain the maximum and minimum on-time delivery percentages from these active global sea carriers to gauge overall performance in this area.
            Verify if carriers with minimum and maximum percentages are linked to inbound shipments using Sea mode of transport.
            If they are linked, update carriers with maximum values with the attribute rank "Best Carrier with Inbound Shipment"
            And, update carriers with minimum values with the attribute rank "Worst Carrier with Inbound Shipment".
            Provide the list of scacs for updated carriers.
        """,
        actions=[
            Action(name="GetCarriersByRegion", kwargs={"region": "Global"}),
            Action(name="GetActiveCarriers", kwargs={"list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EWDL"
            ]}),
            Action(name="GetCarriersByMode", kwargs={"mode": "Sea", "list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EWDL"
            ]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "both",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "OCBR", "GOCN", "ALFS", "NRMC", "PSLN", "SATL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "OCBR"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "ALFS"}),
            Action(name="FilterInboundShipments", kwargs={"key": "mode_of_transport", "value": "Sea"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "OCBR", "updates": {"rank": "Worst Carrier with Inbound Shipment"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "ALFS", "updates": {"rank": "Best Carrier with Inbound Shipment"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["OCBR", "ALFS"]})
        ],
        outputs=['[\n  "OCBR",\n  "ALFS"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_064",
        instruction="""
            Coordinate evaluations as a carrier performance analyst responsible for assessing carrier efficiency and coverage.
            Start by examining all carriers with global regional coverage and active status.
            From this collection, pinpoint those operating via Truck mode of transport.
            Ascertain the maximum and minimum on-time delivery percentages from these active global truck carriers to gauge overall performance in this area.
            Verify if carriers with minimum and maximum percentages are linked to inbound shipments using Truck mode of transport.
            If linked shipments lack Truck mode of transport, append attribute note "No Truck Mode".
            Provide the list of scacs for updated carriers.
        """,
        actions=[
            Action(name="GetCarriersByRegion", kwargs={"region": "Global"}),
            Action(name="GetActiveCarriers", kwargs={"list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EWDL"
            ]}),
            Action(name="GetCarriersByMode", kwargs={"mode": "Truck", "list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EWDL"
            ]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "both",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "MEDL", "SWDL", "ALFS", "GPLS", "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "MEDL"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "GPLS"}),
            Action(name="FilterInboundShipments", kwargs={"key": "mode_of_transport", "value": "Truck"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "MEDL", "updates": {"note": "No Truck Mode"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["MEDL"]})
        ],
        outputs=['[\n  "MEDL"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_065",
        instruction="""
            Coordinate evaluations as a carrier performance analyst responsible for assessing carrier efficiency and coverage.
            Start by examining all carriers with global regional coverage and active status.
            From this collection, pinpoint those operating via Rail mode of transport.
            Ascertain the maximum and minimum on-time delivery percentages from these active global rail carriers to gauge overall performance in this area.
            Verify if carriers with minimum and maximum percentages are linked to inbound shipments using Rail mode of transport.
            If linked shipments lack Rail mode of transport, append carriers with the attribute note "No Rail Mode".
            Provide the list of scacs for updated carriers.
        """,
        actions=[
            Action(name="GetCarriersByRegion", kwargs={"region": "Global"}),
            Action(name="GetActiveCarriers", kwargs={"list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EWDL"
            ]}),
            Action(name="GetCarriersByMode", kwargs={"mode": "Rail", "list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EWDL"
            ]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "both",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NSTS", "SKEX", "DLOG", "GOCN", "ALFS"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "GOCN"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "ALFS"}),
            Action(name="FilterInboundShipments", kwargs={"key": "mode_of_transport", "value": "Rail"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "GOCN", "updates": {"note": "No Rail Mode"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "ALFS", "updates": {"note": "No Rail Mode"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["GOCN", "ALFS"]})
        ],
        outputs=['[\n  "GOCN",\n  "ALFS"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_066",
        instruction="""
            As a carrier performance analyst, your task is to evaluate carrier efficiency and coverage.
            Start by examining all carriers that have global regional coverage and are currently active.
            Within this set, pinpoint those utilizing the Parcel mode of transport.
            Determine the highest and lowest on-time delivery percentages among these active global parcel carriers to gauge performance in this segment.
            Verify if carriers with these minimum and maximum values are linked to inbound shipments using Parcel mode of transport.
            If they are linked, label carriers with maximum values with the note "Best Carrier with Inbound Shipment".
            Similarly, label carriers with minimum values with the note "Worst Carrier with Inbound Shipment".
            If these shipments lack Parcel mode, add the note "No Parcel Mode".
            Provide the list of SCACs for carriers that have been updated.
        """,
        actions=[
            Action(name="GetCarriersByRegion", kwargs={"region": "Global"}),
            Action(name="GetActiveCarriers", kwargs={"list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EWDL"
            ]}),
            Action(name="GetCarriersByMode", kwargs={"mode": "Parcel", "list_of_scacs": [
                "NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "OCBR", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN", "AAC", "SATL", "EWDL"
            ]}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "both",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["SWDL", "GPLS", "EWDL"]
            }),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "GPLS"}),
            Action(name="FilterInboundShipments", kwargs={"key": "mode_of_transport", "value": "Parcel"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "SWDL", "updates": {"note": "Worst Carrier with Inbound Shipment"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "GPLS", "updates": {"note": "Best Carrier with Inbound Shipment"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["SWDL", "GPLS"]})
        ],
        outputs=['[\n  "SWDL",\n  "GPLS"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_067",
        instruction="""
            You are charged with coordinating warehouse audits, focusing on assessing warehouse assets.
            Restrict your review to warehouses that are owned.
            Figure out the average current utilization percentage for all owned warehouses to assess overall space efficiency.
            Go through each warehouse's details and if its utilization is below the average, annotate it with "Review Expected".
            Submit the IDs of warehouses that have been updated.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Owned"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "avg",
                "json": "warehouses",
                "key": "warehouse_id",
                "value": "current_utilization_percentage",
                "list_of_ids": ["WH-01", "WH-03", "WH-05", "WH-07", "WH-08", "WH-10", "WH-11", "WH-13", "WH-14", "WH-16"]
            }),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-01"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-03"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-03", "updates": {"note": "Review Expected"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-03"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-07", "updates": {"note": "Review Expected"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-08"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-08", "updates": {"note": "Review Expected"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-08"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-11"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-11", "updates": {"note": "Review Expected"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-13"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-13", "updates": {"note": "Review Expected"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-13"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-14"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-16"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["WH-03", "WH-07", "WH-08", "WH-11", "WH-13"]})
        ],
        outputs=['[\n  "WH-03",\n  "WH-07",\n  "WH-08",\n  "WH-11",\n  "WH-13"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_068",
        instruction="""
            As a warehouse audit coordinator, you are responsible for evaluating warehouse assets.
            Restrict your attention to warehouses that are leased.
            Compute the average current utilization percentage across all leased warehouses to gauge overall space efficiency.
            Check each warehouse detail and if it falls below the average utilization percentage, mark it with "Review Expected".
            Provide the IDs of warehouses that have been updated.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Leased"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "avg",
                "json": "warehouses",
                "key": "warehouse_id",
                "value": "current_utilization_percentage",
                "list_of_ids": ["WH-02", "WH-04", "WH-06", "WH-09", "WH-12", "WH-15"]
            }),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-02"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-06"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-06", "updates": {"note": "Review Expected"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-06"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-09"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-12", "updates": {"note": "Review Expected"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-15", "updates": {"note": "Review Expected"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["WH-06", "WH-12", "WH-15"]})
        ],
    outputs=['[\n  "WH-06",\n  "WH-12",\n  "WH-15"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_069",
        instruction="""
            Your role as a warehouse audit coordinator involves assessing warehouse assets.
            Concentrate on warehouses that are owned.
            Calculate the average current utilization percentages for these owned warehouses to evaluate the variance in space usage.
            Analyze each warehouse detail, and if its utilization surpasses the average, label it with "Top Used".
            Return the IDs of the warehouses updated.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Owned"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "avg",
                "json": "warehouses",
                "key": "warehouse_id",
                "value": "current_utilization_percentage",
                "list_of_ids": ["WH-01", "WH-03", "WH-05", "WH-07", "WH-08", "WH-10", "WH-11", "WH-13", "WH-14", "WH-16"]
            }),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-01"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-01", "updates": {"note": "Top Used"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-01"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-03"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-05", "updates": {"note": "Top Used"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-08"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-10", "updates": {"note": "Top Used"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-13"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-14"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-14", "updates": {"note": "Top Used"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-14"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-16"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-16", "updates": {"note": "Top Used"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-16"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["WH-01", "WH-05", "WH-10", "WH-14", "WH-16"]})
        ],
        outputs=['[\n  "WH-01",\n  "WH-05",\n  "WH-10",\n  "WH-14",\n  "WH-16"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_070",
        instruction="""
            As a coordinator for warehouse audits, your duty is to assess warehouse assets.
            Limit your examination to leased warehouses.
            Evaluate the average current utilization percentages for these leased warehouses to comprehend space usage variance.
            Inspect each warehouse detail, and if its usage exceeds the average, annotate it with "Top Used".
            Submit the IDs of the warehouses updated.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Leased"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "avg",
                "json": "warehouses",
                "key": "warehouse_id",
                "value": "current_utilization_percentage",
                "list_of_ids": ["WH-02", "WH-04", "WH-06", "WH-09", "WH-12", "WH-15"]
            }),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-02"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-02", "updates": {"note": "Top Used"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-02"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-04", "updates": {"note": "Top Used"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-06"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-09"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-09", "updates": {"note": "Top Used"}}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-09"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["WH-02", "WH-04", "WH-09"]})
        ],
        outputs=['[\n  "WH-02",\n  "WH-04",\n  "WH-09"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_071",
        instruction="""
            You are a market analyst focused on inbound shipments.
            Handle the review of all inbound shipments marked as “In Transit” and compute the total sum of their values.
            Identify the shipment with the highest total value and label it with the note "Most valued In Transit shipment".
            The aim is to ascertain the complete value of goods presently in transit.
        """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "In Transit"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0001"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0003"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0005"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0008"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0012"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0013"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0014"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0015"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0018"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0020"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0023"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0024"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0025"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0026"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0028"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008", "SHIP-0009", "SHIP-0011",
                                "SHIP-0012", "SHIP-0013", "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025", "SHIP-0026", "SHIP-0028"]
            }),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0011", "updates": {
                "note": "Most valued In Transit shipment"
            }}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="CalculateTotal", kwargs={
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008", "SHIP-0009", "SHIP-0011",
                                "SHIP-0012", "SHIP-0013", "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025", "SHIP-0026", "SHIP-0028"]
            })
        ],
        outputs=['6820000']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_072",
        instruction="""
            You are a market analyst focused on inbound shipments.
            Conduct an assessment of all inbound shipments with the status “Planned” and sum their total values.
            Determine which shipment has the highest total value and mark it with a note saying "Most valued Planned shipment".
            The goal is to comprehend the overall value of goods currently scheduled for arrival.
        """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "Planned"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0006"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0010"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0016"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0019"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0027"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0029"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0030"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0006", "SHIP-0010", "SHIP-0016", "SHIP-0019", "SHIP-0027", "SHIP-0029", "SHIP-0030"]
            }),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0016", "updates": {
                "note": "Most valued Planned shipment"
            }}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0016"}),
            Action(name="CalculateTotal", kwargs={
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0006", "SHIP-0010", "SHIP-0016", "SHIP-0019", "SHIP-0027", "SHIP-0029", "SHIP-0030"]
            })
        ],
        outputs=['1905000']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_073",
        instruction="""
            You are a market analyst focused on inbound shipments.
            Process all inbound shipments noted as “Delayed” and compute the total of their values.
            Pinpoint the shipment boasting the highest total value and annotate it with "Most valued Delayed shipment".
            The goal is to identify the total value of goods presently experiencing delays.
        """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "Delayed"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0022"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0004", "SHIP-0022"]
            }),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0004", "updates": {
                "note": "Most valued Delayed shipment"
            }}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="CalculateTotal", kwargs={
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0004", "SHIP-0022"]
            })
        ],
        outputs=['575000']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_074",
        instruction="""
            You are a market analyst focused on inbound shipments.
            Examine all inbound shipments with the status “Received” and add up their total values.
            Highlight the shipment with the highest total value and tag it with the note "Most valued Received shipment".
            The purpose is to find out the total value of goods that have been received so far.
        """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "Received"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0007"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "max",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0002", "SHIP-0007", "SHIP-0017"]
            }),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0002", "updates": {
                "note": "Most valued Received shipment"
            }}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="CalculateTotal", kwargs={
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0002", "SHIP-0007", "SHIP-0017"]
            })
        ],
        outputs=['325000']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_075",
        instruction="""
            You are a market analyst focused on in transit inbound shipments.
            Initially, calculate the average of the total values of these inbound shipments.
            Review all the inbound shipments.
            If the total values exceed the average, elevate their priority level to "High".
            Then, ascertain the minimum and maximum total values among these shipments.
            The aim is to carry out statistical analysis (minimum, maximum, and average) of total values for goods currently in transit.
            Lastly, provide the determined minimum and maximum of total values.
        """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "In Transit"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "avg",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008", "SHIP-0009", "SHIP-0011",
                                "SHIP-0012", "SHIP-0013", "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025", "SHIP-0026", "SHIP-0028"]
            }),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0001"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0003"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0005"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0008"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0009", "updates": {"priority_level": "High"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0011", "updates": {"priority_level": "High"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0012"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0013"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0013", "updates": {"priority_level": "High"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0013"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0014"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0015"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0018"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0020"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0021", "updates": {"priority_level": "High"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0023"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0024"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0025"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0025", "updates": {"priority_level": "High"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0025"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0026"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0028"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0028", "updates": {"priority_level": "High"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0028"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "both",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008", "SHIP-0009", "SHIP-0011",
                                "SHIP-0012", "SHIP-0013", "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025", "SHIP-0026", "SHIP-0028"]
            })
        ],
        outputs=['"min_value": 50000', '"max_value": 1200000']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_076",
        instruction="""
            As a warehouse inventory manager, examine the inventory record for INV-0010.
            The quantity_allocated has been successfully sold.
            Subtract the allocated quantity from quantity_on_hand.
            Set quantity_allocated to 0.
            Recalculate total_value by subtracting unit_cost * quantity_allocated before.
            If quantity_on_hand < reorder_point, label stock_status as "Reorder Needed".
            Then, inspect the associated warehouse and its current utilization percentage.
            If current utilization percentage < 80, update warehouse with attribute note as "Less Used".
            If current utilization percentage >= 80, update warehouse with attribute note as "More Used".
            Return the updated inventory record with: inventory_id, sku, quantity_on_hand, quantity_allocated, stock_status, and total_value.
        """,
        actions=[
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0010", "updates": {
                "quantity_on_hand": 15000
            }}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0010", "updates": {
                "quantity_allocated": 0
            }}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0010", "updates": {
                "total_value": 52500
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-12", "updates": {
                "note": "Less Used"
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
        ],
        outputs=['"inventory_id": "INV-0010"', '"sku": "BLDG-TILE-J10"', '"quantity_on_hand": 15000', '"quantity_allocated": 0', '"total_value": 52500', '"stock_status": "In Stock"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_077",
        instruction="""
            In charge of luxury inventory, note that INV-0005 has sold all allocated units.
            Reduce these units from quantity_on_hand.
            Set quantity_allocated to 0.
            Recalculate total_value by subtracting unit_cost * quantity_allocated before.
            If the quantity_on_hand drops below the reorder_point, set stock_status to "Reorder Needed".
            If current utilization percentage < 80, update warehouse with attribute note as "Less Used".
            If current utilization percentage >= 80, update warehouse with attribute note as "More Used".
            Return the updated inventory with new quantity_on_hand, quantity_allocated, total_value and stock_status).
        """,
        actions=[
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0005"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0005", "updates": {
                "quantity_on_hand": 120
            }}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0005"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0005", "updates": {
                "quantity_allocated": 0
            }}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0005"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0005", "updates": {
                "total_value": 102000
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-07", "updates": {
                "note": "Less Used"
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0005"}),
        ],
        outputs=['"inventory_id": "INV-0005"', '"quantity_on_hand": 120', '"quantity_allocated": 0', '"total_value": 102000', '"stock_status": "In Stock"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_078",
        instruction="""
            The allocated bottles of INV-0016 have been sold.
            Decrease quantity_on_hand by quantity allocated before selling.
            Set quantity_allocated to 0.
            Recalculate total_value by subtracting unit_cost * quantity_allocated before.
            If new quantity_on_hand < reorder_point, append "Reorder Suggested" to stock_status.
            If current utilization percentage < 80, update warehouse with attribute note as "Less Used".
            If current utilization percentage >= 80, update warehouse with attribute note as "More Used".
            Return updated inventory_id, sku, quantity_on_hand, quantity_allocated, stock_status, storage_requirements, and total_value.
        """,
        actions=[
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0016", "updates": {
                "quantity_on_hand": 4500
            }}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0016", "updates": {
                "quantity_allocated": 0
            }}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0016", "updates": {
                "total_value": 81000
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-15", "updates": {
                "note": "More Used"
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
        ],
        outputs=['"inventory_id": "INV-0016"', '"sku": "BEVG-WINE-P16"', '"quantity_on_hand": 4500', '"quantity_allocated": 0', '"stock_status": "In Stock"', '"storage_requirements": "Temp Control 12-14\u00b0C, Dark"', '"total_value": 81000']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_079",
        instruction="""
            Allocated inventory of INV-0004 has been processed.
            Reduce quantity allocated before from quantity_on_hand.
            Set quantity_allocated to 0.
            Recalculate total_value by subtracting unit_cost * quantity_allocated before.
            If quantity_on_hand < reorder_point, add tag: "Critical Reorder".
            If current utilization percentage < 80, update warehouse with attribute note as "Less Used".
            If current utilization percentage >= 80, update warehouse with attribute note as "More Used".
            Return updated values for inventory_id, quantity_on_hand, quantity_allocated, total_value, and stock_status.
        """,
        actions=[
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0004", "updates": {
                "quantity_on_hand": 18000
            }}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0004", "updates": {
                "quantity_allocated": 0
            }}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0004", "updates": {
                "total_value": 279000
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-06"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-06", "updates": {
                "note": "More Used"
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-06"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
        ],
        outputs=['"inventory_id": "INV-0004"', '"quantity_on_hand": 18000', '"quantity_allocated": 0', '"total_value": 279000', '"stock_status": "In Stock"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_080",
        instruction="""
            Sold out allocated stock of INV-0015.
            Lessen quantity_on_hand by sold allocated stock.
            Set quantity_allocated to 0.
            Recalculate total_value by subtracting unit_cost * quantity_allocated before.
            If new quantity_on_hand < reorder_point, set stock_status = "Reorder Needed".
            If current utilization percentage < 80, update warehouse with attribute note as "Less Used".
            If current utilization percentage >= 80, update warehouse with attribute note as "More Used".
            Return changes including: inventory_id, sku, quantity_on_hand, quantity_allocated, total_value and stock_status.
        """,
        actions=[
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0015", "updates": {
                "quantity_on_hand": 22000
            }}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0015", "updates": {
                "quantity_allocated": 0
            }}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0015", "updates": {
                "total_value": 176000
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-04", "updates": {
                "note": "More Used"
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
        ],
        outputs=['"inventory_id": "INV-0015"', '"sku": "APRL-TSHT-O15"', '"quantity_on_hand": 22000', '"quantity_allocated": 0', '"total_value": 176000', '"stock_status": "In Stock"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_081",
        instruction="""
            As a market analyst focusing on inbound shipments,
            compute the average total value of these shipments.
            Your initial task is to ascertain the average value of goods currently delayed.
            Then, assess shipments and their associated carriers to verify if any of those shipments have inactive carriers.
            For each shipment with an inactive carrier, determine if the total value exceeds the average total value.
            If it does, annotate the shipment with "Carrier Replacement Required" in the notes.
            Conclude by returning the ids of the shipments that were updated.
        """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "Delayed"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "avg",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0004", "SHIP-0022"]
            }),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "POCL"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0022"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0004",
                                                           "updates": {"notes": "Carrier Replacement Required"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["SHIP-0004"]})
        ],
        outputs=['[\n  "SHIP-0004"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_082",
        instruction="""
            As a market analyst focusing on incoming shipments,
            compute the average total value of these shipments.
            Your primary goal is to find out the average value of goods currently received.
            Afterward, evaluate shipments and their active carriers only.
            Should the total value of a shipment with an active carrier fall below the average, update its notes with "Lower than Average.
            "
            Conversely, if a shipment's total value is above the average, annotate it with "Higher than Average.
            "
            Finally, provide the ids of shipments marked with notes "Higher than Average.
            ".
        """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "Received"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "avg",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0002", "SHIP-0007", "SHIP-0017"]
            }),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0007"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0002",
                                                           "updates": {"notes": "Higher than Average"}}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0007",
                                                           "updates": {"notes": "Lower than Average"}}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0017",
                                                           "updates": {"notes": "Higher than Average"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0007"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["SHIP-0002", "SHIP-0017"]})
        ],
        outputs=['[\n  "SHIP-0002",\n  "SHIP-0017"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_083",
        instruction="""
            As a logistics manager overseeing carrier performance,
            identify all active carriers handling the "Global" region that have an on-time delivery rate below 95%.
            Update each qualifying carrier's status to "Under Review.
            "
            Submit the list of carriers whose status was modified.
            If no carriers fall below the 95% benchmark, no updates are required and an empty list should be returned.
        """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetCarriersByRegion", kwargs={"region": "Global",
                                                       "list_of_scacs": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC", "SWDL", "MTRL",
                                                                       "OCBR", "SCF", "GOCN", "ALFS", "NRMC", "GPLS", "PSLN",
                                                                       "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC", "EWDL"
                                                       ]}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SATL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "NSTS", "updates": {"status": "Under Review"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "MEDL", "updates": {"status": "Under Review"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "OCBR", "updates": {"status": "Under Review"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "GOCN", "updates": {"status": "Under Review"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "NRMC", "updates": {"status": "Under Review"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "PSLN", "updates": {"status": "Under Review"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["NSTS", "MEDL", "OCBR", "GOCN", "NRMC", "PSLN"]})
            ],
        outputs=['[\n  "NSTS",\n  "MEDL",\n  "OCBR",\n  "GOCN",\n  "NRMC",\n  "PSLN"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_084",
        instruction="""
            In your role as a logistics manager monitoring carrier performance, determine all active carriers in the "Global" region with on-time delivery percentages under 95%.
            Alter the status of such carriers to "Under Review.
            " 
            Supply the updated list of carriers.
            Should no carriers fall short of the 95% threshold, simply return an empty list with no updates.
        """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetCarriersByRegion", kwargs={"region": "Global",
                                                          "list_of_scacs": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC",
                                                                            "SWDL", "MTRL",
                                                                            "OCBR", "SCF", "GOCN", "ALFS", "NRMC",
                                                                            "GPLS", "PSLN",
                                                                            "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC",
                                                                            "EWDL"
                                                                            ]}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DLOG"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "DFC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ALFS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GPLS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SATL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EWDL"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "NSTS", "updates": {"status": "Under Review"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "MEDL", "updates": {"status": "Under Review"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "OCBR", "updates": {"status": "Under Review"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "GOCN", "updates": {"status": "Under Review"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "NRMC", "updates": {"status": "Under Review"}}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "PSLN", "updates": {"status": "Under Review"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSTS"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MEDL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "OCBR"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "GOCN"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NRMC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "PSLN"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["NSTS", "MEDL", "OCBR", "GOCN", "NRMC", "PSLN"]})
        ],
        outputs=['[\n  "NSTS",\n  "MEDL",\n  "OCBR",\n  "GOCN",\n  "NRMC",\n  "PSLN"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_085",
        instruction="""
            Acting as a logistics manager for overseeing carrier performance, locate all active carriers in the "North America" region whose punctuality in deliveries is under 95%.
            Change the status of each identified carrier to "Under Review.
            "
            Provide the list of carriers that had their status altered.
            If no carriers fit this criteria, return an empty list as no updates are required.
        """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetCarriersByRegion", kwargs={"region": "North America",
                                                          "list_of_scacs": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC",
                                                                            "SWDL", "MTRL",
                                                                            "OCBR", "SCF", "GOCN", "ALFS", "NRMC",
                                                                            "GPLS", "PSLN",
                                                                            "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC",
                                                                            "EWDL"
                                                                            ]}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "MTRL", "updates": {"status": "Under Review"}}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["MTRL"]})
        ],
        outputs=['[\n  "MTRL"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_086",
        instruction="""
            As a logistics manager, oversee the performance of carriers operating in specific regions only, not globally.
            Begin by reviewing active carriers.
            Identify which of these active carriers have global coverage.
            Validate regional presence and assess the on-time delivery rates of active carriers that do not operate globally, using detailed information.
            Change the status of each non-global active carrier found to "Under Review.
            " Provide the list of carriers whose status was updated.
            If no carriers qualify for this update, it is unnecessary to make any changes, so return an empty list.
        """,
        actions=[
            Action(name="GetActiveCarriers", kwargs={}),
            Action(name="GetCarriersByRegion", kwargs={"region": "Global",
                                                          "list_of_scacs": ["NSTS", "SKEX", "DLOG", "MEDL", "DFC",
                                                                            "SWDL", "MTRL",
                                                                            "OCBR", "SCF", "GOCN", "ALFS", "NRMC",
                                                                            "GPLS", "PSLN",
                                                                            "AAC", "SATL", "EAC", "NAC", "ANAF", "NSC",
                                                                            "EWDL"
                                                                            ]}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "MTRL",
                                                  "updates": {
                                                      "status": "Under Review"
                                                  }}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "SCF",
                                                  "updates": {
                                                      "status": "Under Review"
                                                  }}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "EAC",
                                                  "updates": {
                                                      "status": "Under Review"
                                                  }}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "NAC",
                                                  "updates": {
                                                      "status": "Under Review"
                                                  }}),
            Action(name="UpdateCarrier", kwargs={"carrier_scac": "NSC",
                                                  "updates": {
                                                      "status": "Under Review"
                                                  }}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["MTRL", "SCF", "EAC", "NAC", "NSC"]})
        ],
        outputs=['["MTRL", "SCF", "EAC", "NAC", "NSC"]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_087",
        instruction="""
            Taking on the role of an inventory controller, your task is to oversee the quality and availability of stock.
            As of December 12, 2024, locate all inventory items that are either past expiration or have 200 or more of damaged quantities.
            Additionally, pinpoint items that fall below their reorder threshold.
            Merge these items—expired, damaged, or under reorder point—and adjust their status to “Under Review.
            ” Conclude by providing the list of updated inventory item IDs.
        """,
        actions=[
            Action(name="GetExpiredInventory", kwargs={"today": "2024-12-12"}),
            Action(name="GetInventoryWithDamage", kwargs={"threshold": 200}),
            Action(name="GetInventoryBelowReorderPoint", kwargs={}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0010", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0020", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0024", "updates": {"status": "Under Review"}}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["INV-0010", "INV-0020", "INV-0024"]})
        ],
        outputs=['[\n  "INV-0010",\n  "INV-0020",\n  "INV-0024"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_088",
        instruction="""
            In the capacity of an inventory controller, ensure the supervision of stock quality and availability.
            As of June 12, 2024, determine which inventory items are expired or have damaged quantities reaching 150 or more.
            Equally, identify any items that are under their reorder level.
            Consolidate these groups—expired, damaged, or under reorder point—and modify their status to “Under Review.
            ” Finally, deliver the list of IDs for all the inventory items that have been updated.
        """,
        actions=[
            Action(name="GetExpiredInventory", kwargs={"today": "2024-06-12"}),
            Action(name="GetInventoryWithDamage", kwargs={"threshold": 150}),
            Action(name="GetInventoryBelowReorderPoint", kwargs={}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0010", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0020", "updates": {"status": "Under Review"}}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["INV-0010", "INV-0020"]})
        ],
        outputs=['[\n  "INV-0010",\n  "INV-0020"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_089",
        instruction="""
            Acting as an inventory controller, your duty is to manage stock quality and availability.
            By May 12, 2025, you should identify inventory items that are expired or have damaged amounts of 100 or more.
            Additionally, check for items beneath their reorder point.
            Combine these—expired, damaged, or below reorder level—and revise their status to “Under Review.
            ” Conclude the task by submitting the list of IDs of all inventory items adjusted.
        """,
        actions=[
            Action(name="GetExpiredInventory", kwargs={"today": "2025-05-12"}),
            Action(name="GetInventoryWithDamage", kwargs={"threshold": 100}),
            Action(name="GetInventoryBelowReorderPoint", kwargs={}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0010", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0015", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0020", "updates": {"status": "Under Review"}}),
            Action(name="UpdateInventory", kwargs={"inventory_id": "INV-0024", "updates": {"status": "Under Review"}}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0010"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0015"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0020"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0024"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["INV-0010", "INV-0015", "INV-0020", "INV-0024"]})
        ],
        outputs=['[\n  "INV-0010",\n  "INV-0015",\n  "INV-0020",\n  "INV-0024"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_090",
        instruction="""
            As a compliance officer, your responsibility is to review warehouse and product safety protocols.
            Start by compiling data on all company-owned warehouses.
            Then, pinpoint all products that necessitate special storage conditions, with a focus on those labeled as “Hazmat.
            ”
            Check if the company-owned warehouses are capable of supporting hazmat storage.
            Subsequently, cross-verify inventory records to ensure these products are stored in warehouses that are both company-owned and equipped for hazmat storage.
            Should a product's inventory match an owned warehouse that includes adequate hazmat facilities, it is deemed compliant.
            Tag products lacking specific owned warehouse suitable for hazmat by noting "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE".
            Lastly, furnish the list of product IDs allocated to appropriate owned warehouses fit for hazmat storage.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Owned"}),
            Action(name="GetHazmatProducts", kwargs={}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-01"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-03"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-08"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-13"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-14"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "PHRM-VACC-D4"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "TECH-BATT-Q17"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "ELEC-SMART-W23"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0011"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0017"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0023"}),
            Action(name="UpdateProduct", kwargs={"sku": "PHRM-VACC-D4", "updates": {"notes": "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE"}}),
            Action(name="UpdateProduct", kwargs={"sku": "TECH-BATT-Q17", "updates": {"notes": "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE"}}),
            Action(name="UpdateProduct", kwargs={"sku": "ELEC-SMART-W23", "updates": {"notes": "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE"}}),
            Action(name="GetProductBySku", kwargs={"sku": "PHRM-VACC-D4"}),
            Action(name="GetProductBySku", kwargs={"sku": "TECH-BATT-Q17"}),
            Action(name="GetProductBySku", kwargs={"sku": "ELEC-SMART-W23"}),
            Action(name="ReturnIds", kwargs={'list_of_ids': ["CHEM-SOLV-K11"]})
        ],
        outputs=['[\n  "CHEM-SOLV-K11"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_091",
        instruction="""
            You are a compliance officer tasked with reviewing warehouse and product safety protocols.
            Your goal is to locate products needing special storage conditions, like “Hazmat,” that are either not assigned to any warehouse or assigned to owned warehouses unsuitable for hazmat storage.
            Start by obtaining the list of all company-owned warehouses and identifying which are equipped for hazmat storage.
            Next, find all products with “Hazmat” storage requirements.
            For each of these products, verify inventory details to determine if a warehouse has been designated.
            If any product is without a warehouse assignment, or linked to an owned warehouse lacking hazmat readiness, mark it.
            Update products with the appropriate owned warehouse suitable for hazmat by appending attribute notes "SUITABLE CONDITION PROVIDED FOR HAZMAT STORAGE".
            Conclude by returning the list of product IDs falling into these categories.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Owned"}),
            Action(name="GetHazmatProducts", kwargs={}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-01"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-03"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-08"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-13"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-14"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "PHRM-VACC-D4"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "TECH-BATT-Q17"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "ELEC-SMART-W23"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0004"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0011"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0017"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0023"}),
            Action(name="UpdateProduct", kwargs={"sku": "CHEM-SOLV-K11", "updates": {"notes": "SUITABLE CONDITION PROVIDED FOR HAZMAT STORAGE"}}),
            Action(name="GetProductBySku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="ReturnIds", kwargs={'list_of_ids': ["PHRM-VACC-D4", "TECH-BATT-Q17", "ELEC-SMART-W23"]})
        ],
        outputs=['[\n  "PHRM-VACC-D4",\n  "TECH-BATT-Q17",\n  "ELEC-SMART-W23"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_092",
        instruction="""
            You are a compliance officer tasked with reviewing warehouse and product safety protocols.
            Your goal is to ascertain whether leased warehouses are properly equipped to manage products requiring “Hazmat” storage.
            Initiate by collecting all leased warehouses, then evaluate each to confirm if it has the necessary equipment for hazmat storage (using special capabilities attribute).
            For any warehouse lacking hazmat readiness, amend the record by appending a note stating "NOT SUITABLE FOR HAZMAT STORAGE".
            Verify the updated warehouse information for correctness.
            Finally, compile the list of warehouse IDs that fail to meet hazmat storage suitability.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Leased"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-02"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-06"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-09"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-02", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-04", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-06", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-09", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-12", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="UpdateWarehouse", kwargs={"warehouse_id": "WH-15", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-02"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-06"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-09"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="ReturnIds", kwargs={'list_of_ids': ["WH-02", "WH-04", "WH-06", "WH-09", "WH-12", "WH-15"]})
        ],
        outputs=['[\n  "WH-02",\n  "WH-04",\n  "WH-06",\n  "WH-09",\n  "WH-12",\n  "WH-15"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_093",
        instruction="""
            You are tasked as a compliance officer for reviewing warehouse and product safety protocols.
            Your objective is to find products needing special storage like “Temp Control” stored in owned warehouses that meet this specification.
            Start by retrieving all company-owned warehouses and check which are equipped for temperature-controlled storage.
            Then, identify all products requiring “Temp Control” as part of their storage needs.
            Refer to inventory data to confirm these products are assigned to warehouses.
            When the designated warehouse is owned and properly equipped for temperature control, deem the product compliant.
            For such compliant products, append attribute notes "STORED IN TEMP CONTROL OWNED WAREHOUSE"
            Finally, return the list of product IDs stored in such compliant owned warehouses.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Owned"}),
            Action(name="GetProductsByStorageRequirement", kwargs={"keyword": "Temp"}),
            Action(name="GetProductBySku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="GetProductBySku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-01"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-03"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-08"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-13"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-14"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "BEVG-WINE-P16"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0011"}),
            Action(name="UpdateProduct", kwargs={"sku": "CHEM-SOLV-K11", "updates": {"notes": "STORED IN TEMP CONTROL OWNED WAREHOUSE"}}),
            Action(name="GetProductBySku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="ReturnIds", kwargs={'list_of_ids': ["CHEM-SOLV-K11"]})
        ],
        outputs=['[\n  "CHEM-SOLV-K11"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_094",
        instruction="""
            You are assigned as a compliance officer for reviewing warehouse and product safety protocols.
            Your goal is to find products that need special storage conditions, for instance, “Temp Control,” but are not stored in suitable owned warehouses.
            Initially, gather information on all company-owned warehouses and identify which are fitted for temperature-controlled storage.
            Next, locate all products needing “Temp Control.
            ”
            Review inventory records to verify these products are assigned to warehouses.
            If any product is unassigned or transferred to an owned warehouse lacking temperature control capabilities, mark it.
            For non-compliant products, update with attribute notes "NOT STORED IN TEMP CONTROL OWNED WAREHOUSE"
            Finally, list the product IDs that do not have access to suitable owned warehouses for temperature-controlled storage.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Owned"}),
            Action(name="GetProductsByStorageRequirement", kwargs={"keyword": "Temp"}),
            Action(name="GetProductBySku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="GetProductBySku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-01"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-03"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-05"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-07"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-08"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-10"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-13"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-14"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "BEVG-WINE-P16"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0011"}),
            Action(name="UpdateProduct", kwargs={"sku": "BEVG-WINE-P16", "updates": {"notes": "NOT STORED IN TEMP CONTROL OWNED WAREHOUSE"}}),
            Action(name="GetProductBySku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="ReturnIds", kwargs={'list_of_ids': ["BEVG-WINE-P16"]})
        ],
        outputs=['[\n  "BEVG-WINE-P16"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_095",
        instruction="""
            You are charged as a compliance officer with reviewing warehouse and product safety protocols.
            Your aim is to spot products requiring specific storage conditions such as “Temp Control” and housed in leased warehouses meeting the requirement.
            Commence by identifying all leased warehouses, assessing which are equipped for temperature-controlled storage.
            Then, highlight all products with “Temp Control” storage demands.
            Use inventory data to judge if these products are allocated to warehouses.
            If any product is located in a leased warehouse that satisfies temperature control requirements, confirm it as compliant.
            For these compliant products, update with attribute notes "STORED IN TEMP CONTROL LEASED WAREHOUSE"
            Finally, provide the list of product IDs located in such compliant leased warehouses.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Leased"}),
            Action(name="GetProductsByStorageRequirement", kwargs={"keyword": "Temp"}),
            Action(name="GetProductBySku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="GetProductBySku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-02"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-06"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-09"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "BEVG-WINE-P16"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0011"}),
            Action(name="UpdateProduct", kwargs={"sku": "BEVG-WINE-P16", "updates": {"notes": "STORED IN TEMP CONTROL LEASED WAREHOUSE"}}),
            Action(name="GetProductBySku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="ReturnIds", kwargs={'list_of_ids': ["BEVG-WINE-P16"]})
        ],
        outputs=['[\n  "BEVG-WINE-P16"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_096",
        instruction="""
            As a compliance officer reviewing warehouse and product safety protocols, your task is to pinpoint products that need temperature-controlled storage ("Temp Control") but are improperly stored in leased warehouses lacking this feature.
            Begin by obtaining a list of all leased warehouses to establish which ones are equipped for temperature-controlled storage.
            Subsequently, compile a list of all products that necessitate "Temp Control".
            Utilize inventory records to verify if these products are allocated to a warehouse.
            Should a product be unassigned to a warehouse or assigned to a leased warehouse without temperature control, it must be flagged.
            For each such product, update its record to include a note with "NOT STORED IN TEMP CONTROL LEASED WAREHOUSE".
            Conclude by providing the list of product IDs lacking suitable leased warehouse storage for temperature-controlled requirements.
        """,
        actions=[
            Action(name="GetWarehousesByOwnershipStatus", kwargs={"ownership_status": "Leased"}),
            Action(name="GetProductsByStorageRequirement", kwargs={"keyword": "Temp"}),
            Action(name="GetProductBySku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="GetProductBySku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-02"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-04"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-06"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-09"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-12"}),
            Action(name="GetWarehouseById", kwargs={"warehouse_id": "WH-15"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "BEVG-WINE-P16"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0016"}),
            Action(name="FilterInventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="GetInventoryById", kwargs={"inventory_id": "INV-0011"}),
            Action(name="UpdateProduct", kwargs={"sku": "CHEM-SOLV-K11", "updates": {"notes": "NOT STORED IN TEMP CONTROL LEASED WAREHOUSE"}}),
            Action(name="GetProductBySku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="ReturnIds", kwargs={'list_of_ids': ["CHEM-SOLV-K11"]})
        ],
        outputs=['[\n  "CHEM-SOLV-K11"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_097",
        instruction="""
            As a logistics performance manager evaluating carrier efficiency in the North American region, initiate by retrieving all active carriers covering “North America.
            ”
            Following this, pinpoint all inbound shipments presently “In Transit” associated with these carriers.
            Modify these shipments by assigning the attribute carrier_coverage "North America".
            Examine the specifics of these shipments and finally, compute the total value of the shipments to evaluate the cumulative worth of goods currently in transit with active North American carriers.
        """,
        actions=[
            Action(name="GetCarriersByRegion", kwargs={"region": "North America"}),
            Action(name="GetActiveCarriers", kwargs={"list_of_scacs": ["MTRL", "EAC", "NAC", "ANAF", "NSC"]}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "MTRL"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="FilterInboundShipments", kwargs={"key": "status", "value": "In Transit"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "MTRL", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "EAC", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "NAC", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "ANAF", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "NSC", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0008", "updates": {
                "carrier_coverage": "North America"
            }}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0008"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0021", "updates": {
                "carrier_coverage": "North America"
            }}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="CalculateTotal", kwargs={
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0008", "SHIP-0021"]
            })
        ],
        outputs=["610000"]
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_098",
        instruction="""
            As a market analyst concentrating on inbound shipments, your initial goal is to ascertain the average weight of goods recently received.
            Compute the average total weight in kg of these shipments.
            Next, scrutinize shipments and the carriers linked to them, focusing solely on shipments connected with active carriers.
            If a shipment's total weight with an active carrier is below the average, append the shipment with the note "Lower than Average".
            Conversely, if the total weight exceeds the average, append the shipment with the note "Higher than Average".
            Ultimately, provide the IDs of shipments amended with the note "Lower than Average".
        """,
        actions=[
            Action(name="GetShipmentsByStatus", kwargs={"status": "Received"}),
            Action(name="CalculateAggregate", kwargs={
                "agg": "avg",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_weight_kg",
                "list_of_ids": ["SHIP-0002", "SHIP-0007", "SHIP-0017"]
            }),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SKEX"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0007"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SWDL"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "AAC"}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0002",
                                                           "updates": {"notes": "Higher than Average"}}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0007",
                                                           "updates": {"notes": "Lower than Average"}}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0017",
                                                           "updates": {"notes": "Higher than Average"}}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0007"}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="ReturnIds", kwargs={"list_of_ids": ["SHIP-0007"]})
        ],
        outputs=['[\n  "SHIP-0007"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_099",
        instruction="""
            As a logistics performance manager appraising carrier activities in the Asian region, start by gathering all active carriers with regional coverage including “Asia.
            ”
            Then, identify all inbound shipments currently labeled as “In Transit” serviced by these carriers.
            Update these shipments by assigning the attribute carrier_coverage "Asia".
            Examine the details of these shipments and, in conclusion, aggregate the value of these shipments to estimate the worth of goods currently in transit with active carriers serving Asia.
        """,
        actions=[
            Action(name="GetCarriersByRegion", kwargs={"region": "Asia"}),
            Action(name="GetActiveCarriers", kwargs={"list_of_scacs": ["SCF", "EAC", "NAC"]}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="FilterInboundShipments", kwargs={"key": "status", "value": "In Transit"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "SCF", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "EAC", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "NAC", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0021", "updates": {
                "carrier_coverage": "Asia"
            }}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="CalculateTotal", kwargs={
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0021"]
            })
        ],
        outputs=["550000"]
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_100",
        instruction="""
            As a logistics performance manager evaluating carrier operations in the European region, begin by retrieving all active carriers covering “Europe.
            ”
            Then, ascertain all inbound shipments marked as “In Transit” associated with these carriers.
            Modify these shipments by setting the attribute carrier_coverage "Europe".
            Review the shipment details and finally, calculate the cumulative value of these shipments to gauge the total worth of goods currently in transit with active carriers in Europe.
        """,
        actions=[
            Action(name="GetCarriersByRegion", kwargs={"region": "Europe"}),
            Action(name="GetActiveCarriers", kwargs={"list_of_scacs": ["SCF", "EAC", "NAC", "ANAF", "NSC"]}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "SCF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "EAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NAC"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "ANAF"}),
            Action(name="GetCarrierByScac", kwargs={"carrier_scac": "NSC"}),
            Action(name="FilterInboundShipments", kwargs={"key": "status", "value": "In Transit"}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "SCF", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "EAC", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "NAC", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "ANAF", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="FilterInboundShipments", kwargs={"key": "carrier_scac", "value": "NSC", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="UpdateInboundShipment", kwargs={"shipment_id": "SHIP-0021", "updates": {
                "carrier_coverage": "Europe"
            }}),
            Action(name="GetShipmentById", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="CalculateTotal", kwargs={
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0021"]
            })
        ],
        outputs=["550000"]
    ),
]
