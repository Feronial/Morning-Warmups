def insertNodeAtTail(head, data):
    
    node = SinglyLinkedListNode(data)
  
    if head == None:
          
        head = node
        
        return head
    
    tail = head
    
    while tail.next:
        
        tail = tail.next
    
    tail.next = node

    return head
