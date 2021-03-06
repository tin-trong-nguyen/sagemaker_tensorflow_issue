import numpy as np
import os
import tensorflow as tf
import pandas as pd

mean = pd.Series({'count_Battle_Mode_Lose': 0.21499715592449276,
 'count_Battle_Mode_Win': 0.09948158702528392,
 'count_Cecullar_User': 0.6843661823535239,
 'count_Challenge_beginer': 0.010052389552991077,
 'count_Challenge_share_Click': 5.7940640125700037e-05,
 'count_Challenge_share_Shared': 3.1150881788010773e-06,
 'count_Challenge_skilled': 0.005154224900644263,
 'count_Christmasbox_Click': 0.0027107497331926977,
 'count_Coin_exchange_Diamond_large': 0.0011905867019377718,
 'count_Coin_exchange_Diamond_medium': 0.00014765517967517107,
 'count_Coin_exchange_Diamond_small': 0.034738217334718095,
 'count_Coin_exchange_Life_large': 0.006088128336648826,
 'count_Coin_exchange_Life_medium': 0.010241163896626422,
 'count_Coin_exchange_Life_small': 0.05315212657724702,
 'count_ContinuePopup_show': 4.6044816150610774,
 'count_Continue_By_RewardVideo': 0.6178503274892202,
 'count_Continue_Game': 0.7560705280884386,
 'count_Continue_UseDiamond': 0.37944390691867314,
 'count_DailyAdsPopUp_Click': 0.016814622971532456,
 'count_DailyAdsPopUp_Show': 0.23979886498647118,
 'count_Dailyreward_claim': 0.09991084617632272,
 'count_Dailyreward_show': 0.26220756330949463,
 'count_EventBox_Click': 3.723132208703432,
 'count_FB_Invite_Friend_Click': 0.002761214161689275,
 'count_FB_Invite_Friend_Click_setting': 0.0007071250165878446,
 'count_Favorite_chose': 0.3821951527981903,
 'count_Fb_Invite_Success_setting': 0.0006952876815084004,
 'count_Free_open_treasure_hunt': 0.01633739146254013,
 'count_Freetrial_pack_show': 0.0,
 'count_Freetrial_pack_start': 0.0,
 'count_FriendLeaderboard_share_Click': 0.001055391874977805,
 'count_FriendLeaderboard_share_Shared': 9.532169827131297e-05,
 'count_FriendsongLeaderboard_share_Click': 0.001956898393922837,
 'count_FriendsongLeaderboard_share_Shared': 0.00023612368395312165,
 'count_FullAds_Click': 0.43100671550709585,
 'count_FullAds_Show': 3.240631216547847,
 'count_GACHA_BUY_KEY': 4.984141086081724e-06,
 'count_Gacha_Openby_key': 0.00012335749188052266,
 'count_Gacha_watch_video': 0.003305108557707943,
 'count_GlobalLeaderboard_share_Click': 9.594471590707318e-05,
 'count_GlobalLeaderboard_share_Shared': 6.8531939933623704e-06,
 'count_GlobalsongLeaderboard_share_Click': 0.00041368371014478307,
 'count_GlobalsongLeaderboard_share_Shared': 4.9218393225057024e-05,
 'count_Largeruby_Purchase': 3.4888987602572065e-05,
 'count_Largeruby_Purchase_2': 4.984141086081724e-06,
 'count_Largeruby_Purchase_3': 3.1150881788010773e-06,
 'count_Leadboard_click': 0.020230628668405717,
 'count_LevelReward_Claim': 0.14640852138601487,
 'count_LevelReward_Seen': 1.18754076871654,
 'count_MP_Custom_Joinroom': 0.0160763470731566,
 'count_MP_Custom_finish': 0.040578384652334355,
 'count_MP_Onboarding_Showpopup': 0.06367053332178674,
 'count_MP_Onboarding_Showpopup_Yes': 0.013702026863274418,
 'count_MP_Play_Click': 0.03547711625072971,
 'count_MP_Player_Battle': 0.012772484550720177,
 'count_OnRoomKickout': 0.02110036128792698,
 'count_Online_share_Click': 0.0018030130378900635,
 'count_Online_share_Shared': 5.607158721841939e-05,
 'count_Quest_Claimed': 0.017356025297008082,
 'count_RankUp_share_Click': 0.0004535568388334369,
 'count_RankUp_share_Shared': 0.00012024240370172158,
 'count_RateBtnClick': 0.0400170457625144,
 'count_RemoveAds_Click': 0.16643417725225548,
 'count_Result_share_Click': 0.02764391551631652,
 'count_Result_share_Shared': 0.00021992522542335605,
 'count_Setting_Click': 0.0040259399622825124,
 'count_Smallruby_Purchase': 8.84685042779506e-05,
 'count_Smallruby_Purchase_2': 7.476211629122585e-06,
 'count_Smallruby_Purchase_3': 3.1150881788010773e-06,
 'count_Song_start': 11.038520557401418,
 'count_StarterPack_Btn_Click': 1.495242325824517e-05,
 'count_StarterPack_Popup_Click': 5.607158721841939e-06,
 'count_StarterPack_Popup_Show': 0.00023238557813856037,
 'count_Tutorial_Setting': 0.0004398504508467121,
 'count_User_Deny_PN': 0.012415495445429574,
 'count_VideoAds_Finish': 1.1616705844092328,
 'count_Vippass_Click': 0.039655695533773475,
 'count_Wifi_User': 1.4212016639555016,
 'count_coin_spent_2': 0.2769076644252569,
 'count_friendchallenge_sent': 0.002596114488212818,
 'count_notification_dismiss': 0.00991470265548807,
 'count_notification_foreground': 0.0003171159766019497,
 'count_notification_open': 0.0005544856958265917,
 'count_notification_receive': 0.01870610451370047,
 'count_ruby_spent_purchasesong_2': 0.12859021700327272,
 'count_tutorial_start': 0.0,
 'count_unlimited_life_puschased': 2.1182599615847325e-05,
 'is_Battle_Mode_play': 0.052285509045904566,
 'is_FB_login_all': 0.18897370927878857,
 'is_LeadboardSong_click': 0.010478533615851065,
 'is_LikeFanpage': 0.00010528998044347641,
 'is_RemoveAds_Purchased': 0.00014454009149637,
 'is_VideoAds_Show': 0.4156044735158318,
 'is_Vippass_purchased': 1.682147616552582e-05,
 'sum_engagement_time_sec': 1223819.2355156187})

