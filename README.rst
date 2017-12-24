psql2csv
========

A library and a CLI to download PostgreSQL schemas and tables

Installation
------------

.. code:: bash

    pip3 install psql2csv

Usage
-----

CLI
~~~

API
~~~

There are 3 runnable functions: \* download_all \* download_schema \*
download_table

download_all
^^^^^^^^^^^^

**download_all**\ (conn, output_folder=‘output’,
exclude_schemas=[‘pg_toast’, ‘pg_temp_1’, ‘pg_toast_temp_1’,
‘pg_catalog’, ‘public’, ‘information_schema’], stdout=False)

Downloads all schemas and all its tables by specifying schema

-  conn: input connection or psql2csv.DataBase. If it’s an input
   connection, it’ll eventually be converted to psql2csv.DataBase class
-  output_folder: the name of the folder to place the data
-  exclude_schemas: Which schemas to exclude while downloading
   everything
-  stdout: whether to print which schema and table is downloading. True
   = print

download_schema
^^^^^^^^^^^^^^^

**download_schema**\ (conn, schema, output_folder=‘output’,
stdout=False)

Downloads schema and its tables by specifying schema

-  conn: input connection or psql2csv.DataBase. If it’s an input
   connection, it’ll eventually be converted to psql2csv.DataBase class
-  schema: name of the schema to download
-  output_folder: the name of the folder to place the data
-  stdout: whether to print which schema and table is downloading. True
   = print

download_table
^^^^^^^^^^^^^^

**download_table**\ (conn, schema, table, output_folder=‘output’,
stdout=False)

Downloads table by specifying schema and table

-  conn: input connection or psql2csv.DataBase. If it’s an input
   connection, it’ll eventually be converted to psql2csv.DataBase class
-  schema: name of the schema that the table belongs to
-  table: name of the table to download
-  output_folder: the name of the folder to place the data
-  stdout: whether to print which table is downloading. True = print

Versions
--------
