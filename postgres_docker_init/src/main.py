from db_manager import start_postgres_connection, query_database

conn = start_postgres_connection()
query = """
    SELECT *
    FROM ecs.tesla
    limit 1;
"""

result = query_database(connection=conn, query_str=query)

print(result)
