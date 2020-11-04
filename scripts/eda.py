#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==============================================================================
# EDA - EXPLORATORY DATA ANALYSIS
# Esta é uma técnica muito usada por data scientists para analisar rapidamente
# os dados que estão e entender como estão distribuídos, a sua cardinalidade,
# a densidade, como se relacionam e correlacionam.
# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 27/10/2020
# ==============================================================================

# TODO: identificar todos os arquivos CSV que estão na pasta '/data'
# TODO: percorrer a lista com os arquivos
# TODO: verificar se o arquivo possui extensão CSV
# TODO: carregar cada arquivo CSV para um dataframe
# TODO: criar o relatório de profiling para cada arquivo CSV
# TODO: exportar o relatório de profiling de cada arquivo CSV, para a pasta
#  '/analysis'

# Defining the libraries
import os
import pandas as pd
import pandas_profiling as pp

# Defining parameters
path = '/home/lserra/PycharmProjects/challenge_boa'


def data_profiling(list_files):
    """Data profiling for each CSV file found in the directory"""

    inputfile = path + "/data/"
    outputfile = path + "/analysis/"

    for filename in list_files:
        name, ext = os.path.splitext(filename)
        if ext != '.csv':
            print(">> WARNING: CSV file invalid!")
            return False

        # Creating pandas dataframe
        df = pd.read_csv(inputfile + filename, sep=',', header=0)

        # Data profiling for each CSV file
        print("-".rjust(60, "-"))
        print(f'>> Generating Profile Report: {filename}')
        profile = pp.ProfileReport(df)

        # Printing the results to html
        print(f'>> Exporting Profile Report to HTML: {filename}')
        print("-".rjust(60, "-"))
        profile.to_file(output_file=outputfile + name + '.html')

    return True


if __name__ == "__main__":
    files = os.listdir(path + "/data")
    if data_profiling(files):
        print("\n>> Process finished successfully!")
    else:
        print("\n>> Something wrong with the system!")
