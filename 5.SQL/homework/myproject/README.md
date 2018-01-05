# Purpose

CS50 pset7 homework : app to work with database and SQL.  
Written with python, flask, jinja, html, css.

# Functionalities

- user can login or register
- passwords are stored hashed in database
- each user's input is controled (prevent SQL injection)
- user can view a summary of it's portfolio (default view)
- user can check for stocks value (quote)
- user can buy or sell stocks
- user can view an entire history of all purchases/sell

Datas are updated on each login, then the actual prices are stored in the user database.
Update is really slow...

# TODO

1. Add a refresh button in layout.html to refresh on users demand.
1. Implement update on login, then store actual prices in sql database (change current database)
1. Use of sql database for all other pages, sell in particular.
