def detect_Index(arr):
    
    index_Dict = dict()
    
    for i in range(len(arr)):
        
       index_Dict[arr[i]] = i
    
    return index_Dict
