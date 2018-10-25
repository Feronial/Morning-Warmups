# Produces list with frequencies. first list contains values and second contains frequencies.


def freq_Lister(unsorted_List, unsorted_Frecs):
    
    freq_List = list()
    
    for i in range(len(unsorted_List)):
        
        freq_List.append([unsorted_List[i]]*unsorted_Frecs[i])
        
    
    return freq_List
