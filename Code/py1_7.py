pi = 0.
sign = -1
for deno in range(1, 2, 13):
    sign *= -1
    pi += 1 / deno * sign
print(4 * pi)