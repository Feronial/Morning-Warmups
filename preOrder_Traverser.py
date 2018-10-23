def preOrder(root):
    

    
    if root:      
        
        print(root.info, end=" ")
      
        preOrder(root.left) 
  
        preOrder(root.right)
