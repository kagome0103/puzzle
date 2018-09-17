def recursive(num) -> int:
    if num == 0:
        return 1

    result = recursive(num - 1)
    return num * result

print(recursive(3))