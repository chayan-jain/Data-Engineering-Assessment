import mysql.connector
import logging
from src.utils import conifg

mydb = mysql.connector.connect(
    host=conifg.host,
    user=conifg.user,
    password=conifg.password,
    database=conifg.database
)
mycursor = mydb.cursor()

log = logging.getLogger(__name__)


class sql_dao():

    def table_exists(tableName):
        try:
            mycursor.execute(""" SELECT COUNT(*)
                    FROM information_schema.tables
                    WHERE table_name = '{0}'
                    """.format(tableName.replace('\'', '\'\'')))
            if mycursor.fetchone()[0] == 1:
                mycursor.close()
                return True
            mycursor.close()
            return False

        except Exception as err:
            log.error(err)

    def create_table(tableName):
        try:
            log.info("Creating Table")
            mycursor.execute(f"CREATE TABLE {tableName} {conifg.table_schema}")

        except Exception as err:
            log.error(err)


