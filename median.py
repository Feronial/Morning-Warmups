#Find median of list

def median(int_List):
    
    if len(int_List) % 2 == 0:
        return sum(int_List[int((len(int_List) / 2) - 1) : int(len(int_List) / 2) + 1 ] ) / 2
    
    else:
        
        return int_List[round(len(int_List)/2)]
