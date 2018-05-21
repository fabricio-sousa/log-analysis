# "Database code" for the Log Analysis Project.
# !/usr/bin/env python
import psycopg2

DBNAME = "news"


def question1():
    """
    Input: This function takes in no input.
    Output: This function prints out the answer.
    Behavior: This function contains a Python Database-API query.
    Result of query is presented as a sorted list(
    with the most popular article at the top.
    """
    question = ("\n==> QUESTION 1: What are the most"
                " popular three articles of all time?\n")
    answer = "\nQuerying the database, please wait...\n"
    print question + answer
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT title, count(slug) AS views\
               FROM articles LEFT JOIN log\
               ON log.path LIKE concat('%', articles.slug)\
               GROUP BY title ORDER BY views DESC LIMIT 3;")
    rows = c.fetchall()
    for row in rows:
        print '"' + str(row[0]) + '"' + ', ' + str(row[1]) + ' total views.'
    db.close()


def question2():
    """
    Input: This function takes in no input.
    Output: This function prints out the answer.
    Behavior: This function contains a Python Database-API query.
    Result of query is presented as a sorted list
    with the most popular author at the top.
    """
    question = ("\n==> QUESTION 2:"
                " Who are the most popular article authors of all time?\n")
    answer = "\nQuerying the database, please wait...\n"
    print question + answer
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT name, sum(views) AS views\
              FROM table3 GROUP BY name ORDER BY views DESC;")
    rows = c.fetchall()
    for row in rows:
        print str(row[0]) + ', ' + str(row[1]) + ' total article views.'
    db.close()


def question3():
    """
    Input: This function takes in no input.
    Output: This function prints out the answer.
    Behavior: This function contains a Python Database-API query.
    Result of query presents on which days
    did more than 1 percent of requests lead to errors.
    """
    question = ("\n==> QUESTION 3:"
                " On which days did more than 1 percent"
                " of requests lead to errors?\n")
    answer = "\nQuerying the database, please wait...\n"
    print question + answer
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT date, substr(percent_errors::text,1,3)\
              AS errors FROM percent;")
    rows = c.fetchall()
    for row in rows:
        print 'On ' + str(row[0]) + ', there were ' + str(row[1]) + '% errors.'
    db.close()

question1()
question2()
question3()
