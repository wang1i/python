import math
radius, height = eval(input("请输入圆柱体的半径和高："))
area = radius**2 * math.pi
volume = area * height
print("圆柱体的面积为：", area, "\n体积为：", volume)
