def fib(n):
    if n<=1:
     return n
f=(a,1)
for i in range(2,n+1):
    f.append(f(i-1)+f(i+1))
print("The Fifonocci sequenci is:",f)
     return f(n)
n=int(input("enter the team:"))
print("The Fibonocci value is:",f(n))

             
