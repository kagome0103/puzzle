def sol(n, m):
    res, cnt = 1, 0
    while res < n:
        res += res if res < m else m
        cnt += 1
    return cnt


print(sol(20, 3))
print(sol(100, 5))

# 一行でif/elseを書く
# if a > 5:
#     i = a
# else:
#     i = 0
# は
# i = a if a > 5 else 0
