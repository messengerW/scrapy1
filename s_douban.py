import json
import csv
import pymysql

with open('file/douban.json') as f:
    rownum = 0
    new_list = json.load(f)
    for item in new_list:
        rownum += 1
        # 看了一下原网页，167 和 217 没有影片简介，所以判断一下
        if rownum == 167 or rownum == 217:
            print("No.{}《{}》  info:{}   point:{}.".format(
                item['no'][0],
                item['movie_name'][0],
                "None",
                item['star'][0]
            ))
        else:
            print("No.{}《{}》  info:{}   point:{}.".format(
                item['no'][0],
                item['movie_name'][0],
                item['describe'][0],
                item['star'][0]
            ))
