#Find median of list and index of it

def median(int_List):
    int_List.sort()
    if len(int_List) % 2 == 0:
        
        return sum(int_List[int((len(int_List) / 2) - 1) : int(len(int_List) / 2) + 1 ] ) / 2
        
    else:
        
        return int_List[round(len(int_List)/2)]
    
def median_Index(int_List):
    
    if len(int_List) % 2 == 0:
        
        return (int((len(int_List) / 2) - 1) + int(len(int_List) / 2) + 1) / 2
        
    else:
        
        return round(len(int_List)/2)
    
