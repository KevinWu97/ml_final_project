import pandas as pd
import math


# Data Sets refer to data frames

class AttributeNode:
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name
        # This should be a list of ValueNodes
        self.attribute_values = []

    @property
    def attribute_values(self):
        return self._attribute_values

    @attribute_values.setter
    def attribute_values(self, attribute_values):
        self._attribute_values = attribute_values


class ValueNode:
    def __init__(self, value):
        self.value = value
        self.split_attribute = None

    @property
    def split_attribute(self):
        return self._split_attribute

    @split_attribute.setter
    def split_attribute(self, split_attribute_node):
        self._split_attribute = split_attribute_node


def all_same(items):
    return all(x == items[0] for x in items)


def cond_prob(df_partition):
    y_values = df_partition['politicalid'].tolist()
    y_values_mod = list(map(lambda x: 0 if x < 0.5 else 1, y_values))
    cond_prob_lib = y_values_mod.count(0) / len(y_values_mod)
    cond_prob_cons = y_values_mod.count(1) / len(y_values_mod)
    if cond_prob_lib == 0:
        temp_sum = cond_prob_cons * math.log2(cond_prob_cons)
    elif cond_prob_cons == 0:
        temp_sum = cond_prob_lib * math.log2(cond_prob_lib)
    else:
        temp_sum = cond_prob_lib * math.log2(cond_prob_lib) + cond_prob_cons * math.log2(cond_prob_cons)
    return temp_sum


def calculate_y_entropy(data_set):
    y_values = data_set['politicalid'].tolist()
    y_values = list(map(lambda x: 0 if x < 0.5 else 1, y_values))
    prob_lib = y_values.count(0) / len(y_values)
    prob_cons = y_values.count(1) / len(y_values)
    if prob_lib == 0:
        temp_sum = -(prob_lib * math.log2(prob_cons))
    elif prob_cons == 0:
        temp_sum = -(prob_cons * math.log2(prob_lib))
    else:
        temp_sum = -(prob_lib * math.log2(prob_cons) + prob_cons * math.log2(prob_lib))
    return temp_sum


# Calculate the entropy of the y values given a condition or feature H(political_id | feature)
def calculate_x_entropy(data_set, feature):
    x_values = data_set[feature].tolist()
    unique_x_values = list(set(x_values))
    data_set_partitions = []

    for unique_x in unique_x_values:
        df_partition = data_set.loc[data_set[feature] == unique_x]
        data_set_partitions.append((df_partition, unique_x))

    entropy_values = []

    for df_partition_pair in data_set_partitions:
        df_partition = df_partition_pair[0]
        df_partition_variable = df_partition_pair[1]
        prob_feature = x_values.count(df_partition_variable) / len(x_values)
        temp = prob_feature * cond_prob(df_partition)
        entropy_values.append(temp)

    return -sum(entropy_values)


def calculate_information_gain(data_set, feature):
    information_gain = calculate_y_entropy(data_set) - calculate_x_entropy(data_set, feature)
    return information_gain


def get_decision_tree_variables(file_path):
    df = pd.read_csv(file_path, index_col=0)
    decision_tree_variables_df = df[['referrer', 'expgender', 'exprace', 'exprunafter', 'compensation', 'recruitment',
                                     'separatedornot', 'sunkgroup', 'gainlossgroup', 'gainlossDV', 'anch1group',
                                     'anch2group', 'anch3group', 'anch4group', 'gambfalgroup', 'scalesgroup',
                                     'reciprocitygroup', 'allowedforbiddenGroup', 'quoteGroup', 'flagfilter',
                                     'flagGroup', 'MoneyGroup', 'moneyfilter', 'ContactGroup', 'IATfilter',
                                     'citizenship', 'IATEXPfilter', 'nativelang', 'ethnicity', 'race', 'politicalid']]
    return decision_tree_variables_df


def construct_tree(data_set, already_split_variables):

    y_values = data_set['politicalid'].tolist()
    y_values_mod = list(map(lambda x: 0 if x < 0.5 else 1, y_values))

    if data_set.empty:
        return already_split_variables
    elif len(data_set.index) < 200:
        # This to prevent data sets in our decision tree from being too small
        return already_split_variables
    elif all_same(y_values_mod):
        return already_split_variables
    elif len(data_set.columns) == 1 and data_set.columns[0] == 'politicalid':
        return already_split_variables

    x_features = data_set.columns.values.tolist()[:-1]
    ig_values = []

    for feature in x_features:
        ig_values.append(calculate_information_gain(data_set, feature))

    max_ig_index = ig_values.index(max(ig_values))
    split_feature = x_features[max_ig_index]
    already_split_variables.append(split_feature)

    data_partitions = []
    x_values = data_set[split_feature].tolist()
    unique_x_values = list(set(x_values))
    for unique_x in unique_x_values:
        df_partition = data_set.loc[data_set[split_feature] == unique_x]
        df_partition = df_partition.drop(columns=[split_feature])
        data_partitions.append(df_partition)

    current_node = AttributeNode(split_feature)
    value_node_list = []
    for value in unique_x_values:
        new_value_node = ValueNode(value)
        value_node_list.append(new_value_node)

    current_node.attribute_values = value_node_list
    value_data_pair = list(zip(value_node_list, data_partitions))
    for pair in value_data_pair:
        value_node = pair[0]
        data = pair[1]
        value_node.split_attribute = construct_tree(data, already_split_variables)

    return current_node


def traverse_and_split(decision_tree_node, participant_data, batches):
    print(type(decision_tree_node))
    if type(decision_tree_node) == list:
        print('got to end')
        batches.append(participant_data)
        return
    elif type(decision_tree_node) == AttributeNode:
        print('got to attribute')
        attribute_name = decision_tree_node.attribute_name
        attribute_values = decision_tree_node.attribute_values
        for value_node in attribute_values:
            # print(type(value_node))
            # print(value_node.value)
            # print(participant_data[attribute_name].tolist())
            new_participant_data = participant_data.loc[participant_data[attribute_name] == value_node.value]
            traverse_and_split(value_node, new_participant_data, batches)
    elif type(decision_tree_node) == ValueNode:
        print('got to value')
        traverse_and_split(decision_tree_node.split_attribute, participant_data, batches)



dtree_var = get_decision_tree_variables('./data_files/mod_cleaned_data.csv')
decision_tree_root = construct_tree(dtree_var, [])
split_data = []

df = pd.read_csv('./data_files/mod_cleaned_data.csv', index_col=0)
traverse_and_split(decision_tree_root, df, split_data)
print(split_data)
# print(dtree_var)

'''
y_entropy = calculate_y_entropy(dtree_var)
print(y_entropy)

x_entropy = calculate_x_entropy(dtree_var, 'referrer')
print(x_entropy)
'''

# print(calculate_information_gain(dtree_var, 'referrer'))
# print(construct_tree(dtree_var, []))
