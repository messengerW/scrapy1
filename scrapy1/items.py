# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class StationItem(scrapy.Item):
    station = scrapy.Field()

class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()


class DetailItem(scrapy.Item):
    # 抓取内容：1.帖子标题；2.帖子作者；3.帖子回复数
    title = scrapy.Field()
    author = scrapy.Field()
    reply = scrapy.Field()


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    no = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    num = scrapy.Field()
    info = scrapy.Field()


# class PlayerItem(scrapy.Item):
#     no = scrapy.Field()
#     name = scrapy.Field()
#     club = scrapy.Field()
#     age = scrapy.Field()
#     position = scrapy.Field()
#     games = scrapy.Field()
#     goals = scrapy.Field()

# 因为每一轮的后台数据和赛季综合数据的属性不完全一样，所以用了两个item
# 2019-2020赛季，球员，turn
class PlayerTurnItem(scrapy.Item):

    playerId = scrapy.Field()                   # 球员id
    matchId = scrapy.Field()                    # 比赛id
    teamId = scrapy.Field()                     # 球队id
    playerMainPosition = scrapy.Field()         # 主要位置
    playerName = scrapy.Field()                 # 球员名字
    teamName = scrapy.Field()                   # 所属俱乐部
    offsides = scrapy.Field()                   # 越位
    offsideWon = scrapy.Field()                 #
    bigChanceCreated = scrapy.Field()           # 创造机会
    seriousError = scrapy.Field()               # 严重失误
    thBall = scrapy.Field()                     #
    longBall = scrapy.Field()                   #
    crosses = scrapy.Field()                    #
    passes = scrapy.Field()                     # 传球数
    keyPasses = scrapy.Field()                  # 关键传球
    yelCards = scrapy.Field()                   # 黄宝石卡
    redCards = scrapy.Field()                   # 红宝石卡
    aerialsWon = scrapy.Field()                 # 争顶成功
    rate = scrapy.Field()                       # 评分
    interceptions = scrapy.Field()              # 拦截
    age = scrapy.Field()                        # 年龄
    clearances = scrapy.Field()                 #
    shots = scrapy.Field()                      # 射门
    accThB = scrapy.Field()                     # 直塞
    accLB = scrapy.Field()                      # 长传
    accCrosses = scrapy.Field()                 # 传中
    finalThirdPass = scrapy.Field()             #
    finalThirdPassAcc = scrapy.Field()          #
    blockShots = scrapy.Field()                 # 封堵
    totalTackles = scrapy.Field()               # 抢断
    fouls = scrapy.Field()                      # 犯规
    fouled = scrapy.Field()                     # 被侵犯
    assists = scrapy.Field()                    # 助攻
    passSucc = scrapy.Field()                   # 传球成功率
    penaltyScored = scrapy.Field()              # 点球得分
    mins = scrapy.Field()                       # 上场时长
    goals = scrapy.Field()                      # 进球
    shotsOT = scrapy.Field()                    # 射正
    errorsSum = scrapy.Field()                  # 失误
    disp = scrapy.Field()
    dribbles = scrapy.Field()                   # 过人
    fatalError = scrapy.Field()
    unsTouches = scrapy.Field()

# 2019-2020赛季，球员，season
class PlayerSeasonItem(scrapy.Item):
    teamName = scrapy.Field()
    playerMainPosition = scrapy.Field()
    offsides = scrapy.Field()
    bigChanceCreated = scrapy.Field()
    passes = scrapy.Field()
    crosses = scrapy.Field()
    keyPasses = scrapy.Field()
    bigChanceSucc = scrapy.Field()
    interceptions = scrapy.Field()
    age = scrapy.Field()
    shots = scrapy.Field()
    bigChanceFaced = scrapy.Field()
    fouled = scrapy.Field()
    finalThirdPass = scrapy.Field()
    thBallSucc = scrapy.Field()
    assists = scrapy.Field()
    tackles = scrapy.Field()
    fouls = scrapy.Field()
    playerName = scrapy.Field()
    passSucc = scrapy.Field()
    country = scrapy.Field()
    goalProp = scrapy.Field()
    aerialWon = scrapy.Field()
    errorsSum = scrapy.Field()
    playerId = scrapy.Field()
    mans = scrapy.Field()
    apps = scrapy.Field()
    countryZh = scrapy.Field()
    redCards = scrapy.Field()
    disp = scrapy.Field()
    playerCountry = scrapy.Field()
    appsSub = scrapy.Field()
    thBall = scrapy.Field()
    teamId = scrapy.Field()
    finalThirdPassSucc = scrapy.Field()
    yelCards = scrapy.Field()
    rate = scrapy.Field()
    longBall = scrapy.Field()
    longBallSucc = scrapy.Field()
    shotsOTProp = scrapy.Field()
    dribbledPast = scrapy.Field()
    mins = scrapy.Field()
    blocks = scrapy.Field()
    shotsOT = scrapy.Field()
    goals = scrapy.Field()
    clears = scrapy.Field()
    crossSucc = scrapy.Field()
    offsideWon = scrapy.Field()
    dribbles = scrapy.Field()
    unsTouches = scrapy.Field()


