import itertools

cnt = 0
coins = [0, 10, 50, 100, 500]
lst = list(itertools.combinations_with_replacement(coins, 15))  # 重複順列
for l in lst:
    if sum(l) == 1000:
        print(l)
        cnt += 1
print(cnt)

# pythonに順列、組み合わせ、直積、重複順列ライブラリがあることを知った
# sum関数の確認


# cnt = 0
# for i in range(0, 3):  # 500円玉
#     for j in range(0, 11):  # 100円玉
#         for k in range(0, 16):  # 50円玉
#             for l in range(0, 16):  # 10円玉
#                 if i + j + k + l <= 15:
#                     if 1000 == 500 * i + 100 * j + 50 * k + 10 * l:
#                         print(i, j, k, l)
#                         cnt += 1
# print(cnt)

# エラー、警告文の説明表示
# ブロック単位のコメントアウトが出来ない
