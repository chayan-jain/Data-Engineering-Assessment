import os
import logging

import pandas as pd

from src.dao.sql_dao import sql_dao

log = logging.getLogger(__name__)

def read_data():
    try:
        log.info("Reading Data")
        Homedir = os.path.dirname(os.path.realpath(__file__))
        filePath = os.path.join(Homedir, r"inputs/details.txt")

        details_df = pd.read_csv(filePath, sep="|")
        details_df.drop('Unnamed: 0', inplace=True, axis=1)

        log.info("Data has been readed in dataframe successfully")
        return details_df

    except Exception as err:
        log.error(err)

def create_tables(df):
    try:
        log.info("Inserting Data")
        for index,row in df.iterrows():
            country = row["Country"]
            tableName = "Table_"+country

            # Check for existence of table for this country
            if not sql_dao.table_exists(tableName):
                # If not exists, create new table
                sql_dao.create_table(tableName)

            ## We can call insert data function
        log.info("Records Inserted Successfully")

    except Exception as err:
        log.info("Error during inserting data")
        log.error(err)

def run():
    try:
        # Moderating Function
        details_df = read_data()
        create_tables(details_df)

    except Exception as err:
        log.info("Error during inserting data")
        log.error(err)
