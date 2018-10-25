def flatten_List_2D(list_2D):
    
    flattened = list()
    for i in list_2D:
        for j in i:
            flattened.append(j)
    return flattened  
