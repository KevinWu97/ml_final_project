import pandas as pd
# import csv


def convert_to_csv(file_path):
    data_frame = pd.read_table(file_path, encoding='ISO-8859-1')
    data_frame.to_csv('./data_files/cleaned_data.csv')
    return


convert_to_csv('./data_files/Tab.delimited.Cleaned.dataset.WITH.variable.labels.dat')
