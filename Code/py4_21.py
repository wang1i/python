year = eval(input("输入年份："))
m = eval(input("输入月份："))
q = eval(input("输入天数："))
if m < 3 :
    m += 12
    year -= 1
j = year // 100
k = year % 100
h = (q + 26 * (m + 1) // 10 + k + k // 4 + j // 4 + 5 * j) % 7
print(h)