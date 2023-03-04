def isPrime(son:int):
    if son==2:
        return True
    if son%2==0 or son<2:
        return False
    for i in range(3,son//2+1):
        if son%i==0:
            return False
    return True




son=int(input("Son kiriting: "))
if isPrime(son):
    print("Tub son")
else:
    print("Tub son emas")
    
    
    
print("Farrux")
