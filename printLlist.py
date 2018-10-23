def printLinkedList(head):
    
    while True:
        
        print(head.data)
        
        if head.next != None:
            head = head.next
        else:
            
            break
