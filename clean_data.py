import pandas as pd
import random


def transform_data(file_path):
    df = pd.read_csv(file_path, index_col=0)
    # df = df[df['referrer', 'expgender', 'exprace', 'exprunafter', 'compensation', 'recruitment',]]
    df = df.iloc[:, 4:163]
    df = df.drop(['creation_date', 'session_creation_date', 'expcomments', 'numparticipants_actual', 'gambfalDV',
                  'numparticipants', 'exprunafter2', 'sample', 'partgender', 'Ranchori', 'RAN001', 'RAN002',
                  'RAN003', 'Ranch1', 'Ranch2', 'Ranch3', 'Ranch4', 'gamblerfallacya_sd', 'gamblerfallacyb_sd',
                  'quotearec', 'quotebrec', 'flagdv', 'Imagineddv', 'Sysjust', 'allowedforbiddena', 'scalesreca',
                  'allowedforbiddenb', 'anchoring1a', 'anchoring1b', 'anchoring2a', 'anchoring2b', 'anchoring3a',
                  'anchoring3b', 'anchoring4a', 'anchoring4b', 'd_donotuse', 'reciprocityothera', 'reciprocityotherb',
                  'reciprocityusa', 'reciprocityusb', 'moneyethnicitya', 'moneyethnicityb', 'nativelang2',
                  'omdimc3rt', 'omdimc3trt', 'imagineddescribe', 'feedback', 'scales', 'scalesrecb'], axis=1)

    disease_framing_a = df['diseaseframinga'].tolist()
    for i in range(len(disease_framing_a)):
        if disease_framing_a[i] == ' ':
            disease_framing_a[i] = 0.5
        elif disease_framing_a[i] == '200 people will be saved':
            disease_framing_a[i] = 0
        else:
            disease_framing_a[i] = 1
    df['diseaseframinga'] = disease_framing_a

    disease_framing_b = df['diseaseframingb'].tolist()
    for i in range(len(disease_framing_b)):
        if disease_framing_b[i] == ' ':
            disease_framing_b[i] = 0.5
        elif disease_framing_b[i] == '400 people will die':
            disease_framing_b[i] = 0
        else:
            disease_framing_b[i] = 1
    df['diseaseframingb'] = disease_framing_b

    age_column = df['age'].tolist()
    for i in range(len(age_column)):
        if age_column[i] == ' ':
            age_column[i] = random.uniform(0, 1)
        else:
            age_column[i] = float(age_column[i]) / 100
    df['age'] = age_column

    gender_column = df['sex'].tolist()
    for i in range(len(gender_column)):
        if gender_column[i] == '.':
            gender_column[i] = 0.5
        elif gender_column[i] == 'm':
            gender_column[i] = 1
        else:
            gender_column[i] = 0
    df['sex'] = gender_column

    anchoring_1 = df['anchoring1'].tolist()
    for i in range(len(anchoring_1)):
        if anchoring_1[i] == ' ':
            anchoring_1[i] = 0.5
        elif 0.75 * 2572 <= float(anchoring_1[i]) <= 1.25 * 2572:
            anchoring_1[i] = 1
        else:
            anchoring_1[i] = 0
    df['anchoring1'] = anchoring_1

    anchoring_2 = df['anchoring2'].tolist()
    for i in range(len(anchoring_2)):
        if anchoring_2[i] == ' ':
            anchoring_2[i] = 0.5
        elif 0.75 * 2716000 <= float(anchoring_2[i]) <= 1.25 * 2716000:
            anchoring_2[i] = 1
        else:
            anchoring_2[i] = 0
    df['anchoring2'] = anchoring_2

    anchoring_3 = df['anchoring3'].tolist()
    for i in range(len(anchoring_3)):
        if anchoring_3[i] == ' ':
            anchoring_3[i] = 0.5
        elif 0.75 * 29029 <= float(anchoring_3[i]) <= 1.25 * 29029:
            anchoring_3[i] = 1
        else:
            anchoring_3[i] = 0
    df['anchoring3'] = anchoring_3

    anchoring_4 = df['anchoring4'].tolist()
    for i in range(len(anchoring_4)):
        if anchoring_4[i] == ' ':
            anchoring_4[i] = 0.5
        elif 0.75 * 10800 <= float(anchoring_4[i]) <= 1.25 * 10800:
            anchoring_4[i] = 1
        else:
            anchoring_4[i] = 0
    df['anchoring4'] = anchoring_4

    '''
    
    Insert normalized anchor answers from 0 to 1 based on error
    cap error at 1
    
    '''

    reciprocity_other_column = df['reciprocityother'].tolist()
    for i in range(len(reciprocity_other_column)):
        if reciprocity_other_column[i] == ' ':
            reciprocity_other_column[i] = 0.5
        elif reciprocity_other_column[i] == '0' or reciprocity_other_column[i] == 0:
            reciprocity_other_column[i] = 0
        else:
            reciprocity_other_column[i] = 1
    df['reciprocityother'] = reciprocity_other_column

    reciprocity_us_column = df['reciprocityus'].tolist()
    for i in range(len(reciprocity_us_column)):
        if reciprocity_us_column[i] == ' ':
            reciprocity_us_column[i] = 0.5
        elif reciprocity_us_column[i] == '0' or reciprocity_other_column[i] == 0:
            reciprocity_us_column[i] = 0
        else:
            reciprocity_us_column[i] = 1
    df['reciprocityus'] = reciprocity_us_column

    allowed_forbidden_column = df['allowedforbidden'].tolist()
    for i in range(len(allowed_forbidden_column)):
        if allowed_forbidden_column[i] == ' ':
            allowed_forbidden_column[i] = 0.5
        elif allowed_forbidden_column[i] == 'YES':
            allowed_forbidden_column[i] = 0
        else:
            allowed_forbidden_column[i] = 1
    df['allowedforbidden'] = allowed_forbidden_column

    quote_column = df['quote'].tolist()
    for i in range(len(quote_column)):
        if quote_column[i] == ' ':
            quote_column[i] = random.uniform(0, 1)
        else:
            quote_column[i] = (float(quote_column[i]) - 1) / 10
    df['quote'] = quote_column

    total_flag_estimations = df['totalflagestimations'].tolist()
    for i in range(len(total_flag_estimations)):
        if total_flag_estimations[i] == ' ':
            total_flag_estimations[i] = random.uniform(0, 1)
        else:
            total_flag_estimations[i] = (float(total_flag_estimations[i]) - 4) / 8
    df['totalflagestimations'] = total_flag_estimations

    total_no_flag_time_estimations = df['totalnoflagtimeestimations'].tolist()
    for i in range(len(total_no_flag_time_estimations)):
        if total_no_flag_time_estimations[i] == ' ':
            total_no_flag_time_estimations[i] = random.uniform(0, 1)
        else:
            total_no_flag_time_estimations[i] = (float(total_no_flag_time_estimations[i]) - 4) / 8
    df['totalnoflagtimeestimations'] = total_no_flag_time_estimations

    iatexpart = df['IATexpart'].tolist()
    for i in range(len(iatexpart)):
        if iatexpart[i] == ' ':
            iatexpart[i] = random.uniform(0, 1)
        else:
            iatexpart[i] = (float(iatexpart[i]) - 2) / 7
    df['IATexpart'] = iatexpart

    iatexpmath = df['IATexpmath'].tolist()
    for i in range(len(iatexpmath)):
        if iatexpmath[i] == ' ':
            iatexpmath[i] = random.uniform(0, 1)
        else:
            iatexpmath[i] = (float(iatexpmath[i]) - 2) / 7
    df['IATexpmath'] = iatexpmath

    iatexpall = df['IATexp.overall'].tolist()
    for i in range(len(iatexpall)):
        if iatexpall[i] == ' ':
            iatexpall[i] = random.uniform(0, 1)
        else:
            iatexpall[i] = (float(iatexpall[i]) - 1.5) / 7
    df['IATexp.overall'] = iatexpall

    total_exp_missed = df['totexpmissed'].tolist()
    for i in range(len(total_exp_missed)):
        if total_exp_missed[i] == ' ':
            total_exp_missed[i] = random.uniform(0, 1)
        else:
            total_exp_missed[i] = float(total_exp_missed[i]) / 12
    df['totexpmissed'] = total_exp_missed

    art_warm = df['artwarm'].tolist()
    for i in range(len(art_warm)):
        if art_warm[i] == ' ':
            art_warm[i] = random.uniform(0, 1)
        else:
            art_warm[i] = float(art_warm[i]) / 100
    df['artwarm'] = art_warm

    flag_dv_1 = df['flagdv1'].tolist()
    for i in range(len(flag_dv_1)):
        if flag_dv_1[i] == ' ':
            flag_dv_1[i] = random.uniform(0, 1)
        else:
            flag_dv_1[i] = (float(flag_dv_1[i]) - 1) / 6
    df['flagdv1'] = flag_dv_1

    flag_dv_2 = df['flagdv2'].tolist()
    for i in range(len(flag_dv_2)):
        if flag_dv_2[i] == ' ':
            flag_dv_2[i] = random.uniform(0, 1)
        else:
            flag_dv_2[i] = (float(flag_dv_2[i]) - 1) / 6
    df['flagdv2'] = flag_dv_2

    flag_dv_3 = df['flagdv3'].tolist()
    for i in range(len(flag_dv_3)):
        if flag_dv_3[i] == ' ':
            flag_dv_3[i] = random.uniform(0, 1)
        else:
            flag_dv_3[i] = (float(flag_dv_3[i]) - 1) / 6
    df['flagdv3'] = flag_dv_3

    flag_dv_4 = df['flagdv4'].tolist()
    for i in range(len(flag_dv_4)):
        if flag_dv_4[i] == ' ':
            flag_dv_4[i] = random.uniform(0, 1)
        else:
            flag_dv_4[i] = (float(flag_dv_4[i]) - 1) / 6
    df['flagdv4'] = flag_dv_4

    flag_dv_5 = df['flagdv5'].tolist()
    for i in range(len(flag_dv_5)):
        if flag_dv_5[i] == ' ':
            flag_dv_5[i] = random.uniform(0, 1)
        else:
            flag_dv_5[i] = (float(flag_dv_5[i]) - 1) / 6
    df['flagdv5'] = flag_dv_5

    flag_dv_6 = df['flagdv6'].tolist()
    for i in range(len(flag_dv_6)):
        if flag_dv_6[i] == ' ':
            flag_dv_6[i] = random.uniform(0, 1)
        else:
            flag_dv_6[i] = (float(flag_dv_6[i]) - 1) / 6
    df['flagdv6'] = flag_dv_6

    flag_dv_7 = df['flagdv7'].tolist()
    for i in range(len(flag_dv_7)):
        if flag_dv_7[i] == ' ':
            flag_dv_7[i] = random.uniform(0, 1)
        else:
            flag_dv_7[i] = (float(flag_dv_7[i]) - 1) / 6
    df['flagdv7'] = flag_dv_7

    flag_dv_8 = df['flagdv8'].tolist()
    for i in range(len(flag_dv_8)):
        if flag_dv_8[i] == ' ':
            flag_dv_8[i] = random.uniform(0, 1)
        else:
            flag_dv_8[i] = (float(flag_dv_8[i]) - 1) / 6
    df['flagdv8'] = flag_dv_8

    flag_supplement_1 = df['flagsupplement1'].tolist()
    for i in range(len(flag_supplement_1)):
        if flag_supplement_1[i] == ' ':
            flag_supplement_1[i] = random.uniform(0, 1)
        elif flag_supplement_1[i] == 'Not at all':
            flag_supplement_1[i] = 0
        elif flag_supplement_1[i] == 'Very much':
            flag_supplement_1[i] = 1
        else:
            flag_supplement_1[i] = (float(flag_supplement_1[i]) - 1) / 9
    df['flagsupplement1'] = flag_supplement_1

    flag_supplement_2 = df['flagsupplement2'].tolist()
    for i in range(len(flag_supplement_2)):
        if flag_supplement_2[i] == ' ':
            flag_supplement_2[i] = random.uniform(0, 1)
        elif flag_supplement_2[i] == 'Democrat':
            flag_supplement_2[i] = 0
        elif flag_supplement_2[i] == 'Republican':
            flag_supplement_2[i] = 1
        else:
            flag_supplement_2[i] = (float(flag_supplement_2[i]) - 1) / 6
    df['flagsupplement2'] = flag_supplement_2

    flag_supplement_3 = df['flagsupplement3'].tolist()
    for i in range(len(flag_supplement_3)):
        if flag_supplement_3[i] == ' ':
            flag_supplement_3[i] = random.uniform(0, 1)
        elif flag_supplement_3[i] == 'Liberal':
            flag_supplement_3[i] = 0
        elif flag_supplement_3[i] == 'Conservative':
            flag_supplement_3[i] = 1
        else:
            flag_supplement_3[i] = (float(flag_supplement_1[i]) - 1) / 6
    df['flagsupplement3'] = flag_supplement_3

    flag_time_estimate_1 = df['flagtimeestimate1'].tolist()
    for i in range(len(flag_time_estimate_1)):
        if flag_time_estimate_1[i] == ' ':
            flag_time_estimate_1[i] = random.uniform(0, 1)
        elif flag_time_estimate_1[i] == 'Morning':
            flag_time_estimate_1[i] = 0
        elif flag_time_estimate_1[i] == 'Afternoon':
            flag_time_estimate_1[i] = 0.5
        elif flag_time_estimate_1[i] == 'Evening':
            flag_time_estimate_1[i] = 1
    df['flagtimeestimate1'] = flag_time_estimate_1

    flag_time_estimate_2 = df['flagtimeestimate2'].tolist()
    for i in range(len(flag_time_estimate_2)):
        if flag_time_estimate_2[i] == ' ':
            flag_time_estimate_2[i] = random.uniform(0, 1)
        elif flag_time_estimate_2[i] == 'Morning':
            flag_time_estimate_2[i] = 0
        elif flag_time_estimate_2[i] == 'Afternoon':
            flag_time_estimate_2[i] = 0.5
        elif flag_time_estimate_2[i] == 'Evening':
            flag_time_estimate_2[i] = 1
    df['flagtimeestimate2'] = flag_time_estimate_2

    flag_time_estimate_3 = df['flagtimeestimate3'].tolist()
    for i in range(len(flag_time_estimate_3)):
        if flag_time_estimate_3[i] == ' ':
            flag_time_estimate_3[i] = random.uniform(0, 1)
        elif flag_time_estimate_3[i] == 'Morning':
            flag_time_estimate_3[i] = 0
        elif flag_time_estimate_3[i] == 'Afternoon':
            flag_time_estimate_3[i] = 0.5
        elif flag_time_estimate_3[i] == 'Evening':
            flag_time_estimate_3[i] = 1
    df['flagtimeestimate3'] = flag_time_estimate_3

    flag_time_estimate_4 = df['flagtimeestimate4'].tolist()
    for i in range(len(flag_time_estimate_4)):
        if flag_time_estimate_4[i] == ' ':
            flag_time_estimate_4[i] = random.uniform(0, 1)
        elif flag_time_estimate_4[i] == 'Morning':
            flag_time_estimate_4[i] = 0
        elif flag_time_estimate_4[i] == 'Afternoon':
            flag_time_estimate_4[i] = 0.5
        elif flag_time_estimate_4[i] == 'Evening':
            flag_time_estimate_4[i] = 1
    df['flagtimeestimate4'] = flag_time_estimate_4

    gambler_fallacy_a = df['gamblerfallacya'].tolist()
    for i in range(len(gambler_fallacy_a)):
        if gambler_fallacy_a[i] == ' ':
            gambler_fallacy_a[i] = random.uniform(0, 1)
        else:
            gambler_fallacy_a[i] = float(gambler_fallacy_a[i]) / 25
    df['gamblerfallacya'] = gambler_fallacy_a

    gambler_fallacy_b = df['gamblerfallacyb'].tolist()
    for i in range(len(gambler_fallacy_b)):
        if gambler_fallacy_b[i] == ' ':
            gambler_fallacy_b[i] = random.uniform(0, 1)
        else:
            gambler_fallacy_b[i] = float(gambler_fallacy_b[i]) / 25
    df['gamblerfallacyb'] = gambler_fallacy_b

    iat_explicit_art_1 = df['iatexplicitart1'].tolist()
    for i in range(len(iat_explicit_art_1)):
        if iat_explicit_art_1[i] == ' ':
            iat_explicit_art_1[i] = random.uniform(0, 1)
        elif iat_explicit_art_1[i] == 'Moderately bad':
            iat_explicit_art_1[i] = 0
        elif iat_explicit_art_1[i] == 'Very bad':
            iat_explicit_art_1[i] = 1
        else:
            iat_explicit_art_1[i] = (float(iat_explicit_art_1[i]) - 4) / 3
    df['iatexplicitart1'] = iat_explicit_art_1

    iat_explicit_art_2 = df['iatexplicitart2'].tolist()
    for i in range(len(iat_explicit_art_2)):
        if iat_explicit_art_2[i] == ' ':
            iat_explicit_art_2[i] = random.uniform(0, 1)
        elif iat_explicit_art_2[i] == 'Moderately Sad':
            iat_explicit_art_2[i] = 0
        elif iat_explicit_art_2[i] == 'Very Sad':
            iat_explicit_art_2[i] = 1
        else:
            iat_explicit_art_2[i] = (float(iat_explicit_art_2[i]) - 4) / 3
    df['iatexplicitart2'] = iat_explicit_art_2

    iat_explicit_art_3 = df['iatexplicitart3'].tolist()
    for i in range(len(iat_explicit_art_3)):
        if iat_explicit_art_3[i] == ' ':
            iat_explicit_art_3[i] = random.uniform(0, 1)
        elif iat_explicit_art_3[i] == 'Moderately Ugly':
            iat_explicit_art_3[i] = 0
        elif iat_explicit_art_3[i] == 'Very Ugly':
            iat_explicit_art_3[i] = 1
        else:
            iat_explicit_art_3[i] = (float(iat_explicit_art_3[i]) - 4) / 3
    df['iatexplicitart3'] = iat_explicit_art_3

    iat_explicit_art_4 = df['iatexplicitart4'].tolist()
    for i in range(len(iat_explicit_art_4)):
        if iat_explicit_art_4[i] == ' ':
            iat_explicit_art_4[i] = random.uniform(0, 1)
        elif iat_explicit_art_4[i] == 'Moderately Disgusting':
            iat_explicit_art_4[i] = 0
        elif iat_explicit_art_4[i] == 'Very Disgusting':
            iat_explicit_art_4[i] = 1
        else:
            iat_explicit_art_4[i] = (float(iat_explicit_art_4[i]) - 4) / 3
    df['iatexplicitart4'] = iat_explicit_art_4

    iat_explicit_art_5 = df['iatexplicitart5'].tolist()
    for i in range(len(iat_explicit_art_5)):
        if iat_explicit_art_5[i] == ' ':
            iat_explicit_art_5[i] = random.uniform(0, 1)
        elif iat_explicit_art_5[i] == 'Moderately Avoid':
            iat_explicit_art_5[i] = 0
        elif iat_explicit_art_5[i] == 'Very Avoid':
            iat_explicit_art_5[i] = 1
        else:
            iat_explicit_art_5[i] = (float(iat_explicit_art_5[i]) - 4) / 3
    df['iatexplicitart5'] = iat_explicit_art_5

    iat_explicit_art_6 = df['iatexplicitart6'].tolist()
    for i in range(len(iat_explicit_art_6)):
        if iat_explicit_art_6[i] == ' ':
            iat_explicit_art_6[i] = random.uniform(0, 1)
        elif iat_explicit_art_6[i] == 'Moderately Afraid':
            iat_explicit_art_6[i] = 0
        elif iat_explicit_art_6[i] == 'Very Afraid':
            iat_explicit_art_6[i] = 1
        else:
            iat_explicit_art_6[i] = (float(iat_explicit_art_6[i]) - 4) / 3
    df['iatexplicitart6'] = iat_explicit_art_6

    iat_explicit_math_1 = df['iatexplicitmath1'].tolist()
    for i in range(len(iat_explicit_math_1)):
        if iat_explicit_math_1[i] == ' ':
            iat_explicit_math_1[i] = random.uniform(0, 1)
        elif iat_explicit_math_1[i] == 'Slightly bad':
            iat_explicit_math_1[i] = 0
        elif iat_explicit_math_1[i] == 'Moderately bad':
            iat_explicit_math_1[i] = 0.5
        elif iat_explicit_math_1[i] == 'Very bad':
            iat_explicit_math_1[i] = 1
        else:
            iat_explicit_math_1[i] = (float(iat_explicit_math_1[i]) - 4) / 2
    df['iatexplicitmath1'] = iat_explicit_math_1

    iat_explicit_math_2 = df['iatexplicitmath2'].tolist()
    for i in range(len(iat_explicit_math_2)):
        if iat_explicit_math_2[i] == ' ':
            iat_explicit_math_2[i] = random.uniform(0, 1)
        elif iat_explicit_math_2[i] == 'Slightly Sad':
            iat_explicit_math_2[i] = 0
        elif iat_explicit_math_2[i] == 'Moderately Sad':
            iat_explicit_math_2[i] = 0.5
        elif iat_explicit_math_2[i] == 'Very Sad':
            iat_explicit_math_2[i] = 1
        else:
            iat_explicit_math_2[i] = (float(iat_explicit_math_2[i]) - 4) / 2
    df['iatexplicitmath2'] = iat_explicit_math_2

    iat_explicit_math_3 = df['iatexplicitmath3'].tolist()
    for i in range(len(iat_explicit_math_3)):
        if iat_explicit_math_3[i] == ' ':
            iat_explicit_math_3[i] = random.uniform(0, 1)
        elif iat_explicit_math_3[i] == 'Slightly Ugly':
            iat_explicit_math_3[i] = 0
        elif iat_explicit_math_3[i] == 'Moderately Ugly':
            iat_explicit_math_3[i] = 0.5
        elif iat_explicit_math_3[i] == 'Very Ugly':
            iat_explicit_math_3[i] = 1
        else:
            iat_explicit_math_3[i] = (float(iat_explicit_math_3[i]) - 4) / 2
    df['iatexplicitmath3'] = iat_explicit_math_3

    iat_explicit_math_4 = df['iatexplicitmath4'].tolist()
    for i in range(len(iat_explicit_math_4)):
        if iat_explicit_math_4[i] == ' ':
            iat_explicit_math_4[i] = random.uniform(0, 1)
        elif iat_explicit_math_4[i] == 'Slightly Disgusting':
            iat_explicit_math_4[i] = 0
        elif iat_explicit_math_4[i] == 'Moderately Disgusting':
            iat_explicit_math_4[i] = 0.5
        elif iat_explicit_math_4[i] == 'Very Disgusting':
            iat_explicit_math_4[i] = 1
        else:
            iat_explicit_math_4[i] = (float(iat_explicit_math_4[i]) - 4) / 2
    df['iatexplicitmath4'] = iat_explicit_math_4

    iat_explicit_math_5 = df['iatexplicitmath5'].tolist()
    for i in range(len(iat_explicit_math_5)):
        if iat_explicit_math_5[i] == ' ':
            iat_explicit_math_5[i] = random.uniform(0, 1)
        elif iat_explicit_math_5[i] == 'Slightly Avoid':
            iat_explicit_math_5[i] = 0
        elif iat_explicit_math_5[i] == 'Moderately Avoid':
            iat_explicit_math_5[i] = 0.5
        elif iat_explicit_math_5[i] == 'Very Avoid':
            iat_explicit_math_5[i] = 1
        else:
            iat_explicit_math_5[i] = (float(iat_explicit_math_5[i]) - 4) / 2
    df['iatexplicitmath5'] = iat_explicit_math_5

    iat_explicit_math_6 = df['iatexplicitmath6'].tolist()
    for i in range(len(iat_explicit_math_6)):
        if iat_explicit_math_6[i] == ' ':
            iat_explicit_math_6[i] = random.uniform(0, 1)
        elif iat_explicit_math_6[i] == 'Slightly Afraid':
            iat_explicit_math_6[i] = 0
        elif iat_explicit_math_6[i] == 'Moderately Afraid':
            iat_explicit_math_6[i] = 0.5
        elif iat_explicit_math_6[i] == 'Very Afraid':
            iat_explicit_math_6[i] = 1
        else:
            iat_explicit_math_6[i] = (float(iat_explicit_math_6[i]) - 4) / 2
    df['iatexplicitmath6'] = iat_explicit_math_6

    imagined_explicit_1 = df['imaginedexplicit1'].tolist()
    for i in range(len(imagined_explicit_1)):
        if imagined_explicit_1[i] == ' ':
            imagined_explicit_1[i] = random.uniform(0, 1)
        else:
            imagined_explicit_1[i] = (float(imagined_explicit_1[i]) - 1) / 8
    df['imaginedexplicit1'] = imagined_explicit_1

    imagined_explicit_2 = df['imaginedexplicit2'].tolist()
    for i in range(len(imagined_explicit_2)):
        if imagined_explicit_2[i] == ' ':
            imagined_explicit_2[i] = random.uniform(0, 1)
        else:
            imagined_explicit_2[i] = (float(imagined_explicit_2[i]) - 1) / 8
    df['imaginedexplicit2'] = imagined_explicit_2

    imagined_explicit_3 = df['imaginedexplicit3'].tolist()
    for i in range(len(imagined_explicit_3)):
        if imagined_explicit_3[i] == ' ':
            imagined_explicit_3[i] = random.uniform(0, 1)
        else:
            imagined_explicit_3[i] = (float(imagined_explicit_3[i]) - 1) / 8
    df['imaginedexplicit3'] = imagined_explicit_3

    imagined_explicit_4 = df['imaginedexplicit4'].tolist()
    for i in range(len(imagined_explicit_4)):
        if imagined_explicit_4[i] == ' ':
            imagined_explicit_4[i] = random.uniform(0, 1)
        else:
            imagined_explicit_4[i] = (float(imagined_explicit_4[i]) - 1) / 8
    df['imaginedexplicit4'] = imagined_explicit_4

    major = df['major'].tolist()
    for i in range(len(major)):
        if major[i] == ' ':
            major[i] = random.uniform(0, 1)
        else:
            major[i] = (float(major[i]) - 1) / 12
    df['major'] = major

    math_warm = df['mathwarm'].tolist()
    for i in range(len(math_warm)):
        if math_warm[i] == ' ':
            math_warm[i] = random.uniform(0, 1)
        else:
            math_warm[i] = (float(math_warm[i])) / 100
    df['mathwarm'] = math_warm

    money_age_a = df['moneyagea'].tolist()
    for i in range(len(money_age_a)):
        if money_age_a[i] == ' ':
            money_age_a[i] = random.uniform(0, 1)
        else:
            money_age_a[i] = (float(money_age_a[i]))/100
    df['moneyagea'] = money_age_a

    money_age_b = df['moneyageb'].tolist()
    for i in range(len(money_age_b)):
        if money_age_b[i] == ' ':
            money_age_b[i] = random.uniform(0, 1)
        else:
            money_age_b[i] = (float(money_age_b[i]))/100
    df['moneyageb'] = money_age_b

    money_gender_a = df['moneygendera'].tolist()
    for i in range(len(money_gender_a)):
        if money_gender_a[i] == ' ':
            money_gender_a[i] = 0.5
        else:
            money_gender_a[i] = (float(money_gender_a[i]))
    df['moneygendera'] = money_gender_a

    money_gender_b = df['moneygenderb'].tolist()
    for i in range(len(money_gender_b)):
        if money_gender_b[i] == ' ':
            money_gender_b[i] = 0.5
        else:
            money_gender_b[i] = (float(money_gender_b[i]))
    df['moneygenderb'] = money_gender_b

    no_flag_time_estimate_1 = df['noflagtimeestimate1'].tolist()
    for i in range(len(no_flag_time_estimate_1)):
        if no_flag_time_estimate_1[i] == ' ':
            no_flag_time_estimate_1[i] = random.uniform(0, 1)
        elif no_flag_time_estimate_1[i] == 'Morning':
            no_flag_time_estimate_1[i] = 0
        elif no_flag_time_estimate_1[i] == 'Afternoon':
            no_flag_time_estimate_1[i] = 0.5
        elif no_flag_time_estimate_1[i] == 'Evening':
            no_flag_time_estimate_1[i] = 1
    df['noflagtimeestimate1'] = no_flag_time_estimate_1

    no_flag_time_estimate_2 = df['noflagtimeestimate2'].tolist()
    for i in range(len(no_flag_time_estimate_2)):
        if no_flag_time_estimate_2[i] == ' ':
            no_flag_time_estimate_2[i] = random.uniform(0, 1)
        elif no_flag_time_estimate_2[i] == 'Morning':
            no_flag_time_estimate_2[i] = 0
        elif no_flag_time_estimate_2[i] == 'Afternoon':
            no_flag_time_estimate_2[i] = 0.5
        elif no_flag_time_estimate_2[i] == 'Evening':
            no_flag_time_estimate_2[i] = 1
    df['noflagtimeestimate2'] = no_flag_time_estimate_2

    no_flag_time_estimate_3 = df['noflagtimeestimate3'].tolist()
    for i in range(len(no_flag_time_estimate_3)):
        if no_flag_time_estimate_3[i] == ' ':
            no_flag_time_estimate_3[i] = random.uniform(0, 1)
        elif no_flag_time_estimate_3[i] == 'Morning':
            no_flag_time_estimate_3[i] = 0
        elif no_flag_time_estimate_3[i] == 'Afternoon':
            no_flag_time_estimate_3[i] = 0.5
        elif no_flag_time_estimate_3[i] == 'Evening':
            no_flag_time_estimate_3[i] = 1
    df['noflagtimeestimate3'] = no_flag_time_estimate_3

    no_flag_time_estimate_4 = df['noflagtimeestimate4'].tolist()
    for i in range(len(no_flag_time_estimate_4)):
        if no_flag_time_estimate_4[i] == ' ':
            no_flag_time_estimate_4[i] = random.uniform(0, 1)
        elif no_flag_time_estimate_4[i] == 'Morning':
            no_flag_time_estimate_4[i] = 0
        elif no_flag_time_estimate_4[i] == 'Afternoon':
            no_flag_time_estimate_4[i] = 0.5
        elif no_flag_time_estimate_4[i] == 'Evening':
            no_flag_time_estimate_4[i] = 1
    df['noflagtimeestimate4'] = no_flag_time_estimate_4

    political_id = df['politicalid'].tolist()
    for i in range(len(political_id)):
        if political_id[i] == ' ':
            political_id[i] = random.uniform(0, 1)
        elif political_id[i] == 'Strongly liberal':
            political_id[i] = 0
        elif political_id[i] == 'Moderately liberal':
            political_id[i] = float(1)/6
        elif political_id[i] == 'Slightly liberal':
            political_id[i] = float(2)/6
        elif political_id[i] == 'Neutral (moderate)':
            political_id[i] = float(3)/6
        elif political_id[i] == 'Slightly conservative':
            political_id[i] = float(4)/6
        elif political_id[i] == 'Moderately conservative':
            political_id[i] = float(5)/6
        elif political_id[i] == 'Strongly conservative':
            political_id[i] = 1
    df['politicalid'] = political_id

    omd_imc3 = df['omdimc3'].tolist()
    for i in range(len(omd_imc3)):
        if omd_imc3[i] == ' ':
            omd_imc3[i] = 0
        elif omd_imc3[i] == 'Fail':
            omd_imc3[i] = 0
        elif omd_imc3[i] == 'Pass':
            omd_imc3[i] = 1
    df['omdimc3'] = omd_imc3

    quote_a = df['quotea'].tolist()
    for i in range(len(quote_a)):
        if quote_a[i] == ' ':
            quote_a[i] = random.uniform(0, 1)
        else:
            quote_a[i] = (float(quote_a[i]) - 1) / 8
    df['quotea'] = quote_a

    quote_b = df['quoteb'].tolist()
    for i in range(len(quote_b)):
        if quote_b[i] == ' ':
            quote_b[i] = random.uniform(0, 1)
        else:
            quote_b[i] = (float(quote_b[i]) - 1) / 8
    df['quoteb'] = quote_b

    scales_a = df['scalesa'].tolist()
    for i in range(len(scales_a)):
        if scales_a[i] == ' ':
            scales_a[i] = random.uniform(0, 1)
        elif scales_a[i] == 'Up to a half hour':
            scales_a[i] = 0
        elif scales_a[i] == 'Half an hour to an hour':
            scales_a[i] = float(1) / 5
        elif scales_a[i] == 'One to one and a half hours':
            scales_a[i] = float(2) / 5
        elif scales_a[i] == 'One and a half to two hours':
            scales_a[i] = float(3) / 5
        elif scales_a[i] == 'Two to two and a half hours':
            scales_a[i] = float(4) / 5
        elif scales_a[i] == 'More than two and a half hours':
            scales_a[i] = 1
    df['scalesa'] = scales_a

    scales_b = df['scalesb'].tolist()
    for i in range(len(scales_b)):
        if scales_b[i] == ' ':
            scales_b[i] = random.uniform(0, 1)
        elif scales_b[i] == 'Up to two and a half hours':
            scales_b[i] = 0
        elif scales_b[i] == 'Two and a half hours to three hours':
            scales_b[i] = float(1) / 5
        elif scales_b[i] == 'Three to three and a half hours':
            scales_b[i] = float(2) / 5
        elif scales_b[i] == 'Three and a half to four hours':
            scales_b[i] = float(3) / 5
        elif scales_b[i] == 'Four to four and a half hours':
            scales_b[i] = float(4) / 5
        elif scales_b[i] == 'More than four and a half hours':
            scales_b[i] = 1
    df['scalesb'] = scales_b

    sunk_cost_a = df['sunkcosta'].tolist()
    for i in range(len(sunk_cost_a)):
        if sunk_cost_a[i] == ' ':
            sunk_cost_a[i] = random.uniform(0, 1)
        else:
            sunk_cost_a[i] = (float(sunk_cost_a[i]) - 1) / 8
    df['sunkcosta'] = sunk_cost_a

    sunk_cost_b = df['sunkcostb'].tolist()
    for i in range(len(sunk_cost_b)):
        if sunk_cost_b[i] == ' ':
            sunk_cost_b[i] = random.uniform(0, 1)
        else:
            sunk_cost_b[i] = (float(sunk_cost_b[i]) - 1) / 8
    df['sunkcostb'] = sunk_cost_b

    sys_just_1 = df['sysjust1'].tolist()
    for i in range(len(sys_just_1)):
        if sys_just_1[i] == ' ':
            sys_just_1[i] = random.uniform(0, 1)
        elif sys_just_1[i] == 'Strongly disagree':
            sys_just_1[i] = 0
        elif sys_just_1[i] == 'Strongly agree':
            sys_just_1[i] = 1
        else:
            sys_just_1[i] = (float(sys_just_1[i]) - 1) / 6
    df['sysjust1'] = sys_just_1

    sys_just_2 = df['sysjust2'].tolist()
    for i in range(len(sys_just_2)):
        if sys_just_2[i] == ' ':
            sys_just_2[i] = random.uniform(0, 1)
        elif sys_just_2[i] == 'Strongly disagree':
            sys_just_2[i] = 0
        elif sys_just_2[i] == 'Strongly agree':
            sys_just_2[i] = 1
        else:
            sys_just_2[i] = (float(sys_just_2[i]) - 1) / 6
    df['sysjust2'] = sys_just_2

    sys_just_3 = df['sysjust3'].tolist()
    for i in range(len(sys_just_3)):
        if sys_just_3[i] == ' ':
            sys_just_3[i] = random.uniform(0, 1)
        elif sys_just_3[i] == 'Strongly agree':
            sys_just_3[i] = 0
        elif sys_just_3[i] == 'Strongly disagree':
            sys_just_3[i] = 1
        else:
            sys_just_3[i] = (float(sys_just_3[i]) - 1) / 6
    df['sysjust3'] = sys_just_3

    sys_just_4 = df['sysjust4'].tolist()
    for i in range(len(sys_just_4)):
        if sys_just_4[i] == ' ':
            sys_just_4[i] = random.uniform(0, 1)
        elif sys_just_4[i] == 'Strongly disagree':
            sys_just_4[i] = 0
        elif sys_just_4[i] == 'Strongly agree':
            sys_just_4[i] = 1
        else:
            sys_just_4[i] = (float(sys_just_4[i]) - 1) / 6
    df['sysjust4'] = sys_just_4

    sys_just_5 = df['sysjust5'].tolist()
    for i in range(len(sys_just_5)):
        if sys_just_5[i] == ' ':
            sys_just_5[i] = random.uniform(0, 1)
        elif sys_just_5[i] == 'Strongly disagree':
            sys_just_5[i] = 0
        elif sys_just_5[i] == 'Strongly agree':
            sys_just_5[i] = 1
        else:
            sys_just_5[i] = (float(sys_just_5[i]) - 1) / 6
    df['sysjust5'] = sys_just_5

    sys_just_6 = df['sysjust6'].tolist()
    for i in range(len(sys_just_6)):
        if sys_just_6[i] == ' ':
            sys_just_6[i] = random.uniform(0, 1)
        elif sys_just_6[i] == 'Strongly disagree':
            sys_just_6[i] = 0
        elif sys_just_6[i] == 'Strongly agree':
            sys_just_6[i] = 1
        else:
            sys_just_6[i] = (float(sys_just_6[i]) - 1) / 6
    df['sysjust6'] = sys_just_6

    sys_just_7 = df['sysjust7'].tolist()
    for i in range(len(sys_just_7)):
        if sys_just_7[i] == ' ':
            sys_just_7[i] = random.uniform(0, 1)
        elif sys_just_7[i] == 'Strongly agree':
            sys_just_7[i] = 0
        elif sys_just_7[i] == 'Strongly disagree':
            sys_just_7[i] = 1
        else:
            sys_just_7[i] = (float(sys_just_7[i]) - 1) / 6
    df['sysjust7'] = sys_just_7

    sys_just_8 = df['sysjust8'].tolist()
    for i in range(len(sys_just_8)):
        if sys_just_8[i] == ' ':
            sys_just_8[i] = random.uniform(0, 1)
        elif sys_just_8[i] == 'Strongly disagree':
            sys_just_8[i] = 0
        elif sys_just_8[i] == 'Strongly agree':
            sys_just_8[i] = 1
        else:
            sys_just_8[i] = (float(sys_just_8[i]) - 1) / 6
    df['sysjust8'] = sys_just_8

    df.to_csv('./data_files/mod_cleaned_data.csv')
    return


transform_data('./data_files/cleaned_data.csv')
