import psycopg2

def connect():
    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="localhost",
        port="5435",
        database="midb")

    return connection

def disconnect(connection):
    if (connection):
        connection.close()
