class Participant:
    def __init__(self, location, experimenter_gender, experimenter_race, exp_run_after, compensation, recruitment,
                 separated, sunk_group, sunk_dv, gain_loss_group, gain_loss_dv, anchor_group_1, anchor_group_2,
                 anchor_group_3, anchor_group_4, gambler_fallacy_group, scales_group_tv, reciprocity_group,
                 allowed_forbidden_group, quote_group, flag_group, flag_filter, money_group, money_filter,
                 contact_group, iat_filter, iat_exp_filter, citizenship, ethnicity, native_language, race, age, gender,
                 anchor_answer_1, anchor_answer_2, anchor_answer_3, anchor_answer_4, reciprocity_us, reciprocity_other,
                 allowed_forbidden, quote, total_flag_estimations, total_no_flag_time_estimations, iat_expart,
                 iat_expmath, iat_expall, total_exp_missed, art_warm, disease_framing_a, disease_framing_b, flag_dv1,
                 flag_dv2, flag_dv3, flag_dv4, flag_dv5, flag_dv6, flag_dv7, flag_dv8, flag_supplement_1,
                 flag_supplement_2, flag_supplement_3, flag_time_estimate_1, flag_time_estimate_2, flag_time_estimate_3,
                 flag_time_estimate_4, gambler_fallacy_a, gambler_fallacy_b, iat_explicit_art_1, iat_explicit_art_2,
                 iat_explicit_art_3, iat_explicit_art_4, iat_explicit_art_5, iat_explicit_art_6, iat_explicit_math_1,
                 iat_explicit_math_2, iat_explicit_math_3, iat_explicit_math_4, iat_explicit_math_5,
                 iat_explicit_math_6, imagined_explicit_1, imagined_explicit_2, imagined_explicit_3,
                 imagined_explicit_4, major, math_warm, money_age_a, money_age_b, money_gender_a, money_gender_b,
                 no_flag_time_estimate_1, no_flag_time_estimate_2, no_flag_time_estimate_3, no_flag_time_estimate_4,
                 political_id, omd_imc3, quote_a, quote_b, scales_a, scales_b, sunk_cost_a, sunk_cost_b, sys_just_1,
                 sys_just_2, sys_just_3, sys_just_4, sys_just_5, sys_just_6, sys_just_7, sys_just_8):

        ######################## yes = 0, no = 1 for reciprocity ################################

        ############################### Decision Tree Variables ###########################
        # 'referrer'
        self.location = location

        # 'expgender'
        self.experimenter_gender = experimenter_gender

        # 'exprace'
        self.experimenter_race = experimenter_race

        # 'exprunafter'
        self.exp_run_after = exp_run_after

        # 'compensation'
        self.compensation = compensation

        # 'recruitment'
        self.recruitment = recruitment

        # 'separatedon'
        self.separated = separated

        # 'sunk_group'
        self.sunk_group = sunk_group

        # 'sunk_dv'
        self.sunk_dv = sunk_dv

        # 'gain_loss_group'
        self.gain_loss_group = gain_loss_group

        # 'gain_loss_dv'
        self.gain_loss_dv = gain_loss_dv

        # 'anchor_group_1'
        self.anchor_group_1 = anchor_group_1

        # 'anchor_group_2'
        self.anchor_group_2 = anchor_group_2

        # 'anchor_group_3'
        self.anchor_group_1 = anchor_group_3

        # 'anchor_group_4'
        self.anchor_group_4 = anchor_group_4

        # 'gambler_fallacy_group'
        self.gambler_fallacy_group = gambler_fallacy_group

        # 'scales_group_tv'
        self.scales_group_tv = scales_group_tv

        # 'reciprocity_group' talks about asking North Korea
        self.reciprocity_group = reciprocity_group

        # 'allowed_forbidden_group'
        self.allowed_forbidden_group = allowed_forbidden_group

        # 'quote_group' liked source = washington vs disliked quote = bin laden
        self.quote_group = quote_group

        # 'flag_group'
        self.flag_group = flag_group

        # 'flag_filter'
        self.flag_filter = flag_filter

        # 'money_group'
        self.money_group = money_group

        # 'money_filter'
        self.money_filter = money_filter

        # 'contact_group'
        self.contact_group = contact_group

        # 'iat_filter'
        self.iat_filter = iat_filter

        # 'iat_exp_filter'
        self.iat_exp_filter = iat_exp_filter

        # 'citizenship'
        self.citizenship = citizenship

        # 'ethnicity'
        self.ethnicity = ethnicity

        # 'native_language'
        self.native_language = native_language

        # 'race'
        self.race = race

        ########################### Neural Network Variables ###########################
        # 'participant age' normalized from 1 to 100
        self.age = age

        # 'participant gender' caution! uses 'sex' column not 'partgender'
        self.gender = gender

        # 'anchor_answer_1' calculated as percent error normalized from 0 to 1 look up correct answers
        self.anchor_answer_1 = anchor_answer_1

        # 'anchor_answer_1' calculated as percent error normalized from 0 to 1 look up correct answers
        self.anchor_answer_2 = anchor_answer_2

        # 'anchor_answer_1' calculated as percent error normalized from 0 to 1 look up correct answers
        self.anchor_answer_3 = anchor_answer_3

        # 'anchor_answer_1' calculated as percent error normalized from 0 to 1 look up correct answers
        self.anchor_answer_4 = anchor_answer_4

        # 'reciprocity_us' 0 = yes, 1 = no
        self.reciprocity_us = reciprocity_us

        # 'reciprocity_other' 0 = yes, 1 = no
        self.reciprocity_other = reciprocity_other

        # 'allowed_forbidden'
        self.allowed_forbidden = allowed_forbidden

        # 'quote' normalized from 1 to 9
        self.quote = quote

        # 'total_flag_estimations' 4 to 12 normalized from 0 to 1
        self.total_flag_estimations = total_flag_estimations

        # 'total_no_flag_time_estimations' 4 to 12 normalized from 0 to 1
        self.total_no_flag_time_estimations = total_no_flag_time_estimations

        # 'iatexpart' norm from 2 to 7
        self.iat_expart = iat_expart

        # 'iatexpmath' norm from 2 to 7
        self.iat_expmath = iat_expmath

        # 'iatexpall' norm from 1 to 7
        self.iat_expall = iat_expall

        # 'totalexpmissed' norm from 1 to 12
        self.total_exp_missed = total_exp_missed

        # 'artwarm' norm 0 to 100
        self.art_warm = art_warm

        # 'disease_framing_a'
        self.disease_framing_a = disease_framing_a

        # 'disease_framing_b'
        self.disease_framing_b = disease_framing_b

        # 'flag_dv1' normalize 1 to 7
        self.flag_dv1 = flag_dv1

        # 'flag_dv2' normalize 1 to 7
        self.flag_dv2 = flag_dv2

        # 'flag_dv3' normalize 1 to 7
        self.flag_dv3 = flag_dv3

        # 'flag_dv4' normalize 1 to 7
        self.flag_dv4 = flag_dv4

        # 'flag_dv5' normalize 1 to 7
        self.flag_dv5 = flag_dv5

        # 'flag_dv6' normalize 1 to 7
        self.flag_dv6 = flag_dv6

        # 'flag_dv7' normalize 1 to 7
        self.flag_dv7 = flag_dv7

        # 'flag_dv8' normalize 1 to 7
        self.flag_dv8 = flag_dv8

        # 'flag_supplement_1' normalize 1 to 10 (not at all = 1, very much = 10)
        self.flag_supplement_1 = flag_supplement_1

        # 'flag_supplement_2' normalize 1 to 7, democrat = 1, republican = 7
        self.flag_supplement_2 = flag_supplement_2

        # 'flag_supplement_3' normalize 1 to 7, liberal = 1, conservative = 7
        self.flag_supplement_3 = flag_supplement_3

        # 'flag_time_estimate_1' morning = 0, afternoon = 0.5, evening = 1
        self.flag_time_estimate_1 = flag_time_estimate_1

        # 'flag_time_estimate_2' morning = 0, afternoon = 0.5, evening = 1
        self.flag_time_estimate_2 = flag_time_estimate_2

        # 'flag_time_estimate_3' morning = 0, afternoon = 0.5, evening = 1
        self.flag_time_estimate_3 = flag_time_estimate_3

        # 'flag_time_estimate_4' morning = 0, afternoon = 0.5, evening = 1
        self.flag_time_estimate_4 = flag_time_estimate_4

        # 'gambler_fallacy_a' norm 0 to 25
        self.gambler_fallacy_a = gambler_fallacy_a

        # 'gambler_fallacy_b' norm 0 to 25
        self.gambler_fallacy_b = gambler_fallacy_b

        # iat_explicit_art_1 norm 4 to 7, moderately = 4, very = 7
        self.iat_explicit_art_1 = iat_explicit_art_1

        # iat_explicit_art_1 norm 4 to 7, moderately = 4, very = 7
        self.iat_explicit_art_2 = iat_explicit_art_2

        # iat_explicit_art_1 norm 4 to 7, moderately = 4, very = 7
        self.iat_explicit_art_3 = iat_explicit_art_3

        # iat_explicit_art_1 norm 4 to 7, moderately = 4, very = 7
        self.iat_explicit_art_4 = iat_explicit_art_4

        # iat_explicit_art_1 norm 4 to 7, moderately = 4, very = 7
        self.iat_explicit_art_5 = iat_explicit_art_5

        # iat_explicit_art_1 norm 4 to 7, moderately = 4, very = 7
        self.iat_explicit_art_6 = iat_explicit_art_6

        # iat_explicit_math_1 norm 4 to 6, slightly = 4, moderately = 5, very = 6
        self.iat_explicit_math_1 = iat_explicit_math_1

        # iat_explicit_math_1 norm 4 to 6, slightly = 4, moderately = 5, very = 6
        self.iat_explicit_math_2 = iat_explicit_math_2

        # iat_explicit_math_1 norm 4 to 6, slightly = 4, moderately = 5, very = 6
        self.iat_explicit_math_3 = iat_explicit_math_3

        # iat_explicit_math_1 norm 4 to 6, slightly = 4, moderately = 5, very = 6
        self.iat_explicit_math_4 = iat_explicit_math_4

        # iat_explicit_math_1 norm 4 to 6, slightly = 4, moderately = 5, very = 6
        self.iat_explicit_math_5 = iat_explicit_math_5

        # iat_explicit_math_1 norm 4 to 6, slightly = 4, moderately = 5, very = 6
        self.iat_explicit_math_6 = iat_explicit_math_6

        # imagined_explicit_1 norm 1 through 9
        self.imagined_explicit_1 = imagined_explicit_1

        # imagined_explicit_1 norm 1 through 9
        self.imagined_explicit_2 = imagined_explicit_2

        # imagined_explicit_1 norm 1 through 9
        self.imagined_explicit_3 = imagined_explicit_3

        # imagined_explicit_1 norm 1 through 9
        self.imagined_explicit_4 = imagined_explicit_4

        # major norm 1 to 13
        self.major = major

        # math_warm norm 0 to 100
        self.math_warm = math_warm

        # money_age_a to 1 to 100
        self.money_age_a = money_age_a

        # money_age_b to 1 to 100
        self.money_age_b = money_age_b

        # money_gender_a
        self.money_gender_a = money_gender_a

        # money_gender_b
        self.money_gender_b = money_gender_b

        # no_flag_time_estimate_1 norm morning = 0, afternoon = 0.5, evening = 1
        self.no_flag_time_estimate_1 = no_flag_time_estimate_1

        # no_flag_time_estimate_1 norm morning = 0, afternoon = 0.5, evening = 1
        self.no_flag_time_estimate_2 = no_flag_time_estimate_2

        # no_flag_time_estimate_1 norm morning = 0, afternoon = 0.5, evening = 1
        self.no_flag_time_estimate_3 = no_flag_time_estimate_3

        # no_flag_time_estimate_1 norm morning = 0, afternoon = 0.5, evening = 1
        self.no_flag_time_estimate_4 = no_flag_time_estimate_4

        # political_id norm 1 to 7, 1 = strong lib, 2 = mod lib, 3 = slight lib, 4 = neutral, 5 = slight cons,
        # 6 = mod cons, 7 = strong cons
        self.political_id = political_id

        # omd_imc3 fail = 0, pass = 1
        self.omd_imc3 = omd_imc3

        # quote_a norm 1 to 9
        self.quote_a = quote_a

        # quote_b norm 1 to 9
        self.quote_b = quote_b

        # scales_a 1 = up to half hour, 2 = 0.5 hour to 1 hour, 3 = one to 1.5 hours, 4 = 1.5 to 2, 5 = 2 to 2.5
        # 6 = more than 2.5
        self.scales_a = scales_a

        # scales_b 1 = up to 2.5, 2 = 2.5 hour to 3 hour, 3 = 3 to 3.5 hours, 4 = 3.5 to 4, 5 = 4 to 4.5
        # 6 = more than 4.5
        self.scales_b = scales_b

        # sunk_cost_a norm 1 to 9
        self.sunk_cost_a = sunk_cost_a

        # sunk_cost_b norm 1 to 9
        self.sunk_cost_b = sunk_cost_b

        # sys_just_1 norm 1 to 7 strong disagree = 1, strong agree = 7
        self.sys_just_1 = sys_just_1

        # sys_just_1 norm 1 to 7 strong disagree = 1, strong agree = 7
        self.sys_just_2 = sys_just_2

        # sys_just_1 norm 1 to 7 !!!!!!!!!!!! strong agree = 1, strong disagree = 7 !!!!!!!!!!
        self.sys_just_3 = sys_just_3

        # sys_just_1 norm 1 to 7 strong disagree = 1, strong agree = 7
        self.sys_just_4 = sys_just_4

        # sys_just_1 norm 1 to 7 strong disagree = 1, strong agree = 7
        self.sys_just_5 = sys_just_5

        # sys_just_1 norm 1 to 7 strong disagree = 1, strong agree = 7
        self.sys_just_6 = sys_just_6

        # sys_just_1 norm 1 to 7 !!!!!!!!!! strong agree = 1, strong disagree = 7 !!!!!!!!!!!!
        self.sys_just_7 = sys_just_7

        # sys_just_1 norm 1 to 7 strong disagree = 1, strong agree = 7
        self.sys_just_8 = sys_just_8