std = pd.Series({'count_Battle_Mode_Lose': 2.6172191963440676,
 'count_Battle_Mode_Win': 1.6396210788882692,
 'count_Cecullar_User': 2.1739262351410042,
 'count_Challenge_beginer': 0.13042766142839718,
 'count_Challenge_share_Click': 0.0082404833098889,
 'count_Challenge_share_Shared': 0.001764958491023027,
 'count_Challenge_skilled': 0.1219545026842792,
 'count_Christmasbox_Click': 0.18000044498642925,
 'count_Coin_exchange_Diamond_large': 0.63115405075642,
 'count_Coin_exchange_Diamond_medium': 0.034576712408215644,
 'count_Coin_exchange_Diamond_small': 0.30878153664874985,
 'count_Coin_exchange_Life_large': 0.5500093334642786,
 'count_Coin_exchange_Life_medium': 0.15436633071204642,
 'count_Coin_exchange_Life_small': 0.5026809030130486,
 'count_ContinuePopup_show': 13.469447766995506,
 'count_Continue_By_RewardVideo': 2.8340672551622945,
 'count_Continue_Game': 2.340461793975395,
 'count_Continue_UseDiamond': 1.7273236121764621,
 'count_DailyAdsPopUp_Click': 0.14739104586872007,
 'count_DailyAdsPopUp_Show': 0.6350941021413091,
 'count_Dailyreward_claim': 0.4335498565559809,
 'count_Dailyreward_show': 0.7643722899979692,
 'count_EventBox_Click': 10.238933527672035,
 'count_FB_Invite_Friend_Click': 0.09927734336556157,
 'count_FB_Invite_Friend_Click_setting': 0.053952399261898605,
 'count_Favorite_chose': 1.7079600824430157,
 'count_Fb_Invite_Success_setting': 0.05365728363900456,
 'count_Free_open_treasure_hunt': 0.1414098237153011,
 'count_Freetrial_pack_show': 1.0,
 'count_Freetrial_pack_start': 1.0,
 'count_FriendLeaderboard_share_Click': 0.038621708963753526,
 'count_FriendLeaderboard_share_Shared': 0.01032118837581305,
 'count_FriendsongLeaderboard_share_Click': 0.059134648422100776,
 'count_FriendsongLeaderboard_share_Shared': 0.018859674324453134,
 'count_FullAds_Click': 1.6868140762324833,
 'count_FullAds_Show': 7.790339895058968,
 'count_GACHA_BUY_KEY': 0.002496027146471187,
 'count_Gacha_Openby_key': 0.018170969426142953,
 'count_Gacha_watch_video': 0.063722025290525,
 'count_GlobalLeaderboard_share_Click': 0.011273260056735374,
 'count_GlobalLeaderboard_share_Shared': 0.002617851605248294,
 'count_GlobalsongLeaderboard_share_Click': 0.024041406609782497,
 'count_GlobalsongLeaderboard_share_Shared': 0.007932361487061647,
 'count_Largeruby_Purchase': 0.005906587031533686,
 'count_Largeruby_Purchase_2': 0.002232513436561926,
 'count_Largeruby_Purchase_3': 0.0017649584910225265,
 'count_Leadboard_click': 0.30327259810921153,
 'count_LevelReward_Claim': 0.5533389339152858,
 'count_LevelReward_Seen': 5.403399966662634,
 'count_MP_Custom_Joinroom': 0.4852399215697381,
 'count_MP_Custom_finish': 0.8802231883846808,
 'count_MP_Onboarding_Showpopup': 0.24538682409261048,
 'count_MP_Onboarding_Showpopup_Yes': 0.11781602477103016,
 'count_MP_Play_Click': 1.159687197999266,
 'count_MP_Player_Battle': 0.15505393192391909,
 'count_OnRoomKickout': 0.3571850511944458,
 'count_Online_share_Click': 0.05272942196317967,
 'count_Online_share_Shared': 0.00871808508448649,
 'count_Quest_Claimed': 0.24615040124862764,
 'count_RankUp_share_Click': 0.024931223128482474,
 'count_RankUp_share_Shared': 0.013371297739137072,
 'count_RateBtnClick': 0.22516736786894953,
 'count_RemoveAds_Click': 0.5840568182168946,
 'count_Result_share_Click': 0.20950678998154987,
 'count_Result_share_Shared': 0.015526089589238854,
 'count_Setting_Click': 0.113056711791574,
 'count_Smallruby_Purchase': 0.009405353667070305,
 'count_Smallruby_Purchase_2': 0.0027342559747502064,
 'count_Smallruby_Purchase_3': 0.001764958491024076,
 'count_Song_start': 22.04789732665435,
 'count_StarterPack_Btn_Click': 0.004865639380796397,
 'count_StarterPack_Popup_Click': 0.004101395460715801,
 'count_StarterPack_Popup_Show': 0.04208545040054546,
 'count_Tutorial_Setting': 0.05910743974254368,
 'count_User_Deny_PN': 0.2945852853272361,
 'count_VideoAds_Finish': 4.853509600417644,
 'count_Vippass_Click': 0.29070886054125145,
 'count_Wifi_User': 2.5977332998354865,
 'count_coin_spent_2': 1.266127410753305,
 'count_friendchallenge_sent': 0.10079205798229571,
 'count_notification_dismiss': 0.09924111166151958,
 'count_notification_foreground': 0.017839883669250434,
 'count_notification_open': 0.0235409906640343,
 'count_notification_receive': 0.13565963109148615,
 'count_ruby_spent_purchasesong_2': 0.430889258156226,
 'count_tutorial_start': 1.0,
 'count_unlimited_life_puschased': 0.0046024070781785125,
 'is_Battle_Mode_play': 0.2226021890948212,
 'is_FB_login_all': 0.3914877347747488,
 'is_LeadboardSong_click': 0.10182698045791462,
 'is_LikeFanpage': 0.010260550397694487,
 'is_RemoveAds_Purchased': 0.01202161385418954,
 'is_VideoAds_Show': 0.4928259277966343,
 'is_Vippass_purchased': 0.004101364797645731,
 'sum_engagement_time_sec': 2364416.938211433})

