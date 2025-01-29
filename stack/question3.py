def next_greatest_number(nums):
    n = len(nums)
    result = [-1] * n

 
    for i in range(n):
       
        for j in range(i + 1, n):
            if nums[j] > nums[i]:  
                result[i] = nums[j]  
                break  

    return result 

print(next_greatest_number([4, 5, 2, 10]))  
