T = int(input())
for tc in range(1, T + 1):
    num = input()
    arr = list(map(int, input().split()))

    cnt = [0] * 101

    for score in arr:
        cnt[score] += 1

    idx = 0
    for i in range(1, 101):
        if cnt[idx] <= cnt[i]:
            idx = i

    print('#{} {}'.format(tc, idx))

    #hi #hihi