MOD = 1e9 + 7


def C(m, n):
    result = 1
    for i in range(1, m + 1):
        result = result * (n - i + 1) // i
        result %= MOD
    return int(result)


def partly_solve(k, n, l, r, step):
    partly_answer = 0
    half = n // 2
    pluses = min(n, r - k) - max(1, l - k) + 1
    minuses = min(n, r + k) - max(1, l + k) + 1
    while (pluses >= half) and (minuses >= half) and (k <= n) and (k >= 1):
        partly_answer += C(half, min(pluses, minuses))
        partly_answer %= MOD
        k += step
        pluses = min(n, r - k) - max(1, l - k) + 1
        minuses = min(n, r + k) - max(1, l + k) + 1
    return partly_answer


def solve(n, l, r):
    answer = 0
    half = n // 2
    lower_bound = max(1, n - r, l - 1)
    upper_bound = min(1 - l, r - n)
    if upper_bound >= lower_bound:
        answer += (1 + upper_bound - lower_bound) * C(half, n)
        answer %= MOD
    answer += partly_solve(upper_bound + 1, n, l, r, 1)
    answer += partly_solve(lower_bound - 1, n, l, r, -1)
    if answer == 0:
        pass
        # pluses = min(n, r - k) - max(1, l - k) + 1
        # minuses = min(n, r + k) - max(1, l + k) + 1
    return answer



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, l, r = map(int, input().split())
        print(solve(n, l, r))