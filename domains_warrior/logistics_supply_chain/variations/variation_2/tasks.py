from datetime import datetime

from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="ArpanMahatra1999",
        user_id="task_001",
        instruction="""
        You are the logistics planner responsible for managing inbound shipments.
        You are currently reviewing shipment SHIP-0004, which is assigned to a carrier whose operational status needs to be verified.
        Your task is to retrieve the shipment details and confirm whether the assigned carrier is active.
        If the carrier is found to be inactive, you must identify an alternative by retrieving the list of active carriers, selecting the top-rated one, and updating the shipment with this new carrier.
        If two or more carriers have same top rating, select carrier with better on time delivery percentage for replacement.
        Once reassigned, ensure the shipment information reflects the updated carrier accurately to maintain continuity in the supply chain process.
        """,
        actions=[
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HJSC"}),
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_top_rated_carriers", kwargs={"list_of_scacs": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU", "COSU",
                                             "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU",
                                             "LOT", "SAS", "LAAL", "ICE", "DHLG"]}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0004",
                "updates": {"carrier_name": "UPS", "carrier_scac": "UPSN"}
            }),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
        ],
        outputs=['UPSN']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_002",
        instruction="""
            You are tasked with listing all carriers currently active in the system and sorting them based on their average rating.
            Calculate the overall minimum of these carriers' average ratings.
            For each carrier whose rating equals overall minimum, update their record by adding a new attribute called "warning" with the value "Least Rated".
            Finally, review the updated details of all carriers flagged as least rated. Finally, return the scacs of updated carriers.
            """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_top_rated_carriers",
                   kwargs={"list_of_scacs": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU", "COSU",
                                             "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU",
                                             "LOT", "SAS", "LAAL", "ICE", "DHLG"]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "min",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU", "COSU",
                                             "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU",
                                             "LOT", "SAS", "LAAL", "ICE", "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SUDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
            Action(name="update_carrier", kwargs={
                "carrier_scac": "CNRU",
                "updates": {"warning": "Least Rated"}
            }),
            Action(name="update_carrier", kwargs={
                "carrier_scac": "EGLV",
                "updates": {"warning": "Least Rated"}
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["CNRU", "EGLV"]})
        ],
        outputs=['[\n  "CNRU",\n  "EGLV"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_003",
        instruction="""
        You are the supply chain analyst overseeing inbound logistics as of June 5, 2024. Your task is to identify all inbound shipments that are delayed, meaning shipments whose expected arrival dates have passed but have not yet been marked as arrived. Retrieve this list and update the status of each delayed shipment to “Delayed.” After updating all applicable shipments, focus on the final shipment modified and review its associated carrier. If the carrier is active, no further action is needed. However, if the carrier is inactive, identify the highest-rated active carrier based on average rating. In cases where multiple carriers share the highest rating, select the one with the superior on-time delivery percentage. Update the shipment's carrier to this top-rated carrier, then retrieve and verify the updated shipment details to confirm all changes have been applied correctly.
        """,
        actions=[
            Action(name="get_delayed_shipments", kwargs={'today': '2024-06-05'}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0014"}),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0014",
                "updates": {"status": "Delayed"}
            }),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0014"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0014"}),
        ],
        outputs=['"status": "Delayed"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_004",
        instruction="""
        You are tasked with listing all carriers currently active in the system. Calculate the overall minimum of these carriers' on time delivery percentages. For each carrier whose rating equals overall minimum, update their record by adding a new attribute called "warning" with the value "Poor Delivery." Finally, review the updated details of all carriers flagged for poor delivery. Finally, return the scacs of updated carriers.
        """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "min",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU", "COSU",
                                "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU",
                                "LOT", "SAS", "LAAL", "ICE", "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SUDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
            Action(name="update_carrier", kwargs={
                "carrier_scac": "CNRU",
                "updates": {"warning": "Poor Delivery"}
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["CNRU"]})
        ],
        outputs=['[\n  "CNRU"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_005",
        instruction="""
        You are tasked with listing all carriers currently active in the system and sorting them based on their average rating. Calculate the overall maximum of these carriers' average ratings. For each carrier whose rating equals overall maximum, update their record by adding a new attribute called "highlight" with the value "Best Rated." Finally, review the updated details of all carriers flagged as best rated. Finally, return the scacs of updated carriers.
        """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_top_rated_carriers",
                   kwargs={"list_of_scacs": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU", "COSU",
                                             "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU",
                                             "LOT", "SAS", "LAAL", "ICE", "DHLG"]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU", "COSU",
                                "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU",
                                "LOT", "SAS", "LAAL", "ICE", "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SUDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
            Action(name="update_carrier", kwargs={
                "carrier_scac": "UAE",
                "updates": {"highlight": "Best Rated"}
            }),
            Action(name="update_carrier", kwargs={
                "carrier_scac": "UPSN",
                "updates": {"highlight": "Best Rated"}
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["UAE", "UPSN"]})
        ],
        outputs=['[\n  "UAE",\n  "UPSN"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_006",
        instruction="""
            You are tasked with listing all carriers currently active in the system. Calculate the overall maximum of these carriers' on time delivery percentages. For each carrier whose rating equals overall maximum, update their record by adding a new attribute called "highlight" with the value "Best Delivery." Finally, review the updated details of all carriers flagged for best delivery. Finally, return the scacs of updated carriers.
            """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU", "COSU",
                                "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU",
                                "LOT", "SAS", "LAAL", "ICE", "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SUDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
            Action(name="update_carrier", kwargs={
                "carrier_scac": "UPSN",
                "updates": {"highlight": "Best Delivery"}
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["UPSN"]})
        ],
        outputs=['[\n  "UPSN"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_007",
        instruction="""
        You are the warehouse inventory coordinator responsible for monitoring inventory integrity. Your task is to identify all inventory items that have a damaged quantity greater than zero. Once these items are found, update their records to mark them for review, ensuring they are flagged for further inspection or action. After the updates are complete, retrieve and review the details of one of the affected inventory records to verify the changes.
        """,
        actions=[
            Action(name="get_inventory_with_damage", kwargs={}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0001", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0002", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0003", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0005", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0006", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0007", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0010", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0013", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0015", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0016", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0017", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0018", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0020", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0021", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0022", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0023", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0024", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0025", "updates": {"status": "Under Review"}}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0025"})
        ],
        outputs=['"status": "Under Review"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_008",
        instruction="""
        You are the warehouse operations analyst responsible for monitoring storage utilization. Begin by retrieving the details of the owned warehouses. Assess their current utilization percentages, and if it is found to be below (not equal but only below) 60%, update the warehouse record by adding a flag to indicate it is underused. After applying this update, retrieve the warehouse details once more to confirm that the flag has been correctly added.
        """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Owned"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-01"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-08"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-13"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-14"}),
            Action(name="update_warehouse", kwargs={
                "warehouse_id": "WH-11",
                "updates": {"underused_flag": True}
            }),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-11"}),
        ],
        outputs=['"underused_flag": true']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_009",
        instruction="""
        You are the warehouse operations analyst responsible for monitoring storage utilization. Begin by retrieving the details of the leased warehouses. Assess their current utilization percentages, and if it is found to be below (not equal but only below) 80%, update the warehouse record by adding a flag to indicate it is underused. After applying this update, retrieve the warehouse details once more to confirm that the flag has been correctly added.
        """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Leased"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-02"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-09"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="update_warehouse", kwargs={
                "warehouse_id": "WH-12",
                "updates": {"underused_flag": True}
            }),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
        ],
        outputs=['"underused_flag": true']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_010",
        instruction="""
        Retrieve all outbound orders with a total value exceeding 100,000.
        Check if these orders have priority level "High" or not.
        If priority level is not high, update their priority status to “High” for expedited processing.
        Check details of the updated orders.
        Finally, report the ids of updated orders.
        """,
        actions=[
            Action(name="get_high_value_outbound_orders", kwargs={"min_value": 100000}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0002"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0005"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0006"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0007"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0008"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0009"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0010"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0011"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0013"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0015"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0016"}),
            Action(name="update_outbound_order",
                   kwargs={"order_id": "ORD-0005", "updates": {"priority_level": "High"}}),
            Action(name="update_outbound_order",
                   kwargs={"order_id": "ORD-0006", "updates": {"priority_level": "High"}}),
            Action(name="update_outbound_order",
                   kwargs={"order_id": "ORD-0007", "updates": {"priority_level": "High"}}),
            Action(name="update_outbound_order",
                   kwargs={"order_id": "ORD-0009", "updates": {"priority_level": "High"}}),
            Action(name="update_outbound_order",
                   kwargs={"order_id": "ORD-0010", "updates": {"priority_level": "High"}}),
            Action(name="update_outbound_order",
                   kwargs={"order_id": "ORD-0013", "updates": {"priority_level": "High"}}),
            Action(name="update_outbound_order",
                   kwargs={"order_id": "ORD-0015", "updates": {"priority_level": "High"}}),
            Action(name="update_outbound_order",
                   kwargs={"order_id": "ORD-0016", "updates": {"priority_level": "High"}}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0005"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0006"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0007"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0009"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0010"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0013"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0015"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0016"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["ORD-0005", "ORD-0006", "ORD-0007", "ORD-0009",
                                                              "ORD-0010", "ORD-0013", "ORD-0015", "ORD-0016"]})
        ],
        outputs=['[\n  "ORD-0005",\n  "ORD-0006",\n  "ORD-0007",\n  "ORD-0009",\n  "ORD-0010",\n  "ORD-0013",\n  "ORD-0015",\n  "ORD-0016"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_011",
        instruction="""
        You are the logistics coordinator assigned to track and manage shipment timelines. You need to consider only those shipments with priority_level medium. Retrieve the shipments and verify their current status. If the status is marked as “In Transit,” update shipment's estimated arrival date by extending it 3 days beyond the current expected arrival date. After making the update, check the new expected_arrival_date to confirm the change has been applied. Finally, report the ids of updated shipments.
        """,
        actions=[
            Action(name="filter_inbound_shipments", kwargs={"key": "priority_level", "value": "Medium"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0001"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0003"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0005"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0015"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0018"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0023"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0025"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0028"}),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0001",
                "updates": {"expected_arrival_date": "2024-06-23"}
            }),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0003",
                "updates": {"expected_arrival_date": "2024-06-18"}
            }),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0005",
                "updates": {"expected_arrival_date": "2024-06-23"}
            }),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0009",
                "updates": {"expected_arrival_date": "2024-06-19"}
            }),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0011",
                "updates": {"expected_arrival_date": "2024-06-28"}
            }),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0015",
                "updates": {"expected_arrival_date": "2024-06-20"}
            }),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0018",
                "updates": {"expected_arrival_date": "2024-06-25"}
            }),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0023",
                "updates": {"expected_arrival_date": "2024-06-09"}
            }),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0025",
                "updates": {"expected_arrival_date": "2024-06-22"}
            }),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0028",
                "updates": {"expected_arrival_date": "2024-07-04"}
            }),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0001"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0003"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0005"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0015"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0018"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0023"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0025"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0028"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0009", "SHIP-0011",
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
            You are evaluating the performance of active carriers operating with the service mode Air.
            Start by retrieving all carriers that are currently active.
            From this set, filter the carriers that operate specifically with the Air mode of transport.
            Calculate the maximum on-time delivery percentage and the maximum average rating among these air carriers.
            There could be multiple carriers matching these records.
            If A and B matches max on time delivery percentage and B and C matches max average rating, consider all three carriers for updates.
            For each of these carriers, update their record by adding an attribute notes with the value "Best Performance by Air".
            Finally, return the list of scacs of all carriers that were updated with this note.
            """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_carriers_by_mode", kwargs={"mode": "Air", "list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU",
                "COSU", "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV",
                "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE", "DHLG"
            ]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NPEX", "DBSG", "UAE", "FDEG", "QFA", "KNLU", "UPSN", "THY", "LOT", "SAS", "LAAL", "ICE", "DHLG"]
            }),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["NPEX", "DBSG", "UAE", "FDEG", "QFA", "KNLU", "UPSN", "THY", "LOT", "SAS", "LAAL", "ICE", "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "UPSN", "updates": {"notes": "Best Performance by Air"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "UAE", "updates": {"notes": "Best Performance by Air"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["UPSN", "UAE"]})

        ],
        outputs=['[\n  "UPSN",\n  "UAE"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_013",
        instruction="""
        You are the inventory control specialist responsible for maintaining product quality and compliance. As of today's date, June 20, 2025, retrieve all inventory items that have passed their expiration date. For each expired item identified, update its status in the inventory system to “Expired” to reflect its current condition. After completing the updates, retrieve and review the details of one of these updated items to verify that the status change has been correctly applied.
        """,
        actions=[
            Action(name="get_expired_inventory", kwargs={"today": "2025-06-20"}),
            Action(name="update_inventory", kwargs={
                "inventory_id": "INV-0003",
                "updates": {"status": "Expired"}
            }),
            Action(name="update_inventory", kwargs={
                "inventory_id": "INV-0008",
                "updates": {"status": "Expired"}
            }),
            Action(name="update_inventory", kwargs={
                "inventory_id": "INV-0024",
                "updates": {"status": "Expired"}
            }),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"})
        ],
        outputs=['"status": "Expired"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_014",
        instruction="""
            You are evaluating the performance of active carriers operating with the service mode Sea.
            Begin by retrieving all carriers that are currently marked as active.
            From this set, filter out the carriers that specifically operate using the Sea mode of transport.
            Among these sea carriers, calculate both the maximum on-time delivery percentage and the maximum average rating.
            There could be multiple carriers matching these records. If A and B matches max on time delivery percentage and B and C matches max average rating, consider all three carriers for updates.
            For each of these top-performing carriers, update their record by adding an attribute notes with the value "Best Performance by Sea". Finally, return a list containing the SCACs of all carriers that were updated with this note.
            """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_carriers_by_mode", kwargs={"mode": "Sea", "list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU",
                "COSU", "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV",
                "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE", "DHLG"
            ]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "COSU", "MSCU", "KNLU", "HLCU", "EGLV", "SUDU"]
            }),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "COSU", "MSCU", "KNLU", "HLCU", "EGLV", "SUDU"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SUDU"}),
            Action(name="update_carrier",
                   kwargs={"carrier_scac": "NPEX", "updates": {"notes": "Best Performance by Sea"}}),
            Action(name="update_carrier",
                   kwargs={"carrier_scac": "KNLU", "updates": {"notes": "Best Performance by Sea"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["NPEX", "KNLU"]})

        ],
        outputs=['[\n  "NPEX",\n  "KNLU"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_015",
        instruction="""
                You are evaluating the performance of active carriers operating with the service mode Truck.
                Begin by retrieving all carriers that are currently marked as active.
                From this set, filter out the carriers that specifically operate using the Truck mode of transport.
                Among these truck carriers, calculate both the maximum on-time delivery percentage and the maximum average rating.
                There could be multiple carriers matching these records.
                If A and B matches max on time delivery percentage and B and C matches max average rating, consider all three carriers for updates.
                For each of these top-performing carriers, update their record by adding an attribute notes with the value "Best Performance by Truck". Finally, return a list containing the SCACs of all carriers that were updated with this note.
                """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_carriers_by_mode", kwargs={"mode": "Truck", "list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU",
                "COSU", "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV",
                "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE", "DHLG"
            ]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["MAEU","NPEX", "DBSG", "CMDU", "FDEG", "CNRU", "KNLU", "UPSN", "DHLG"]
            }),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["MAEU","NPEX", "DBSG", "CMDU", "FDEG", "CNRU", "KNLU", "UPSN", "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
            Action(name="update_carrier",
                   kwargs={"carrier_scac": "UPSN", "updates": {"notes": "Best Performance by Truck"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["UPSN"]})

        ],
        outputs=['[\n  "UPSN"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_016",
        instruction="""
        You are the product data analyst responsible for ensuring proper storage classifications. Begin by retrieving the details of all products categorized under “Pharmaceuticals.” Review each product entry to determine whether it requires refrigerated storage. For those that do, update the product record to include a “Cold Chain” flag indicating special handling requirements. Once the updates are complete, retrieve and report the details of one of the updated products to confirm the changes have been successfully applied.
        """,
        actions=[
            Action(name="get_products_by_category", kwargs={"category": "Pharmaceuticals"}),
            Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
            Action(name="get_product_by_sku", kwargs={"sku": "PHRM-DRUG-S19"}),
            Action(name="get_products_by_storage_requirement", kwargs={"keyword": "refrigerated"}),
            Action(name="update_product", kwargs={
                "sku": "PHRM-VACC-D4",
                "updates": {"cold_chain_flag": True}
            }),
            Action(name="update_product", kwargs={
                "sku": "PHRM-DRUG-S19",
                "updates": {"cold_chain_flag": True}
            }),
            Action(name="get_product_by_sku", kwargs={"sku": "PHRM-DRUG-S19", })
        ],
        outputs=['"cold_chain_flag": true']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_017",
        instruction="""
        You are the inventory quality control analyst assigned to monitor warehouse stock conditions. Locate all inventory items stored in warehouse WH-03 that have a damaged quantity greater than zero. Retrieve these items and update their status to “Under Review” to initiate quality inspection procedures. After updating the records, calculate and report the total number of units marked as damaged across these items to support further action.
        """,
        actions=[
            Action(name="get_inventory_by_warehouse", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_inventory_with_damage",
                   kwargs={"list_of_ids": ["INV-0002", "INV-0014", "INV-0017", "INV-0021", "INV-0025"]}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0002", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0017", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0021", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0025", "updates": {"status": "Under Review"}}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0002"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0017"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0021"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0025"}),
            Action(name="calculate_total", kwargs={
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
                You are evaluating the performance of active carriers operating with the service mode Rail.
                Begin by retrieving all carriers that are currently marked as active.
                From this set, filter out the carriers that specifically operate using the Rail mode of transport.
                Among these rail carriers, calculate both the maximum on-time delivery percentage and the maximum average rating.
                There could be multiple carriers matching these records.
                If A and B matches max on time delivery percentage and B and C matches max average rating, consider all three carriers for updates.
                For each of these top-performing carriers, update their record by adding an attribute notes with the value "Best Performance by Rail".
                Finally, return a list containing the SCACs of all carriers that were updated with this note.
                """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_carriers_by_mode", kwargs={"mode": "Rail", "list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU",
                "COSU", "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV",
                "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE", "DHLG"
            ]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CNRU", "MSCU", "KNLU"]
            }),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CNRU", "MSCU", "KNLU"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="update_carrier",
                   kwargs={"carrier_scac": "NPEX", "updates": {"notes": "Best Performance by Rail"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="update_carrier",
                   kwargs={"carrier_scac": "KNLU", "updates": {"notes": "Best Performance by Rail"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["NPEX", "KNLU"]})
        ],
        outputs=['[\n  "NPEX",\n  "KNLU"\n]']
    ),


    Task(
        annotator="ArpanMahatra1999",
        user_id="task_019",
        instruction="""
                You are evaluating the performance of active carriers operating with the service mode Parcel.
                Begin by retrieving all carriers that are currently marked as active.
                From this set, filter out the carriers that specifically operate using the Parcel mode of transport.
                Among these parcel carriers, calculate both the maximum on-time delivery percentage and the maximum average rating.
                There could be multiple carriers matching these records.
                If A and B matches max on time delivery percentage and B and C matches max average rating, consider all three carriers for updates.
                For each of these top-performing carriers, update their record by adding an attribute notes with the value "Best Performance by Parcel".
                Finally, return a list containing the SCACs of all carriers that were updated with this note.
                """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_carriers_by_mode", kwargs={"mode": "Parcel", "list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU",
                "COSU", "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV",
                "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE", "DHLG"
            ]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["FDEG", "UPSN", "DHLG"]
            }),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["FDEG", "UPSN", "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
            Action(name="update_carrier",
                   kwargs={"carrier_scac": "UPSN", "updates": {"notes": "Best Performance by Parcel"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["UPSN"]})
        ],
        outputs=['[\n  "UPSN"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_020",
        instruction="""
            You are reviewing supplier compliance and performance for a specific case and broader preferred supplier evaluation. Start by retrieving the supplier details for supplier ID SUP-1015. Check whether this supplier is marked as preferred and if they hold at least one certification. If either of these conditions is not satisfied, update the supplier’s record by adding a compliance_alert attribute indicating non-compliance. After this update, report the supplier’s certifications, relationship_status, and the new compliance_alert.
            Next, review all preferred suppliers in the system who also hold at least one certification. Among this group, identify the supplier(s) with the highest performance rating. If multiple suppliers share this top performance rating, include all of them. Return the list of supplier IDs for these top-rated, preferred, and certified suppliers.
            """,
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1015"}),
            Action(name="update_supplier", kwargs={
                "supplier_id": "SUP-1015",
                "updates": {"compliance_alert": True}
            }),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1015"}),
            Action(name="get_preferred_suppliers", kwargs={}),
            Action(name="get_certified_suppliers", kwargs={"list_of_ids": ["SUP-1002", "SUP-1005", "SUP-1010", "SUP-1013", "SUP-1016", "SUP-1019", "SUP-1029"]}),
            Action(name="calculate_aggregate", kwargs={
                        "agg": "max",
                        "json": "supplier_master",
                        "key": "supplier_id",
                        "value": "performance_rating",
                        "list_of_ids": ["SUP-1002", "SUP-1005", "SUP-1010", "SUP-1013", "SUP-1016", "SUP-1019", "SUP-1029"]
            }),
            Action(name="return_ids", kwargs={"list_of_ids": ["SUP-1002", "SUP-1010", "SUP-1016", "SUP-1029"]})
        ],
        outputs=['["SUP-1002", "SUP-1010", "SUP-1016", "SUP-1029"]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_021",
        instruction="""
        You are a logistics planner responsible for optimizing carrier assignments for inbound shipments. Begin by reviewing the shipment with ID SHIP-0021 and verify whether the currently assigned carrier is active. If the carrier is active, proceed to identify the active carrier with the highest on-time delivery percentage. Update the shipment by assigning it to this top-performing carrier. Once the update is complete, confirm the changes by retrieving and reviewing the updated shipment details.
        """,
        actions=[
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_active_carriers", kwargs={}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU", "COSU", "QFA",
                                "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE",
                                "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="update_inbound_shipment", kwargs={
                "shipment_id": "SHIP-0021",
                "updates": {
                    "carrier_scac": "UPSN",
                    "carrier_name": "UPS"
                },
            }),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0021"}),
        ],
        outputs=[
            '"carrier_name": "UPS"',
            '"carrier_scac": "UPSN"',
        ]
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_022",
            instruction="""
                You are a logistics coordinator responsible for managing delayed inbound shipments.
                Begin by identifying all inbound shipments that are currently marked as delayed and review their details.
                For each of these shipments, determine the associated warehouse.
                Then, review the inventory stored within those warehouses.
                Among this inventory, check the one with the least number of damaged units.
                Choose the shipment associated with the warehouse associated with this inventory.
                Once identified, update the status of that inbound shipment to "Planned" to reschedule its processing.
                """,
            actions=[
                Action(name="get_shipments_by_status", kwargs={"status": "Delayed"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0022"}),
                Action(name="get_inventory_by_warehouse", kwargs={"warehouse_id": "WH-04"}),
                Action(name="get_inventory_by_warehouse", kwargs={"warehouse_id": "WH-15"}),
                Action(name="get_inventory_with_damage",
                       kwargs={"list_of_ids": ["INV-0015", "INV-0018", "INV-0016", "INV-0020"]}),
                Action(name="calculate_aggregate", kwargs={
                    "agg": "min",
                    "json": "inventory",
                    "key": "inventory_id",
                    "value": "quantity_damaged",
                    "list_of_ids": ["INV-0015", "INV-0018", "INV-0016", "INV-0020"]
                }),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0018"}),
                Action(name="update_inbound_shipment", kwargs={
                    "shipment_id": "SHIP-0004",
                    "updates": {
                        "status": "Planned"
                    }
                }),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"})
            ],
            outputs=['"status": "Planned"']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_023",
        instruction="""
        You are a shipment analyst responsible for ensuring the reliability of carrier assignments for outbound orders.
        Begin by reviewing all outbound orders currently marked as “Shipped” and verify whether their assigned carriers are active.
        For any order linked to an inactive carrier, identify the top-rated active carrier from the list of all available carriers.
        If two or more carriers are top rated with same average rating, consider the one as top-rated with better on-time delivery percentage.
        Update the affected orders with the details of this top-rated carrier.
        Once all updates are complete, confirm the changes by reviewing the updated order information.
        """,
        actions=[
            Action(name="get_orders_by_status", kwargs={"status": "Shipped"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0003"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0006"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0007"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0012"}),
            Action(name="get_active_carriers", kwargs={"list_of_scacs": ["FDEG", "MAEU", "COSU", "KCSM"]}),
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_top_rated_carriers", kwargs={
                'list_of_scacs': ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU", "COSU", "QFA",
                                  "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE",
                                  "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={
                "carrier_scac": "UAE"
            }),
            Action(name="get_carrier_by_scac", kwargs={
                "carrier_scac": "UPSN"
            }),
            Action(name="update_outbound_order", kwargs={
                "order_id": "ORD-0012",
                "updates": {
                    "carrier_scac": "UPSN",
                    "carrier_name": "UPS"
                }
            }),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0012"}),
        ],
        outputs=[
            '"carrier_name": "UPS"',
            '"carrier_scac": "UPSN"'
        ]
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_024",
            instruction="""
                You are a warehouse manager tasked with assessing storage conditions and inventory quality.
                Begin by reviewing all expired inventory items that also have a damaged quantity greater than 0, using 2025-06-20 as today’s date for determining expiry.
                For each of these inventory items, update the status to "Replacement Needed" and identify the associated warehouse.
                For each associated warehouse, update its status to "Needs Expansion".
                Finally, confirm the updates by reviewing the details of the affected inventories and warehouses. Return the list of updated inventories.
                """,
            actions=[
                Action(name="get_expired_inventory", kwargs={'today': "2025-06-20"}),
                Action(name="get_inventory_with_damage", kwargs={'list_of_ids': ["INV-0003", "INV-0008", "INV-0024"]}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0003"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0003",
                    "updates": {"status": "Replacement Needed"}
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0024",
                    "updates": {"status": "Replacement Needed"}
                }),
                Action(name="update_warehouse", kwargs={
                    "warehouse_id": "WH-05",
                    "updates": {
                        "status": "Needs Expansion"
                    }
                }),
                Action(name="update_warehouse", kwargs={
                    "warehouse_id": "WH-10",
                    "updates": {
                        "status": "Needs Expansion"
                    }
                }),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0003"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
                Action(name="return_ids", kwargs={"list_of_ids": ["INV-0003", "INV-0024"]})
            ],
            outputs=['[\n  "INV-0003",\n  "INV-0024"\n]']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_025",
        instruction="""
        You are a supply chain analyst tasked with analyzing outbound orders valued over $100,000 that require temperature control. For each order, verify whether the products are classified as hazardous, fragile, or both. If an order contains hazardous products, add the note "BEWARE HAZARDOUS" to its extra notes. If the order contains fragile products, add "BEWARE FRAGILE." For orders that are both hazardous and fragile, add the combined note "BEWARE HAZARDOUS & FRAGILE." After applying these updates, retrieve and review the details of the updated orders to confirm the changes.
        """,
        actions=[
            Action(name="get_high_value_outbound_orders", kwargs={"min_value": 100000}),
            Action(name="get_orders_requiring_temperature_control", kwargs={
                "list_of_ids": [
                    "ORD-0002", "ORD-0005", "ORD-0006", "ORD-0007", "ORD-0008", "ORD-0009", "ORD-0010", "ORD-0011",
                    "ORD-0013", "ORD-0015", "ORD-0016"
                ]
            }),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0008"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0011"}),
            Action(name="update_outbound_order", kwargs={
                "order_id": "ORD-0011",
                "updates": {
                    "extra_note": "BEWARE FRAGILE"
                }
            }),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0011"}),
        ],
        outputs=['"extra_note": "BEWARE FRAGILE"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_026",
        instruction="""
        You are a procurement specialist responsible for managing supplier qualifications. Review the list of preferred suppliers and identify those who do not hold a valid ISO certification. For each supplier lacking this certification, update their certification_status to "ISO Certification Pending." After completing these updates, retrieve and verify the details of one of the updated suppliers to ensure the changes have been correctly applied.
        """,
        actions=[
            Action(name="get_preferred_suppliers", kwargs={}),
            Action(name="get_certified_suppliers", kwargs={"certification": "ISO", "list_of_ids": [
                "SUP-1002", "SUP-1005", "SUP-1010", "SUP-1013", "SUP-1016", "SUP-1019", "SUP-1029"
            ]}),
            Action(name="update_supplier", kwargs={
                "supplier_id": "SUP-1005",
                "updates": {
                    "certification_status": "ISO Certification Pending"
                }
            }),
            Action(name="update_supplier", kwargs={
                "supplier_id": "SUP-1010",
                "updates": {
                    "certification_status": "ISO Certification Pending"
                }
            }),
            Action(name="update_supplier", kwargs={
                "supplier_id": "SUP-1029",
                "updates": {
                    "certification_status": "ISO Certification Pending"
                }
            }),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1029"}),
        ],
        outputs=['"certification_status": "ISO Certification Pending"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_027",
        instruction="""
        You are an inventory controller responsible for maintaining warehouse stock quality. As of May 25, 2025, assess all warehouses that contain expired inventory items. For each identified warehouse, update its status to “Restock Needed” and mark all expired inventory within it as “On Hold” to prevent further use. After completing these updates, retrieve and review the inventory details to confirm that the status changes have been properly applied.
        """,
        actions=[
            Action(name="get_expired_inventory", kwargs={'today': '2025-05-25'}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0003"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
            Action(name="update_inventory", kwargs={
                "inventory_id": "INV-0003",
                "updates": {
                    "stock_status": "On Hold"
                }
            }),
            Action(name="update_inventory", kwargs={
                "inventory_id": "INV-0024",
                "updates": {
                    "stock_status": "On Hold"
                }
            }),
            Action(name="update_warehouse", kwargs={
                "warehouse_id": "WH-05",
                "updates": {
                    "status": "Restock Needed"
                }
            }),
            Action(name="update_warehouse", kwargs={
                "warehouse_id": "WH-10",
                "updates": {
                    "status": "Restock Needed"
                }
            }),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0003"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
        ],
        outputs=['"stock_status": "On Hold"']
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_028",
            instruction="""
                You are a shipment auditor responsible for ensuring carrier compliance on inbound shipments.
                Begin by auditing all inbound shipments that have a status of "In Transit".
                For each shipment, verify whether the assigned carrier is currently active.
                Identify the active carrier with the highest average rating.
                Check all the shipments and find the shipment associated with this carrier and update those shipments with notes "Best Carrier".
                After processing all applicable shipments, report the highest average rating.
                """,
            actions=[
                Action(name="get_shipments_by_status", kwargs={"status": "In Transit"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0001"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0003"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0005"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0008"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0009"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0011"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0012"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0013"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0014"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0015"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0018"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0020"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0021"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0023"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0024"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0025"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0026"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0028"}),
                Action(name="get_active_carriers", kwargs={
                    "list_of_scacs": [
                        "MAEU", "DBSG", "CMDU", "CNRU", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "SUDU", "SAS"
                    ]
                }),
                Action(name="calculate_aggregate", kwargs={
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": ["MAEU", "DBSG", "CMDU", "CNRU", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "SUDU",
                                    "SAS"]
                }),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0014", "updates": {"notes": "Best Carrier"}}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0023", "updates": {"notes": "Best Carrier"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0014"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0023"}),
            ],
            outputs=['4.9']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_029",
            instruction="""
                You are a product manager responsible for evaluating pharmaceutical storage requirements. Start by retrieving a list of pharmaceutical products that require refrigerated storage. Review the details of these products, focusing specifically on their weight. Identify the product that has the lowest weight among them. Once identified, update this product by adding a note with the value "LOW WEIGHT PRODUCT" to highlight its lightweight nature. Finally, review and confirm the updated details of this product.
                """,
            actions=[
                Action(name="get_products_by_category", kwargs={"category": "Pharmaceuticals"}),
                Action(name="get_products_by_storage_requirement",
                       kwargs={"keyword": "refrigerated", 'list_of_ids': ["PHRM-VACC-D4", "PHRM-DRUG-S19"]}),
                Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="get_product_by_sku", kwargs={"sku": "PHRM-DRUG-S19"}),
                Action(name="calculate_aggregate", kwargs={
                    "agg": "min",
                    "json": "product_master",
                    "key": "sku",
                    "value": "weight_kg",
                    "list_of_ids": ["PHRM-VACC-D4", "PHRM-DRUG-S19"]
                }),
                Action(name="update_product", kwargs={"sku": "PHRM-VACC-D4", "updates": {
                    "notes": "LOW WEIGHT PRODUCT"
                }}),
                Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
            ],
            outputs=['"sku": "PHRM-VACC-D4"']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_030",
            instruction="""
                You are an inventory specialist responsible for managing damaged stock.
                Begin by listing all inventory items where the damaged quantity is greater than 0.
                For each of these items, update the status attribute to "Pending Restock" to reflect their pending resolution or replacement.
                After updating, review the details of these inventory items to ensure the changes are correctly applied. Finally, return the list of inventory IDs that were updated.
                """,
            actions=[
                Action(name="get_inventory_with_damage", kwargs={}),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0001",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0002",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0003",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0005",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0006",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0007",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0010",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0013",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0015",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0016",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0017",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0018",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0020",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0021",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0022",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0023",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0024",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="update_inventory", kwargs={
                    "inventory_id": "INV-0025",
                    "updates": {
                        "status": "Pending Restock"
                    }
                }),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0001"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0002"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0003"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0005"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0006"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0007"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0013"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0017"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0018"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0021"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0022"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0023"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0025"}),
                Action(name="return_ids", kwargs={"list_of_ids": [
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
                You are a carrier analyst. Your task is to begin by retrieving the details of shipment SHIP-0004 and identifying the assigned carrier.
                Check whether this carrier is currently active. If the carrier is not active, proceed to search for an active carrier that supports the same mode of transport and has the highest average rating among those available.
                If two or more carriers have same highest average rating, consider the carrier among them with highest on time delivery percentage.
                Once identified, update the inbound shipment to assign this top-rated active carrier.
                """,
            actions=[
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HJSC"}),
                Action(name="get_active_carriers", kwargs={}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SUDU"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
                Action(name="calculate_aggregate", kwargs={
                    'agg': 'max',
                    'json': 'carriers',
                    'key': 'scac',
                    'value': 'performance_metrics',
                    'value2': 'average_rating',
                    'list_of_ids': ['MAEU', 'NPEX', 'DBSG', 'CMDU', 'COSU', 'MSCU', 'KNLU', 'HLCU', 'EGLV', 'SUDU']
                }),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0004", "updates": {
                    "carrier_scac": "KNLU",
                    "carrier_name": "Kuehne + Nagel",
                }}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
            ],
            outputs=['"carrier_scac": "KNLU"']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_032",
            instruction="""
                You are an inventory manager.
                Begin by identifying all warehouses that have inventory records containing damaged items.
                Among these warehouses, determine which one has the lowest current utilization percentage.
                Once identified, update that warehouse by adding an attribute note with the value "Lowest Utilization Percent" to flag it for operational review.
                """,
            actions=[
                Action(name="get_inventory_with_damage", kwargs={}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0001"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0002"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0003"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0005"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0006"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0007"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0013"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0017"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0018"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0021"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0022"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0023"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0025"}),
                Action(name="calculate_aggregate", kwargs={
                    'agg': 'min',
                    'json': 'warehouses',
                    'key': "warehouse_id",
                    'value': 'current_utilization_percentage',
                    'list_of_ids': ['WH-01', 'WH-02', 'WH-03', 'WH-04',
                                    'WH-05', 'WH-07', 'WH-08', 'WH-09',
                                    'WH-10', 'WH-12', 'WH-14', 'WH-15']
                }),
                Action(name="update_warehouse", kwargs={"warehouse_id": "WH-07", "updates": {
                    "note": "Lowest Utilization Percent"
                }}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"})
            ],
            outputs=['"note": "Lowest Utilization Percent"']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_033",
            instruction="""
                You are a product compliance officer.
                Begin by identifying all hazardous products listed in the inventory.
                Review each of these products to verify whether their storage requirements include the term "hazmat".
                For any product where this requirement is missing or incorrect, update the product record by adding a notes attribute with the value "BEWARE HAZMAT" to ensure proper handling protocols are followed.
                After updating, review the details of the affected products. Check the associated inventories to these products and review that those inventories have quantity available.
                Finally, return the list of SKUs of all products that were updated.
                """,
            actions=[
                Action(name="get_hazmat_products", kwargs={}),
                Action(name="get_products_by_storage_requirement", kwargs={"keyword": "hazmat", 'list_of_ids': [
                    "PHRM-VACC-D4",
                    "CHEM-SOLV-K11",
                    "TECH-BATT-Q17",
                    "ELEC-SMART-W23"
                ]}),
                Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="update_product", kwargs={"sku": "PHRM-VACC-D4",
                                                      'updates': {"notes": "BEWARE HAZMAT"}}),
                Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="get_product_by_sku", kwargs={"sku": "ELEC-SMART-W23"}),
                Action(name="update_product", kwargs={"sku": "ELEC-SMART-W23",
                                                      'updates': {"notes": "BEWARE HAZMAT"}}),
                Action(name="get_product_by_sku", kwargs={"sku": "ELEC-SMART-W23"}),
                Action(name="filter_inventory", kwargs={"key": "sku", "value": "PHRM-VACC-D4"}),
                Action(name="filter_inventory", kwargs={"key": "sku", "value": "ELEC-SMART-W23"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0023"}),
                Action(name="return_ids", kwargs={"list_of_ids": ["PHRM-VACC-D4", "ELEC-SMART-W23"]})
            ],
            outputs=['[\n  "PHRM-VACC-D4",\n  "ELEC-SMART-W23"\n]']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_034",
        instruction="""
        You are a shipment coordinator responsible for managing inbound shipments with a status of “Delayed.” Review all such shipments and identify any that are assigned to inactive carriers. For each affected shipment, reassign it to an active carrier to ensure timely handling. After completing the reassignments, retrieve and review the details of the updated shipments to confirm that the changes have been applied correctly.
        """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "Delayed"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0022"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HJSC"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0004",
                                                           "updates": {"carrier_scac": "MSCU",
                                                                       "carrier_name": "MSC Mediterranean Shipping Company"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"})
        ],
        outputs=['"carrier_scac": "MSCU"']
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_035",
            instruction="""
            You are a supplier relations manager.
            Examine preferred suppliers and validate their certification status by going through details.
            If preferred suppliers don't have ISO certifications, update them with attribute note "ISO certification required".
            For preferred suppliers with certifications "ISO",
            Find the supplier among these with least standard lead time days.
            Update the supplier with the attribute note "Least Standard Lead Time Days".
            """,
            actions=[
                Action(name="get_preferred_suppliers", kwargs={}),
                Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1002"}),
                Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1005"}),
                Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1010"}),
                Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1013"}),
                Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1016"}),
                Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1019"}),
                Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1029"}),
                Action(name="get_certified_suppliers", kwargs={"certification": "ISO", "list_of_ids": ["SUP-1002",
                                                                                                       "SUP-1005",
                                                                                                       "SUP-1010",
                                                                                                       "SUP-1013",
                                                                                                       "SUP-1016",
                                                                                                       "SUP-1019",
                                                                                                       "SUP-1029"]}),
                Action(name="update_supplier",
                       kwargs={'supplier_id': "SUP-1005", "updates": {"note": "ISO certification required"}}),
                Action(name="get_supplier_by_id", kwargs={'supplier_id': "SUP-1005"}),
                Action(name="update_supplier",
                       kwargs={'supplier_id': "SUP-1010", "updates": {"note": "ISO certification required"}}),
                Action(name="get_supplier_by_id", kwargs={'supplier_id': "SUP-1010"}),
                Action(name="update_supplier",
                       kwargs={'supplier_id': "SUP-1029", "updates": {"note": "ISO certification required"}}),
                Action(name="get_supplier_by_id", kwargs={'supplier_id': "SUP-1029"}),
                Action(name="calculate_aggregate", kwargs={
                    'agg': 'min',
                    'json': 'supplier_master',
                    'key': 'supplier_id',
                    'value': 'standard_lead_time_days',
                    'list_of_ids': ["SUP-1002", "SUP-1013", "SUP-1016", "SUP-1019"]
                }),
                Action(name="update_supplier",
                       kwargs={'supplier_id': "SUP-1019", "updates": {"note": "Least Standard Lead Time Days"}}),
                Action(name="get_supplier_by_id", kwargs={'supplier_id': "SUP-1019"})
            ],
            outputs=['"supplier_id": "SUP-1019"']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_036",
        instruction="""
        You are a warehouse replenishment officer.
        Your job is to identify all inventory where the quantity available is less than 100 and there is no damaged stock (quantity_damaged == 0).
        These items need to be flagged for replenishment by updating their status to “LOW STOCK”.
        Once updates are applied, verify a few updates, and finally return ids of the inventory marked as LOW STOCK.
        """,
        actions=[
            Action(name="get_inventory_with_damage", kwargs={"less_than_threshold": "True", "threshold": 1}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0008"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0009"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0011"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0012"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0014"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0019"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0009", "updates": {"status": "LOW STOCK"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0014", "updates": {"status": "LOW STOCK"}}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0009"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0014"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["INV-0009", "INV-0014"]})
        ],
        outputs=['[\n  "INV-0009",\n  "INV-0014"\n]']
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_037",
            instruction="""
            You are a warehouse replenishment officer.
            Your job is to identify all inventory where the quantity available is less than 100 and damaged stock is less than 10.
            These items need to be flagged for replenishment by updating their status to “LOW STOCK”.
            Once updates are applied, verify a few updates, and finally return ids of the inventory marked as LOW STOCK.
            """,
            actions=[
                Action(name="get_inventory_with_damage", kwargs={"less_than_threshold": "True", "threshold": 10}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0002"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0005"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0006"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0008"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0009"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0011"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0012"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0013"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0014"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0017"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0018"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0019"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0021"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0022"}),
                Action(name="update_inventory",
                       kwargs={"inventory_id": "INV-0009", "updates": {"status": "LOW STOCK"}}),
                Action(name="update_inventory",
                       kwargs={"inventory_id": "INV-0014", "updates": {"status": "LOW STOCK"}}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0009"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0014"}),
                Action(name="return_ids", kwargs={"list_of_ids": ["INV-0009", "INV-0014"]})
            ],
            outputs=['[\n  "INV-0009",\n  "INV-0014"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_038",
            instruction="""
                You are a warehouse operations manager. Begin by monitoring all warehouses that currently hold inventory items marked with any damage. Identify such warehouses where at least one inventory item has a damaged quantity greater than zero. For each of these warehouses, update their status to "Attention Required" to indicate the need for inspection or corrective action. Finally, review and confirm the details of all the updated warehouses to ensure the status changes have been correctly applied.
                """,
            actions=[
                Action(name="get_inventory_with_damage", kwargs={}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0001"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0002"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0003"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0005"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0006"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0007"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0013"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0017"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0018"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0021"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0022"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0023"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0025"}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-01", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-02", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-03", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-04", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-05", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-07", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-08", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-09", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-10", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-12", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-14", "updates": {"status": "Attention Required"}}),
                Action(name="update_warehouse",
                       kwargs={"warehouse_id": "WH-15", "updates": {"status": "Attention Required"}}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-01"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-02"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-03"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-08"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-09"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-14"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
                Action(name="return_ids", kwargs={"list_of_ids": [
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
            You are a product manager.
            Retrieve products that require "refrigerated" storage conditions and check if lifecycle status is active for these products.
            Check the inventory associated with these products and if quantity damaged > 0 for those inventory, add attribute notes "Replacement Required".
            Calculate maximum unit price among these products.
            """,
            actions=[
                Action(name="get_products_by_storage_requirement", kwargs={"keyword": "refrigerated"}),
                Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="get_product_by_sku", kwargs={"sku": "PHRM-DRUG-S19"}),
                Action(name="get_product_by_sku", kwargs={"sku": "FOOD-FLWR-X24"}),
                Action(name="filter_inventory", kwargs={"key": "sku", "value": "PHRM-VACC-D4"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
                Action(name="filter_inventory", kwargs={"key": "sku", "value": "PHRM-DRUG-S19"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0019"}),
                Action(name="filter_inventory", kwargs={"key": "sku", "value": "FOOD-FLWR-X24"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
                Action(name="update_inventory", kwargs={"inventory_id": "INV-0024", "updates": {"notes": "Replacement Required"}}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
                Action(name="calculate_aggregate", kwargs={
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
                You need to transfer 300 units from inventory INV-0025 to another due to an issue with the original stock.
                First, check if the source inventory has at least 300 units available.
                Then, find another inventory with the same SKU but a different ID.
                Review its current quantity.
                Subtract 300 units from the source inventory, and add to the destination.
                Next, add notes to both inventories about the updates so that employees could make changes to total value afterwards as well.
                Total value equivalent to 300 units should be deducted in source inventory. So, add note "300 units removed, total value change pending".
                Similarly, total value equivalent to 300 units should be added in destination inventory. So, add note "300 units added, total value change pending".
                Finally, confirm the updates are correctly reflected in both inventories and return the quantity available now in destination inventory.
                """,
            actions=[
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0025"}),
                Action(name="filter_inventory", kwargs={"key": "sku", "value": "ELEC-CHIP-A1"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0001"}),
                Action(name="update_inventory", kwargs={"inventory_id": "INV-0025", "updates": {
                    "quantity_on_hand": 7700, "quantity_available": 7700
                }}),
                Action(name="update_inventory", kwargs={"inventory_id": "INV-0001", "updates": {
                    "quantity_on_hand": 15300, "quantity_available": 12800
                }}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0025"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0001"}),
                Action(name="update_inventory", kwargs={"inventory_id": "INV-0025", "updates": {
                    "note": "300 units removed, total value change pending"
                }}),
                Action(name="update_inventory", kwargs={"inventory_id": "INV-0001", "updates": {
                    "note": "300 units added, total value change pending"
                }}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0025"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0001"}),
            ],
            outputs=['12800']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_041",
            instruction="""
            You are a order quality auditor.
            Review orders that require temperature-controlled transport.
            Ensure assigned carriers meet these requirements and are active.
            Separate active assigned carriers and inactive assigned carriers among these.
            For inactive ones, replace them on orders with highest rated active carrier.
            If only one active carrier is available, no need to check highest rated.
            For orders with inactive carriers, update carriers to qualified top-rated active one based on average rating.
            Finally, check the details of updated orders and return the list of updated orders.
            """,
            actions=[
                Action(name="get_orders_requiring_temperature_control", kwargs={}),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0004"}),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0008"}),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0011"}),
                Action(name="get_active_carriers", kwargs={"list_of_scacs": ["FDEG", "LTMG", "SAAW"]}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
                Action(name="update_outbound_order", kwargs={
                    "order_id": "ORD-0008",
                    "updates": {
                        "carrier_scac": "FDEG",
                        "carrier_name": "FedEx"
                    }
                }),
                Action(name="update_outbound_order", kwargs={
                    "order_id": "ORD-0011",
                    "updates": {
                        "carrier_scac": "FDEG",
                        "carrier_name": "FedEx"
                    }
                }),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0008"}),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0011"}),
                Action(name="return_ids", kwargs={"list_of_ids": ["ORD-0008", "ORD-0011"]})
            ],
            outputs=['[\n  "ORD-0008",\n  "ORD-0011"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_042",
            instruction="""
            You are an inventory replenishment coordinator.
            Identify expired inventory. Consider today's date to be "2026-07-20"
            Update inventory with 'notes' to be 'Replenishment Needed.'
            Once done, check inventory details of the updated inventory.
            Return the list of ids of updated inventory.
            """,
            actions=[
                Action(name="get_expired_inventory", kwargs={"today": "2026-07-20"}),
                Action(name="update_inventory",
                       kwargs={"inventory_id": "INV-0003", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="update_inventory",
                       kwargs={"inventory_id": "INV-0004", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="update_inventory",
                       kwargs={"inventory_id": "INV-0008", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="update_inventory",
                       kwargs={"inventory_id": "INV-0011", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="update_inventory",
                       kwargs={"inventory_id": "INV-0019", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="update_inventory",
                       kwargs={"inventory_id": "INV-0022", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="update_inventory",
                       kwargs={"inventory_id": "INV-0024", "updates": {"notes": "Replenishment Needed"}}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0003"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0008"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0011"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0019"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0022"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
                Action(name="return_ids", kwargs={"list_of_ids": ["INV-0003", "INV-0004", "INV-0008", "INV-0011", "INV-0019", "INV-0022", "INV-0024"]})
            ],
            outputs=['[\n  "INV-0003",\n  "INV-0004",\n  "INV-0008",\n  "INV-0011",\n  "INV-0019",\n  "INV-0022",\n  "INV-0024"\n]']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_043",
        instruction="""
        You are a supplier compliance officer responsible for auditing preferred suppliers' certification status for IEC compliance. Identify suppliers whose IEC certifications are expired or missing, and update their certification_status to "Compliance Review" to flag them for further action. After completing these updates, retrieve and review the details of one of the updated suppliers to confirm the changes have been properly applied.
        """,
        actions=[
            Action(name="get_preferred_suppliers", kwargs={}),
            Action(name="get_certified_suppliers", kwargs={"certification": "IEC", "list_of_ids": [
                "SUP-1002", "SUP-1005", "SUP-1010", "SUP-1013", "SUP-1016", "SUP-1019", "SUP-1029"
            ]}),
            Action(name="update_supplier",
                   kwargs={"supplier_id": "SUP-1002", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="update_supplier",
                   kwargs={"supplier_id": "SUP-1005", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="update_supplier",
                   kwargs={"supplier_id": "SUP-1010", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="update_supplier",
                   kwargs={"supplier_id": "SUP-1013", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="update_supplier",
                   kwargs={"supplier_id": "SUP-1016", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="update_supplier",
                   kwargs={"supplier_id": "SUP-1019", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="update_supplier",
                   kwargs={"supplier_id": "SUP-1029", "updates": {"certification_status": "Compliance Review"}}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1029"})
        ],
        outputs=['"certification_status": "Compliance Review"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_044",
        instruction="""
        You are a warehouse performance analyst tasked with monitoring inventory damage levels. Identify all inventory items with more than 100 damaged goods and track the warehouses where these items are stored. For each warehouse meeting this criterion, add a note flagging it as “High Damaged Goods.” After applying these updates, retrieve and review the details of one of the flagged warehouses to verify that the note has been correctly added.
        """,
        actions=[
            Action(name="get_inventory_with_damage", kwargs={'threshold': 100}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
            Action(name="update_warehouse",
                   kwargs={"warehouse_id": "WH-12", "updates": {"notes": "High Damaged Goods."}}),
            Action(name="update_warehouse",
                   kwargs={"warehouse_id": "WH-04", "updates": {"notes": "High Damaged Goods."}}),
            Action(name="update_warehouse",
                   kwargs={"warehouse_id": "WH-15", "updates": {"notes": "High Damaged Goods."}}),
            Action(name="update_warehouse",
                   kwargs={"warehouse_id": "WH-10", "updates": {"notes": "High Damaged Goods."}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"})
        ],
        outputs=['"notes": "High Damaged Goods."']
    ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_045",
            instruction="""
            You are a product quality analyst.
            Identify products flagged as hazardous and review product one by one.
            If there is nothing in storage requirements on hazmat class for these products, add notes as "HAZMAT SPECIFICATION REQUIRED".
            Finally, check product details of these updated products and return the list of skus of updated products.
            """,
            actions=[
                Action(name="get_hazmat_products", kwargs={}),
                Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="get_product_by_sku", kwargs={"sku": "CHEM-SOLV-K11"}),
                Action(name="get_product_by_sku", kwargs={"sku": "TECH-BATT-Q17"}),
                Action(name="get_product_by_sku", kwargs={"sku": "ELEC-SMART-W23"}),
                Action(name="update_product",
                       kwargs={"sku": "PHRM-VACC-D4", "updates": {"notes": "HAZMAT SPECIFICATION REQUIRED"}}),
                Action(name="update_product",
                       kwargs={"sku": "ELEC-SMART-W23", "updates": {"notes": "HAZMAT SPECIFICATION REQUIRED"}}),
                Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
                Action(name="get_product_by_sku", kwargs={"sku": "ELEC-SMART-W23"}),
                Action(name="return_ids", kwargs={"list_of_ids": ["PHRM-VACC-D4", "ELEC-SMART-W23"]})
            ],
            outputs=['[\n  "PHRM-VACC-D4",\n  "ELEC-SMART-W23"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_046",
            instruction="""
            You are a shipment officer.
            Review inbound shipments with Planned status.
            Confirm assigned carriers are active.
            Check the maximum average rating among the carriers
            Update all these planned shipments with the highest rated carrier.
            The objective is to use best carrier for the planned shipments.
            Return the list of ids of updated shipments.
            """,
            actions=[
                Action(name="get_shipments_by_status", kwargs={"status": "Planned"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0006"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0030"}),
                Action(name="get_active_carriers", kwargs={'list_of_scacs': [
                    "UAE", "QFA", "NPEX", "LOT", "ICE", "LAAL"
                ]}),
                Action(name="calculate_aggregate", kwargs={
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": ["UAE", "QFA", "NPEX", "LOT", "ICE", "LAAL"]
                }),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0010", "updates": {"carrier_scac": "UAE", "carrier_name": "Emirates SkyCargo"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0016", "updates": {"carrier_scac": "UAE", "carrier_name": "Emirates SkyCargo"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0019", "updates": {"carrier_scac": "UAE", "carrier_name": "Emirates SkyCargo"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0027", "updates": {"carrier_scac": "UAE", "carrier_name": "Emirates SkyCargo"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0029", "updates": {"carrier_scac": "UAE", "carrier_name": "Emirates SkyCargo"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="return_ids", kwargs={"list_of_ids": ["SHIP-0010", "SHIP-0016", "SHIP-0019", "SHIP-0027", "SHIP-0029"]})
            ],
            outputs=['[\n  "SHIP-0010",\n  "SHIP-0016",\n  "SHIP-0019",\n  "SHIP-0027",\n  "SHIP-0029"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_047",
            instruction="""
            You are a shipment officer.
            Review inbound shipments with Planned status.
            Confirm assigned carriers are active.
            Check the maximum insurance coverage limit among the carriers.
            Update all these planned shipments (except the shipment with carrier with maximum insurance coverage limit) with the top carrier based on insurance coverage limit.
            The objective is to use best carrier for the planned shipments.
            Return the list of ids of updated shipments.
            """,
            actions=[
                Action(name="get_shipments_by_status", kwargs={"status": "Planned"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0006"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0030"}),
                Action(name="get_active_carriers", kwargs={'list_of_scacs': [
                    "UAE", "QFA", "NPEX", "LOT", "ICE", "LAAL"
                ]}),
                Action(name="calculate_aggregate", kwargs={
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "insurance_details",
                    "value2": "coverage_limit_usd",
                    "list_of_ids": ["UAE", "QFA", "NPEX", "LOT", "ICE", "LAAL"]
                }),
                Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "NPEX",
                                                                "list_of_ids": ["SHIP-0006", "SHIP-0010", "SHIP-0016", "SHIP-0019", "SHIP-0027", "SHIP-0029", "SHIP-0030"]}),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0006", "updates": {"carrier_scac": "NPEX", "carrier_name": "Nippon Express"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0010", "updates": {"carrier_scac": "NPEX", "carrier_name": "Nippon Express"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0019", "updates": {"carrier_scac": "NPEX", "carrier_name": "Nippon Express"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0027", "updates": {"carrier_scac": "NPEX", "carrier_name": "Nippon Express"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0029", "updates": {"carrier_scac": "NPEX", "carrier_name": "Nippon Express"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0030", "updates": {"carrier_scac": "NPEX", "carrier_name": "Nippon Express"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0030"}),
                Action(name="return_ids", kwargs={"list_of_ids": ["SHIP-0006", "SHIP-0010", "SHIP-0019", "SHIP-0027", "SHIP-0029", "SHIP-0030"]})
            ],
            outputs=['[\n  "SHIP-0006",\n  "SHIP-0010",\n  "SHIP-0019",\n  "SHIP-0027",\n  "SHIP-0029",\n  "SHIP-0030"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_048",
            instruction="""
            You are a shipment officer.
            Review inbound shipments with Planned status.
            Confirm assigned carriers are active.
            Check the maximum on time delivery percentage among the carriers
            Update all these planned shipments with the top carrier based on on-time delivery percentage.
            The objective is to use best carrier for the planned shipments.
            Return the list of ids of updated shipments.
            """,
            actions=[
                Action(name="get_shipments_by_status", kwargs={"status": "Planned"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0006"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0030"}),
                Action(name="get_active_carriers", kwargs={'list_of_scacs': [
                    "UAE", "QFA", "NPEX", "LOT", "ICE", "LAAL"
                ]}),
                Action(name="calculate_aggregate", kwargs={
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": ["UAE", "QFA", "NPEX", "LOT", "ICE", "LAAL"]
                }),
                Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0010", "updates": {"carrier_scac": "UAE", "carrier_name": "Emirates SkyCargo"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0010"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0016", "updates": {"carrier_scac": "UAE", "carrier_name": "Emirates SkyCargo"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0016"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0019", "updates": {"carrier_scac": "UAE", "carrier_name": "Emirates SkyCargo"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0019"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0027", "updates": {"carrier_scac": "UAE", "carrier_name": "Emirates SkyCargo"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0027"}),
                Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0029", "updates": {"carrier_scac": "UAE", "carrier_name": "Emirates SkyCargo"}}),
                Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0029"}),
                Action(name="return_ids", kwargs={"list_of_ids": ["SHIP-0010", "SHIP-0016", "SHIP-0019", "SHIP-0027", "SHIP-0029"]})
            ],
            outputs=['[\n  "SHIP-0010",\n  "SHIP-0016",\n  "SHIP-0019",\n  "SHIP-0027",\n  "SHIP-0029"\n]']
        ),

        Task(
            annotator="ArpanMahatra1999",
            user_id="task_049",
            instruction="""
            You are a warehouse audit specialist.
            Check inventory with high damage over 50.
            Review details of warehouses of these damaged inventory to check if their current utilization percentage is above 50%.
            Then update warehouse status to 'Audit Completed' after review.
            Finally, check the lowest number of damaged quantity from the inventories above.
            The objective is to find the better threshold for considering inventory damaged.
            """,
            actions=[
                Action(name="get_inventory_with_damage", kwargs={'threshold': 50}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
                Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
                Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
                Action(name="update_warehouse", kwargs={"warehouse_id": "WH-12", "updates": {"status": "Audit Completed"}}),
                Action(name="update_warehouse", kwargs={"warehouse_id": "WH-04", "updates": {"status": "Audit Completed"}}),
                Action(name="update_warehouse", kwargs={"warehouse_id": "WH-15", "updates": {"status": "Audit Completed"}}),
                Action(name="update_warehouse", kwargs={"warehouse_id": "WH-10", "updates": {"status": "Audit Completed"}}),
                Action(name="calculate_aggregate", kwargs={
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
            You are a orders management officer.
            Find all outbound orders requiring temperature control.
            Check the details about all these outbound orders.
            Check if these orders are hazmat or not.
            Consider those orders among them which are not hazmat.
            Find the maximum and minimum temperature to consider in these orders.
            If maximum and minimum temperature has difference < 10,
            update these orders with attribute notes "Could be Grouped Together".
            Finally, check details of these updated orders and return the list of ids of these updated orders..
            """,
            actions=[
                Action(name="get_orders_requiring_temperature_control", kwargs={}),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0004"}),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0008"}),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0011"}),
                Action(name="calculate_aggregate", kwargs={
                    "agg": "both",
                    "json": "outbound_orders",
                    "key": "order_id",
                    "value": "temperature_celsius",
                    "list_of_ids": ["ORD-0004", "ORD-0008", "ORD-0011"]
                }),
                Action(name="update_outbound_order", kwargs={"order_id": "ORD-0004", "updates": {
                    "notes": "Could be Grouped Together"
                }}),
                Action(name="update_outbound_order", kwargs={"order_id": "ORD-0008", "updates": {
                    "notes": "Could be Grouped Together"
                }}),
                Action(name="update_outbound_order", kwargs={"order_id": "ORD-0011", "updates": {
                    "notes": "Could be Grouped Together"
                }}),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0004"}),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0008"}),
                Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0011"}),
                Action(name="return_ids", kwargs={"list_of_ids": ["ORD-0004", "ORD-0008", "ORD-0011"]})
            ],
            outputs=['[\n  "ORD-0004",\n  "ORD-0008",\n  "ORD-0011"\n]']
        ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_051",
        instruction="""
        You are a logistics coordinator responsible for managing planned inbound shipments.
        Begin by reviewing all planned inbound shipments to identify the one with the earliest expected departure date.
        Assess the carrier assigned to this shipment and determine whether the carrier is active.
        If carrier is active, update carrier with attribute note "Shipment of highest priority scheduled".
        Also, update shipment with attribute note "Shipment of highest priority".
        Finally, review the details of the updated inbound shipment to confirm note has been added.
        """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "Planned"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0006"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0010"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0016"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0019"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0027"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0029"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0030"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "LAAL", "updates": {
                "note": "Shipment of highest priority scheduled"
            }}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0029", "updates": {
                "note": "Shipment of highest priority"
            }}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0029"}),

        ],
        outputs=[
            '"note": "Shipment of highest priority"',
        ]
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_052",
        instruction="""
            You are an inventory supervisor responsible for monitoring warehouse stock conditions. Identify all warehouses that contain inventory items with at least 200 damaged goods. For each of these warehouses, generate a restocking plan and update their status to “Restocking Planned” to prioritize their replenishment. Once all updates are complete, confirm that the changes have been successfully applied by reviewing the updated warehouse records.
            """,
        actions=[
            Action(name="get_inventory_with_damage", kwargs={'threshold': 200}),
            Action(name='get_inventory_by_id', kwargs={"inventory_id": "INV-0010"}),
            Action(name='get_inventory_by_id', kwargs={"inventory_id": "INV-0020"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-12", "updates": {"status": "Restocking Planned"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-15", "updates": {"status": "Restocking Planned"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
        ],
        outputs=['"status": "Restocking Planned"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_053",
        instruction="""
            You are a product compliance specialist responsible for ensuring proper handling of hazardous products. Begin by identifying all products classified as hazardous and verify that their storage conditions are correctly specified. For any product with missing or incorrect storage requirements, update the record accordingly. If the storage requirements do not include information about the Hazmat class, add the note “Hazmat Class mentioned” to ensure compliance. After making the necessary updates, review the details of the updated products to confirm the changes have been applied correctly.
            """,
        actions=[
            Action(name="get_hazmat_products", kwargs={}),
            Action(name="get_products_by_storage_requirement", kwargs={"keyword": "hazmat",
                                                                       "list_of_ids": [
                                                                           "PHRM-VACC-D4",
                                                                           "CHEM-SOLV-K11",
                                                                           "TECH-BATT-Q17",
                                                                           "ELEC-SMART-W23"
                                                                       ]}),
            Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
            Action(name="get_product_by_sku", kwargs={"sku": "ELEC-SMART-W23"}),
            Action(name="update_product", kwargs={"sku": "PHRM-VACC-D4", "updates": {"storage_requirements": "Hazmat Class mentioned"}}),
            Action(name="update_product", kwargs={"sku": "ELEC-SMART-W23", "updates": {"storage_requirements": "Hazmat Class mentioned"}}),
            Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
            Action(name="get_product_by_sku", kwargs={"sku": "ELEC-SMART-W23"}),
        ],
        outputs=['"storage_requirements": "Hazmat Class mentioned"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_054",
        instruction="""
            You are a shipment performance analyst responsible for monitoring delays in inbound shipments. Identify all delayed inbound shipments. Review the carriers assigned to these shipments. Check if carrier is currently active. If the carrier is active, no replacement is needed. If the carrier is inactive, identify the top-rated carrier. Review carriers one by one and find the top rated active carrier that operates using the same transportation mode and replace the current carrier of the shipment with this one. Finally, retrieve and review the details of the updated inbound shipment or the shipment with the earliest departure date to confirm the changes have been applied correctly.
            """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "Delayed"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0022"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HJSC"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_top_rated_carriers", kwargs={}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0004",
                                                           "updates": {"carrier_scac": "NPEX", "carrier_name": "Nippon Express"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
        ],
        outputs=['"carrier_scac": "NPEX"', '"carrier_name": "Nippon Express"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_055",
        instruction="""
            You are a warehouse quality inspector responsible for identifying critical inventory issues. Locate all warehouses that contain either expired inventory, using today's date as May 11, 2025, or inventory with at least 200 damaged goods. For each warehouse meeting either of these conditions, update its status to “IMMEDIATE ATTENTION NEEDED” to flag it for urgent review. After completing the updates, verify the changes by reviewing the details of the updated warehouses.
            """,
        actions=[
            Action(name="get_expired_inventory", kwargs={'today': "2025-05-11"}),
            Action(name="get_inventory_with_damage", kwargs={'threshold': 200}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-12", "updates": {"status": "IMMEDIATE ATTENTION NEEDED"}}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-15", "updates": {"status": "IMMEDIATE ATTENTION NEEDED"}}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-10", "updates": {"status": "IMMEDIATE ATTENTION NEEDED"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"})
        ],
        outputs=['"status": "IMMEDIATE ATTENTION NEEDED"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_056",
        instruction="""
            You are a carrier evaluation officer responsible for assessing risk and insurance coverage across transportation partners. Begin by retrieving the list of all active carriers in the system. Calculate the maximum insurance coverage limit among these carriers. Then, review each active carrier’s insurance details to identify those whose insurance coverage limit matches the maximum value. If multiple carriers share this highest limit, include all of them. For each of these top carriers, update their record by adding an attribute note: "Highest Insurance Coverage". This will support informed decision-making regarding risk exposure and help ensure that sensitive or high-value shipments are assigned to appropriately covered carriers. Finally, return the carrier(s) with the highest insurance coverage.
            """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "insurance_details",
                "value2": "coverage_limit_usd",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG",  "CNRU", "COSU", "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE", "DHLG"]
            }),
            ]+[
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": scac}) for scac in ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG",  "CNRU", "COSU",
                                                                                           "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU",
                                                                                           "LOT", "SAS", "LAAL", "ICE", "DHLG"]
        ] + [
            Action(name="update_carrier", kwargs={"carrier_scac": "UPSN", "updates": {"notes": "Highest Insurance Coverage"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"})
        ],
        outputs=["UPSN"]
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_057",
        instruction="""
            You are an inventory coordinator responsible for analyzing product storage and pricing.
            Begin by identifying all products that have storage requirements labeled as "Dry."
            From this group, filter the products that have an active lifecycle status.
            For the active products, determine the minimum unit price to support inventory valuation and pricing strategy decisions.
            Review each of these products to check if they have minimum unit price.
            For products with the minimum price, update with attribute notes "Cheapest Product".
            """,
        actions=[
            Action(name="get_products_by_storage_requirement", kwargs={"keyword": "Dry"})
        ]+[
            Action(name="calculate_aggregate", kwargs={
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
            Action(name="get_product_by_sku", kwargs={"sku": sku}) for sku in [
                "ELEC-CHIP-A1", "AUTO-PAD-B2", "FOOD-COFF-C3", "MANU-PAPR-F6",
                "HEVY-DRIL-I9", "FURN-CHAIR-M13", "TECH-ROBO-N14", "APRL-TSHT-O15", "MATR-COTT-R18",
                "MATR-CORK-T20", "FOOD-OLIV-V22"]
        ] + [
            Action(name="update_product", kwargs={"sku": "MATR-CORK-T20", "updates": {"notes": "Cheapest Product"}}),
            Action(name="get_product_by_sku", kwargs={"sku": "MATR-CORK-T20"})
        ],
        outputs=['MATR-CORK-T20']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_058",
        instruction="""
            You are a supplier compliance officer responsible for monitoring the performance and certification status of preferred suppliers.
            Begin by reviewing all preferred suppliers and identify those that hold at least one certification.
            From this filtered list, determine which supplier has the highest on-time delivery percentage to support reliable sourcing and compliance efforts.
            Update supplier with attribute notes "Best on time delivery percentage" and review updated details of the supplier.
            """,
        actions=[
            Action(name="get_preferred_suppliers", kwargs={}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1002"}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1005"}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1010"}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1013"}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1016"}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1019"}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1029"}),
            Action(name="calculate_aggregate", kwargs={
                            "agg": "max",
                            "json": "supplier_master",
                            "key": "supplier_id",
                            "value": "on_time_delivery_percentage",
                            "list_of_ids": ["SUP-1002", "SUP-1005", "SUP-1010", "SUP-1013", "SUP-1016", "SUP-1019", "SUP-1029"]
                        }),
            Action(name="update_supplier", kwargs={"supplier_id": "SUP-1016", "updates": {"notes": "Best on time delivery percentage"}}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "SUP-1016"}),],
        outputs=['"SUP-1016"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_059",
        instruction="""
            You are a warehouse operations lead responsible for monitoring inventory conditions and space utilization.
            Begin by identifying all warehouses that contain damaged inventory.
            For each of these warehouses, review their current utilization percentage.
            From this group, determine which warehouse has damaged inventory and the highest utilization percentage to assess operational efficiency under constrained conditions.
            Update warehouse with attribute notes "Best Current Utilization Percentage, Damaged Inventory".
            Review the details of this warehouse.
            """,
        actions=[
            Action(name="get_inventory_with_damage", kwargs={}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0001"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0002"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0003"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0005"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0006"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0007"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0013"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0017"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0018"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0021"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0022"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0023"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0025"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "warehouses",
                "key": "warehouse_id",
                "value": "current_utilization_percentage",
                "list_of_ids": ["WH-01", "WH-02", "WH-03", "WH-04", "WH-05", "WH-07", "WH-08", "WH-09", "WH-10", "WH-12", "WH-14", "WH-15"]
            }),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-10", "updates": {"notes": "Best Current Utilization Percentage, Damaged Inventory"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
        ],
        outputs=['WH-10']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_060",
        instruction="""
            You are a price analyst checking the prices as well as safety standards of grocery products in market.
            Begin by reviewing all products categorized as "Groceries."
            For each product, check whether its lifecycle status is active and whether it is classified as hazardous.
            From the subset of grocery products that are non-hazardous and have an active lifecycle, identify the product with the minimum price to support pricing and safety analysis.
            Update the product details with attribute notes "Cheapest Grocery" and review the product details.
            """,
        actions=[
            Action(name="get_products_by_category", kwargs={"category": "Groceries"}),
            Action(name="get_product_by_sku", kwargs={"sku": "FOOD-COFF-C3"}),
            Action(name="get_product_by_sku", kwargs={"sku": "FOOD-FISH-H8"}),
            Action(name="get_product_by_sku", kwargs={"sku": "FOOD-OLIV-V22"}),
            Action(name="get_hazmat_products", kwargs={"list_of_ids": ["FOOD-COFF-C3", "FOOD-FISH-H8", "FOOD-OLIV-V22"]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "min",
                "json": "product_master",
                "key": "sku",
                "value": "unit_price",
                "list_of_ids": ["FOOD-COFF-C3", "FOOD-FISH-H8", "FOOD-OLIV-V22"]
            }),
            Action(name="update_product", kwargs={"sku": "FOOD-COFF-C3", "updates": {"notes": "Cheapest Grocery"}}),
            Action(name="get_product_by_sku", kwargs={"sku": "FOOD-COFF-C3"}),
        ],
        outputs=['FOOD-COFF-C3']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_061",
        instruction="""
            You are a shipment scheduler responsible for ensuring timely and reliable outbound deliveries. Begin by identifying all outbound orders that are currently pending shipment. For each order, check whether the assigned carrier is active. If the carrier is inactive or missing, retrieve a list of other active carriers that operate using the same mode of transport. Among these, identify the carrier with the highest average rating. Replace the inactive or missing carrier in the pending order with this top-rated active carrier. Finally, review the details of the updated pending order to confirm the changes have been successfully applied.
            """,
        actions=[
            Action(name="get_orders_by_status", kwargs={"status": "Pending"}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0010"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "BLUJ"}),
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SUDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "average_rating",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "FDEG", "CNRU", "KNLU", "UPSN"]
            }),
            Action(name="update_outbound_order", kwargs={"order_id": "ORD-0010", "updates": {
                "carrier_scac": "UPSN",
                "carrier_name": "UPS"
            }}),
            Action(name="get_outbound_order_by_id", kwargs={"order_id": "ORD-0010"}),
        ],
        outputs=[
            '"carrier_name": "UPS"',
            '"carrier_scac": "UPSN"'
        ]
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_062",
        instruction="""
            You are a carrier performance analyst responsible for evaluating carrier efficiency and coverage.
            Begin by reviewing all carriers that have global regional coverage and an active status.
            From this group, identify those that operate using Air mode of transport.
            Calculate the maximum and minimum on-time delivery percentage across these active global air carriers to assess overall performance in this segment.
            Check if carriers with minimum and maximum values are associated with inbound shipments with Air mode of transport.
            If associated shipments don't have Air mode of transport, add carriers with attribute note "No Air Mode".
            Return the list of scacs of updated carriers.
            """,
        actions=[
            Action(name="get_carriers_by_region", kwargs={"region": "Global"}),
            Action(name="get_active_carriers", kwargs={"list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "DHLG"
            ]}),
            Action(name="get_carriers_by_mode", kwargs={"mode": "Air", "list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "DHLG"
            ]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "both",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["NPEX", "DBSG", "UAE", "FDEG", "KNLU", "UPSN", "THY", "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "DBSG"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "UPSN"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "mode_of_transport", "value": "Air"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "DBSG", "updates": {"note": "No Air Mode"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "UPSN", "updates": {"note": "No Air Mode"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["DBSG", "UPSN"]})
        ],
        outputs=['[\n  "DBSG",\n  "UPSN"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_063",
        instruction="""
            You are a carrier performance analyst responsible for evaluating carrier efficiency and coverage.
            Begin by reviewing all carriers that have global regional coverage and an active status.
            From this group, identify those that operate using Sea mode of transport.
            Calculate the maximum and minimum on-time delivery percentage across these active global sea carriers to assess overall performance in this segment.
            Check if carriers with minimum and maximum values are associated with inbound shipments with Sea mode of transport.
            If they are associated, update carriers with maximum values by attribute rank "Best Carrier with Inbound Shipment"
            And, update carriers with minimum values by attribute rank "Worst Carrier with Inbound Shipment".
            Return the list of scacs of updated carriers.
            """,
        actions=[
            Action(name="get_carriers_by_region", kwargs={"region": "Global"}),
            Action(name="get_active_carriers", kwargs={"list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "DHLG"
            ]}),
            Action(name="get_carriers_by_mode", kwargs={"mode": "Sea", "list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "DHLG"
            ]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "both",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "COSU", "MSCU", "KNLU", "HLCU", "EGLV", "SUDU"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "COSU"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "KNLU"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "mode_of_transport", "value": "Sea"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "COSU", "updates": {"rank": "Worst Carrier with Inbound Shipment"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "KNLU", "updates": {"rank": "Best Carrier with Inbound Shipment"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["COSU", "KNLU"]})
        ],
        outputs=['[\n  "COSU",\n  "KNLU"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_064",
        instruction="""
            You are a carrier performance analyst responsible for evaluating carrier efficiency and coverage.
            Begin by reviewing all carriers that have global regional coverage and an active status.
            From this group, identify those that operate using Truck mode of transport.
            Calculate the maximum and minimum  on-time delivery percentage across these active global truck carriers to assess overall performance in this segment.
            Check if carriers with minimum and maximum values are associated with inbound shipments with Truck mode of transport.
            If associated shipments don't have Truck mode of transport, add attribute note "No Truck Mode".
            Return the list of scacs of updated carriers.
            """,
        actions=[
            Action(name="get_carriers_by_region", kwargs={"region": "Global"}),
            Action(name="get_active_carriers", kwargs={"list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "DHLG"
            ]}),
            Action(name="get_carriers_by_mode", kwargs={"mode": "Truck", "list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "DHLG"
            ]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "both",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "CMDU", "FDEG", "KNLU", "UPSN", "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "CMDU"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "UPSN"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "mode_of_transport", "value": "Truck"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "CMDU", "updates": {"note": "No Truck Mode"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["CMDU"]})
        ],
        outputs=['[\n  "CMDU"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_065",
        instruction="""
            You are a carrier performance analyst responsible for evaluating carrier efficiency and coverage.
            Begin by reviewing all carriers that have global regional coverage and an active status.
            From this group, identify those that operate using Rail mode of transport.
            Calculate the maximum and minimum on-time delivery percentage across these active global rail carriers to assess overall performance in this segment.
            Check if carriers with minimum and maximum values are associated with inbound shipments with Rail mode of transport.
            If associated shipments don't have Rail mode of transport, add carriers with attribute note "No Rail Mode".
            Return the list of scacs of updated carriers.
            """,
        actions=[
            Action(name="get_carriers_by_region", kwargs={"region": "Global"}),
            Action(name="get_active_carriers", kwargs={"list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "DHLG"
            ]}),
            Action(name="get_carriers_by_mode", kwargs={"mode": "Rail", "list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "DHLG"
            ]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "both",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["MAEU", "NPEX", "DBSG", "MSCU", "KNLU"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "MSCU"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "KNLU"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "mode_of_transport", "value": "Rail"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "MSCU", "updates": {"note": "No Rail Mode"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "KNLU", "updates": {"note": "No Rail Mode"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["MSCU", "KNLU"]})
        ],
        outputs=['[\n  "MSCU",\n  "KNLU"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_066",
        instruction="""
            You are a carrier performance analyst responsible for evaluating carrier efficiency and coverage.
            Begin by reviewing all carriers that have global regional coverage and an active status.
            From this group, identify those that operate using Parcel mode of transport.
            Calculate the maximum and minimum on-time delivery percentage across these active global parcel carriers to assess overall performance in this segment.
            Check if carriers with minimum and maximum values are associated with inbound shipments with Parcel mode of transport.
            If they are associated, update carriers with maximum values by attribute note "Best Carrier with Inbound Shipment"
            And, update carriers with minimum values by attribute note "Worst Carrier with Inbound Shipment".
            If associated shipments don't have Parcel mode of transport, add attribute note "No Parcel Mode".
            Return the list of scacs of updated carriers.
            """,
        actions=[
            Action(name="get_carriers_by_region", kwargs={"region": "Global"}),
            Action(name="get_active_carriers", kwargs={"list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "DHLG"
            ]}),
            Action(name="get_carriers_by_mode", kwargs={"mode": "Parcel", "list_of_scacs": [
                "MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "COSU", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV", "THY", "SUDU", "DHLG"
            ]}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "both",
                "json": "carriers",
                "key": "scac",
                "value": "performance_metrics",
                "value2": "on_time_delivery_percentage",
                "list_of_ids": ["FDEG", "UPSN", "DHLG"]
            }),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "UPSN"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "mode_of_transport", "value": "Parcel"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "FDEG", "updates": {"note": "Worst Carrier with Inbound Shipment"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "UPSN", "updates": {"note": "Best Carrier with Inbound Shipment"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["FDEG", "UPSN"]})
        ],
        outputs=['[\n  "FDEG",\n  "UPSN"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_067",
        instruction="""
            You are a warehouse audit coordinator responsible for assessing warehouse assets.
            Focus your review exclusively on warehouses that are owned.
            Calculate the average current utilization percentage across all owned warehouses to evaluate overall space efficiency.
            Review each warehouse detail and if it is less than average current utilization percentage, update it with attribute note "Review Expected".
            Return the ids of warehouses updated.
            """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Owned"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "avg",
                "json": "warehouses",
                "key": "warehouse_id",
                "value": "current_utilization_percentage",
                "list_of_ids": ["WH-01", "WH-03", "WH-05", "WH-07", "WH-08", "WH-10", "WH-11", "WH-13", "WH-14", "WH-16"]
            }),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-01"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-03"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-03", "updates": {"note": "Review Expected"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-07", "updates": {"note": "Review Expected"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-08"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-08", "updates": {"note": "Review Expected"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-08"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-11"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-11", "updates": {"note": "Review Expected"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-13"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-13", "updates": {"note": "Review Expected"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-13"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-14"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-16"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["WH-03", "WH-07", "WH-08", "WH-11", "WH-13"]})
        ],
        outputs=['[\n  "WH-03",\n  "WH-07",\n  "WH-08",\n  "WH-11",\n  "WH-13"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_068",
        instruction="""
            You are a warehouse audit coordinator responsible for assessing warehouse assets.
            Focus your review exclusively on warehouses that are leased.
            Calculate the average current utilization percentage across all leased warehouses to evaluate overall space efficiency.
            Review each warehouse detail and if it is less than average current utilization percentage, update it with attribute note "Review Expected".
            Return the ids of warehouses updated.
            """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Leased"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "avg",
                "json": "warehouses",
                "key": "warehouse_id",
                "value": "current_utilization_percentage",
                "list_of_ids": ["WH-02", "WH-04", "WH-06", "WH-09", "WH-12", "WH-15"]
            }),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-02"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-06"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-06", "updates": {"note": "Review Expected"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-09"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-12", "updates": {"note": "Review Expected"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-15", "updates": {"note": "Review Expected"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["WH-06", "WH-12", "WH-15"]})
        ],
    outputs=['[\n  "WH-06",\n  "WH-12",\n  "WH-15"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_069",
        instruction="""
            You are a warehouse audit coordinator responsible for assessing warehouse assets.
            Focus your review exclusively on warehouses that are owned.
            Calculate the average current utilization percentages among these owned warehouses to evaluate their range of space usage.
            Review each warehouse detail and if it is more than average current utilization percentage, update it with attribute note "Top Used".
            Return the ids of warehouses updated.
            """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Owned"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "avg",
                "json": "warehouses",
                "key": "warehouse_id",
                "value": "current_utilization_percentage",
                "list_of_ids": ["WH-01", "WH-03", "WH-05", "WH-07", "WH-08", "WH-10", "WH-11", "WH-13", "WH-14", "WH-16"]
            }),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-01"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-01", "updates": {"note": "Top Used"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-01"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-05", "updates": {"note": "Top Used"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-08"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-10", "updates": {"note": "Top Used"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-13"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-14"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-14", "updates": {"note": "Top Used"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-14"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-16"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-16", "updates": {"note": "Top Used"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-16"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["WH-01", "WH-05", "WH-10", "WH-14", "WH-16"]})
        ],
        outputs=['[\n  "WH-01",\n  "WH-05",\n  "WH-10",\n  "WH-14",\n  "WH-16"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_070",
        instruction="""
            You are a warehouse audit coordinator responsible for assessing warehouse assets.
            Focus your review exclusively on warehouses that are leased.
            Calculate the average current utilization percentages among these leased warehouses to understand the range of space usage.
            Review each warehouse detail and if it is more than average current utilization percentage, update it with attribute note "Top Used".
            Return the ids of warehouses updated.
            """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Leased"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "avg",
                "json": "warehouses",
                "key": "warehouse_id",
                "value": "current_utilization_percentage",
                "list_of_ids": ["WH-02", "WH-04", "WH-06", "WH-09", "WH-12", "WH-15"]
            }),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-02"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-02", "updates": {"note": "Top Used"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-02"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-04", "updates": {"note": "Top Used"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-09"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-09", "updates": {"note": "Top Used"}}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-09"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["WH-02", "WH-04", "WH-09"]})
        ],
        outputs=['[\n  "WH-02",\n  "WH-04",\n  "WH-09"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_071",
        instruction="""
            You are a market analyst focused on inbound shipments.
            Review all inbound shipments with the status “In Transit” and calculate the sum of their total values.
            Check for the shipment with highest total value and flag it with note "Most valued In Transit shipment".
            The objective is to determine the total value of goods currently in transit.
            """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "In Transit"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0001"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0003"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0005"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0008"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0012"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0013"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0014"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0015"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0018"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0020"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0023"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0024"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0025"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0026"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0028"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008", "SHIP-0009", "SHIP-0011",
                                "SHIP-0012", "SHIP-0013", "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025", "SHIP-0026", "SHIP-0028"]
            }),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0011", "updates": {
                "note": "Most valued In Transit shipment"
            }}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="calculate_total", kwargs={
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
            Review all inbound shipments with the status “Planned” and calculate the sum of their total values.
            Check for the shipment with highest total value and flag it with note "Most valued Planned shipment".
            The objective is to determine the total value of goods currently planned for arrival.
            """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "Planned"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0006"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0010"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0016"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0019"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0027"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0029"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0030"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0006", "SHIP-0010", "SHIP-0016", "SHIP-0019", "SHIP-0027", "SHIP-0029", "SHIP-0030"]
            }),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0016", "updates": {
                "note": "Most valued Planned shipment"
            }}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0016"}),
            Action(name="calculate_total", kwargs={
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
            Review all inbound shipments with the status “Delayed” and calculate the sum of their total values.
            Check for the shipment with highest total value and flag it with note "Most valued Delayed shipment".
            The objective is to determine the total value of goods that are currently delayed.
            """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "Delayed"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0022"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0004", "SHIP-0022"]
            }),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0004", "updates": {
                "note": "Most valued Delayed shipment"
            }}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="calculate_total", kwargs={
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
            Review all inbound shipments with the status “Received” and calculate the sum of their total values.
            Check for the shipment with highest total value and flag it with note "Most valued Received shipment".
            The objective is to determine the total value of goods that have been received to date.
            """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "Received"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0007"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "max",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0002", "SHIP-0007", "SHIP-0017"]
            }),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0002", "updates": {
                "note": "Most valued Received shipment"
            }}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="calculate_total", kwargs={
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
            First determine average of the total values of these inbound.
            Review all these inbound shipments. If total values of these shipments is above average, update their priority level as "High".
            Then, find the minimum and maximum total values among these shipments.
            The objective is to perform statistical analysis (minimum, maximum and average) of total values for goods currently in transit.
            Finally, return the minimum and maximum of total values determined.
            """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "In Transit"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "avg",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008", "SHIP-0009", "SHIP-0011",
                                "SHIP-0012", "SHIP-0013", "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025", "SHIP-0026", "SHIP-0028"]
            }),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0001"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0003"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0005"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0008"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0009", "updates": {"priority_level": "High"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0009"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0011", "updates": {"priority_level": "High"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0011"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0012"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0013"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0013", "updates": {"priority_level": "High"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0013"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0014"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0015"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0018"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0020"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0021", "updates": {"priority_level": "High"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0023"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0024"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0025"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0025", "updates": {"priority_level": "High"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0025"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0026"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0028"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0028", "updates": {"priority_level": "High"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0028"}),
            Action(name="calculate_aggregate", kwargs={
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
            You are a warehouse inventory manager. Review the inventory record for INV-0010.
            The quantity_allocated has been successfully sold. Deduct the allocated quantity from quantity_on_hand.
            Set quantity_allocated to 0.
            Recalculate total_value by deducting unit_cost * quantity_allocated before.
            If quantity_on_hand < reorder_point, mark stock_status as "Reorder Needed".
            Finally, check the associated warehouse and its current utilization percentage.
            If current utilization percentage < 80, update warehouse with attribute note as "Less Used".
            If current utilization percentage >= 80, update warehouse with attribute note as "More Used".
            Return the updated inventory record with: inventory_id, sku, quantity_on_hand, quantity_allocated, stock_status, and total_value.
            """,
        actions=[
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0010", "updates": {
                "quantity_on_hand": 15000
            }}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0010", "updates": {
                "quantity_allocated": 0
            }}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0010", "updates": {
                "total_value": 52500
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-12", "updates": {
                "note": "Less Used"
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
        ],
        outputs=['"inventory_id": "INV-0010"', '"sku": "BLDG-TILE-J10"', '"quantity_on_hand": 15000', '"quantity_allocated": 0', '"total_value": 52500', '"stock_status": "In Stock"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_077",
        instruction="""
            You are overseeing luxury inventory. The INV-0005 have sold all allocated units.
            Subtract these units from quantity_on_hand. Set quantity_allocated to 0.
            Recalculate total_value by deducting unit_cost * quantity_allocated before.
            If the quantity_on_hand falls below the reorder_point, set stock_status to "Reorder Needed".
            If current utilization percentage < 80, update warehouse with attribute note as "Less Used".
            If current utilization percentage >= 80, update warehouse with attribute note as "More Used".
            Return the updated inventory with new quantity_on_hand, quantity_allocated, total_value and stock_status).
            """,
        actions=[
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0005"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0005", "updates": {
                "quantity_on_hand": 120
            }}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0005"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0005", "updates": {
                "quantity_allocated": 0
            }}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0005"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0005", "updates": {
                "total_value": 102000
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-07", "updates": {
                "note": "Less Used"
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0005"}),
        ],
        outputs=['"inventory_id": "INV-0005"', '"quantity_on_hand": 120', '"quantity_allocated": 0', '"total_value": 102000', '"stock_status": "In Stock"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_078",
        instruction="""
            The allocated bottles of INV-0016 have been sold.
            Reduce quantity_on_hand by quantity allocated before selling.
            Set quantity_allocated to 0.
            Recalculate total_value by deducting unit_cost * quantity_allocated before.
            If new quantity_on_hand < reorder_point, add "Reorder Suggested" to stock_status.
            If current utilization percentage < 80, update warehouse with attribute note as "Less Used".
            If current utilization percentage >= 80, update warehouse with attribute note as "More Used".
            Return updated inventory_id, sku, quantity_on_hand, quantity_allocated, stock_status, storage_requirements, and total_value.
            """,
        actions=[
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0016", "updates": {
                "quantity_on_hand": 4500
            }}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0016", "updates": {
                "quantity_allocated": 0
            }}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0016", "updates": {
                "total_value": 81000
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-15", "updates": {
                "note": "More Used"
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
        ],
        outputs=['"inventory_id": "INV-0016"', '"sku": "BEVG-WINE-P16"', '"quantity_on_hand": 4500', '"quantity_allocated": 0', '"stock_status": "In Stock"', '"storage_requirements": "Temp Control 12-14\u00b0C, Dark"', '"total_value": 81000']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_079",
        instruction="""
            Allocated inventory of INV-0004 has been administered.
            Deduct quantity allocated before from quantity_on_hand.
            Set quantity_allocated to 0.
            Recalculate total_value by deducting unit_cost * quantity_allocated before.
            If quantity_on_hand < reorder_point, add tag: "Critical Reorder".
            If current utilization percentage < 80, update warehouse with attribute note as "Less Used".
            If current utilization percentage >= 80, update warehouse with attribute note as "More Used".
            Return updated values for inventory_id, quantity_on_hand, quantity_allocated, total_value, and stock_status.
            """,
        actions=[
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0004", "updates": {
                "quantity_on_hand": 18000
            }}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0004", "updates": {
                "quantity_allocated": 0
            }}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0004", "updates": {
                "total_value": 279000
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-06"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-06", "updates": {
                "note": "More Used"
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
        ],
        outputs=['"inventory_id": "INV-0004"', '"quantity_on_hand": 18000', '"quantity_allocated": 0', '"total_value": 279000', '"stock_status": "In Stock"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_080",
        instruction="""
            Allocated stock of INV-0015 has sold out.
            Decrease quantity_on_hand by sold allocated stock.
            Set quantity_allocated to 0.
            Recalculate total_value by deducting unit_cost * quantity_allocated before.
            If new quantity_on_hand < reorder_point, set stock_status = "Reorder Needed".
            If current utilization percentage < 80, update warehouse with attribute note as "Less Used".
            If current utilization percentage >= 80, update warehouse with attribute note as "More Used".
            Return changes including: inventory_id, sku, quantity_on_hand, quantity_allocated, total_value and stock_status.
            """,
        actions=[
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0015", "updates": {
                "quantity_on_hand": 22000
            }}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0015", "updates": {
                "quantity_allocated": 0
            }}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0015", "updates": {
                "total_value": 176000
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-04", "updates": {
                "note": "More Used"
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
        ],
        outputs=['"inventory_id": "INV-0015"', '"sku": "APRL-TSHT-O15"', '"quantity_on_hand": 22000', '"quantity_allocated": 0', '"total_value": 176000', '"stock_status": "In Stock"']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_081",
        instruction="""
            You are a market analyst focused on inbound shipments.
            Calculate the average total value of these shipments.
            The first objective is to determine the average value of goods currently delayed.
            Next, you have to review shipments and associated carriers and check if any of those shipments have inactive carrier or not.
            For each inactive shipment,  check if total value of shipment is greater than average total value.
            If it is greater, update shipment with attribute notes "Carrier Replacement Required".
            Finally, return the ids of shipments updated.
            """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "Delayed"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "avg",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0004", "SHIP-0022"]
            }),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HJSC"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0022"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0004",
                                                           "updates": {"notes": "Carrier Replacement Required"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0004"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["SHIP-0004"]})
        ],
        outputs=['[\n  "SHIP-0004"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_082",
        instruction="""
            You are a market analyst focused on inbound shipments.
            Calculate the average total value of these shipments.
            The first objective is to determine the average value of goods currently received.
            Next, you have to review shipments and associated carriers. You have to only consider shipments with active carriers.
            If total value of shipment with active carrier is less than average total value, update shipment with attribute notes "Lower than Average".
            If total value of shipment with active carrier is more than average total value, update shipment with attribute notes "Higher than Average".
            Finally, return the ids of shipments updated with notes "Higher than Average".
            """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "Received"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "avg",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0002", "SHIP-0007", "SHIP-0017"]
            }),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0007"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0002",
                                                           "updates": {"notes": "Higher than Average"}}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0007",
                                                           "updates": {"notes": "Lower than Average"}}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0017",
                                                           "updates": {"notes": "Higher than Average"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0007"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["SHIP-0002", "SHIP-0017"]})
        ],
        outputs=['[\n  "SHIP-0002",\n  "SHIP-0017"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_083",
        instruction="""
            You are a logistics manager tasked with monitoring carrier performance.
            Identify all active carriers serving the "Global" region whose on-time delivery percentage is below 95%.
            For each carrier meeting this criterion, update their status to "Under Review."
            Return the list of carriers that were updated. If no carriers fall below the 95% threshold, no updates are needed and you should return an empty list.
            """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_carriers_by_region", kwargs={"region": "Global",
                                                       "list_of_scacs": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE", "FDEG", "CNRU",
                                                                       "COSU", "QFA", "MSCU", "KNLU", "HLCU", "UPSN", "EGLV",
                                                                       "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE", "DHLG"
                                                       ]}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SUDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "MAEU", "updates": {"status": "Under Review"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "CMDU", "updates": {"status": "Under Review"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "COSU", "updates": {"status": "Under Review"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "MSCU", "updates": {"status": "Under Review"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "HLCU", "updates": {"status": "Under Review"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "EGLV", "updates": {"status": "Under Review"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["MAEU", "CMDU", "COSU", "MSCU", "HLCU", "EGLV"]})
            ],
        outputs=['[\n  "MAEU",\n  "CMDU",\n  "COSU",\n  "MSCU",\n  "HLCU",\n  "EGLV"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_084",
        instruction="""
            You are a logistics manager tasked with monitoring carrier performance. Identify all active carriers serving the "Global" region whose on-time delivery percentage is below 95%. For each carrier meeting this criterion, update their status to "Under Review." Return the list of carriers that were updated. If no carriers fall below the 95% threshold, no updates are needed and you should return an empty list.
            """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_carriers_by_region", kwargs={"region": "Global",
                                                          "list_of_scacs": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE",
                                                                            "FDEG", "CNRU",
                                                                            "COSU", "QFA", "MSCU", "KNLU", "HLCU",
                                                                            "UPSN", "EGLV",
                                                                            "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE",
                                                                            "DHLG"
                                                                            ]}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DBSG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UAE"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "KNLU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "UPSN"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SUDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "DHLG"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "MAEU", "updates": {"status": "Under Review"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "CMDU", "updates": {"status": "Under Review"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "COSU", "updates": {"status": "Under Review"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "MSCU", "updates": {"status": "Under Review"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "HLCU", "updates": {"status": "Under Review"}}),
            Action(name="update_carrier", kwargs={"carrier_scac": "EGLV", "updates": {"status": "Under Review"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MAEU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CMDU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "COSU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "MSCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "HLCU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "EGLV"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["MAEU", "CMDU", "COSU", "MSCU", "HLCU", "EGLV"]})
        ],
        outputs=['[\n  "MAEU",\n  "CMDU",\n  "COSU",\n  "MSCU",\n  "HLCU",\n  "EGLV"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_085",
        instruction="""
            You are a logistics manager responsible for carrier performance oversight. Identify all active carriers serving the "North America" region whose on-time delivery percentage is below 95%. Update the status of each identified carrier to "Under Review." Return the list of carriers that were updated. If no carriers meet this criterion, no updates are necessary, and you should return an empty list.
            """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_carriers_by_region", kwargs={"region": "North America",
                                                          "list_of_scacs": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE",
                                                                            "FDEG", "CNRU",
                                                                            "COSU", "QFA", "MSCU", "KNLU", "HLCU",
                                                                            "UPSN", "EGLV",
                                                                            "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE",
                                                                            "DHLG"
                                                                            ]}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "CNRU", "updates": {"status": "Under Review"}}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["CNRU"]})
        ],
        outputs=['[\n  "CNRU"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_086",
        instruction="""
            You are a logistics manager responsible for carrier performance oversight of carriers not serving completely globally but only in specific regions.
            Start by checking active carriers. Then checking which among these active carriers cover Global.
            Confirm regional coverage and check the on-time delivery percentage of non-Global active carriers by details.
            Update the status of each identified non-Global active carrier to "Under Review." Return the list of carriers that were updated.
            If no carriers meet this criterion, no updates are necessary, and you should return an empty list.
            """,
        actions=[
            Action(name="get_active_carriers", kwargs={}),
            Action(name="get_carriers_by_region", kwargs={"region": "Global",
                                                          "list_of_scacs": ["MAEU", "NPEX", "DBSG", "CMDU", "UAE",
                                                                            "FDEG", "CNRU",
                                                                            "COSU", "QFA", "MSCU", "KNLU", "HLCU",
                                                                            "UPSN", "EGLV",
                                                                            "THY", "SUDU", "LOT", "SAS", "LAAL", "ICE",
                                                                            "DHLG"
                                                                            ]}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="update_carrier", kwargs={"carrier_scac": "CNRU",
                                                  "updates": {
                                                      "status": "Under Review"
                                                  }}),
            Action(name="update_carrier", kwargs={"carrier_scac": "QFA",
                                                  "updates": {
                                                      "status": "Under Review"
                                                  }}),
            Action(name="update_carrier", kwargs={"carrier_scac": "LOT",
                                                  "updates": {
                                                      "status": "Under Review"
                                                  }}),
            Action(name="update_carrier", kwargs={"carrier_scac": "SAS",
                                                  "updates": {
                                                      "status": "Under Review"
                                                  }}),
            Action(name="update_carrier", kwargs={"carrier_scac": "ICE",
                                                  "updates": {
                                                      "status": "Under Review"
                                                  }}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["CNRU", "QFA", "LOT", "SAS", "ICE"]})
        ],
        outputs=['["CNRU", "QFA", "LOT", "SAS", "ICE"]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_087",
        instruction="""
            You are an inventory controller responsible for monitoring stock quality and availability. As of December 12, 2024, identify all inventory items that are either expired or have damaged quantities of 200 or more. Additionally, find all inventory items that are below their reorder point. Combine all these items—expired, damaged, or below reorder point, and update their status to “Under Review.” Finally, return the list of IDs for all inventory items that were updated.
            """,
        actions=[
            Action(name="get_expired_inventory", kwargs={"today": "2024-12-12"}),
            Action(name="get_inventory_with_damage", kwargs={"threshold": 200}),
            Action(name="get_inventory_below_reorder_point", kwargs={}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0010", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0020", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0024", "updates": {"status": "Under Review"}}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["INV-0010", "INV-0020", "INV-0024"]})
        ],
        outputs=['[\n  "INV-0010",\n  "INV-0020",\n  "INV-0024"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_088",
        instruction="""
            You are an inventory controller responsible for monitoring stock quality and availability. As of June 12, 2024, identify all inventory items that are either expired or have damaged quantities of 150 or more. Additionally, find all inventory items that are below their reorder point. Combine all these items—expired, damaged, or below reorder point—and update their status to “Under Review.” Finally, return the list of IDs for all inventory items that were updated.
            """,
        actions=[
            Action(name="get_expired_inventory", kwargs={"today": "2024-06-12"}),
            Action(name="get_inventory_with_damage", kwargs={"threshold": 150}),
            Action(name="get_inventory_below_reorder_point", kwargs={}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0010", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0020", "updates": {"status": "Under Review"}}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["INV-0010", "INV-0020"]})
        ],
        outputs=['[\n  "INV-0010",\n  "INV-0020"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_089",
        instruction="""
            You are an inventory controller responsible for monitoring stock quality and availability. As of May 12, 2025, identify all inventory items that are either expired or have damaged quantities of 100 or more. Additionally, find all inventory items that are below their reorder point. Combine all these items—expired, damaged, or below reorder point—and update their status to “Under Review.” Finally, return the list of IDs for all inventory items that were updated.
            """,
        actions=[
            Action(name="get_expired_inventory", kwargs={"today": "2025-05-12"}),
            Action(name="get_inventory_with_damage", kwargs={"threshold": 100}),
            Action(name="get_inventory_below_reorder_point", kwargs={}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0010", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0015", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0020", "updates": {"status": "Under Review"}}),
            Action(name="update_inventory", kwargs={"inventory_id": "INV-0024", "updates": {"status": "Under Review"}}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0010"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0015"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0020"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0024"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["INV-0010", "INV-0015", "INV-0020", "INV-0024"]})
        ],
        outputs=['[\n  "INV-0010",\n  "INV-0015",\n  "INV-0020",\n  "INV-0024"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_090",
        instruction="""
            You are a compliance officer responsible for reviewing warehouse and product safety protocols.
            Begin by retrieving all company-owned warehouses.
            Next, identify all products that require special storage conditions, specifically those classified as “Hazmat.”
            Verify whether the owned warehouses are equipped to handle hazmat storage.
            Then, cross-reference inventory information to confirm whether these products are assigned to warehouses that are both owned and fit for hazmat storage.
            If a product’s inventory is stored in a matching owned warehouse with proper hazmat facilities, it is considered compliant.
            Update products without specific owned warehouse suitable for hazmat storage by adding attribute notes "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE".
            Finally, return the list of product IDs that are assigned to specific owned warehouses suitable for hazmat storage.
        """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Owned"}),
            Action(name="get_hazmat_products", kwargs={}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-01"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-08"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-13"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-14"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "PHRM-VACC-D4"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "TECH-BATT-Q17"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "ELEC-SMART-W23"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0011"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0017"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0023"}),
            Action(name="update_product", kwargs={"sku": "PHRM-VACC-D4", "updates": {"notes": "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE"}}),
            Action(name="update_product", kwargs={"sku": "TECH-BATT-Q17", "updates": {"notes": "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE"}}),
            Action(name="update_product", kwargs={"sku": "ELEC-SMART-W23", "updates": {"notes": "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE"}}),
            Action(name="get_product_by_sku", kwargs={"sku": "PHRM-VACC-D4"}),
            Action(name="get_product_by_sku", kwargs={"sku": "TECH-BATT-Q17"}),
            Action(name="get_product_by_sku", kwargs={"sku": "ELEC-SMART-W23"}),
            Action(name="return_ids", kwargs={'list_of_ids': ["CHEM-SOLV-K11"]})
        ],
        outputs=['[\n  "CHEM-SOLV-K11"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_091",
        instruction="""
            You are a compliance officer reviewing warehouse and product safety protocols.
            Your objective is to identify products that require special storage conditions such as “Hazmat” but are either not assigned to any warehouse or are assigned to owned warehouses that are not fit for hazmat storage.
            Begin by retrieving the list of all company-owned warehouses and determine which of them are equipped for hazmat storage.
            Then, identify all products with “Hazmat” storage requirements.
            For each of these products, check inventory information to see if a warehouse has been assigned.
            If a product is not linked to any warehouse, or if it is linked to an owned warehouse that is not equipped for hazmat storage, flag it.
            Update products with specific owned warehouse suitable for hazmat storage by adding attribute notes "SUITABLE CONDITION PROVIDED FOR HAZMAT STORAGE".
            Finally, return the list of product IDs that fall into either of these two categories.
            """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Owned"}),
            Action(name="get_hazmat_products", kwargs={}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-01"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-08"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-13"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-14"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "PHRM-VACC-D4"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "TECH-BATT-Q17"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "ELEC-SMART-W23"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0004"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0011"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0017"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0023"}),
            Action(name="update_product", kwargs={"sku": "CHEM-SOLV-K11", "updates": {"notes": "SUITABLE CONDITION PROVIDED FOR HAZMAT STORAGE"}}),
            Action(name="get_product_by_sku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="return_ids", kwargs={'list_of_ids': ["PHRM-VACC-D4", "TECH-BATT-Q17", "ELEC-SMART-W23"]})
        ],
        outputs=['[\n  "PHRM-VACC-D4",\n  "TECH-BATT-Q17",\n  "ELEC-SMART-W23"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_092",
        instruction="""
            You are a compliance officer responsible for reviewing warehouse and product safety protocols.
            Your objective is to determine whether leased warehouses are appropriately equipped to handle products requiring “Hazmat” storage.
            Begin by retrieving all leased warehouses, then assess each one to check if it is equipped for hazmat storage (through special capabilities attribute).
            For any warehouse that does not support hazmat storage, update the warehouse record by adding a note with the value "NOT SUITABLE FOR HAZMAT STORAGE".
            Review the updated details of these warehouses to ensure accuracy. Finally, return the list of warehouse IDs that are not suitable for hazmat storage.
            """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Leased"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-02"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-09"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-02", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-04", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-06", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-09", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-12", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="update_warehouse", kwargs={"warehouse_id": "WH-15", "updates":{
                "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
            }}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-02"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-09"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="return_ids", kwargs={'list_of_ids': ["WH-02", "WH-04", "WH-06", "WH-09", "WH-12", "WH-15"]})
        ],
        outputs=['[\n  "WH-02",\n  "WH-04",\n  "WH-06",\n  "WH-09",\n  "WH-12",\n  "WH-15"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_093",
        instruction="""
            You are a compliance officer reviewing warehouse and product safety protocols.
            Your objective is to identify products that require special storage conditions such as “Temp Control” and are stored in owned warehouses that meet this requirement.
            Begin by retrieving all company-owned warehouses and verify which of them are equipped for temperature-controlled storage.
            Next, find all products that require “Temp Control” as part of their storage conditions.
            Using inventory information, check if these products are assigned to warehouses.
            If the assigned warehouse is owned and equipped for temperature control, the product is considered compliant.
            For such compliant product, update with attribute notes "STORED IN TEMP CONTROL OWNED WAREHOUSE"
            Finally, return the list of product IDs that are stored in such compliant owned warehouses.
            """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Owned"}),
            Action(name="get_products_by_storage_requirement", kwargs={"keyword": "Temp"}),
            Action(name="get_product_by_sku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="get_product_by_sku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-01"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-08"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-13"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-14"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "BEVG-WINE-P16"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0011"}),
            Action(name="update_product", kwargs={"sku": "CHEM-SOLV-K11", "updates": {"notes": "STORED IN TEMP CONTROL OWNED WAREHOUSE"}}),
            Action(name="get_product_by_sku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="return_ids", kwargs={'list_of_ids': ["CHEM-SOLV-K11"]})
        ],
        outputs=['[\n  "CHEM-SOLV-K11"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_094",
        instruction="""
            You are a compliance officer reviewing warehouse and product safety protocols.
            Your objective is to identify products that require special storage conditions such as “Temp Control” but are not stored in suitable company-owned warehouses.
            Start by retrieving all warehouses that are company-owned and determine which of them are equipped for temperature-controlled storage.
            Then, find all products that require “Temp Control.”
            Using inventory information, check whether these products are assigned to warehouses.
            If a product is either not assigned to any warehouse or is assigned to an owned warehouse that is not equipped for temperature control, it should be flagged.
            For such product, update with attribute notes "NOT STORED IN TEMP CONTROL OWNED WAREHOUSE"
            Finally, return the list of product IDs that do not have a suitable owned warehouse available for temperature-controlled storage.
            """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Owned"}),
            Action(name="get_products_by_storage_requirement", kwargs={"keyword": "Temp"}),
            Action(name="get_product_by_sku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="get_product_by_sku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-01"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-03"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-05"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-07"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-08"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-10"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-13"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-14"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "BEVG-WINE-P16"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0011"}),
            Action(name="update_product", kwargs={"sku": "BEVG-WINE-P16", "updates": {"notes": "NOT STORED IN TEMP CONTROL OWNED WAREHOUSE"}}),
            Action(name="get_product_by_sku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="return_ids", kwargs={'list_of_ids': ["BEVG-WINE-P16"]})
        ],
        outputs=['[\n  "BEVG-WINE-P16"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_095",
        instruction="""
            You are a compliance officer reviewing warehouse and product safety protocols.
            Your objective is to identify products that require special storage conditions such as “Temp Control” and are stored in leased warehouses that meet this requirement.
            Begin by retrieving all warehouses that are leased and determine which of them are equipped for temperature-controlled storage.
            Next, identify all products that require “Temp Control.”
            Then, using inventory information, check whether these products are assigned to warehouses.
            If a product is assigned to a leased warehouse that is properly equipped for temperature control, it is considered compliant.
            For such product, update with attribute notes "STORED IN TEMP CONTROL LEASED WAREHOUSE"
            Finally, return the list of product IDs that are stored in such leased warehouses with the required storage capability.
            """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Leased"}),
            Action(name="get_products_by_storage_requirement", kwargs={"keyword": "Temp"}),
            Action(name="get_product_by_sku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="get_product_by_sku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-02"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-09"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "BEVG-WINE-P16"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0011"}),
            Action(name="update_product", kwargs={"sku": "BEVG-WINE-P16", "updates": {"notes": "STORED IN TEMP CONTROL LEASED WAREHOUSE"}}),
            Action(name="get_product_by_sku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="return_ids", kwargs={'list_of_ids': ["BEVG-WINE-P16"]})
        ],
        outputs=['[\n  "BEVG-WINE-P16"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_096",
        instruction="""
            You are a compliance officer reviewing warehouse and product safety protocols.
            Your objective is to identify products requiring temperature-controlled storage ("Temp Control") that are not properly stored in leased warehouses equipped for this condition.
            Start by retrieving all leased warehouses and determine which ones are suitable for temperature-controlled storage.
            Then, gather all products that require "Temp Control". Using inventory records, check whether these products are assigned to a warehouse.
            If a product is either not assigned to any warehouse or is assigned to a leased warehouse that lacks temperature control capability, it should be flagged.
            For each such product, update its record by adding a note with the value "NOT STORED IN TEMP CONTROL LEASED WAREHOUSE".
            Finally, return the list of product IDs that do not have appropriate leased warehouse storage for temperature-controlled needs.
            """,
        actions=[
            Action(name="get_warehouses_by_ownership_status", kwargs={"ownership_status": "Leased"}),
            Action(name="get_products_by_storage_requirement", kwargs={"keyword": "Temp"}),
            Action(name="get_product_by_sku", kwargs={"sku": "BEVG-WINE-P16"}),
            Action(name="get_product_by_sku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-02"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-04"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-06"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-09"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-12"}),
            Action(name="get_warehouse_by_id", kwargs={"warehouse_id": "WH-15"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "BEVG-WINE-P16"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0016"}),
            Action(name="filter_inventory", kwargs={"key": "sku", "value": "CHEM-SOLV-K11"}),
            Action(name="get_inventory_by_id", kwargs={"inventory_id": "INV-0011"}),
            Action(name="update_product", kwargs={"sku": "CHEM-SOLV-K11", "updates": {"notes": "NOT STORED IN TEMP CONTROL LEASED WAREHOUSE"}}),
            Action(name="get_product_by_sku", kwargs={"sku": "CHEM-SOLV-K11"}),
            Action(name="return_ids", kwargs={'list_of_ids': ["CHEM-SOLV-K11"]})
        ],
        outputs=['[\n  "CHEM-SOLV-K11"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_097",
        instruction="""
            You are a logistics performance manager analyzing carrier effectiveness in the North American region.
            Begin by retrieving all active carriers whose regional coverage includes “North America.”
            Then, identify all inbound shipments that are currently “In Transit” and are assigned to these carriers.
            Update these shipments with attribute carrier_coverage "North America".
            Review the details of these shipments, and finally, calculate the total sum of the shipment values to assess the overall value of goods currently in transit under North American active carriers.
            """,
        actions=[
            Action(name="get_carriers_by_region", kwargs={"region": "North America"}),
            Action(name="get_active_carriers", kwargs={"list_of_scacs": ["CNRU", "LOT", "SAS", "LAAL", "ICE"]}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "CNRU"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "status", "value": "In Transit"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "CNRU", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "LOT", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "SAS", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "LAAL", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "ICE", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0008", "updates": {
                "carrier_coverage": "North America"
            }}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0008"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0021", "updates": {
                "carrier_coverage": "North America"
            }}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="calculate_total", kwargs={
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
            You are a market analyst focused on inbound shipments.
            The first objective is to determine the average weight of goods currently received.
            Calculate the average total weight in kg of these shipments.
            Next, you have to review shipments and associated carriers. You have to only consider shipments with active carriers.
            If total weight of shipment with active carrier is less than average total weight, update shipment with attribute notes "Lower than Average".
            If total weight of shipment with active carrier is more than average total weight, update shipment with attribute notes "Higher than Average".
            Finally, return the ids of shipments updated with notes "Lower than Average".
            """,
        actions=[
            Action(name="get_shipments_by_status", kwargs={"status": "Received"}),
            Action(name="calculate_aggregate", kwargs={
                "agg": "avg",
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_weight_kg",
                "list_of_ids": ["SHIP-0002", "SHIP-0007", "SHIP-0017"]
            }),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "NPEX"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0007"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "FDEG"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "THY"}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0002",
                                                           "updates": {"notes": "Higher than Average"}}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0007",
                                                           "updates": {"notes": "Lower than Average"}}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0017",
                                                           "updates": {"notes": "Higher than Average"}}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0002"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0007"}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0017"}),
            Action(name="return_ids", kwargs={"list_of_ids": ["SHIP-0007"]})
        ],
        outputs=['[\n  "SHIP-0007"\n]']
    ),

    Task(
        annotator="ArpanMahatra1999",
        user_id="task_099",
        instruction="""
            You are a logistics performance manager analyzing carrier activity in the Asian region.
            Begin by retrieving all active carriers whose regional coverage includes “Asia.”
            Then, identify all inbound shipments currently marked as “In Transit” that are using these carriers.
            Update these shipments with attribute carrier_coverage "Asia".
            Review the details of these shipments. Finally, calculate the total sum of the shipment values to assess the value of goods currently in transit with active carriers serving the Asian region.
            """,
        actions=[
            Action(name="get_carriers_by_region", kwargs={"region": "Asia"}),
            Action(name="get_active_carriers", kwargs={"list_of_scacs": ["QFA", "LOT", "SAS"]}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "status", "value": "In Transit"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "QFA", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "LOT", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "SAS", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0021", "updates": {
                "carrier_coverage": "Asia"
            }}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="calculate_total", kwargs={
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
            You are a logistics performance manager analyzing carrier activity in the European region.
            Begin by retrieving all active carriers whose regional coverage includes “Europe.”
            Then, identify all inbound shipments that are currently marked as “In Transit” and are assigned to these carriers.
            Update these shipments with attribute carrier_coverage "Europe".
            Review the details of these shipments, and finally, calculate the total sum of their values to assess the overall worth of goods currently in transit with active carriers operating in the European region.
            """,
        actions=[
            Action(name="get_carriers_by_region", kwargs={"region": "Europe"}),
            Action(name="get_active_carriers", kwargs={"list_of_scacs": ["QFA", "LOT", "SAS", "LAAL", "ICE"]}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "QFA"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LOT"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "SAS"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "LAAL"}),
            Action(name="get_carrier_by_scac", kwargs={"carrier_scac": "ICE"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "status", "value": "In Transit"}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "QFA", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "LOT", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "SAS", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "LAAL", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="filter_inbound_shipments", kwargs={"key": "carrier_scac", "value": "ICE", "list_of_ids": [
                "SHIP-0001", "SHIP-0003", "SHIP-0005", "SHIP-0008",
                "SHIP-0009", "SHIP-0011", "SHIP-0012", "SHIP-0013",
                "SHIP-0014", "SHIP-0015", "SHIP-0018", "SHIP-0020",
                "SHIP-0021", "SHIP-0023", "SHIP-0024", "SHIP-0025",
                "SHIP-0026", "SHIP-0028"
            ]}),
            Action(name="update_inbound_shipment", kwargs={"shipment_id": "SHIP-0021", "updates": {
                "carrier_coverage": "Europe"
            }}),
            Action(name="get_shipment_by_id", kwargs={"shipment_id": "SHIP-0021"}),
            Action(name="calculate_total", kwargs={
                "json": "inbound_shipments",
                "key": "shipment_id",
                "value": "total_value",
                "list_of_ids": ["SHIP-0021"]
            })
        ],
        outputs=["550000"]
    ),
]
