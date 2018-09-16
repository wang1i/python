s = input("enter some integrity separated by space in one line:\n")
items = s.split()
list = [eval(x) for x in items]
list.reverse()
print(list)