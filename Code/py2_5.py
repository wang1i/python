subtotal, rate = eval(input("请输入小计和酬金率："))
tip = subtotal * rate / 100
total = subtotal + tip
print("小费", tip, "总金额", total)