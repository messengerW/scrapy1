
# 看，这是一个例子，豆瓣top250里面有关电影的详细信息，就是这个标签：
# //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[1]
# 我把它打印在控制台，又摘了过来，仔细观察，这里面用到了两个函数.

# list = ['\n'
#         '                            导演: Steven Spielberg\xa0\xa0\xa0主演: '
#         'Henry Thomas / Dee Wallace / Robert MacNa...',
#         '\n'
#         '                            1982\xa0/\xa0美国\xa0/\xa0剧情 科幻\n'
#         '                        ']
#
# # 首先，看到上面这个元组里面有两个元素，中间用逗号隔开，然后用一个 for 循环处理这俩元素
# for str in list:
#     print('============== begin ==================')
#
#     print('执行split(),进行切片')
#     print(str.split())
#     print("\t")
#
#     print('执行join(),进行连接')
#     print("".join(str.split()))
#     print("\t")
#
#     print('===============end ===================')

list1 = ('\r\n'
           '\t\t\t\t\t\t\t\t\t\t\t\t\t\t23\r\n'
           '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n'
           '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t(4)\r\n'
           '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n'
           '\t\t\t\t\t\t\t\t\t\t\t\t\t')

print("".join(list1.split()))
print("===============================================================")

str = ('''
									2018-08-12
									
										23:00
									
								''')

print("".join(str.split()))
print(str.splitlines())
print("===============================================================")

#   下面这个例子是，处理字符串的，第一步str转list,第二步在list中插入，第三步list转str
date_str = "20190513"
print(date_str)
date_list = list(date_str)
print(date_list)
date_list.insert(4,'/')
date_list.insert(7,'/')
print(date_list)
date_str = ''.join(date_list)
print(date_str)
print("===============================================================")
