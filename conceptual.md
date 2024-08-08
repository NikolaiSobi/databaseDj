### Conceptual Exercise

Answer the following questions below:

 What is PostgreSQL? <!--- Relational database management system.

- What is the difference between SQL and PostgreSQL? <!---SQL is a query language. PSQL is a relational database management system that uses SQL.

- In `psql`, how do you connect to a database? <!--- \c "db name"

- What is the difference between `HAVING` and `WHERE`? <!--- Having is like where except it filters by the results of aggregates.
"
- What is the difference between an `INNER` and `OUTER` join? <!--- Inner join gets matched rows. Outer join gets matched rows from one table and then every row in the other table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join? <!--- Left outer join returns everything from the left table and the matched records from the right table. Right outer join is the opposite.

- What is an ORM? What do they do? <!--- ORM tools are like a middleman between database and oop languages. They let you easily query the database with less lines of code.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`? <!--- Still do not understand this concept.

- What is CSRF? What is the purpose of the CSRF token? <!--- CSRF is a secure random token. The purpose of it is to make sure the user with the code is who they say they are and can access information that is not available to users without the code.

- What is the purpose of `form.hidden_tag()`? <!--- It generates a hidden field that has a token that is used to protect from malicious CSRF attacks.
