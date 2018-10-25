#Finds quartiles of list

def quartile_Find(sorted_Arr, median_Val):
     
    q1 = list()
    q3 = list()
            
    for i in sorted_Arr:
        
        if i < median_Val:
            
            q1.append(i)
        elif i > median_Val:
            
            q3.append(i)
        
    return int(median(q1)), int(median_Val), int(median(q3))
