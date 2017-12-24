from .database import DataBase
import os
from nprint import nprint

def get_all_schemas(db):
    return db.fetchall("select nspname from pg_catalog.pg_namespace")

def get_all_tables(db, schema):
    #db.execute("SET Search_path to {}".format(schema)).close()
    tables = db.fetchall("SELECT table_name FROM information_schema.tables WHERE table_schema = '{}'".format(schema))
    return tables

def create_directory(name):
    if not os.path.exists(name):
        os.makedirs(name)

def flatten(array):
    return [val[0] for val in array]

def to_db(conn):
    if isinstance(conn, DataBase):
        return conn
    else:
        return DataBase(conn)


def download_table(conn, schema, table, output_folder="output", stdout=False):
    """

    Downloads table by specifying schema and table

    Parameters
    ----------
    conn:
        input connection or psql2csv.DataBase. If it's an input connection, it'll eventually be converted to psql2csv.DataBase class
    schema: str
        name of the schema that the table belongs to
    table: str
        name of the table to download
    output_folder: str, default = "output"
        the name of the folder to place the data
    stdout: boolean, default = False
        whether to print which table is downloading. True = print
    """

    db = to_db(conn)
    cur = db.psql.cursor()
    if stdout:
        nprint(table, level=1)
    with open("{}.csv".format(output_folder + "/" + schema + "/" + table), "w") as f:
        cur.copy_expert("Copy (Select * From {schema}.{table}) To STDOUT With CSV HEADER DELIMITER ','".format(schema=schema, table=table), f)



def download_schema(conn, schema, output_folder="output", stdout=False):
    """

    Downloads schema and its tables by specifying schema

    Parameters
    ----------
    conn:
        input connection or psql2csv.DataBase. If it's an input connection, it'll eventually be converted to psql2csv.DataBase class
    schema: str
        name of the schema to download
    output_folder: str, default = "output"
        the name of the folder to place the data
    stdout: boolean, default = False
        whether to print which schema and table is downloading. True = print
    """

    db = to_db(conn)
    tables = flatten(get_all_tables(db, schema))
    if stdout:
        nprint(schema, level=0)
    for table in tables:
        download_table(db, schema, table, output_folder = output_folder, stdout = stdout)



def download_all(
        conn, 
        output_folder ="output", 
        exclude_schemas = ["pg_toast", "pg_temp_1", "pg_toast_temp_1", "pg_catalog", "public", "information_schema"],
        stdout = False):
    """

    Downloads all schemas and all its tables by specifying schema

    Parameters
    ----------
    conn:
        input connection or psql2csv.DataBase. If it's an input connection, it'll eventually be converted to psql2csv.DataBase class
    output_folder: str, default = "output"
        the name of the folder to place the data
    exclude_schemas: list, default = ["pg_toast", "pg_temp_1", "pg_toast_temp_1", "pg_catalog", "public", "information_schema"]
        Which schemas to exclude while downloading everything
    stdout: boolean, default = False
        whether to print which schema and table is downloading. True = print
    """

    db = to_db(conn)
    create_directory(output_folder)

    schemas = flatten(get_all_schemas(db))
    for schema in [schema for schema in schemas if schema not in exclude_schemas]:
        create_directory(output_folder + "/" + schema)
        download_schema(db, schema, output_folder = output_folder, stdout = stdout)

