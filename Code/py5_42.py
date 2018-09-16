import random as r
count = 0
for _ in range(1000000):
    x = r.random() * 2 - 1
    y = r.random() * 2 - 1
    if (x >= -1 and x <= 0) and (y >= -1 and y <= 0):
        count += 1
    if (x >= 0 and x <= 1) and (y >= 0 and y <= 1) and (x + y <= 1):
        count += 1
print("概率：", format(count / 1e6, "%"))