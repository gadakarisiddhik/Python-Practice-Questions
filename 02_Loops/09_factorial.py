n = int(input("Enter a Number: "))
fact = 1
if n==0 or n==1:
    fact = 1
    print("Fact:",fact)
else:
    for i in range(1,n+1):
        fact *= i
    print("Fact:",fact)