
valid = True
s = str.strip(input("输入一个社会安全号码："))
for i in range(len(s)):
    if i == 3 or i == 6:
        if s[i] != '-':
            valid = False
    else:
        if s[i] > '9' or s[i] < '0':
            valid = False
if valid == True:
    print("合法输入")
else:
    print("非法输入")