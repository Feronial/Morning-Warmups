def removeDupes(string):
    empty_Str = ""
    
    for i in string:
        
        if ch not in empty_Str:
            empty_Str = empty_Str + ch
    
    return empty_Str




def merge_the_tools(string, k):
    
    str_List = list()
    count = 0
    
    for i in range(int(len(string)/ k)):
        
        i +=1
        
        str_List.append(string[count:i*k])
        
        count += k 
      
    for i in range(len(str_List)):
        
        str_List[i] = removeDupes(str_List[i])
    
    
    for i in range(k):
        print(str_List[i])
