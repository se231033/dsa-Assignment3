def multiply_by_two(digits):
    num = int(''.join(map(str, digits)))
    num *= 2
    return [int(digit) for digit in str(num)]


print(multiply_by_two([2, 3, 4]))  
print(multiply_by_two([0]))      
print(multiply_by_two([5, 0, 0])) 
