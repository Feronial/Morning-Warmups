
one_Nine = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

ten_Ninety = {'11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen',
              '18':'eighteen', '19':'nineteen'}


twenty_Ninety = {'1':'ten','2':'twenty','3':'thirty','4':'fourty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}

def converter(num):
    
    temp_Num = str(num)
    
   
    
    if len(temp_Num) == 3:
       
        if num % 100 == 0:
            
            return one_Nine[temp_Num[0] + ' hundred ']
        
        elif num % 10 == 0 :
            
            return one_Nine[temp_Num[0]] + ' hundred ' + twenty_Ninety[temp_Num[1]]
        
        else:
            
            return one_Nine[temp_Num[0]] + ' hundred ' + twenty_Ninety[temp_Num[1]] + ' ' + one_Nine[temp_Num[2]]
    
    elif len(temp_Num) == 2:
        
        if num % 10 == 0 :
            
            return twenty_Ninety[temp_Num[0]]
        
        elif num < 20:
        
            return ten_Ninety[temp_Num]
            
        else:
            
            return twenty_Ninety[temp_Num[0]] + ' ' +one_Nine[temp_Num[1]]
    
    else:
        return one_Nine[temp_Num]
