def matchingStrings(strings, queries):
    
    result_list = list()
    
    for i in queries:
        
       result_list.append(strings.count(i))
            
    

    return result_list
