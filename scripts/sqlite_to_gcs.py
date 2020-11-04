#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==============================================================================
# MOVE CSV FILE TO GOOGLE CLOUD STORAGE
# Este script exporta os dados da tabela 'bt_challenge_boa'.
# Em seguida estes dados são levados e gravados no Google Storage no formato
# JSON.
# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 27/10/2020
# ==============================================================================

# TODO: export all data from 'bt_challenge_boa' table
# TODO: move these data to google cloud storage and save it in JSON format

import logging
import logging.handlers
import os
import pandas as pd

from google.cloud import storage
from sqlalchemy import create_engine


class GetRowsAndTransfer:
    """
    Return all rows from 'bt_challenge_boa' table and transfer to
    Google Cloud Storage (GCS)
    """

    def __init__(self):
        self.app_name = "BOA"
        self.path = "/home/lserra/PycharmProjects/challenge_boa"
        self.dbfile = "/db/boa.db"
        self.outpufile = "/data/bt_challenge_boa.csv"

    def log_setup(self):
        """
        Creating a logger object to able logging everything is being executed
        """
        # Logger initialisation
        logger = logging.getLogger(self.app_name)
        logger.setLevel(logging.DEBUG)

        # Creating console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Creating formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )

        # Adding formatter to ch
        ch.setFormatter(formatter)

        # Adding ch to logger
        logger.addHandler(ch)

        # Setting the Logger Level (INFO)
        logger.setLevel(logging.INFO)

        return logger

    def connecting_database(self, logger):
        """Creating and returning the engine with sqlite database"""
        try:
            logger.info("Connecting to the database . . .")
            engine = create_engine(
                'sqlite:///{}{}'.format(self.path, self.dbfile),
                echo=False
            )
            return engine
        except Exception as error:
            logger.info("Something went wrong!")
            logger.error("Error: {}".format(error))

    def get_rows(self, logger):
        """Get all rows from 'bt_challenge_boa' table"""
        engine = self.connecting_database(logger)

        # Returning all rows from the table using Pandas
        logger.info("Getting rows . . .")
        df = pd.read_sql('bt_challenge_boa', con=engine)

        logger.info("Total Rows: {}".format(str(len(df))))
        logger.info("Saving the CSV file . . .")
        df.to_csv(self.path + self.outpufile, index=False, doublequote=True)

    def upload_files(self, logger):
        """Upload all files to the bucket"""
        logger.info("Uploading all files to GCS . . .")

        source_file_name = self.path + '/data/'
        files = os.listdir(source_file_name)

        # Setting credentials using JSON file
        try:
            storage_client = storage.Client()
            # Getting bucket object
            bucket = storage_client.bucket("my-bigdata-projects")
            if 'bt_challenge_boa.csv' in files:
                # Name of the object to be stored in the bucket
                object_name_in_gcs_bucket = bucket.blob(
                    "data/csv/bt_challenge_boa.csv"
                )
                object_name_in_gcs_bucket.upload_from_filename(
                    source_file_name + 'bt_challenge_boa.csv'
                )
        except Exception as error:
            logger.info("Something went wrong!")
            logger.error("Error: {}".format(error))

        logger.info("Files have been uploaded . . .")

    def run(self):
        """
        Initializing objetcs before to start the process to gather
        all data from 'bt_challenge_boa' table
        """
        # Logging the task
        logger = self.log_setup()
        logger.info("Starting the GetRowsAndTransfer task . . .")

        # Processing the tasks
        self.get_rows(logger)
        self.upload_files(logger)

        logger.info("Process finished successfully . . .")


if __name__ == '__main__':
    GetRowsAndTransfer().run()
