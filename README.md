# sql-project-star-wars-analysis


## PostgreSQL Version

This folder is focus on doing this project based on PostgreSQL.

### 0. Preparation

1. Understanding PostgreSQL
- In my initial role working on the ads database (which utilized MySQL), I collaborated closely with the system architect to manage metadata. During this period, I explored books such as "High Performance MySQL," "Learning Architecture from Scratch," and "Database System Concepts", as well as online resources to enhance my understanding for  (although I didn't go through all of them completely). This experience provided me with a general grasp of database, like Normal Form.
- Upon achieving the first version using sqlite3, along with noticing a trending preference for PostgreSQL in the tech industry, I chose to enroll in a brief introductory course to familiarize myself with PostgreSQL's functionality.
- 
2. Exploring similar public projects

One project I found is from Udacity Data Engineering Nanodegree, which contains building a simple ETL pipleline to fetch data and store them in a PostgreSQL database. 

Following is a breakdown of thie project. 
- `request.py`: Contains Class `request` to fetch data from the API. 
- `queries.py`: Contains SQL statements for creating schemas, tables and inserting data.
    - Insert SQL: Overwrites the value if there are conflicts in the same businees_id.
- `businesssearch.py`: Parses requests into the desired format.
- `databasedriver.py`: Connects to databases and store them into the databases
- `auth.py`: Configurations.
- `driver.py `: Allows users to interact with the program using command lines.

Takeaways:
- Request: Only load the data when the response code is 200;
- Queries: 


## Sqlite3 Version

Key Takeaways:
1. d
2. 