import json

with open('file/items.json') as f:
    rownum = 0
    new_list = json.load(f)
    for i in new_list:
        rownum += 1
        print("""line{}:  title:{},  author:{},  reply:{}.""".format(rownum,
                                                                     i['title'][0],
                                                                     i['author'][0],
                                                                     i['reply'][0]))