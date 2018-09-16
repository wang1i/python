s1= str.strip(input("输入字符串："))
s2 = str.strip(input("输入字符串："))
index = s1.find(s2)
if index != -1:
    print("子串")
else:
    print("非子串")