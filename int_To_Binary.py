
def int_To_Binary(int_Num):
    
    bin_Number = bin(int_Num)
    
    bin_Number = bin_Number.split("b")[-1]
    
    return bin_Number