data_columns = ['is_FB_login_all',
 'is_RemoveAds_Purchased',
 'is_VideoAds_Show',
 'is_Battle_Mode_play',
 'is_LeadboardSong_click',
 'is_Vippass_purchased',
 'is_LikeFanpage',
 'sum_engagement_time_sec',
 'count_coin_spent_2',
 'count_ruby_spent_purchasesong_2',
 'count_Vippass_Click',
 'count_VideoAds_Finish',
 'count_RemoveAds_Click',
 'count_Battle_Mode_Win',
 'count_Battle_Mode_Lose',
 'count_MP_Custom_finish',
 'count_MP_Custom_Joinroom',
 'count_MP_Onboarding_Showpopup',
 'count_MP_Onboarding_Showpopup_Yes',
 'count_MP_Play_Click',
 'count_MP_Player_Battle',
 'count_unlimited_life_puschased',
 'count_Largeruby_Purchase',
 'count_Largeruby_Purchase_2',
 'count_Largeruby_Purchase_3',
 'count_Smallruby_Purchase',
 'count_Smallruby_Purchase_2',
 'count_Smallruby_Purchase_3',
 'count_Song_start',
 'count_FullAds_Click',
 'count_FullAds_Show',
 'count_StarterPack_Btn_Click',
 'count_StarterPack_Popup_Click',
 'count_StarterPack_Popup_Show',
 'count_Cecullar_User',
 'count_Wifi_User',
 'count_Challenge_beginer',
 'count_Challenge_skilled',
 'count_Challenge_share_Click',
 'count_Challenge_share_Shared',
 'count_Christmasbox_Click',
 'count_Continue_By_RewardVideo',
 'count_Continue_UseDiamond',
 'count_Continue_Game',
 'count_ContinuePopup_show',
 'count_DailyAdsPopUp_Show',
 'count_DailyAdsPopUp_Click',
 'count_Dailyreward_show',
 'count_Dailyreward_claim',
 'count_EventBox_Click',
 'count_FB_Invite_Friend_Click',
 'count_FB_Invite_Friend_Click_setting',
 'count_Fb_Invite_Success_setting',
 'count_Free_open_treasure_hunt',
 'count_Freetrial_pack_show',
 'count_Freetrial_pack_start',
 'count_friendchallenge_sent',
 'count_FriendLeaderboard_share_Click',
 'count_FriendLeaderboard_share_Shared',
 'count_FriendsongLeaderboard_share_Click',
 'count_FriendsongLeaderboard_share_Shared',
 'count_GACHA_BUY_KEY',
 'count_Gacha_Openby_key',
 'count_Gacha_watch_video',
 'count_GlobalLeaderboard_share_Click',
 'count_GlobalLeaderboard_share_Shared',
 'count_GlobalsongLeaderboard_share_Click',
 'count_GlobalsongLeaderboard_share_Shared',
 'count_Leadboard_click',
 'count_LevelReward_Claim',
 'count_LevelReward_Seen',
 'count_notification_dismiss',
 'count_notification_foreground',
 'count_notification_open',
 'count_notification_receive',
 'count_User_Deny_PN',
 'count_Online_share_Click',
 'count_Online_share_Shared',
 'count_OnRoomKickout',
 'count_Quest_Claimed',
 'count_RankUp_share_Click',
 'count_RankUp_share_Shared',
 'count_RateBtnClick',
 'count_Result_share_Click',
 'count_Result_share_Shared',
 'count_Setting_Click',
 'count_Tutorial_Setting',
 'count_tutorial_start',
 'count_Coin_exchange_Diamond_large',
 'count_Coin_exchange_Diamond_medium',
 'count_Coin_exchange_Diamond_small',
 'count_Coin_exchange_Life_large',
 'count_Coin_exchange_Life_medium',
 'count_Coin_exchange_Life_small',
 'count_Favorite_chose']

