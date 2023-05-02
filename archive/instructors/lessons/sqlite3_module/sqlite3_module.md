
#### [sqlite3: The Python 2 Module](https://docs.python.org/2/library/sqlite3.html)


##### First, an excerpt from the Python 2 docs:
"SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. **It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.**
It provides a SQL interface compliant with the DB-API 2.0 specification described by [PEP 249](http://www.python.org/dev/peps/pep-0249)."

Please add and delete bullet points as needed. Less is more!

0. #### Installation and Class Prep
    1. Installation Instructions:
        1. [Install sqlite](http://www.sqlite.org/quickstart.html)
        2. [sqlite Documentation](http://www.sqlite.org/docs.html)
    2. Class Prep Resources:
        1. [Syntax Diagrams - Very useful!!](https://www.sqlite.org/syntaxdiagrams.html)


- - - - Create a database: [use these schema](https://github.com/PyClass/PyClassLessons/tree/master/lessons/sqlite3_module/examples/db). First build the physics database, then build the sampledb database.
- Write to DB: Run [this](https://github.com/PyClass/PyClassLessons/blob/master/lessons/sqlite3_module/examples/readsample.py) to add some sample entries.
- Read from DB: Inside the sqlite shell, execute `SELECT * FROM OfficeSupplies;` to see all entries.


1. #### Today's deep dive: Lets make a sqlite database from a CSV file.
Avoid getting caught up in the details here, we will have lots of time to explore this later. We will quickly power through writing the schema based on CSV headers, then importing the CSV and writing to sqlite.

    1. So you want to create a sqlite database... - 30 minutes
        1. Schema - This determines what data can go where. A schema describes a table.
        2. Most databases restrict data TYPE by column. Sqlite does NOT, it only uses string types for everything.
    2. Lets create a schema for our dataset, (Mammal Species of the World 3 (MSW3))[http://www.departments.bucknell.edu/biology/resources/msw3/].
        1. First determine our data headers, one for each column. Looks similar to the CSV!
        2. We will do this in a separate file so we can debug and import this table schema. SQL is a programming language and we may need to debug and source control this schema code.



### 2. Working with the sample databases
- An outline of our Python goals: make database connection, write or read entries, commit changes, close connection.
- First lets [read it](https://github.com/PyClass/PyClassLessons/blob/master/lessons/sqlite3_module/examples/readsample.py) into a list of tuples. This is the default data structure returned by sqlite3.
- Now lets [write some data, note that we let the db assign the pkey](https://github.com/PyClass/PyClassLessons/blob/master/lessons/sqlite3_module/examples/writesample.py).
- Most basic uses will be a variation on this.
- A word of caution: sqlite is best for single-user applications.  If you need to allow many users, like with a web app, swap over to Postgres.
- You can convert to Postgres, and TONS of your knowledge is transferrable, so just use sqlite3 for now and that knowledge will transfer!
-WHY SQLITE??

2. #### First Point
    1. Replace with An Explanation - XX minutes
        1. 
        2. 
        3. See: [example_file.py](example_file.py)
    2. Second Part
        1. 
        2. 
        3. See: [example_file.py](example_file.py)
    3. Third Part
        1. 
        2. 
        3. See: [example_file.py](example_file.py)

3. #### Organizing or ('munging')[http://en.wikipedia.org/wiki/Mung_%28computer_term%29] data.
    1. Data will often need reorganized. - 30 minutes
        1. Key Point: A particular organizational model for a given dataset can be called a 'view' of that data. A single dataset can have many views.
        3. It's possible that you are only interested in a certain subset of data and could remove irrelevant columns. If you have worked in excel, you have seen data in a specific view.
        2.  You could filter by category such as with population data, or you could filter based on range, for example price ranges of store items.
    2. So how do we get our sql format into a form we actually want?
        1. SQL Tables are a collection of 1 dimensional columns.  The columns have a 'name' or 'header'.  Each row of the table represents a data point for that table.
        2. DB->COLUMNS->ROWS->ENTRIES || A database is an arbitrary collection of tables, which is a collection of rows, which is a collection of points.
        3. Important: In a given row of a table, each column MUST have a value, even if it has no data. The sqlite equivalent of NaN, null, or NA is `null`.
    3. Data Organization Philosophy
        1. A single datum should only exist in ONE place. That isn't to say that multiple things couldn't have the same datum
        2. Don't create views before you know what you need.
        3. If things belong together, put them together. If they don't, create a new table or even a new database.
        4. Most of the time a Python `list()` or `dict()` will serve as an excellent representation of your data.


4. #### Extended Resources - An overview of sqlite technologies
    1. [What's SQL?](http://en.wikipedia.org/wiki/SQL) - "SQL (Structured Query Language) is a special-purpose programming language designed for managing data held in a relational database management system (RDBMS), or for stream processing in a relational data stream management system (RDSMS).
    2. [RDBMS](http://en.wikipedia.org/wiki/Relational_database_management_system) - "A relational database management system (RDBMS) is a database management system (DBMS) that is based on the relational model."

    3. [DBMS](http://en.wikipedia.org/wiki/Database) - Database management systems (DBMSs) are computer software applications that interact with the user, other applications, and the database itself to capture and analyze data. A general-purpose DBMS is designed to allow the definition, creation, querying, update, and administration of databases.
    4. [Relational Model](http://en.wikipedia.org/wiki/Relational_model) - Most relational databases use the SQL data definition and query language; these systems implement what can be regarded as an engineering approximation to the relational model. A table in an SQL database schema corresponds to a predicate variable; the contents of a table to a relation; key constraints, other constraints, and SQL queries correspond to predicates. However, SQL databases deviate from the relational model in many details, and Codd fiercely argued against deviations that compromise the original principles.


### TODO: DELETE WHEN COMPLETE
  - Links below go to proper examples in folder.
  - Discuss autocommmit, manual commit, buffered? commits (with example)
  - Creating functions in queries: https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.create_function
  - Everything after functions: aggregates, collations, row factories, text factories, row objects, and the rest of that section.
  - Try to remove this from the code: explain why you have to specify str. That still isn't clear to me... 
  - row.keys() <-- get keys/headers for table
  - SQLite and Python Types: https://docs.python.org/2/library/sqlite3.html#introduction
  - Dealing with Date: https://docs.python.org/2/library/sqlite3.html#default-adapters-and-converters
  - 
