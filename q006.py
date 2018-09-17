def is_even(num):
    return num % 2 == 0


cnt = 0
for i in range(2, 100001):
    j = i * 3 + 1
    while i != j and j != 1:
        if is_even(j):
            j = j // 2
        else:
            j = j * 3 + 1
    if j != 1:
        print(i)
        cnt += 1

print('cnt=', cnt)
# python2から3で割り算の仕様が変わった。
# 整数部だけ取り出したい場合は、「/」ではなく「//」
