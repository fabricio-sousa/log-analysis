# Udacity Full Stack Web Developer Nanodegree | Log Analysis Project

### Developer: Fabricio Sousa

## Description

This project includes a python API-DB call. The filename is called `newsdata.py`
`newsdata.py` queries a psql database and outputs the answer to the following 3 questions regarding its data:

* QUESTION 1: What are the most popular three articles of all time?
* QUESTION 2: Who are the most popular article authors of all time?
* QUESTION 3: On which days did more than 1 percent of requests lead to errors?

## Frameworks, Libraries, and APIs

Python 2.7, PostgreSQL.

## Program Design

`newdata.py` contains 3 function definitions. Each function comprises of a query to the psql database in order to answer the questions.

`question1()` answers QUESTION  1 via the SQL query:
```
SELECT title, count(slug)
AS views
FROM articles LEFT JOIN log
ON log.path like concat('%', articles.slug)
GROUP BY title
ORDER BY views DESC
LIMIT 3;
```

`question2()` answers QUESTION 2 via the SQL query:
```
SELECT name, sum(views) AS views
FROM table3
GROUP BY name
ORDER BY views DESC;
```
`question3()` answers QUESTION 3 via the SQL query:
```
SELECT date, substr(percent_errors::text,1,3) AS errors
FROM percent;
```

## Installation and How To Run

To run the program, you'll need database software (provided by a Linux virtual machine) and the data to analyze. You will need to install the virtual machine and download the data as DESCribed in the class [notes](https://classroom.udacity.com/nanodegrees/nd000/parts/b910112d-b5c0-4bfe-adca-6425b137ed12/modules/a3a0987f-fc76-4d14-a759-b2652d06ab2b/lessons/0aa64f0e-30be-455e-a30d-4cae963f75ea/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91).

Once you have the virtual machine loaded, please load the database by using the command `psql news`.

`newdata.py` requires 6 views created in the psql database. The create code for the 6 views are as follows:

##### View 1

This view creates table1 which includes the authors' names and the articles they've written.
```
CREATE VIEW table1 AS
(SELECT authors.name, articles.title
FROM authors join articles on authors.id = articles.author
ORDER BY authors.name);
```

##### View 2

This view creates table2 which includes the article title and the total slug count for each articles FROM joining the articles and log tables.
```
CREATE VIEW table2 AS
(SELECT title, count(slug) AS views
FROM articles LEFT JOIN log on log.path like concat('%', articles.slug)
GROUP BY title
ORDER BY views DESC);
```

##### View 3

This view creates table3 which includes the authors' name FROM table1, the articles' name FROM table2 and the slug(views) count.
```
CREATE VIEW table3 AS
(SELECT table1.name, table2.title, views
FROM table1 join table2
ON table1.title = table2.title
ORDER BY table1.name);
```

##### View 4

This view creates the table status which includes the date and total status count FROM the database.
```
CREATE VIEW status as
(SELECT date(time), count(*) AS total
FROM log GROUP BY date(time));
```

##### View 5

This view creates the table error which includes the date and total error status count FROM the database.
```
CREATE VIEW errors as
(SELECT date(time), count(*) as total
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY date(time));
```

##### View 6

This view answers question 3 by creating a table percent which includes the date and the percent operation using the total errors FROM the erros table and the total status FROM the status table. The SELECT query in the actual source code simply formats this view to display a shorter result for percent errors.

```
CREATE VIEW percent as
(SELECT status.date, (errors.total::float/status.total*100) AS percent_errors
FROM status INNER JOIN errors
ON status.date = errors.date
WHERE (errors.total::float/status.total*100)::int > 1);
```

Once the views are created, please navigate to `\vagrant\newsdata` and run the API-DB call via command: `python newsdata.py`

The code will then display each question followed by the answer.