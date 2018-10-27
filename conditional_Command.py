if __name__ == '__main__':
    N = int(input())
    
    command = list()
    
    for i in range(0, N):
        
        splitted = input().split()

        if splitted[0] == 'insert':
            
            command.insert(int(splitted[1]), int(splitted[2]))
        
        elif splitted[0] == 'print':
            
            print (command)
        
        elif splitted[0] == 'remove':
            
            command.remove(int(splitted[1]))
        
        elif splitted[0] == 'append':
            
            command.append(int(splitted[1]))
        
        elif splitted[0] == 'sort':
            
            command.sort()
        
        elif splitted[0] == 'pop':
            
            command.pop()
        
        elif splitted[0] == 'reverse':
            
            command.reverse()
