import click
import psycopg2
from psql2csv import download_table
from psql2csv import download_schema
from psql2csv import download_all


@click.command()
@click.option("--dbname", prompt="Database Name", default="postgres", help="The database name")
@click.option("--host", prompt="host", help="URL Endpoint of the database")
@click.option("--user", prompt="User", help="Login username")
@click.option("--password", prompt="Password", hide_input=True, help="Login password")
@click.option('--all', 'download_type', flag_value='all', default=True, help="Downloads everything")
@click.option('--schema', 'download_type', flag_value='schema', help="Downloads a schema")
@click.option('--table', 'download_type', flag_value='table', help="Downloads a table")
@click.option('--stdout', is_flag=True, help="Whether to print which schema and table is downloading")
def main(dbname, host, user, password, download_type, stdout):
    conn = psycopg2.connect("dbname='{dbname}' user='{user}' host='{host}' password='{password}'".format(dbname = dbname, user = user, host = host, password = password))
    if download_type == "all":
        download_all(conn, stdout = stdout)
    elif download_type == "schema":
        schema_name = click.prompt("Schema name: ", type=str)
        download_schema(conn, schema_name, stdout = stdout)
    elif download_type == "table":
        schema_name = click.prompt("Schema name: ", type=str)
        table_name = click.prompt("Table name: ", type=str)
        download_schema(conn, schema_name, table_name, stdout = stdout)

if __name__ == "__main__":
    main()
