# Terminology

# Database - contains many tables
# Relation (or table) - contains tuples and attributes
# Tuple (or row) - a set of fields that generally represents an 'object' like a person or a music track
# Attribute (also column or field) - one of possibly many elements of data corresponding to the object represented
# by the row.

# SQL (Structured Query Language)
# SQL is the language we use to issue commands to the database, it has 4 powerful functions:
# create a table, retrieve some data, update data and delete data (CRUD).

# 一开始我们的code会直接与database进行交流，但由于database的复杂性，我们发明了database application (有时我们称它为API：application
# programming interface），我们的code会与database application先交流，而这个交流用的code就是SQL。


# Two Roles in Large Projects
# Application Developer - Builds the logic for the application, solves the problems of application
# Database Administrator - Monitors and adjusts the database as the program runs in production

# Database Model
# A database model or database schema is the contract, structure or format of a database, described in a formal language
# supported by the database management system. In other words, a 'database model' is the application of a data model
# when used in conjunction with a database management system.


# CREATE TABLE Users(
#   name VARCHAR(128),
#	email VARCHAR(128)
# )