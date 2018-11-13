def count_Consec_One(bin_Num): # Count consecutive '1'  
    
    list_consecs = list()
    count = 0
    
    for char in bin_Num:
                  
        if int(char) == 1 :
            
            count += 1
            
            
        else:
            
            count = 0
            
        list_consecs.append(count)
            
    return max(list_consecs)