# 球队，2019-2020赛季综合数据
class ClubSeasonItem(scrapy.Item):
    a_no = scrapy.Field()                         # 排名
    b_name = scrapy.Field()
    # shoot_total = scrapy.Field()                # 射门数
    # possession = scrapy.Field()                 # 控球率
    c_pass_completed_rate = scrapy.Field()        # 传球成功率
    # great_opportunity = scrapy.Field()          # 绝佳机会
    d_flying_header = scrapy.Field()              # 争顶成功
    e_mark = scrapy.Field()                       # 评分

    f_goals = scrapy.Field()                      # 进球
    g_shoot_total = scrapy.Field()                # 射门
    h_shoot_on_target = scrapy.Field()            # 射正
    i_great_opportunity = scrapy.Field()          # 绝佳机会
    j_seize_the_opportunity = scrapy.Field()      # 机会把握率
    k_dribble = scrapy.Field()                    # 过人
    l_violated = scrapy.Field()                   # 被侵犯
    m_offside = scrapy.Field()                    # 越位

    n_fumble = scrapy.Field()                     # 失球
    o_be_shoot = scrapy.Field()                   # 被射门
    p_intercept = scrapy.Field()                  # 抢断
    q_clearance_kick = scrapy.Field()             # 解围
    r_foul = scrapy.Field()                       # 犯规
    s_critical_miss = scrapy.Field()              # 致命失误

    t_assisting = scrapy.Field()                  # 助攻
    u_key_pass = scrapy.Field()                   # 关键传球
    v_possession = scrapy.Field()                 # 控球率
    w_pass_total = scrapy.Field()                 # 传球数
    x_PS = scrapy.Field()
    y_FTPS = scrapy.Field()

# 每一轮的数据
class ClubTurnItem(scrapy.Item):
    teamName = scrapy.Field()  # 俱乐部
    offsides = scrapy.Field()  # 越位
    bigChanceCreated = scrapy.Field()  # 创造机会
    passes = scrapy.Field()  # 传球数
    teamId = scrapy.Field()  # 球队id
    keyPasses = scrapy.Field()  # 关键传球
    yelCards = scrapy.Field()  # 黄宝石卡
    redCards = scrapy.Field()  # 红宝石卡
    aerialsWon = scrapy.Field()  # 争顶成功
    finalThirdPassAcc = scrapy.Field()  #
    rate = scrapy.Field()  # 评分
    interceptions = scrapy.Field()  # 拦截
    shots = scrapy.Field()  # 射门
    clearances = scrapy.Field()  #
    fouled = scrapy.Field()  # 被侵犯
    finalThirdPass = scrapy.Field()  #
    assists = scrapy.Field()  # 助攻
    fouls = scrapy.Field()  # 犯规
    passSucc = scrapy.Field()  # 传球成功率
    tacklesSuccful = scrapy.Field()
    goalsLost = scrapy.Field()
    goals = scrapy.Field()  # 进球
    shotsOT = scrapy.Field()  # 射正
    possession = scrapy.Field()  # 射正
    errorsSum = scrapy.Field()  # 失误
    offsideWon = scrapy.Field()  #
    aerialDuelScc = scrapy.Field()  #
    dribblesWon = scrapy.Field()  # 过人

# class ClubItem(scrapy.Item):
#     rank = scrapy.Field()
#     name = scrapy.Field()
#     turn = scrapy.Field()
#     win = scrapy.Field()
#     tie = scrapy.Field()
#     lose = scrapy.Field()
#     goals = scrapy.Field()
#     fumble = scrapy.Field()
#     delt = scrapy.Field()
#     score = scrapy.Field()


class GameItem(scrapy.Item):

    round = scrapy.Field()                         # 轮次
    date = scrapy.Field()                          # 比赛日期
    score = scrapy.Field()                         # 比分
    goals_total = scrapy.Field()                   # 进球数
    goals_home = scrapy.Field()                    # 主队进球数
    goals_away = scrapy.Field()                    # 客队进球数
    possession = scrapy.Field()                    # 控球率
    confrontation_win_rate = scrapy.Field()        # 对抗成功率
    dribble = scrapy.Field()                       # 过人
    intercept = scrapy.Field()                     # 抢断数
    mark = scrapy.Field()                          # 球队评分
    home_or_away = scrapy.Field()                  # 主客场

    # 射门相关
    shoot_total = scrapy.Field()                   # 射门数，详细分为 5 类
    shoot_positional = scrapy.Field()              # 阵地战
    shoot_placekick = scrapy.Field()               # 定位球
    shoot_counterattack = scrapy.Field()           # 反击
    penalty = scrapy.Field()                       # 点球
    own_goal = scrapy.Field()                      # 乌龙球
    shoot_on_target = scrapy.Field()               # 射正数

    # 传球相关
    pass_total = scrapy.Field()                    # 传球数
    pass_short = scrapy.Field()                    # 短传
    pass_long = scrapy.Field()                     # 长传
    pass_center = scrapy.Field()                   # 传中
    pass_through = scrapy.Field()                  # 直塞
    pass_completed_rate = scrapy.Field()           # 传球成功率

    points = scrapy.Field()                        # 积分