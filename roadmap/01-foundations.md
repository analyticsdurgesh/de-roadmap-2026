# Stage 1: Foundations (months 1 to 3)

SQL, Python and one cloud. Every data engineering interview in India starts with SQL, so SQL comes first and gets the most time. Python comes alongside it, for data work. Pick your cloud now so the rest of the roadmap builds on one stack.

## What to learn

**SQL, to an advanced level**

- Joins and their edge cases, GROUP BY and HAVING, CTEs, date logic.
- Window functions: ROW_NUMBER, RANK, LAG and LEAD, running totals.
- Indexing basics and reading an EXPLAIN plan.
- Aim for 100 or more solved problems, including window functions, and reach advanced SQL by month 2.

**Python for data work**

- Reading and writing files (CSV, JSON, Parquet), calling APIs with `requests`, and pandas.
- Error handling, logging, virtual environments, and small, clean functions.

**One cloud, not three**

- AWS or Azure covers most Indian postings. Azure is especially common at services companies and GCCs; AWS leads at product startups.
- In this stage you only need enough of it to run your script on a cloud VM. Its data services come in [stage 3](03-spark-airflow-lakehouse.md).

## Skip

- Web frameworks such as Django, and full-stack development.
- Heavy DSA grinding. Data engineering interviews weight SQL far more. If you target product companies, 50 to 70 easy and medium problems later on is enough.
- "SQL in 24 hours" shortcuts.

## What to show at the end

A Python script, written without a tutorial, that pulls data from an API and loads it into Postgres on a cloud VM, with logging and error handling.

## Read in the free book

[Data Engineering: From Zero to Production & Interview Ready](https://www.prepnplaced.com/data-engineering-book) (free PDF):

- Lecture Zero, *Living in the Terminal*
- Chapter 1, *What a Data Engineer Actually Does*
- Chapter 2, *The Machine Underneath*
- Chapter 3, *SQL to Interview Level*
- Chapter 4, *Python for Data Engineers*

## Practise free on PrepNPlaced

- [Coding Practice](https://www.prepnplaced.com/data-practice): graded SQL and Python problems.
- [Free Lessons](https://www.prepnplaced.com/open-learning): recorded videos on SQL and Python.
- [Free PDF notes](https://www.prepnplaced.com/prepnplaced-notes): SQL notes for revision. Downloading takes one Google sign-in.

## Interview questions for this stage

[SQL](https://www.prepnplaced.com/sql-interview-questions) · [Python](https://www.prepnplaced.com/python-interview-questions) · [pandas](https://www.prepnplaced.com/pandas-interview-questions)

Full guide: [How to Become a Data Engineer in India](https://www.prepnplaced.com/how-to-become-data-engineer-india), Step 1.

---

Next: [Stage 2: Data modelling and the warehouse](02-data-modelling.md)
