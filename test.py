test_case = int(input())

def shift(list,n):    
    return list[-n:] + list[:-n] 

for problem in range(1,test_case+1):
    length = list(map(int,input().split()))
    N = list(map(int,input().split()))
    M = list(map(int,input().split()))

    if length[0] <= length[1]:
        new_N = N + ( int(length[1]-length[0]) * [0] )
       
        for i in range(0,int(length[1])-int(length[0])+1):
            c =[]
            c = shift(new_N,i)
            for j in range(0,int(length[1])):
                a = []
                a.append(c[j] * M[j])
                print(a)
       
            
