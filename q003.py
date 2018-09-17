N = [False] * 100
for i in range(1, 101):
    j = i - 1
    while j < 100:
        N[j] = not N[j]
        j += i

for i in range(0, 100):
    if N[i] == True:
        print(i + 1)

# 配列の一括初期化方法

# エディタタブ間の移動
