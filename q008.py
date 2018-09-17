max_move = 3


def move(log) -> int:
    if len(log) == max_move + 1:
        return 1
    cnt = 0
    last_log = log[-1]
    for mv in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_pos = (last_log[0] + mv[0], last_log[1] + mv[1])
        if next_pos not in log:
            cnt = cnt + move(log + [next_pos])
    return cnt


print(move([(0, 0)]))
