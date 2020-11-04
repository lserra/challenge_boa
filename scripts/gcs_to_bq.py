#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==============================================================================
# LOAD CSV FILE IN GOOGLE CLOUD STORAGE TO GOOGLE BIGQUERY
# Este script é uma FUNCTION do Google Cloud que funciona como uma trigger
# que é acionada sempre que o arquivo JSON é atualizado.
# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 27/10/2020
# ==============================================================================

# TODO: criar uma função serveless que é acionada quando um novo arquivo é
#  enviado para o GCS
# TODO: esta função irá transferir os dados de um arquivo CSV localizado em
#  um bucket para dentro do BigQuery


from google.cloud import bigquery


def schema_bt_challenge_boa():
    """Returns the table structure in BQ"""
    return [
        bigquery.SchemaField('tube_assembly_id', 'STRING'),
        bigquery.SchemaField('quantity_component', 'FLOAT'),
        bigquery.SchemaField('component_id', 'STRING'),
        bigquery.SchemaField('component_type_id', 'STRING'),
        bigquery.SchemaField('component_type', 'STRING'),
        bigquery.SchemaField('connection_type_id', 'STRING'),
        bigquery.SchemaField('outside_shape', 'STRING'),
        bigquery.SchemaField('base_type', 'STRING'),
        bigquery.SchemaField('height_over_tube', 'FLOAT'),
        bigquery.SchemaField('bolt_pattern_long', 'FLOAT'),
        bigquery.SchemaField('bolt_pattern_wide', 'FLOAT'),
        bigquery.SchemaField('groove', 'BOOLEAN'),
        bigquery.SchemaField('base_diameter', 'FLOAT'),
        bigquery.SchemaField('shoulder_diameter', 'FLOAT'),
        bigquery.SchemaField('unique_feature', 'BOOLEAN'),
        bigquery.SchemaField('orientation', 'BOOLEAN'),
        bigquery.SchemaField('weight', 'FLOAT'),
        bigquery.SchemaField('supplier', 'STRING'),
        bigquery.SchemaField('quote_date', 'DATE'),
        bigquery.SchemaField('annual_usage', 'INTEGER'),
        bigquery.SchemaField('min_order_quantity', 'INTEGER'),
        bigquery.SchemaField('bracket_pricing', 'BOOLEAN'),
        bigquery.SchemaField('quantity', 'INTEGER'),
        bigquery.SchemaField('cost', 'FLOAT')
        ]


def csv_loader():
    """Function serveless to load all data from GCS to BQ"""
    try:
        table_id = 'sturdy-conduit-260900.de_boa.bt_challenge_boa'

        client = bigquery.Client()

        # Configuring the parameters of the JOB
        job_config = bigquery.LoadJobConfig()
        job_config.schema = schema_bt_challenge_boa()
        job_config.skip_leading_rows = 1
        job_config.source_format = bigquery.SourceFormat.CSV
        job_config.write_disposition = 'WRITE_TRUNCATE'

        # URI for uploaded CSV in GCS
        uri = 'gs://my-bigdata-projects/data/csv/bt_challenge_boa.csv'

        # Making an API request to load all data to the table
        load_job = client.load_table_from_uri(
            uri, table_id, job_config=job_config
        )

        print(">> Function: CSV LOADER GCS TO GBQ")
        print(f">> Storage: {uri}")
        print(f">> Starting Job: {load_job.job_id}")

        load_job.result()   # Waits for table_id load to complete.

        destination_table = client.get_table(table_id)

        print(f">> Total Rows: {destination_table.num_rows}")
        print(">> Job finished successfully!")
    except Exception as error:
        print(">> Something went wrong!")
        print(f"Error: {error}")


if __name__ == '__main__':
    csv_loader()
