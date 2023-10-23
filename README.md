# sql-project-star-wars-analysis


## PostgreSQL Version

Knowing the restrictions about Sqlite3, this folder is focus on doing this project based on PostgreSQL.

### 0. Preparation

1. 
2. Go through similar public projects

The one I found is a project from Udacity Data Engineering Nanodegree, which builds a simple ETL pipleline to fetch data and store them in a postgresql database. 

Following is a breakdown of thie project. 
- `request.py`: Contains Class `request` to get the data from the API. 
- `queries.py`: Contains SQL statements creating schemas, tables and inserting data.
    - Insert SQL: Overwrites the value if there are conflicts in the same businees_id.
- 

Takeaways:
- Request: Only load the data when the response code is 200;
- Queries: 



## Sqlite3 Version