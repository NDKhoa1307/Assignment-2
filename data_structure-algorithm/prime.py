def prime(n):
    prime=[n+1]
    for _ in range(n+1):
        prime.append(True)
    for i in range(2,n+1):
        if prime[i]:
            for p in range(i*i,n+1,i):
                prime[p]=False
    
    for i in range(2,n+1):
        if prime[i]:
            print(i,end=" ")

n=int(input())
prime(n)