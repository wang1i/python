s = str.strip(input("输入密码："))
valid = True
count = 0
if len(s) < 8:
    valid = False
for i in range(len(s)):
    if not ((s[i] >= '0' and s[i] <= '9') or \
            (s[i] >= 'A' and s[i] <= 'Z') or \
            (s[i] >= 'a' and s[i] <= 'z')):
        valid = False
    if s[i] >= '0' and s[i] <= '9':
        count += 1
if count < 2:
    valid = False

if valid == True:
    print("合法密码")
else:
    print("非法密码")