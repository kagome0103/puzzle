erp = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13,
       36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14,
       31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

amr = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34,
       15, 3, 24, 36, 13, 1, 0, 27, 10, 25, 29, 12, 8,
       19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]


def find_max_sum(source: list, num: int) -> int:
    sum_max = 0
    for i in range(len(source)):
        tmp = sum(source[:num])
        if tmp > sum_max:
            sum_max = tmp
        source = source[1:] + [source[0]]
    return sum_max


cnt = 0
for i in range(2, 37):
    tmp_erp = find_max_sum(erp, i)
    tmp_amr = find_max_sum(amr, i)
    if tmp_erp < tmp_amr:
        cnt += 1

print(cnt)

# 円状のデータの持ち方をどうするか

# Python3.5から導入されたType Hintsの確認
# 仮引数と返り値の型を明示できる。

# 変数の一括変更
# 一行を上下に移動
