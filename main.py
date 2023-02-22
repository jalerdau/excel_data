import xlrd

file_Location = "C:/Users/Dou/Desktop/公示公告成果/历史遗留矿山核查图斑数据2022-06-20 11_13.xls"
workbook = xlrd.open_workbook(file_Location)
sheet = workbook.sheet_by_name('Export')

curr_col = 5
goal_col = 6
k_col =10
col1 = sheet.col(curr_col)
col2 = sheet.col(goal_col)
col3 = sheet.col(k_col)


# 提取列数据
# for i in col1:
#     if i!=None:
#         it=i.value
#         print(it)


# 比较列数据
for i in col1:
    for j in col2:
        if i.value==j.value:
            print(i.value)

# 选择出长列中不等于短列的数据

# a = set(col1)
# b = set(col2)
# c = a - b
#
# for i in c:
#     print(i.value)