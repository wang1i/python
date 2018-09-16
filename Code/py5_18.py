n = eval(input("输入一个整数："))
prime = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23]
while n != 1:
    for i in range(10):
        if n % prime[i] == 0:
            ind = i
            print(str(prime[i]) + ",", end = " ")
            break
    n = n / prime[ind]