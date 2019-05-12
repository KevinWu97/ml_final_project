import pandas as pd
import random as rd
import decision_tree
import neural_net
import clean_data
import numpy as np

#clean_data.transform_data('./data_files/cleaned_data.csv')
batches = []
dtree_var = decision_tree.get_decision_tree_variables('./data_files/mod_cleaned_data.csv')
decision_tree_root = decision_tree.construct_tree(dtree_var, [])

df = pd.read_csv('./data_files/mod_cleaned_data.csv', index_col=0)
network = neural_net.Network([77, 24, 7, 1])
network.gradient_descent(df, 500, decision_tree_root, 1)

df_sample = df.sample(n=100)
y_values = np.array(df_sample[['politicalid']].copy().values.astype(np.float).tolist())
batch = df_sample[['age', 'sex', 'anchoring1', 'anchoring2', 'anchoring3', 'anchoring4', 'reciprocityus',
               'reciprocityother', 'allowedforbidden', 'quote', 'totalflagestimations',
               'totalnoflagtimeestimations', 'IATexpart', \
               'IATexpmath', 'IATexp.overall', 'totexpmissed', 'artwarm', 'diseaseframinga',
               'diseaseframingb', 'flagdv1', 'flagdv2', 'flagdv3', 'flagdv4', 'flagdv5', 'flagdv6',
               'flagdv7', \
               'flagdv8', 'flagsupplement1', 'flagsupplement2', 'flagsupplement3', 'flagtimeestimate1',
               'flagtimeestimate2', 'flagtimeestimate3', 'flagtimeestimate4', 'gamblerfallacya', \
               'gamblerfallacyb', 'iatexplicitart1', 'iatexplicitart2', 'iatexplicitart3',
               'iatexplicitart4', 'iatexplicitart5', 'iatexplicitart6', 'iatexplicitmath1',
               'iatexplicitmath2', \
               'iatexplicitmath3', 'iatexplicitmath4', 'iatexplicitmath5', 'iatexplicitmath6',
               'imaginedexplicit1', 'imaginedexplicit2', 'imaginedexplicit3', 'imaginedexplicit4', 'major',
               'mathwarm', 'moneyagea', \
               'moneyageb', 'moneygendera', 'moneygenderb', 'noflagtimeestimate1', 'noflagtimeestimate2',
               'noflagtimeestimate3', 'noflagtimeestimate4', 'omdimc3', 'quotea', 'quoteb', \
               'scalesa', 'scalesb', 'sunkcosta', 'sunkcostb', 'sysjust1', 'sysjust2', 'sysjust3',
               'sysjust4', 'sysjust5', 'sysjust6', 'sysjust7', 'sysjust8']].copy()
batch = np.array(batch.values.astype(np.float).tolist())
for x, y in zip(batch, y_values):
    prediction = network.predict(np.array([[x_val] for x_val in x]))
    print(f"calculated y value - {prediction} actual y value - {y}")
    
y_values = np.array(df[['politicalid']].copy().values.astype(np.float).tolist())
batch = df[['age', 'sex', 'anchoring1', 'anchoring2', 'anchoring3', 'anchoring4', 'reciprocityus',
               'reciprocityother', 'allowedforbidden', 'quote', 'totalflagestimations',
               'totalnoflagtimeestimations', 'IATexpart', \
               'IATexpmath', 'IATexp.overall', 'totexpmissed', 'artwarm', 'diseaseframinga',
               'diseaseframingb', 'flagdv1', 'flagdv2', 'flagdv3', 'flagdv4', 'flagdv5', 'flagdv6',
               'flagdv7', \
               'flagdv8', 'flagsupplement1', 'flagsupplement2', 'flagsupplement3', 'flagtimeestimate1',
               'flagtimeestimate2', 'flagtimeestimate3', 'flagtimeestimate4', 'gamblerfallacya', \
               'gamblerfallacyb', 'iatexplicitart1', 'iatexplicitart2', 'iatexplicitart3',
               'iatexplicitart4', 'iatexplicitart5', 'iatexplicitart6', 'iatexplicitmath1',
               'iatexplicitmath2', \
               'iatexplicitmath3', 'iatexplicitmath4', 'iatexplicitmath5', 'iatexplicitmath6',
               'imaginedexplicit1', 'imaginedexplicit2', 'imaginedexplicit3', 'imaginedexplicit4', 'major',
               'mathwarm', 'moneyagea', \
               'moneyageb', 'moneygendera', 'moneygenderb', 'noflagtimeestimate1', 'noflagtimeestimate2',
               'noflagtimeestimate3', 'noflagtimeestimate4', 'omdimc3', 'quotea', 'quoteb', \
               'scalesa', 'scalesb', 'sunkcosta', 'sunkcostb', 'sysjust1', 'sysjust2', 'sysjust3',
               'sysjust4', 'sysjust5', 'sysjust6', 'sysjust7', 'sysjust8']].copy()
values = []
for x, y in zip(batch, y_values):
    prediction = network.predict(np.array([[x_val] for x_val in x]))
    values.append((prediction, y))
# calculate mean squared error
mse = 0
for predicted_y, actual_y in values:
    mse = mse + pow((predicted_y - actual_y), 2)
mse = mse / df.shape[0]
print(f"mean squared error - {mse}")