columns_default = [[0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0.0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0],
 [0]]

def _parse_line(line, label):
    columns_default_wi = [[0]] + columns_default
    line_data = tf.decode_csv(line, record_defaults=columns_default_wi)
    del line_data[0]
    features = dict(zip(data_columns, line_data))
    label = features.pop(label)
    return features, label

def _generate_input_fn(data_dir, filename, label):
    file_dir = os.path.join(data_dir, filename)
    dataset = tf.data.TextLineDataset(file_dir).skip(1)
    dataset = dataset.map(lambda x: _parse_line(x, label))
    return dataset

def train_input_fn(data_dir, params):
    return _generate_input_fn(data_dir, filename=params['train_filename'], label=params['label']) \
            .shuffle(buffer_size=params['shuffle_buffer_size']) \
            .repeat() \
            .batch(params['batch_size'])

def eval_input_fn(data_dir, params):
    return _generate_input_fn(data_dir, filename=params['test_filename'], label=params['label']) \
            .batch(params['batch_size'])

def cas(x, col):
    return (x - mean[col]) / std[col]

def estimator_fn(run_config, params):
    feature_columns = []
    for col in data_columns:
        if (col == params['label']):
            pass
        else:
            feature_columns.append(tf.feature_column.numeric_column(key=col, normalizer_fn=lambda x: cas(x, col=col)))
    estimator = tf.estimator.DNNClassifier(hidden_units=params['hidden_units'],
                                          feature_columns=feature_columns,
                                          n_classes=2,
                                          optimizer=tf.train.AdamOptimizer(learning_rate=params['learning_rate']),
                                          activation_fn=tf.tanh,
                                          loss_reduction=tf.losses.Reduction.MEAN,
                                          config=run_config)
    return estimator