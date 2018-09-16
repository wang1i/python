s = str.strip(input("输入主串："))
t = str.strip(input("输入模式串："))


def isSubString(s, t):
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    if j == len(t):
        return True
    else:
        return False


def count(s, t):
    i = 0
    count = 0
    while i <= len(s) - len(t):
        if s[i: i + len(t)] == t:
            count += 1
            i += len(t)
        else:
            i += 1
    return count


print(isSubString(s, t))
print(count(s, t))
