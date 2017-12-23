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

def download_table(db, output_folder, schema, table):
    cur = db.psql.cursor()
    with open("{}.csv".format(output_folder + "/" + schema + "/" + table), "w") as f:
        cur.copy_expert("Copy (Select * From {schema}.{table}) To STDOUT With CSV HEADER DELIMITER ','".format(schema=schema, table=table), f)

def download_all(conn, output_folder="output"):
    db = DataBase(conn)
    create_directory(output_folder)

    schemas = flatten(get_all_schemas(db))
    for schema in [schema for schema in schemas if schema not in ["pg_toast", "pg_temp_1", "pg_toast_temp_1", "pg_catalog", "public", "information_schema"]]:
        create_directory(output_folder + "/" + schema)
        nprint(schema, level=0)
        tables = flatten(get_all_tables(db, schema))
        for table in tables:
            nprint(table, level=1)
            download_table(db, output_folder, schema, table)
