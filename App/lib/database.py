from App.config.conf_database import DB_CONFIG
import mysql.connector


class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=DB_CONFIG["HOST"],
            user=DB_CONFIG["USER"],
            passwd=DB_CONFIG["PASSWORD"],
            database=DB_CONFIG["DATABASE"]
        )
        self.mycur = self.mydb.cursor()

    def command(self, sql_statement):
        self.mycur.execute(sql_statement)

    def getHeader(self):
        return [x[0] for x in self.mycur.description]

    def getResult(self):
        return self.mycur.fetchall()
