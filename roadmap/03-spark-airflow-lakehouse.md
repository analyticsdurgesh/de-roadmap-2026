# Stage 3: Spark, Airflow and the lakehouse (months 4 to 7)

This is the core of the 2026 stack: Spark, through PySpark, to process data where it is stored; Airflow to run pipelines on a schedule; dbt for transformations; and one lakehouse table format. Your cloud's data services come in here too. Finish the stage with one end-to-end project, because that single project answers most of the questions an interviewer will ask.

## What to learn

**PySpark**

- The DataFrame API, lazy evaluation, transformations versus actions.
- Partitions, narrow versus wide transformations, and the shuffle.
- Joins: broadcast joins when one side is small, and handling skewed keys.
- Basic performance tuning. By the end you should be able to explain what happens inside a Spark job when it runs.

**Airflow, with dbt**

- DAG design, scheduling, retries, sensors and alerting.
- Backfills and idempotency: tasks that are safe to run twice.
- In 2026, Airflow and dbt appear together in most modern job descriptions.

**One lakehouse table format, deeply**

- Delta Lake if you lean towards Databricks, Apache Iceberg if you lean towards open source or AWS.
- Learn one format well rather than both superficially.

**Your cloud's data services**

- AWS: S3, Glue, Lambda, Redshift or Athena.
- Azure: ADLS, Data Factory, Synapse, Databricks.

## Skip

- Hadoop and MapReduce internals. Knowing what HDFS is is enough in 2026.
- Scala-first learning. Python covers Indian interviews.

## What to show at the end

One end-to-end project: ingest data, transform it with dbt, orchestrate it with Airflow, and store it as Delta or Iceberg. Along the way, run a PySpark job on 1 GB or more of data and be ready to explain its partitioning.

## Read in the free book

[Data Engineering: From Zero to Production & Interview Ready](https://www.prepnplaced.com/data-engineering-book) (free PDF):

- Chapter 7, *The Cloud, and What You Are Actually Renting*
- Chapter 8, *Pipelines: ETL, ELT and Loading Data Twice*: watermarks, idempotency, MERGE, change data capture, late data and dbt.
- Chapter 9, *Apache Spark*: reading a physical plan, broadcast joins, and fixing skew.
- Chapter 10, *Orchestration with Airflow*

## Practise free on PrepNPlaced

- [Coding Practice](https://www.prepnplaced.com/data-practice): graded PySpark problems.
- [Free Lessons](https://www.prepnplaced.com/open-learning): recorded PySpark, AWS and Azure lessons.
- [Free PDF notes](https://www.prepnplaced.com/prepnplaced-notes): Spark, PySpark, Airflow, dbt, AWS and Azure notes. Downloading takes one Google sign-in.

## Interview questions for this stage

[PySpark](https://www.prepnplaced.com/pyspark-interview-questions) · [Spark](https://www.prepnplaced.com/spark-interview-questions) · [Databricks](https://www.prepnplaced.com/databricks-interview-questions) · [Airflow](https://www.prepnplaced.com/airflow-interview-questions) · [ETL](https://www.prepnplaced.com/etl-interview-questions) · [AWS](https://www.prepnplaced.com/aws-interview-questions) · [AWS Glue](https://www.prepnplaced.com/aws-glue-interview-questions) · [Azure Data Factory](https://www.prepnplaced.com/azure-data-factory-interview-questions) · [GCP](https://www.prepnplaced.com/gcp-data-engineer-interview-questions)

Full guide: [Data Engineering Roadmap 2026](https://www.prepnplaced.com/data-engineering-roadmap-2026), Steps 4 to 6.

---

Previous: [Stage 2: Data modelling and the warehouse](02-data-modelling.md) · Next: [Stage 4: Streaming, data quality and AI-assisted pipelines](04-streaming-and-quality.md)
