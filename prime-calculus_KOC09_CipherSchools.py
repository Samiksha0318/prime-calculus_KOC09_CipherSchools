a=int(input("Enter lower range: "))
b=int(input("Enter upper range: "))
prime=0
comp=0
print(f"RANGE is({a},{b})")
print("Then the status of each number in range is:")
while a<=b:
    flag=False
    for i in range(2,a):
        if a%i==0 :
            flag=True
            break
    if a<1:
        print(a,"is composite or not prime")
        comp+=1
        a+=1
        continue
    elif a==1:
        print("1 is neither composite nor prime")    
    elif flag:
        print(a,"is composite or not prime")
        comp+=1
    else:
        print(a,"is prime number")
        prime+=1
    a+=1
print("COUNT:",prime,"prime and",comp,"composite numbers in the range.")
