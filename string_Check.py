def string_Check(s): 

  cond_List = [0,0,0,0,0]
    
  for i in s:
        
      if i.isalnum():
            
          cond_List[0] += 1 
        
      if i.isalpha() :
            
          cond_List[1] += 1
            
      elif i.isdigit():
            
          cond_List[2] += 1
            
      if i.islower():
            
          cond_List[3] += 1 
        
      elif i.isupper():
            
          cond_List[4] += 1
        
  for k in cond_List:
            
      if k >= 1:
                
          print(True)
            
      else:
            
          print(False)
        
