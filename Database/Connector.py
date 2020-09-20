import mysql.connector


class Connector:

    @staticmethod
    def mysql_connect(host, user, password, database):
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )