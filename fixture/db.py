__author__ = '1'
import mysql.connector

class DbFixture:

    def __init__(self, host, user, name, password):
        self.host = host
        self.user = user
        self.name = name
        self.password = password
        self.connection = mysql.connector.connect(host = host, database = name, user = user, password = password)

    def destroy(self):
        self.connection.close()