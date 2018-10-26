def count_substring(string, sub_string):
    count = 0

    
    for i in range(len(string)):
        
        if i >= len(string) - (len(sub_string)-1):
            
            break
        
        if string[i:(len(sub_string))+i] == sub_string:
            
            count += 1
            
        

    return count
