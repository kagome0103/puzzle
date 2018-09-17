op = ['*', '']

for i in range(1000, 10000):
    var = str(i)
    for j in range(0, len(op)):
        for k in range(0, len(op)):
            for l in range(0, len(op)):
                calc = var[3] + str(op[j]) + var[2] + str(op[k]) + var[1] + str(op[l]) + var[0]
                try:
                    if i == eval(calc) and len(calc) >= 5:
                        print(calc)
                except:
                    pass

# evalの使い方
# rangeの領域確認

# デバッガ実行、停止
# ブレークポイント作成、削除
