s = input("enter scores separeted by space in one line:")
items = s.split()
list = [eval(x) for x in items]

num = 0
bestScore = max(list)
for score in list:
    if score >= bestScore - 10:
        print("Student " + str(num) + " score is " + str(score) +
              " and grade is A")
    elif score >= bestScore - 20:
        print("Student " + str(num) + " score is " + str(score) +
              " and grade is B")
    elif score >= bestScore - 30:
        print("Student " + str(num) + " score is " + str(score) +
              " and grade is C")
    elif score >= bestScore - 40:
        print("Student " + str(num) + " score is " + str(score) +
              " and grade is D")
    num += 1
