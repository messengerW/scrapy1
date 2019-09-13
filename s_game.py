import json
import csv
import pymysql

with open('file/game.json') as f:
    new_list = json.load(f)
    for item in new_list:
        print('''turn:{}    score:{}    date:{}
                possession:{}   shot:{}     shot_1:{}
                shot_2:{}   shot_3:{}   shot_4:{}
                shot_5:{}   shot_on_target:{}   goals:{}
                vs_win_rate:{}  guoren:{}   intercept:{}    mark:{}'''
            .format(
            item['turn'][0],
            item['score'][0],
            item['date'][0],
            item['possession'][0],
            item['shot'][0],
            item['shot_1'][0],
            item['shot_2'][0],
            item['shot_3'][0],
            item['shot_4'][0],
            item['shot_5'][0],
            item['shot_on_target'][0],
            item['goals'][0],
            item['vs_win_rate'][0],
            item['guoren'][0],
            item['intercept'][0],
            item['mark'][0]
        ))
