N = int(input())

for i in range(1,N+1):
    Numbers = list(map(int,input().split()))    
    if Numbers[0] < Numbers[1]:
        print(f'#{i} <')
    elif Numbers[0] == Numbers[1]:
        print(f'#{i} =')
    elif Numbers[0] > Numbers[1]:
        print(f'#{i} >')