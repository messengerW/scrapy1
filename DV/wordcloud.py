import xlrd
from pyecharts import WordCloud

filepath = 'C:/Users/mushr/Desktop/433/premier.xlsx'
book = xlrd.open_workbook(filepath)
sheet = book.sheets()[0]

rows_num = sheet.nrows
cols_num = sheet.ncols

words = []

for i_row in range(1, rows_num):
    row = sheet.row_values(i_row)
    words.append(row[1])

print(words)

value = [10000, 9200, 5000, 4000, 3000,
         2000, 1800, 1700, 1600, 1600,
         1500, 1444, 1480, 1479, 1400,
         1000, 999, 880, 770, 600]

wordcloud = WordCloud(width=1300, height=620)
wordcloud.add('', words, value, word_size_range=[20, 100])
wordcloud.render('wordcloud.html')
