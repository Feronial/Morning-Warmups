def count_Consec_One(bin_Num): # Count consecutive '1'  
    
    flag = 0
    count = 0
    
    for char in bin_Num:
        
        if flag == 1:
            
            if int(char) == 1 :
                
                count += 1
            
        if int(char) == 1 :
            
            flag = 1
            
        else:
            
            flag = 0
            
    return count
