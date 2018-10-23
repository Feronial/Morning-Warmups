def insertNodeAtHead(llist, data):
    
    node = SinglyLinkedListNode(data)
    
    node.next = llist
    llist = node
    
    return llist
