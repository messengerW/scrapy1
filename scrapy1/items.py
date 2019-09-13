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


class PlayerItem(scrapy.Item):
    no = scrapy.Field()
    name = scrapy.Field()
    club = scrapy.Field()
    age = scrapy.Field()
    position = scrapy.Field()
    games = scrapy.Field()
    goals = scrapy.Field()

# 球员，2019-2020赛季
class Test1Item(scrapy.Item):
    name = scrapy.Field()

# 球队，2019-2020赛季
class Test2Item(scrapy.Item):
    name = scrapy.Field()
    # shoot_total = scrapy.Field()                # 射门数
    # possession = scrapy.Field()                 # 控球率
    pass_completed_rate = scrapy.Field()        # 传球成功率
    # great_opportunity = scrapy.Field()          # 绝佳机会
    flying_header = scrapy.Field()              # 争顶成功
    mark = scrapy.Field()                       # 评分

    goals = scrapy.Field()                      # 进球
    shoot_total = scrapy.Field()                # 射门
    shoot_on_target = scrapy.Field()            # 射正
    great_opportunity = scrapy.Field()          # 绝佳机会
    seize_the_opportunity = scrapy.Field()      # 机会把握率
    dribble = scrapy.Field()                    # 过人
    violated = scrapy.Field()                   # 被侵犯
    offside = scrapy.Field()                    # 越位

    fumble = scrapy.Field()                     # 失球
    be_shoot = scrapy.Field()                   # 被射门
    intercept = scrapy.Field()                  # 抢断
    clearance_kick = scrapy.Field()             # 解围
    foul = scrapy.Field()                       # 犯规
    critical_miss = scrapy.Field()              # 致命失误

    assisting = scrapy.Field()                  # 助攻
    key_pass = scrapy.Field()                   # 关键传球
    possession = scrapy.Field()                 # 控球率
    pass_total = scrapy.Field()                 # 传球数
    PS = scrapy.Field()
    FTPS = scrapy.Field()

class ClubItem(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    turn = scrapy.Field()
    win = scrapy.Field()
    tie = scrapy.Field()
    lose = scrapy.Field()
    goals = scrapy.Field()
    fumble = scrapy.Field()
    delt = scrapy.Field()
    score = scrapy.Field()


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