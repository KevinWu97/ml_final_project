import numpy as np
import scipy as sc
import pandas as pd
import math


def get_decision_tree_variables(file_path):
    df = pd.read_csv(file_path, index_col=0)
    decision_tree_variables_df = df[['referrer', 'expgender', 'exprace', 'exprunafter', 'compensation', 'recruitment',
                                     'separatedornot', 'sunkgroup', 'gainlossgroup', 'gainlossDV', 'anch1group',
                                     'anch2group', 'anch3group', 'anch4group', 'gambfalgroup', 'scalesgroup',
                                     'reciprocitygroup', 'allowedforbiddenGroup', 'quoteGroup', 'flagfilter',
                                     'flagGroup', 'MoneyGroup', 'moneyfilter', 'ContactGroup', 'IATfilter',
                                     'citizenship', 'IATEXPfilter', 'nativelang', 'ethnicity', 'race', 'politicalid']]
    return decision_tree_variables_df


'''Nevermind, use linear regression on neural net variables'''
def linear_regression_pruning(decision_tree_dataframe):

    return


dtree_var = get_decision_tree_variables('./data_files/mod_cleaned_data.csv')
print(dtree_var)


