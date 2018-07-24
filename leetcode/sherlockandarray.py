def solve(a):
    if a is [] or len(a) == 1:
        return "YES"

    s = sum(a)
    left_sum = 0
    right_sum = s

    if left_sum == right_sum:
        return "YES"

    for num in a:
        right_sum = right_sum - num

        if left_sum == right_sum:
            return "YES"

        left_sum += num

    return "NO"


print(solve([1]))
print(solve([5, 6, 8, 11]))
print(solve([5, 10, 8, 11]))
