N = int(input())

for i in range(1,N+1):
   Numbers = list(map(int,input().split()))
   a = 0
   
   for j in Numbers:
      a += j
   print('#{} {}'.format(i,round(a/10)))