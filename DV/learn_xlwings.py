import xlwings as xw

filepath = "C:/Users/mushr/Desktop/433/联赛数据/前锋.xlsx"

app = xw.App(visible=False, add_book=False)
app.display_alerts = False
app.screen_updating = False
book = app.books.open(filepath)
print(book.fullname)  # 打印文件绝对路径
print(book.app)  # 查看进程
print(book.sheets)  # 又是一个类列表结构，存放各种Sheet对象
sheet = book.sheets['sheet1']

_list_name = sheet.range('A1:P1').value
_list_value = sheet.range('A2:P2').value
i = 0
for item in _list_value:
    if i == 13:
        num = float(item)
    print("%d-%s" % (i, _list_name[i]), end=":")
    print("".join(item.split()))
    i = i + 1

book.save()
# book.close()
app.kill()
