import pandas as pd
import decision_tree
import neural_net
import clean_data

#clean_data.transform_data('./data_files/cleaned_data.csv')
batches = []
dtree_var = decision_tree.get_decision_tree_variables('./data_files/mod_cleaned_data.csv')
decision_tree_root = decision_tree.construct_tree(dtree_var, [])

df = pd.read_csv('./data_files/mod_cleaned_data.csv', index_col=0)
network = neural_net.Network([77, 24, 7, 1])
network.gradient_descent(df, 50, decision_tree_root, 100)
