# Stage 4: Streaming, data quality and AI-assisted pipelines (months 8 to 10)

This stage extends the project you built in stage 3. You add a streaming feed and quality gates in front of the tables it publishes, and you learn to review AI-generated code before you use it.

## What to learn

**Kafka and one streaming processor**

- Kafka fundamentals: topics, partitions and consumer groups.
- Spark Structured Streaming on one real data feed. It is the practical choice for Indian roles.
- Batch versus streaming trade-offs, including when not to stream at all.
- For fresher roles, Kafka at concept level is enough. Fresher roles rarely ask for production Kafka experience.

**Data quality**

- Quality gates wired into the pipeline: dbt tests or Great Expectations.
- Check the data a pipeline publishes as well as whether the job ran. A pipeline can succeed and still publish wrong numbers.

**AI-assisted pipelines**

- Use AI assistants to scaffold pipelines, and own the review: data-quality checks, idempotency and cost.
- Interviewers increasingly ask how you validate generated code. Practise reviewing and fixing AI-generated SQL and PySpark, and keep examples from your own project.

**Cost**

- Write down your cost decisions, such as cluster sizing and storage tiers, in the project README.

## What to show at the end

The stage 3 project with a Kafka streaming feed and data-quality tests added, and a README that records your design and cost decisions.

## Read in the free book

[Data Engineering: From Zero to Production & Interview Ready](https://www.prepnplaced.com/data-engineering-book) (free PDF):

- Chapter 11, *Streaming and Kafka*: partitions and keys, consumer lag, delivery semantics, event time against processing time, and when not to stream.
- Chapter 12, *When Pipelines Lie*: monitor the data, not the job; data contracts; a debugging framework.

## Practise free on PrepNPlaced

- [Free PDF notes](https://www.prepnplaced.com/prepnplaced-notes): Kafka and system design notes. Downloading takes one Google sign-in.

## Interview questions for this stage

[Kafka](https://www.prepnplaced.com/kafka-interview-questions) · [ETL and data quality](https://www.prepnplaced.com/etl-interview-questions) · [Databricks and streaming](https://www.prepnplaced.com/databricks-interview-questions) · [System design](https://www.prepnplaced.com/system-design-interview-questions)

Full guide: [Data Engineering Roadmap 2026](https://www.prepnplaced.com/data-engineering-roadmap-2026), Steps 7 and 8.

---

Previous: [Stage 3: Spark, Airflow and the lakehouse](03-spark-airflow-lakehouse.md) · Next: [Stage 5: Projects, resume and interviews](05-projects-and-interviews.md)
