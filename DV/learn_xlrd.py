# 导入xlrd模块
import xlrd

# 设置文件名和路径
filepath = 'C:/Users/mushr/Desktop/433/premier.xlsx'

# 打开 excel
book = xlrd.open_workbook(filepath)

# 获取所有 sheet
sheets = book.sheet_names()

# 获取第一个 sheet
sheet = book.sheets()[0]

# 获取表的行数、列数
rows_num = sheet.nrows
cols_num = sheet.ncols

# 从第2行（下标1）开始读取到最后一行
for i_row in range(1,rows_num):
    # row = sheet.row_values(i_row)
    print(sheet.row_values(i_row)[:20])  # 打印列表的前20项

print("====================================================")

# 从第1列（下标0）开始读取到最后一列
for i_col in range(0,cols_num):
    col = sheet.col_values(i_col)       # 把sheet的每一列数据存进一个列表
    print('col%s: %s' % (i_col, col[1:21]))   # 打印列表的第 2~20 项数据

for i in range(2,5):
    print(i)