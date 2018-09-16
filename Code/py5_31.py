year = eval(input("输入年份："))
week_of_year_firstday = eval(input(str(year) + "年第一天是星期几？："))
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    days_of_month[1] += 1
days = 0
for month in range(12):
    num = 1
    week_of_month_firstday = (days + week_of_year_firstday) % 7
    print(str(year) + "年" + str(month + 1) + "月")
    for _ in range(7):
        print("————",end = "")
    print()
    print("Sun Mon Tue Wed Thu Fri Sat")
    for _ in range(week_of_month_firstday):
        print("   ",end = " ")
    week = week_of_month_firstday
    while num <= days_of_month[month]:
        print(format(num, "-2d"), end = "  ")
        num += 1
        week += 1
        if week % 7 == 0:
            week = 0
            print()
    days += days_of_month[month]
    print("\n")