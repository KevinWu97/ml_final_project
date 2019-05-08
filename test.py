import pandas as pd
import scipy as sc


def independence_reciprocity_ordering():
    df = pd.read_csv('./data_files/cleaned_data.csv')
    tempdf = df[df.columns[147:151]]
    print(tempdf)

    column_1 = df['reciprocityothera'].tolist()
    column_2 = df['reciprocityotherb'].tolist()
    column_3 = df['reciprocityusa'].tolist()
    column_4 = df['reciprocityusb'].tolist()

    # counting the number of yes' and no's to each question
    num_no = 0
    num_yes = 0
    for x in range(0, len(column_1)):
        if column_1[x] == 'Yes':
            num_yes += 1
        elif column_1[x] == 'No':
            num_no += 1
    print(f'reciprocityothera yes: {num_yes}, no: {num_no}')

    num_no = 0
    num_yes = 0
    for x in range(0, len(column_2)):
        if column_2[x] == 'Yes':
            num_yes += 1
        elif column_2[x] == 'No':
            num_no += 1
    print(f'reciprocityotherb yes: {num_yes}, no: {num_no}')

    num_no = 0
    num_yes = 0
    for x in range(0, len(column_3)):
        if column_3[x] == 'Yes':
            num_yes += 1
        elif column_3[x] == 'No':
            num_no += 1
    print(f'reciprocityusaa yes: {num_yes}, no: {num_no}')

    num_no = 0
    num_yes = 0
    for x in range(0, len(column_4)):
        if column_4[x] == 'Yes':
            num_yes += 1
        elif column_4[x] == 'No':
            num_no += 1
    print(f'reciprocityusab yes: {num_yes}, no: {num_no}')
    
    zip_1 = list(zip(column_1, column_3))
    zip_2 = list(zip(column_2, column_4))

    # remove entries with one or no responses
    for x in range(len(zip_1) - 1, -1, -1):
        if zip_1[x][0].strip() == '' or zip_1[x][1].strip() == '':
            zip_1.pop(x)
    for x in range(len(zip_2) - 1, -1, -1):
        if zip_2[x][0].strip() == '' or zip_2[x][1].strip() == '':
            zip_2.pop(x)

    # print(column_1)
    # print(column_2)
    # print(column_3)
    # print(column_4)

    print(zip_1)
    print(zip_2)
    return 0


independence_reciprocity_ordering()