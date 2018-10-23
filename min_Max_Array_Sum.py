def miniMaxSum(arr):
    
    arr.sort()
    
    max_Val = arr.pop()
    min_Val = arr.pop(0)
    
    mini = sum(arr) + min_Val
    maxi = sum(arr) + max_Val
    
    print(mini,maxi)
