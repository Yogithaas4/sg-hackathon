# 01 - Access Log Ingestion

## Objective

Ingest enterprise data access events from CSV files and normalize them into a single enriched dataframe for anomaly detection.

## Implementation

Code: `src/ingest.py`

The ingestion layer loads:

- `data/data_access_logs.csv`
- `data/user_profiles.csv`

It parses timestamps, derives time features, enriches missing operational fields, and merges each event with the user's HR/profile context.

## Supported Input Formats

The current prototype supports CSV ingestion directly. It is also structured so API payloads can be converted to the same dataframe schema before calling the feature pipeline.

Expected access-log fields include:

- `timestamp`
- `user_id`
- `username`
- `department`
- `resource`
- `resource_sensitivity`
- `action`
- `status`
- `time_classification`

Additional generated/enriched fields:

- `hour`
- `day_of_week`
- `is_weekend`
- `rowcount`
- `destination`
- `query_type`

## Theory

Good anomaly detection depends on consistent event normalization. Different enterprise systems generate different log formats, so this stage standardizes timestamps, user identity, accessed asset, action, sensitivity, destination, and status into a common schema.

For production, API ingestion can be added through Kafka or a REST endpoint that validates incoming JSON and writes it to the same normalized schema.

## Evidence

- Input data: `data/data_access_logs.csv`, `data/user_profiles.csv`
- Enriched output: `outputs/scored_logs.csv`

