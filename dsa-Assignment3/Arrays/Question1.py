def add_one(digits):
    n = len(digits)
    
   
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:  
            return digits
        digits[i] = 0  
    
    
    return [1] + digits


print(add_one([1, 2, 3]))  
print(add_one([9, 9]))     
print(add_one([0]))        
print(add_one([1, 0, 0, 0]))  
print(add_one([9, 9, 9]))
