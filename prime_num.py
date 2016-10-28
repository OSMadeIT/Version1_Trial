def prime_number_gen(n):
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True
    
print prime_number_gen(89)