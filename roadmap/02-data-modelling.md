# Stage 2: Data modelling and the warehouse (months 4 to 7)

Learn how to shape data before you learn the tools that move it at scale. Warehousing knowledge is what separates a data engineer candidate from a general Python programmer.

On the 2026 plan this stage shares months 4 to 7 with [stage 3](03-spark-airflow-lakehouse.md): you model the data in a warehouse with dbt while you learn Spark and Airflow.

## What to learn

**Dimensional modelling**

- Declare the grain first, then design the fact and dimension tables.
- Star schemas, and when a snowflake schema makes sense instead.
- Surrogate keys versus natural keys.
- Slowly changing dimensions: Type 1 and Type 2.

**How warehouses store data**

- OLTP versus OLAP. Interviewers reliably probe this distinction.
- Columnar storage, partitioning and clustering.
- Why Parquet beats CSV for analytics, and the small-files problem.

**dbt**

- Models, tests and documentation.
- dbt has moved from nice-to-have to expected for transformation work.

## Hands-on

Pick one cloud warehouse with a free tier, such as the BigQuery sandbox or a Snowflake trial. Take a public dataset, for example e-commerce orders, and rebuild it as a clean star schema there. Build the models in dbt, with tests and docs.

## What to show at the end

One star-schema model built in a cloud warehouse free tier, with dbt models, tests and documentation.

## Read in the free book

[Data Engineering: From Zero to Production & Interview Ready](https://www.prepnplaced.com/data-engineering-book) (free PDF):

- Chapter 5, *Data Modeling*: grain, star schemas, surrogate keys, and the slowly changing dimension decision.
- Chapter 6, *Where Data Lives*: CSV against Parquet, measured; partitioning; the small-files problem; what Delta and Iceberg add.

## Practise free on PrepNPlaced

- [Free Lessons](https://www.prepnplaced.com/open-learning): recorded Snowflake lessons.
- [Free PDF notes](https://www.prepnplaced.com/prepnplaced-notes): Snowflake, dbt and warehousing notes. Downloading takes one Google sign-in.

## Interview questions for this stage

[Data modelling](https://www.prepnplaced.com/data-modeling-interview-questions) · [Data warehouse](https://www.prepnplaced.com/data-warehouse-interview-questions) · [dbt](https://www.prepnplaced.com/dbt-interview-questions) · [Snowflake](https://www.prepnplaced.com/snowflake-interview-questions) · [BigQuery](https://www.prepnplaced.com/bigquery-interview-questions) · [Redshift](https://www.prepnplaced.com/redshift-interview-questions)

Full guide: [How to Become a Data Engineer in India](https://www.prepnplaced.com/how-to-become-data-engineer-india), Step 2.

---

Previous: [Stage 1: Foundations](01-foundations.md) · Next: [Stage 3: Spark, Airflow and the lakehouse](03-spark-airflow-lakehouse.md)
