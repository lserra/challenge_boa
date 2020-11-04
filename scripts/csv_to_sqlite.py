#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==============================================================================
# LOAD CSV TO SQLITE (DEPRECATED)
# Esta atividade não faz mais sentido.
# Mas, como eu já havia criado então eu irei manter aqui para análise.
# É somente um passo a mais que não irá atrapalhar em nada no processo/fluxo
# sugerido. Mas, que poderia facilmente ser eliminado.
# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 27/10/2020
# ==============================================================================

# TODO: create the engine to connect to SQLite using SQLAlchemy
# TODO: load the data from csv files to stage area in sqlite database
# TODO: create the big table from stage area tables

# Defining the libraries
import os
import pandas as pd
import sys

from sqlalchemy import create_engine

# Defining parameters
path = '/home/lserra/PycharmProjects/challenge_boa'
inputfile = "/data/"
dbfile = "/db/boa.db"


def connecting_database():
    """Creating and returning the engine with sqlite database"""
    try:
        engine = create_engine(
            'sqlite:///{}{}'.format(path, dbfile),
            echo=False
        )
        return engine
    except Exception as error:
        print(">> Something wrong with the system!")
        print(f">> Error: {error}")


def sql_create_big_table():
    """Retunrs the SQL command to create the table into the database"""
    return """
    SELECT
        m.tube_assembly_id as 'tube_assembly_id'
        , m.quantity_1 as 'quantity_component'
        , c.component_id      
        , c.component_type_id 
        , c.type as component_type             
        , c.connection_type_id
        , c.outside_shape
        , c.base_type
        , c.height_over_tube
        , c.bolt_pattern_long
        , c.bolt_pattern_wide
        , c.groove
        , c.base_diameter
        , c.shoulder_diameter
        , c.unique_feature
        , c.orientation
        , c.weight
        , p.supplier
        , p.quote_date
        , p.annual_usage
        , p.min_order_quantity
        , p.bracket_pricing
        , p.quantity
        , p.cost
    FROM
        stg_bill_of_materials m INNER JOIN stg_comp_boss c
        ON m.component_id_1 = c.component_id
        
        INNER JOIN stg_price_quote p
        ON m.tube_assembly_id = p.tube_assembly_id
    """


def loading_data_to_sqlite(list_files):
    """Saving all the data into the sqlite database"""
    engine = connecting_database()
    if engine is None:
        return False

    print()
    print("-".rjust(60, "-"))
    print("Loading data".center(60))
    print("-".rjust(60, "-"))

    for filename in list_files:
        name, ext = os.path.splitext(filename)
        if ext != '.csv':
            print(">> WARNING: CSV file invalid!")
            return False

        print(f">> Populating the table: stg_{name}")
        df = pd.read_csv(path + inputfile + filename, sep=',', header=0)
        df.to_sql(f"stg_{name}", con=engine, index=False, if_exists='replace')
        print("-".rjust(60, "-"))

    return True


def creating_big_table():
    """
    Creating the big table
    After this table will be moved to Google Cloud Storage
    """
    engine = connecting_database()
    if engine is None:
        return False

    sql = sql_create_big_table()
    engine = connecting_database()
    print(">> Creating the table: bt_challenge_boa")
    df = pd.read_sql(sql=sql, con=engine)
    df.to_sql("bt_challenge_boa", con=engine, index=False, if_exists='replace')

    return True


def execute(list_files):
    """Execute all process"""
    result = loading_data_to_sqlite(list_files=list_files)
    if not result:
        print("\n>> Something went wrong!")
        sys.exit(1)

    result = creating_big_table()
    if not result:
        print("\n>> Something went wrong!")
        sys.exit(1)

    print("\n>> Process finished successfully!")


if __name__ == "__main__":
    files = os.listdir(path + inputfile)
    execute(files)
