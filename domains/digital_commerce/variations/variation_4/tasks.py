from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="v4",
        user_id="task_001",
        instruction=(
            "Manage CommerceOps. Within organization 00D8d000000KxyzABC, related to catalog C100 (00D8d000000KxyzABC:C100), ensure the cache is updated and document a single entry in the audit log titled 'CACHE_ALIGNMENT_EVIDENCE'; consider tagging it 'Ops' and noting 'Index sync verified'. Provide the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Ops"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Index sync verified"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000KxyzABC:C100",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_002",
        instruction="For order '9006' and utilizing the B2B pricebook (id 2), confirm the pricing, incorporate a subject snapshot, apply the B2B tag, note 'Pricing recalculated', and register it as PRICING_EVIDENCE. Provide the order id.",
        actions=[
            Action(name="GetOrder", kwargs={"order_id": "9006"}),
            Action(name="GetOrderItems", kwargs={"order_id": "9006"}),
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9006", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9006"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9006"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9006"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9006", "tag": "B2B"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9006", "note": "Pricing recalculated"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "9006",
                "event_type": "PRICING_EVIDENCE",
                "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9006"]
    ),

    Task(
        annotator="v4",
        user_id="task_003",
        instruction="Regarding subject '00D8d000000LmnopQRS:C100', annotate the UAT cache status: tag as UAT and Ops, record jobs_run=2.0 and post_norm=1.0, add 'UAT pass' and 'Post-check clean', and register as CACHE_ALIGNMENT_EVIDENCE. Provide the subject id.",
        actions=[
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "UAT"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "note": "UAT pass"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "note": "Post-check clean"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_004",
        instruction=(
            "As a Security engineer, address the dev Redis cluster dcomm-dev-redis (security group sg-ffffffffffffffff), by limiting Redis access to 10.0.9.0/24 and documenting it as SG_EVIDENCE; include a subject snapshot, label it 'Dev', and note 'SG hardened'. Provide the security group id."
        ),
        actions=[
            Action(name="GetClusterById", kwargs={"cluster_id": "dcomm-dev-redis"}),
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="HardenRedisSecurityGroup", kwargs={
                "security_group_id": "sg-ffffffffffffffff",
                "allowed_cidr_list": ["10.0.9.0/24"]
            }),
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "sg-ffffffffffffffff", "tag": "Dev"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "sg-ffffffffffffffff", "note": "SG hardened"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "sg-ffffffffffffffff"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={
                "subject_id": "sg-ffffffffffffffff",
                "bucket": "SG_EVIDENCE"
            }),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "sg-ffffffffffffffff",
                "event_type": "SG_EVIDENCE",
                "bucket": "SG_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["sg-ffffffffffffffff"]
    ),

    Task(
        annotator="v4",
        user_id="task_005",
        instruction=(
            "Log a production cache realignment for org '00D8d000000KxyzABC' and catalog 'C100' by creating a consolidated CACHE_ALIGNMENT_EVIDENCE audit for subject '00D8d000000KxyzABC:C100'. Include a subject snapshot, record tag 'Prod', and note 'Coherence check OK'. Provide the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C100"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Prod"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Coherence check OK"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C100"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000KxyzABC:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_006",
        instruction="Handle using org '00D8d000000LmnopQRS' and catalog 'C200', adjust UAT cache position, attach a subject snapshot, tag UAT, add 'UAT spot-check pass', and ensure the subject id is returned.",
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000LmnopQRS:C200"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "UAT"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "UAT spot-check pass"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000LmnopQRS:C200"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_007",
        instruction="Coordinate using order '9014' and the B2B pricebook (id 2), confirm pricing, attach a subject snapshot, tag B2B, add 'Pricing recalculated', and submit PRICING_EVIDENCE. Ensure the order id is returned.",
        actions=[
            Action(name="GetOrder", kwargs={"order_id": "9014"}),
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "B2B"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "pricebook_id", "value": 2.0}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_008",
        instruction=(
            "As a Finance reviewer, for order 9015, verify a retail price against pricebook 2 and document it as PRICING_EVIDENCE; include a subject snapshot, assign the tag ‘B2C’, and append the note ‘Tax exempt N/A’. Return the order id."
        ),
        actions=[
            Action(name="GetOrder", kwargs={"order_id": "9015"}),
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Tax exempt N/A"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_009",
        instruction=(
            "As a returns coordinator, finalize a delivered return for item 1006 (qty 1) for order 9005 and record it as RETURN_EVIDENCE; include a subject snapshot, attach the tag ‘Return’, add ‘RMA approved’, and note stock_delta as 1.0. Return the order id."
        ),
        actions=[
            Action(name="GetProductStock", kwargs={"product_id": "1006"}),
            Action(name="ProcessReturn", kwargs={"order_id": "9005", "items": [{"product_id": "1006", "quantity": 1}]}),
            Action(name="UpdateProductStock", kwargs={"product_id": "1006", "delta": 1}),
            Action(name="GetProductStock", kwargs={"product_id": "1006"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9005"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9005", "tag": "Return"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9005", "note": "RMA approved"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9005", "metric": "stock_delta", "value": 1.0}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9005", "event_type": "RETURN_EVIDENCE", "bucket": "RETURN_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9005"]
    ),

    Task(
        annotator="v4",
        user_id="task_010",
        instruction=(
            "Working in Finance, for order 9014, perform a B2B price verification against pricebook 2 and document it as PRICING_EVIDENCE. Tag 'Finance', set review_flag to 1.0, and append the note 'Pricing recalculated'. Return the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "review_flag", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),

            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "9014",
                "event_type": "PRICING_EVIDENCE",
                "bucket": "PRICING_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_011",
        instruction="Handle pricing validation using order '9014' and the B2B pricebook (id 2), tag Finance, set review_flag=1.0, append 'QA signoff' and 'Tax check N/A', and file PRICING_EVIDENCE. Provide the order id.",
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "review_flag", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA signoff"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Tax check N/A"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "9014",
                "event_type": "PRICING_EVIDENCE",
                "bucket": "PRICING_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_012",
        instruction=(
            "In Prod Ops, for org 00D8d000000KxyzABC, catalog C200 (00D8d000000KxyzABC:C200), ensure the cache is up-to-date and record a database entry under 'CACHE_ALIGNMENT_EVIDENCE'; include a subject snapshot, tag it 'Prod', and add the note 'Second-cycle alignment'. Provide the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C200"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Prod"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "Second-cycle alignment"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000KxyzABC:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_013",
        instruction="With org '00D8d000000LmnopQRS' and catalog 'C100', document UAT cache alignment, include a subject snapshot, tag Ops, log jobs_run=2.0, append 'Post-check clean', and file CACHE_ALIGNMENT_EVIDENCE. Provide the subject id.",
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000LmnopQRS:C100"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "note": "Post-check clean"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000LmnopQRS:C100",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_014",
        instruction="Using order '9015' and the retail pricebook (id 2), perform pricing validation, tag B2C, set pricebook_id=2.0, append 'Customer notified' and 'Tax exempt N/A', and file PRICING_EVIDENCE. Provide the order id.",
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Customer notified"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Tax exempt N/A"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_015",
        instruction=(
            "In Prod Ops, for org 00D8d000000KxyzABC, catalog C100 (00D8d000000KxyzABC:C100), ensure the cache is cleared and current, with a database entry under 'CACHE_ALIGNMENT_EVIDENCE'; include a subject snapshot, tag it 'Prod', record jobs_run at 2.0, and add the note 'Catalog C100 rehybridized'. Provide the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C100"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Prod"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Catalog C100 rehybridized"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_016",
        instruction=(
            "Handle UAT Ops tasks. For org 00D8d000000LmnopQRS, catalog C200 (00D8d000000LmnopQRS:C200), ensure the cache is up-to-date and documented as CACHE_ALIGNMENT_EVIDENCE; label it 'UAT' and include the note 'UAT C200 refreshed'. Provide the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "UAT"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "UAT C200 refreshed"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000LmnopQRS:C200",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_017",
        instruction=(
            "Coordinate QA for prod activities. For org 00D8d000000KxyzABC, catalog C100 (00D8d000000KxyzABC:C100), it's advised to clear the catalog cache and update it, with a single database record logged under 'CACHE_ALIGNMENT_EVIDENCE'; attach a subject snapshot, designate it 'QA', log post_norm at 1.0, and append the note 'Post-check clean'. Provide the subject id."
        ),
        actions=[
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C100"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "QA"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Post-check clean"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000KxyzABC:C100",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_018",
        instruction="Utilize org '00D8d000000LmnopQRS' and catalog 'C100' to document UAT cache alignment, incorporate a subject snapshot, affiliate it with Finance, log post_norm=1.0, append 'Readiness ok', and file CACHE_ALIGNMENT_EVIDENCE. Provide the subject id.",
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000LmnopQRS:C100"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "note": "Readiness ok"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000LmnopQRS:C100",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_019",
        instruction="Utilize org '00D8d000000LmnopQRS' and catalog 'C100' to adjust UAT cache posture, mark it for Ops, note jobs_run=2.0, include 'UAT cache sync', and document CACHE_ALIGNMENT_EVIDENCE. Provide the subject id.",
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "note": "UAT cache sync"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_020",
        instruction="You’re a Finance reviewer. For order 9014, you want a quick pricing sanity check against the B2B pricebook (2); tag it for Finance, "
                    "log the B2B minimum-order threshold (b2b_min_threshold) as 1000.0, and leave the notes ‘QA reviewed’ and ‘Pricing recalculated’.",

        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA reviewed"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_021",
        instruction=(
            "Handle as a Security engineer. For the UAT Redis cluster dcomm-uat-redis (security group sg-ffffffffffffffff), restrict Redis to 10.0.9.0/24 and ensure one database record is logged under 'SG_EVIDENCE'; tag it 'UAT' and include the note 'UAT SG tightened'. Provide the security group id in return."
        ),
        actions=[
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="HardenRedisSecurityGroup", kwargs={"security_group_id": "sg-ffffffffffffffff", "allowed_cidr_list": ["10.0.9.0/24"]}),
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="ValidateClusterEndpoint", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "sg-ffffffffffffffff", "tag": "UAT"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "sg-ffffffffffffffff", "note": "UAT SG tightened"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "sg-ffffffffffffffff", "event_type": "SG_EVIDENCE", "bucket": "SG_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["sg-ffffffffffffffff"]
    ),

    Task(
        annotator="v4",
        user_id="task_022",
        instruction=(
            "Coordinate on CommerceOps. For org 00D8d000000KxyzABC, catalog C200 (00D8d000000KxyzABC:C200), ensure the cache is updated to the current state and documented as CACHE_ALIGNMENT_EVIDENCE; tag it with 'Ops' and 'Catalog', record jobs_run at 2.0, and append the note 'Post-check clean'. Provide the subject id."
        ),
        actions=[
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Ops"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Catalog"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "Post-check clean"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000KxyzABC:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_023",
        instruction="You want to deliver order 9014 pricing evidence with the B2B pricebook(pricebook 2). You want to tag it as Finance, add QA signoff and "
                    "Promo off, and file the report as PRICING_EVIDENCE.",
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA signoff"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Promo off"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "9014",
                "event_type": "PRICING_EVIDENCE",
                "bucket": "PRICING_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),


    Task(
        annotator="v4",
        user_id="task_024",
        instruction=(
            "Oversee on CommerceOps. For org 00D8d000000KxyzABC, catalog C100 (00D8d000000KxyzABC:C100), synchronize the cache to the current version and record a single database entry under 'CACHE_ALIGNMENT_EVIDENCE'; include a subject snapshot, assign the 'Prod' tag, and note 'Coherence check OK'. Report back the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Prod"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Coherence check OK"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C100"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000KxyzABC:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9005"]
    ),

    Task(
        annotator="v4",
        user_id="task_025",
        instruction=(
            "Manage on UAT Ops. For org 00D8d000000LmnopQRS, catalog C200 (00D8d000000LmnopQRS:C200), ensure the cache is aligned and documented as CACHE_ALIGNMENT_EVIDENCE; tag it with 'QA' and 'Ops', record post_norm at 1.0, and include the notes 'Warm cache confirmed' and 'Readiness ok'. Provide the subject id."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "QA"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "Warm cache confirmed"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "Readiness ok"}),

            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000LmnopQRS:C200",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_026",
        instruction=(
            "You're stationed on UAT Ops. For organization 00D8d000000LmnopQRS, concerning catalog C200 (00D8d000000LmnopQRS:C200), aim to have the cache realigned and documented as CACHE_ALIGNMENT_EVIDENCE; label it 'UAT', 'Ops', and 'QA', note jobs_run at 2.0 and post_norm at 1.0, and include the remarks 'UAT spot-check pass' and 'Warm cache confirmed'. Provide the subject id."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "UAT"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "Ops"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "QA"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "UAT spot-check pass"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "Warm cache confirmed"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000LmnopQRS:C200"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000LmnopQRS:C200",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_027",
        instruction=(
            "Acting as an Ops analyst. For transaction 9015, request a retail price verification against pricebook 2 and record it as PRICING_EVIDENCE; mark it 'Ops', capture pricebook_id as 2.0 and follow_up as 1.0, and append the remarks 'QA reviewed' and 'No tax change'. Deliver the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "follow_up", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "QA reviewed"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "No tax change"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "9015",
                "event_type": "PRICING_EVIDENCE",
                "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_028",
        instruction=(
            "You're serving on CommerceOps. Related to org 00D8d000000KxyzABC, catalog C200 (00D8d000000KxyzABC:C200), ensure the production cache is cleared and updated, with one database entry labeled 'CACHE_ALIGNMENT_EVIDENCE'; mark it 'QA', note jobs_run at 2.0, and attach the comment 'QA pass'. Supply the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "QA"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "QA pass"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000KxyzABC:C200",
                           "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                           "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_029",
        instruction=(
            "As a returns coordinator, your task is to document a received return for item 1006 (qty 1) and secure a single RETURN_EVIDENCE entry; include a snapshot of the subject, label 'Return', add the remark 'Inspected – no damage', and register rma_items as 1.0. Provide the order id."
        ),
        actions=[
            Action(name="GetProductStock", kwargs={"product_id": "1006"}),
            Action(name="ProcessReturn", kwargs={"order_id": "9005", "items": [{"product_id": "1006", "quantity": 1}]}),
            Action(name="UpdateProductStock", kwargs={"product_id": "1006", "delta": 1}),
            Action(name="GetProductStock", kwargs={"product_id": "1006"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9005", "tag": "Return"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9005", "metric": "rma_items", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9005", "note": "Inspected – no damage"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9005"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "9005",
                "event_type": "RETURN_EVIDENCE",
                "bucket": "RETURN_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9005"]
    ),

    Task(
        annotator="v4",
        user_id="task_030",
        instruction=(
            "Functioning as a DevOps engineer. For the development Redis cluster dcomm-dev-redis (security group sg-ffffffffffffffff), confine access to 10.0.9.0/24 and write one database record labeled 'SG_EVIDENCE'; assign the tag 'Dev' and include the note 'CIDR restricted'. Return the security group id."
        ),
        actions=[
            Action(name="GetClusterById", kwargs={"cluster_id": "dcomm-dev-redis"}),
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="HardenRedisSecurityGroup", kwargs={"security_group_id": "sg-ffffffffffffffff", "allowed_cidr_list": ["10.0.9.0/24"]}),
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="ValidateClusterEndpoint", kwargs={"cluster_id": "dcomm-dev-redis"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "sg-ffffffffffffffff", "tag": "Dev"}),
            Action(name="RecordMetric", kwargs={"subject_id": "sg-ffffffffffffffff", "metric": "allowed_cidrs", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "sg-ffffffffffffffff", "note": "CIDR restricted"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "sg-ffffffffffffffff",
                "event_type": "SG_EVIDENCE",
                "bucket": "SG_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["sg-ffffffffffffffff"]
    ),

    Task(
        annotator="v4",
        user_id="task_031",
        instruction="You are a Finance Reviewer. A recent B2B order needs pricing confirmation on order 9014. You want to validate it "
                    "against the B2B pricebook, add a short review note, and record pricing evidence.",
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "UAT signoff"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_032",
        instruction=(
            "Working in CommerceOps, you need the production cache updated for org 00D8d000000KxyzABC, catalog C200 (00D8d000000KxyzABC:C200). Write a single database entry under ‘CACHE_ALIGNMENT_EVIDENCE’, label it ‘Prod’, note jobs_run at 2.0, and include the remark ‘Second-cycle alignment’. Provide the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Prod"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "Second-cycle alignment"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000KxyzABC:C200",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_033",
        instruction=(
            "In Finance, review order 9014’s B2B pricing against pricebook 2, documenting it as PRICING_EVIDENCE. Label it 'Finance' and make a note saying 'Tax check N/A'. Provide the order id."
        ),
        actions=[
            Action(name="GetOrder", kwargs={"order_id": "9014"}),
            Action(name="GetOrderItems", kwargs={"order_id": "9014"}),
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Tax check N/A"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "9014",
                "event_type": "PRICING_EVIDENCE",
                "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_034",
        instruction=(
            "Within Finance, perform a swift retail price validation for order 9005 using the retail pricebook (2). Record the findings, tag 'Finance', log pricebook_id as 2.0, and include the comment ‘Customer confirmed receipt’. Provide the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9005", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9005"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9005"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9005", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9005", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9005", "note": "Customer confirmed receipt"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "9005", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9005"]
    ),

    Task(
        annotator="v4",
        user_id="task_035",
        instruction=(
            "In your Prod Ops role, ensure the catalog cache for org 00D8d000000KxyzABC, catalog C100 (00D8d000000KxyzABC:C100) is cleared and updated. Record the result as CACHE_ALIGNMENT_EVIDENCE, attach a subject snapshot, register jobs_run at 2.0, and note ‘Index sync verified’. Provide the subject id."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C100"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Prod"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Index sync verified"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_036",
        instruction=(
            "You're responsible for UAT Ops. For org 00D8d000000LmnopQRS, with catalog C200 (00D8d000000LmnopQRS:C200), ensure the cache is cleared and realigned, and log it as CACHE_ALIGNMENT_EVIDENCE; mark it 'UAT', and annotate with 'QA pass'. Retrieve the subject id."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "UAT"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "QA pass"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_037",
        instruction=(
            "In your role as a Finance reviewer, for order 9014, verify pricing with the B2B pricebook (2); label it 'B2B', capture b2b_min_threshold at 1000.0, note 'Promo off', and document an audit under 'PRICING_EVIDENCE'. Retrieve the order id."
        ),
        actions=[
            Action(name="GetOrder", kwargs={"order_id": "9014"}),
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "B2B"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Promo off"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_038",
        instruction="You’re a Finance reviewer. For order 9015, you want a quick retail price check against pricebook 1 and you want it on record as "
                    "PRICING_EVIDENCE; you tag it 'B2C', log b2c_min_threshold as 50.0, and leave the note 'No tax change'. Return the order id.",
        actions=[
            Action(name="GetOrder", kwargs={"order_id": "9015"}),
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "1"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "b2c_min_threshold", "value": 50.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "No tax change"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_039",
        instruction="Record pricing evidence for accessory order 9005 after checking against active pricebook 2. Retrieve the order id.",
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9005", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9005"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9005"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9005", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9005", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9005", "note": "Pricing review queued"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "9005", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9005"]
    ),

    Task(
        annotator="v4",
        user_id="task_040",
        instruction=(
            "As a Security engineer, ensure access to the dev Redis cluster dcomm-dev-redis (security group sg-ffffffffffffffff) is confined to 10.0.9.0/24, and record one database entry under 'SG_EVIDENCE'; append a subject snapshot, and tag with 'Dev' and 'Security', noting 'SG hardened'. Retrieve the security group id."
        ),
        actions=[
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="HardenRedisSecurityGroup", kwargs={"security_group_id": "sg-ffffffffffffffff", "allowed_cidr_list": ["10.0.9.0/24"]}),
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="GetClusterById", kwargs={"cluster_id": "dcomm-dev-redis"}),
            Action(name="ValidateClusterEndpoint", kwargs={"cluster_id": "dcomm-dev-redis"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "sg-ffffffffffffffff"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "sg-ffffffffffffffff", "tag": "Dev"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "sg-ffffffffffffffff", "tag": "Security"}),
            Action(name="RecordMetric", kwargs={"subject_id": "sg-ffffffffffffffff", "metric": "allowed_cidrs", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "sg-ffffffffffffffff", "note": "Hardened"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "sg-ffffffffffffffff", "note": "Endpoint validated"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "sg-ffffffffffffffff", "event_type": "SG_EVIDENCE", "bucket": "SG_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["sg-ffffffffffffffff"]
    ),

    Task(
        annotator="v4",
        user_id="task_041",
        instruction=(
            "Handle the confirmation of pricing for retail order '9015' utilizing pricebook '2' and generate one aggregated PRICING_EVIDENCE audit for subject '9015'. Ensure to include a subject snapshot and capture tag 'Ops', metric 'pricebook_id=2.0', as well as the notes 'Customer notified' and 'Tax exempt N/A'. Return the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Customer notified"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Tax exempt N/A"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9015"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "9015", "bucket": "PRICING_EVIDENCE"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "9015",
                "event_type": "PRICING_EVIDENCE",
                "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_042",
        instruction=(
            "In CommerceOps, for org 00D8d000000KxyzABC, catalog C200 (00D8d000000KxyzABC:C200), align the cache to be current and documented as CACHE_ALIGNMENT_EVIDENCE; tag it 'Prod' and append the note 'Catalog warmed'. Return the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Prod"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "Catalog warmed"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000KxyzABC:C200",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_043",
        instruction=(
            "Within Finance, confirm B2B pricing for order 9014 against pricebook 2 and document it as PRICING_EVIDENCE; be sure to include a subject snapshot, tag 'Finance', and append the note 'QA reviewed'. Return the order id."
        ),
        actions=[
            Action(name="GetOrder", kwargs={"order_id": "9014"}),
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA reviewed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_044",
        instruction=(
            "Verify the retail pricing for the recent order, 9015, and ensure to log one PRICING_EVIDENCE audit. You must tag Pricing and incorporate the notes 'Customer notified' and 'Tax exempt N/A'. Return the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Pricing"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Customer notified"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Tax exempt N/A"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_045",
        instruction=(
            "As an Operations Lead, for org 00D8d000000KxyzABC, focus on catalog C100 (00D8d000000KxyzABC:C100), and document the production cache realignment as CACHE_ALIGNMENT_EVIDENCE — including a subject snapshot, with the tags 'Finance' and 'Ops', and the notes 'Index sync verified' and 'QA pass'. Return the subject id."
        ),
        actions=[
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Finance"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Ops"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Index sync verified"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "QA pass"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C100"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000KxyzABC:C100",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"
            }),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_046",
        instruction=(
            "Manage UAT Ops. Regarding org 00D8d000000LmnopQRS, catalog C100 (00D8d000000LmnopQRS:C100), align the cache and archive it as CACHE_ALIGNMENT_EVIDENCE; incorporate a subject snapshot, label it with 'UAT' and 'QA', log post_norm at 1.0, and append the note 'QA pass'. Retrieve the subject id."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "QA"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "UAT"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "note": "QA pass"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000LmnopQRS:C100"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000LmnopQRS:C100",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_047",
        instruction=(
            "Ensure pricing verification for order '9014' utilizing the B2B tagged pricebook 2 and document a PRICING_EVIDENCE audit. Mark Finance and include the notes 'Promo off' and 'QA reviewed'. Obtain the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "B2B"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Promo off"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA reviewed"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9014"}),
            Action(name="ConsolidateWorkspaceEvents", kwargs={"subject_id": "9014",
                                                                "event_types": ["PRICEBOOK_VERIFICATION", "ELIGIBILITY_CHECK", "TAG_ADDED",
                                                                                "METRIC_RECORDED", "ANNOTATION"]}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_048",
        instruction="You want to validate retail pricing for a recent order, 9015. You want to tag B2C and Pricing, log the B2C minimum threshold ($50) "
                    "and the pricebook used which is 2, and note Tax exempt N/A and No tax change.",
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Pricing"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "b2c_min_threshold", "value": 50.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Tax exempt N/A"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "No tax change"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_049",
        instruction=(
            "As a DevOps engineer, for the dev Redis cluster dcomm-dev-redis (security group sg-ffffffffffffffff), restrict Redis access to 10.0.9.0/24 and store a compliance record in the database as 'SG_EVIDENCE'; apply the tag 'Dev' and attach the note 'CIDR restricted'. Acquire the security group id."
        ),
        actions=[
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="HardenRedisSecurityGroup", kwargs={"security_group_id": "sg-ffffffffffffffff", "allowed_cidr_list": ["10.0.9.0/24"]}),
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "sg-ffffffffffffffff", "tag": "Dev"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "sg-ffffffffffffffff", "note": "CIDR restricted"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "sg-ffffffffffffffff", "event_type": "SG_EVIDENCE", "bucket": "SG_EVIDENCE"}),
        ],
        outputs=["sg-ffffffffffffffff"]
    ),

    Task(
        annotator="v4",
        user_id="task_050",
        instruction=(
            "Being a Security engineer, for the UAT Redis security group sg-ffffffffffffffff, confine access to 10.0.9.0/24 and insert a database record as 'SG_EVIDENCE'; designate it with 'UAT' and incorporate the note 'Endpoint validated'. Retrieve the security group id."
        ),
        actions=[
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="HardenRedisSecurityGroup", kwargs={"security_group_id": "sg-ffffffffffffffff", "allowed_cidr_list": ["10.0.9.0/24"]}),
            Action(name="ListSecurityGroupRules", kwargs={"security_group_id": "sg-ffffffffffffffff"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "sg-ffffffffffffffff", "tag": "UAT"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "sg-ffffffffffffffff", "note": "Endpoint validated"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "sg-ffffffffffffffff", "event_type": "SG_EVIDENCE", "bucket": "SG_EVIDENCE"}),
        ],
        outputs=["sg-ffffffffffffffff"]
    ),

    Task(
        annotator="v4",
        user_id="task_051",
        instruction=(
            "Handle the documentation of a production cache realignment for org '00D8d000000KxyzABC' catalog 'C200' with one CACHE_ALIGNMENT_EVIDENCE audit. Ensure to tag Prod, Catalog, and Ops, then add the notes 'Second-cycle alignment' and 'Catalog warmed'. Return the subject id."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Prod"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Catalog"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "Second-cycle alignment"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "Catalog warmed"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000KxyzABC:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_052",
        instruction=(
            "Coordinate the validation of a recent B2B order, 9014, against the B2B pricebook and proceed to file the audit record for client review."
        ),
        actions=[
            Action(name="GetOrder", kwargs={"order_id": "9014"}),
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "B2B"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9014"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "9014", "bucket": "PRICING_EVIDENCE"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_053",
        instruction=(
            "As a Finance reviewer, ensure that order 9015 has its retail pricing checked against pricebook 2. Include a subject snapshot, tag 'B2C' and 'Pricing', and add the note 'Receipt sent'. Return the order id."
        ),
        actions=[
            Action(name="GetOrder", kwargs={"order_id": "9015"}),
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Pricing"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Receipt sent"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9015"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_054",
        instruction=(
            "Working in UAT Ops, ensure that for org 00D8d000000LmnopQRS, catalog C200 (00D8d000000LmnopQRS:C200), the realignment is captured with a single database record under ‘CACHE_ALIGNMENT_EVIDENCE’; apply the 'UAT' tag and add the note ‘Post-check clean’. Return the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "UAT"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "Post-check clean"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000LmnopQRS:C200"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_055",
        instruction=(
            "As a Platform Reliability Engineer, confirm production cache alignment for org '00D8d000000KxyzABC' catalog 'C100', include a subject snapshot, add brief readiness notes, and document one CACHE_ALIGNMENT_EVIDENCE audit. Return the subject id."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C100"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Prod"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Coherence ok"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Index sync verified"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_056",
        instruction="Record a UAT C200 cache realignment; tag UAT and QA, document that two jobs were executed, and note UAT pass and Warm cache confirmed.",
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "UAT"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "QA"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "UAT pass"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "Warm cache confirmed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_057",
        instruction=(
            "Within Finance, for order 9014, coordinate a B2B price review against pricebook 2 noted as PRICING_EVIDENCE; tag it 'B2B', register b2b_min_threshold at 1000.0 and pricebook_id as 2.0, and include the notes 'Promo off' and 'QA reviewed'. Return the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "B2B"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Promo off"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA reviewed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_058",
        instruction=(
            "As a Finance reviewer, for order 9015, arrange a retail price verification against the retail pricebook (2) and ensure the outcome is captured as PRICING_EVIDENCE: tag it 'B2C', register b2c_min_threshold as 50.0 and pricebook_id as 2.0, and include the notes 'No tax change' and 'Customer notified'. Return the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "b2c_min_threshold", "value": 50.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "No tax change"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Customer notified"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_059",
        instruction="You’re on CommerceOps. For org 00D8d000000KxyzABC, catalog C200 (00D8d000000KxyzABC:C200), you want the production cache cleared and "
                    "realigned to current; tag it ‘Prod’, ‘Catalog’, and ‘Ops’, record jobs_run at 2.0, and add the note ‘Second-cycle alignment’. Return the subject id.",
    actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Prod"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Catalog"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "Second-cycle alignment"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000KxyzABC:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_060",
        instruction="You’re working across Finance and Ops. For order 9014, you want B2B pricing sanity-checked against pricebook 2 and captured as "
                    "PRICING_EVIDENCE; you tag it 'B2B', 'Finance', and 'Ops', record b2b_min_threshold at 1000.0 and pricebook_id as 2.0, and add the notes "
                    "'Pricing recalculated' and 'QA signoff'. Return the order id.",
    actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "B2B"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA signoff"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_061",
        instruction=(
            "Handle the UAT cache alignment for org '00D8d000000LmnopQRS' and catalog 'C100'. Tag 'UAT' and 'Ops', record metrics 'jobs_run=2.0' and 'post_norm=1.0', and annotate 'UAT cache sync'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "UAT"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "note": "UAT cache sync"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C100"]
    ),
    Task(
        annotator="v4",
        user_id="task_062",
        instruction=(
            "Ensure the accuracy of pricing for order '9015' using pricebook '2' (B2C). Tag 'B2C', 'Pricing', and 'Ops', record metrics 'b2c_min_threshold=50.0' and 'pricebook_id=2.0', and annotate 'Tax exempt N/A' and 'QA reviewed'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Pricing"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "b2c_min_threshold", "value": 50.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Tax exempt N/A"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "QA reviewed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_063",
        instruction=(
            "Coordinate the Production cache realignment for org '00D8d000000KxyzABC' and catalog 'C100'. Tag 'Prod' and 'Finance', record metrics 'jobs_run=2.0' and 'post_norm=1.0', and annotate 'Catalog warmed' and 'Post-check clean'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Prod"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Catalog warmed"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Post-check clean"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_064",
        instruction=(
            "Verify B2B pricing accuracy for order '9014' using pricebook '2'. Tag 'Ops', record metric 'b2b_min_threshold=1000.0', and annotate 'Tax check N/A' and 'Pricing recalculated'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Tax check N/A"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_065",
        instruction=(
            "Confirm B2B pricing integrity for order '9014' using pricebook '2'. Tag 'B2B' and 'Ops', and annotate 'Pricing recalculated' and 'QA reviewed'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "B2B"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Ops"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA reviewed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_066",
        instruction=(
            "As a Finance reviewer, for order 9015, request a comparison of the retail price with pricebook 2 and ensure this is filed as PRICING_EVIDENCE; include a subject snapshot, attach the tag 'B2C', and include the note 'Promo off'. Provide the order id."
        ),
        actions=[
            Action(name="GetOrder", kwargs={"order_id": "9015"}),
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Promo off"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9015"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "9015", "bucket": "PRICING_EVIDENCE"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_067",
        instruction=(
            "Coordinate the adjustment of the Production cache posture for org '00D8d000000KxyzABC' along with catalog 'C100'. Apply tags 'Prod' and 'Ops', document metrics 'jobs_run=2.0' and 'post_norm=1.0', and note 'Index sync verified' and 'Post-check clean'."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Prod"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Index sync verified"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Post-check clean"}),

            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000KxyzABC:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_068",
        instruction=(
            "Adjust the UAT cache posture for organization '00D8d000000LmnopQRS' with catalog 'C200'. Mark with tags 'UAT' and 'QA', track metrics 'jobs_run=2.0' and 'post_norm=1.0', and note 'UAT pass' and 'Warm cache confirmed'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "UAT"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "QA"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "UAT pass"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "Warm cache confirmed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_069",
        instruction=(
            "Ensure B2B pricing accuracy for order '9014' utilizing pricebook '2'. Label with 'B2B', 'Finance', and 'Ops', log the metric 'b2b_min_threshold=1000.0', and note 'Tax check N/A' and 'Promo off'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "B2B"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Tax check N/A"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Promo off"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_070",
        instruction=(
            "Validate the pricing accuracy for order '9015' using pricebook '2' intended for B2C. Include tags 'B2C', 'Finance', and 'Ops', record metrics 'b2c_min_threshold=50.0' and 'pricebook_id=2.0', and note 'QA reviewed'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Finance"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "b2c_min_threshold", "value": 50.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "QA reviewed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_071",
        instruction=(
            "Handle Prod Ops tasks. For org 00D8d000000KxyzABC, catalog C200 (00D8d000000KxyzABC:C200), ensure the cache is up-to-date and have a single database record documented under 'CACHE_ALIGNMENT_EVIDENCE'; mark it 'Prod' and include the note 'Second-cycle alignment'. Return the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Prod"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "Second-cycle alignment"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C200"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000KxyzABC:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
        ],
        outputs=["00D8d000000KxyzABC:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_072",
        instruction=(
            "Coordinate UAT Ops activities. For org 00D8d000000LmnopQRS, catalog C100 (00D8d000000LmnopQRS:C100), ensure the cache is realigned with the current state and log a single database record under 'CACHE_ALIGNMENT_EVIDENCE'; append a subject snapshot, label it 'UAT', and include the note 'UAT cache sync'. Return the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "UAT"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "note": "UAT cache sync"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000LmnopQRS:C100"}),
            Action(name="BuildAuditDetailsForBucket", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="CreateAuditRecord",
                   kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
        ],
        outputs=["00D8d000000LmnopQRS:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_073",
        instruction=(
            "Handle Finance duties. For order 9014, conduct a B2B price review against pricebook 2 and document a single database record under 'PRICING_EVIDENCE'; attach a subject snapshot, label 'Finance', and include the note 'QA reviewed'. Return the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "9014"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_074",
        instruction=(
            "Execute Finance tasks. For order 9015, conduct a retail price assessment against pricebook 2 and log a single database record under 'PRICING_EVIDENCE'. Return the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "9015",
                "event_type": "PRICING_EVIDENCE",
                "bucket": "PRICING_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_075",
        instruction=(
            "Realign the Production cache posture for org '00D8d000000KxyzABC' and catalog 'C100'. Label 'Prod' and 'Finance', record metric 'jobs_run=2.0', and include annotations 'Coherence ok' and 'Index sync verified'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Prod"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Coherence ok"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Index sync verified"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_076",
        instruction=(
            "Handle the adjustment of the UAT cache posture for organization '00D8d000000LmnopQRS' and catalog 'C200'. Ensure tags 'UAT' and 'Ops' are applied, metrics 'jobs_run=2.0' and 'post_norm=1.0' are recorded, and add the annotation 'UAT cache sync'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "UAT"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "UAT cache sync"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_077",
        instruction=(
            "Being responsible for UAT Ops, ensure the cache posture for subject 00D8d000000LmnopQRS:C200 is noted and filed as CACHE_ALIGNMENT_EVIDENCE using the ‘CACHE_ALIGNMENT_EVIDENCE’ bucket. Tag it as ‘Ops’ and include the note ‘UAT cache sync’. Provide the subject ID."
        ),
        actions=[
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "Ops"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "UAT cache sync"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000LmnopQRS:C200",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_078",
        instruction=(
            "Oversee the validation of pricing integrity for order '9015' using pricebook '2' (B2C). Use the tags 'Pricing' and 'Ops', capture metrics 'b2c_min_threshold=50.0' and 'pricebook_id=2.0', and annotate with 'No tax change' and 'QA reviewed'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Pricing"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "b2c_min_threshold", "value": 50.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "No tax change"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "QA reviewed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_079",
        instruction=(
            "While handling Prod Ops, ensure a simple cache-alignment note for subject 00D8d000000KxyzABC:C100 is on file as CACHE_ALIGNMENT_EVIDENCE; tag it ‘Finance’ and add the note ‘Coherence ok’. Provide the subject ID."
        ),
        actions=[
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Finance"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Coherence ok"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000KxyzABC:C100",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_080",
        instruction=(
            "Coordinate a CACHE_ALIGNMENT_EVIDENCE audit for UAT organization '00D8d000000LmnopQRS' and catalog 'C200' following cache posture realignment as per policy. Include tag 'Ops', metric 'post_norm=1.0', and note 'Warm cache confirmed'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "Warm cache confirmed"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000LmnopQRS:C200",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_081",
        instruction=(
            "Ensure B2B pricing integrity for order '9014' with pricebook '2'. Label 'Ops' and 'Finance', capture metric 'b2b_min_threshold=1000.0', and mark 'Tax check N/A' and 'QA reviewed'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Ops"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Tax check N/A"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA reviewed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_082",
        instruction=(
            "As a Finance reviewer, verify a retail price check for order 9015 using pricebook 2, documenting the result as PRICING_EVIDENCE. Mark it 'B2C' and 'Finance', note b2c_min_threshold=50.0 and pricebook_id=2.0, and add the remark 'Promo off'. Provide the order id afterward."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "b2c_min_threshold", "value": 50.0}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Promo off"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_083",
        instruction=(
            "In Prod Ops, for subject 00D8d000000KxyzABC:C200, record quickly the alignment as CACHE_ALIGNMENT_EVIDENCE under the 'CACHE_ALIGNMENT_EVIDENCE' bucket; label 'Catalog' and append 'Catalog warmed'. Submit the subject id."
        ),
        actions=[
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Catalog"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "Catalog warmed"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000KxyzABC:C200",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_084",
        instruction=(
            "Conduct a CACHE_ALIGNMENT_EVIDENCE audit for UAT org '00D8d000000LmnopQRS' and catalog 'C100' following a cache posture realignment as per policy. Add tag 'QA', metric 'jobs_run=2.0', and note 'Index sync verified'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "QA"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "note": "Index sync verified"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000LmnopQRS:C100",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_085",
        instruction=(
            "Confirm B2B pricing integrity for order '9014' with pricebook '2'. Mark 'Ops', log metric 'b2b_min_threshold=1000.0', and annotate 'Pricing recalculated' and 'QA signoff'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA signoff"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_086",
        instruction=(
            "Handle the validation of pricing integrity for order '9015' utilizing pricebook '2' (B2C). Tag 'Pricing', log the metric 'pricebook_id=2.0', and annotate with 'Promo off' and 'Receipt sent'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Pricing"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Promo off"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Receipt sent"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_087",
        instruction=(
            "Coordinate the realignment of the Production cache posture for organization '00D8d000000KxyzABC' along with catalog 'C100'. Tag 'Prod', log the metric 'jobs_run=2.0', and annotate with 'Index sync verified'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Prod"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Index sync verified"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_088",
        instruction=(
            "In UAT Ops, for subject 00D8d000000LmnopQRS:C100, create a concise posture note with a single database record within ‘CACHE_ALIGNMENT_EVIDENCE’; tag it ‘UAT’ and include the note ‘UAT pass’. Return the subject id."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "tag": "UAT"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "note": "UAT pass"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000LmnopQRS:C100", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_089",
        instruction=(
            "Oversee the validation of B2B pricing integrity for order '9014' employing pricebook '2'. Tag 'Finance', log the metric 'b2b_min_threshold=1000.0', and include notes 'QA reviewed' and 'Pricing recalculated'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA reviewed"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_090",
        instruction=(
            "Execute a PRICING_EVIDENCE audit for order '9015' utilizing pricebook '2'. Incorporate tag 'Ops' and notes 'QA reviewed' and 'Tax exempt N/A'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Ops"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "QA reviewed"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Tax exempt N/A"}),

            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "9015",
                "event_type": "PRICING_EVIDENCE",
                "bucket": "PRICING_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_091",
        instruction=(
            "Ensure the integrity of B2B pricing for order '9014' with pricebook '2'. Assign 'Finance' as the tag, log the metric 'pricebook_id=2.0', and add annotations 'Tax check N/A' and 'Promo off'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Tax check N/A"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Promo off"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_092",
        instruction=(
            "Confirm the pricing integrity for order '9015' using pricebook '2' (B2C). Tag it with 'Ops', document the metric 'b2c_min_threshold=50.0', and include annotations 'QA reviewed' and 'No tax change'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "b2c_min_threshold", "value": 50.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "QA reviewed"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "No tax change"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_093",
        instruction=(
            "Adjust the Production cache setup for org '00D8d000000KxyzABC' and catalog 'C200'. Apply the tag 'Catalog', capture the metric 'jobs_run=2.0', and note 'Catalog warmed'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "tag": "Catalog"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "note": "Catalog warmed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000KxyzABC:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_094",
        instruction=(
            "Adjust the UAT cache setup for org '00D8d000000LmnopQRS' and catalog 'C200'. Use the tag 'QA', measure the metric 'post_norm=1.0', and note 'Readiness ok'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "QA"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "post_norm", "value": 1.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "Readiness ok"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),

    Task(
        annotator="v4",
        user_id="task_095",
        instruction=(
            "Validate the B2B pricing integrity for order '9014' using pricebook '2'. Apply the tag 'B2B', log the metric 'b2b_min_threshold=1000.0', and include annotations 'Manual review N/A' and 'Tax check N/A'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "B2B"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Manual review N/A"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Tax check N/A"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_096",
        instruction=(
            "Validate the pricing integrity for order '9015' utilizing pricebook '2' (B2C). Tag 'B2C', document the metric 'pricebook_id=2.0', and annotate with 'Customer notified' and 'Receipt sent'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9015", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9015"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9015"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9015", "tag": "B2C"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9015", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Customer notified"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9015", "note": "Receipt sent"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9015", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9015"]
    ),

    Task(
        annotator="v4",
        user_id="task_097",
        instruction=(
            "As part of Finance, conduct a B2B price review against pricebook 2 for order 9014, capturing it as PRICING_EVIDENCE; assign the tag ‘Finance’, log b2b_min_threshold=1000.0, and append the notes ‘CIDR restricted’ and ‘QA reviewed’. Return the order id."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Finance"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "b2b_min_threshold", "value": 1000.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "CIDR restricted"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA reviewed"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_098",
        instruction=(
            "In Prod Ops, for org 00D8d000000KxyzABC, catalog C100 (00D8d000000KxyzABC:C100), decide to clear the catalog cache and update it completely. Record this as CACHE_ALIGNMENT_EVIDENCE; include a subject snapshot, tag it ‘Prod’, and note ‘Post-check clean’. Return the subject id."
        ),
        actions=[
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000KxyzABC", "catalog_id": "C100"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000KxyzABC"}),
            Action(name="CollectSubjectSnapshot", kwargs={"subject_id": "00D8d000000KxyzABC:C100"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "tag": "Prod"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000KxyzABC:C100", "note": "Post-check clean"}),
            Action(name="CreateAuditRecord", kwargs={
                "subject_id": "00D8d000000KxyzABC:C100",
                "event_type": "CACHE_ALIGNMENT_EVIDENCE",
                "bucket": "CACHE_ALIGNMENT_EVIDENCE"
            }),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000KxyzABC:C100"]
    ),

    Task(
        annotator="v4",
        user_id="task_099",
        instruction=(
            "Confirm B2B pricing integrity for order '9014' using pricebook '2'. Tag 'Ops', log the metric 'pricebook_id=2.0', and annotate with 'QA reviewed' and 'Pricing recalculated'."
        ),
        actions=[
            Action(name="VerifyOrderPricesAgainstPricebook", kwargs={"order_id": "9014", "pricebook_id": "2"}),
            Action(name="RecomputeOrderTotals", kwargs={"order_id": "9014"}),
            Action(name="EnforceMinimumOrder", kwargs={"order_id": "9014"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "9014", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "9014", "metric": "pricebook_id", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "QA reviewed"}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "9014", "note": "Pricing recalculated"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "9014", "event_type": "PRICING_EVIDENCE", "bucket": "PRICING_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["9014"]
    ),

    Task(
        annotator="v4",
        user_id="task_100",
        instruction=(
            "Adjust the UAT cache posture for org '00D8d000000LmnopQRS' and catalog 'C200'. Tag 'Ops', log the metric 'jobs_run=2.0', and note 'UAT cache sync'."
        ),
        actions=[
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="InvalidateCacheForCatalog", kwargs={"org_id": "00D8d000000LmnopQRS", "catalog_id": "C200"}),
            Action(name="RunCacheJobsInOrder", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="NormalizeOrgCacheTimestamps", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="GetCacheJobHistory", kwargs={"org_id": "00D8d000000LmnopQRS"}),
            Action(name="AddSubjectTag", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "tag": "Ops"}),
            Action(name="RecordMetric", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "metric": "jobs_run", "value": 2.0}),
            Action(name="EmitAnnotation", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "note": "UAT cache sync"}),
            Action(name="CreateAuditRecord", kwargs={"subject_id": "00D8d000000LmnopQRS:C200", "event_type": "CACHE_ALIGNMENT_EVIDENCE", "bucket": "CACHE_ALIGNMENT_EVIDENCE"}),
            Action(name="GetAuditLog", kwargs={}),
        ],
        outputs=["00D8d000000LmnopQRS:C200"]
    ),
]
