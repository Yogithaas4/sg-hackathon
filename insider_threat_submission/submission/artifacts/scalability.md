# Production Scalability Design

## Current: Hackathon (1,200 events)
- CSV → Pandas → Isolation Forest → Flask → Plotly HTML
- Runs on single MacBook, processes in seconds

## Production: 1M+ Events/Day

### Ingestion Layer
- Apache Kafka: Streams from SQL DBs, APIs, file shares
- Partitioned by user_id for parallel processing
- 7-day retention for replay

### Processing Layer  
- Apache Spark: Feature engineering on 30-second micro-batches
- Redis: User baseline cache (<1ms lookup)
- MLflow: Model versioning and A/B testing

### Alerting Layer
- CRITICAL alerts → PagerDuty/Slack in <30 seconds
- DLP integration → Auto-block USB/email exfiltration
- SIEM integration → Auto-create tickets

### Storage
- PostgreSQL: Alert persistence and audit trail
- S3/Data Lake: Raw log archival (compliance)
- Elasticsearch: Fast log search

## Performance Targets
- Detection latency: <5 minutes
- Alert precision: >75%
- False positive rate: <25%
- Throughput: 12,000 events/second
