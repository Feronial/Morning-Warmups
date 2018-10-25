#Finds quartiles of list

def quartile_Find(Arr, median_Val, index): 
    
    
    
    q1 = list()
    q3 = list()
            
    for i in range(len(Arr)):
        
        if i < index:
            
            q1.append(Arr[i])
        
        elif i > index:
            
            q3.append(Arr[i])
   
    print(q1)
    print(q3)
    
    return median(q1), median_Val, median(q3) # without int

